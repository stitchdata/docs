import json, re, os
from jsonpath_ng import parse

def getType(format):
    type_formats = ['date-time', 'date', 'time', 'any']
    number_formats = ['singer.decimal', 'singer-decimal', 'float']
    string_formats = ['uri']

    if format in type_formats:
        type = format
    elif format in number_formats:
        type = 'number'
    elif format in string_formats:
        type = 'string'
    
    return type

def replaceFormat(json_content):
    
    pattern_single_type = re.compile('("type":\s"string",\s*"format":\s"([^\"]+)")')
    pattern_multi_types_v1 = re.compile('(("type":\s\[[^\]]*")string("[^\]]*\]),\s*"format":\s"([^\"]+)")')
    pattern_multi_types_v2 = re.compile('("format":\s"([^\"]+)",\s*("type":\s\[[^\]]*")string("[^\]]*\]))')

    single_dt = re.findall(pattern_single_type, json_content)
    multi_dt_v1 = re.findall(pattern_multi_types_v1, json_content)
    multi_dt_v2 = re.findall(pattern_multi_types_v2, json_content)
    

    for i in single_dt:
        full = i[0]
        format = i[1]
        type = getType(format)

        new_single_type = '"type": "{}"'.format(type)
        json_content = json_content.replace(full, new_single_type)
    
    for j in multi_dt_v1:
        format = j[3]
        full = j[0]
        p1 = j[1]
        p2 = getType(format)
        p3 = j[2]

        new_multi_type = p1 + p2 + p3

        json_content = json_content.replace(full, new_multi_type)
    
    for k in multi_dt_v2:
        format = k[1]
        full = k[0]
        p1 = k[2]
        p2 = getType(format)
        p3 = k[3]

        new_multi_type = p1 + p2 + p3

        json_content = json_content.replace(full, new_multi_type)
    
    return json_content

def replaceAnyof(json_content):
    json_data = json.loads(json_content)
    content = json.dumps(json_data)
    jsonpath_expression = parse('$..anyOf.`parent`')
    match = jsonpath_expression.find(json_data)
    i = 0
    while i < len(match):
        value = match[i].value
        new_value = {}
        types = []
        anyof_values = value['anyOf']
        for v in anyof_values:
            v_types = v['type']
            if type(v_types) == list:
                for t in v_types:
                    if t not in types:
                        types.append(t)
            elif type(v_types) == str:
                types.append(v_types)
        
            if 'items' in v:
                items = v['items']
                if bool(items) == True:
                    new_value['items'] = items
            
            if 'properties' in v:
                items = v['properties']
                if bool(items) == True:
                    new_value['properties'] = items

            
        new_value['type'] = types

        old_json = json.dumps(value)
        new_json = json.dumps(new_value)
        
        find = content.find(old_json)

        if find != -1:
            content = content.replace(old_json, new_json)
        else:
            content = content
        i += 1

    return content

def sameFileRef(ref, filepath, folder):
    split_ref = split_ref = ref.split('/')
    steps = len(split_ref)
    
    if steps > 1:
        ref_index = 1
    else:
        ref_index = 0

    with open(filepath) as f:
        file_content = json.load(f)
        try:
            path = file_content[split_ref[ref_index]]
            status = 'found'
        except:
            try:
                path = file_content['properties'][split_ref[ref_index]]
                status = 'found'
            except:
                try:
                    path = file_content['definitions'][split_ref[ref_index]]
                    status = 'found'
                except:
                    split_ref[ref_index] = split_ref[ref_index] + '.json'
                    out_ref = '/'.join(split_ref)
                    for root, dirs, files in os.walk(folder):
                        for file in files:
                            if file == split_ref[ref_index]:
                                status = 'external_file'
                                if steps == 1:
                                    content = fullFileRef(split_ref[ref_index], folder)
                                else:
                                    content = partialRef(out_ref, folder)

        if status == 'external_file':
            pass
        elif status == 'found':
            step = ref_index + 1
            while step < steps :
                path = path[split_ref[step]]
                step +=1

            content = json.dumps(path, indent=2)
    
    return content

def fullFileRef(path, folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            filepath = os.path.join(root, file)
            if file in path:
                with open(filepath) as f:
                    content = f.read()
    
    return content

def partialRef(ref, folder):

    split_ref = ref.split('/')
    path = split_ref[0].replace('#', '')

    steps = len(split_ref)

    for root, dirs, files in os.walk(folder):
        for file in files:
            filepath = os.path.join(root, file)
            if file in path:
                with open(filepath) as f:
                    file_content = json.load(f)
                    try:
                        path = file_content[split_ref[1]]
                    except:
                        path = file_content['properties'][split_ref[1]]
                    step = 2
                    while step < steps :
                        path = path[split_ref[step]]
                        step +=1

                    content = json.dumps(path, indent=2)
    
    return content

def replaceRefs(json_content, folder, filepath):

    pattern = re.compile('(\{\s*\"\$ref\"\:\s\"([^\"]+)\"\s*\})')

    refs = re.findall(pattern, json_content)

    for ref in refs:
        element = ref[0]
        path = ref[1]

        if path.endswith('.json') or path.endswith('.json#/'):
            content = fullFileRef(path, folder)
            json_content = json_content.replace(element, content)
        elif '.json' in path:
            content = partialRef(path, folder)
            json_content = json_content.replace(element, content)
        else:
            content = sameFileRef(path, filepath, folder)
            json_content = json_content.replace(element, content)

    
    
    if '"format": "' in json_content:
        json_content = replaceFormat(json_content)
    

    j = json.loads(json_content)
    
    return j

def formatJSON(folder, json_output_folder):

    table_list = []

    for root, dirs, files in os.walk(folder, topdown=False):
        for file in files:
            filepath = os.path.join(root, file)
            if filepath.endswith('.json'):
                with open(filepath, 'r') as f:
                    table_list.append(file.replace('.json', ''))
                    json_content = f.read()
                    if '$ref' in json_content:
                        json_content = json.dumps(replaceRefs(json_content, folder, filepath))

                    if '"format": "' in json_content:
                        json_content = replaceFormat(json_content)

                    while '"anyOf"' in json_content:
                        json_content = replaceAnyof(json_content)
                
                content = json.loads(json_content)
                with open(json_output_folder + '/' + file, 'w') as j:
                    json.dump(content, j, indent=2)
    
    return table_list