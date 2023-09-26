import json, re, os
from jsonpath_ng import parse

def replaceDatetimeFormat(json_content, output_type):
    
    pattern_single_type = re.compile('"type":\s"string",\s*"format":\s"date-time"')
    pattern_multi_types = re.compile('(("type":\s\[[^\]]*")string("[^\]]*\]),\s*"format":\s"date-time")')

    single_dt = re.findall(pattern_single_type, json_content)
    multi_dt = re.findall(pattern_multi_types, json_content)
    

    for i in single_dt:
        new_single_type = '"type": "date-time"'
        json_content = json_content.replace(i, new_single_type)
    
    for j in multi_dt:
        full = j[0]
        p1 = j[1]
        p2 = 'date-time'
        p3 = j[2]

        new_multi_type = p1 + p2 + p3
        json_content = json_content.replace(full, new_multi_type)
    
    if output_type == 'dict':
        j = json.loads(json_content)
    elif output_type == 'str':
        j = json_content
    
    return j

def replaceAnyof(json_content):
    json_data = json.loads(json_content)
    jsonpath_expression = parse('$..anyOf.`parent`')
    match = jsonpath_expression.find(json_data)
    value = match[0].value
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
        
    new_value['type'] = types

    old_json = json.dumps(value)
    new_json = json.dumps(new_value)
    content = json.dumps(json_data)
    
    find = content.find(old_json)

    if find != -1:
        new_content = content.replace(old_json, new_json)
    else:
        new_content = content

    return new_content

def sameFileRef(ref, filepath):
    split_ref = split_ref = ref.split('/')
    steps = len(split_ref)

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
            content = sameFileRef(path, filepath)
            json_content = json_content.replace(element, content)

    
    
    if '"format": "date-time"' in json_content:
        json_content = replaceDatetimeFormat(json_content, 'str')
    

    j = json.loads(json_content)
    
    return j


def formatJSON(folder, json_output_folder):

    table_list = []

    for root, dirs, files in os.walk(folder, topdown=False):
        for file in files:
            filepath = os.path.join(root, file)
            if filepath.endswith('.json'):
                change = 0
                with open(filepath, 'r') as f:
                    table_list.append(file.replace('.json', ''))
                    json_content = f.read()
                    if '$ref' in json_content:
                        json_content = json.dumps(replaceRefs(json_content, folder, filepath))
                        change +=1

                    elif '"format": "date-time"' in json_content:
                        json_content = replaceDatetimeFormat(json_content, 'str')
                        change +=1

                    if '"anyOf"' in json_content:
                        json_content = replaceAnyof(json_content)
                        change +=1
                
                content = json.loads(json_content)
                with open(json_output_folder + '/' + file, 'w') as j:
                    json.dump(content, j, indent=2)
    
    return table_list