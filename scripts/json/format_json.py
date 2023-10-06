import json, re, os, sys

def getType(format):
    type_formats = ['date-time', 'date', 'time', 'any']
    number_formats = ['singer.decimal', 'singer-decimal', 'float']
    string_formats = ['uri', '']
    int_formats = ['int64']

    if format == 'datetime':
        format = 'date-time'

    if format in type_formats:
        type = format
    elif format in number_formats:
        type = 'number'
    elif format in int_formats:
        type = 'integer'
    elif format in string_formats:
        type = 'string'
    else:
        print('Format {} not found in format list'.format(format))
    
    return type

def replaceFormat(json_content):
    
    pattern_single_type = re.compile('("type":\s*"(string|integer)",\s*"format":\s*"([^\"]+)")')
    pattern_multi_types_v1 = re.compile('(("type":\s*\[[^\]]*")(string|integer)("[^\]]*\]),\s*"format":\s*"([^\"]+)")')
    pattern_multi_types_v2 = re.compile('("format":\s*"([^\"]+)",\s*("type":\s*\[[^\]]*")(string|integer)("[^\]]*\]))')

    single_dt = re.findall(pattern_single_type, json_content)
    multi_dt_v1 = re.findall(pattern_multi_types_v1, json_content)
    multi_dt_v2 = re.findall(pattern_multi_types_v2, json_content)
    
    if re.search(pattern_single_type, json_content) or re.search(pattern_multi_types_v1, json_content) or re.search(pattern_multi_types_v2, json_content):

        for i in single_dt:
            full = i[0]
            format = i[2]
            type = getType(format)

            new_single_type = '"type": "{}"'.format(type)
            json_content = json_content.replace(full, new_single_type)
        
        for j in multi_dt_v1:
            format = j[4]
            full = j[0]
            p1 = j[1]
            p2 = getType(format)
            p3 = j[3]

            new_multi_type = p1 + p2 + p3

            json_content = json_content.replace(full, new_multi_type)
        
        for k in multi_dt_v2:
            format = k[1]
            full = k[0]
            p1 = k[2]
            p2 = getType(format)
            p3 = k[4]

            new_multi_type = p1 + p2 + p3

            json_content = json_content.replace(full, new_multi_type)

    else:
        print('Format pattern not found')
    
    return json_content

def sameFileRef(ref, filepath, folder, type):
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
            if '$ref' in path:
                raise Exception()
        except:
            try:
                path = file_content['properties'][split_ref[ref_index]]
                status = 'found'
                if '$ref' in path:
                    raise Exception()
                    
            except:
                try:
                    path = file_content['definitions'][split_ref[ref_index]]
                    status = 'found'
                    if '$ref' in path:
                        raise Exception()
                except:
                    split_ref[ref_index] = split_ref[ref_index] + '.json'
                    out_ref = '/'.join(split_ref)
                    for root, dirs, files in os.walk(folder):
                        for file in files:
                            if file == split_ref[ref_index]:
                                status = 'external_file'
                                if steps == 1:
                                    content = fullFileRef(split_ref[ref_index], folder, type)
                                else:
                                    content = partialRef(out_ref, folder, type)

        if status == 'external_file':
            pass
        elif status == 'found':
            step = ref_index + 1
            while step < steps :
                path = path[split_ref[step]]
                step +=1

            content = json.dumps(path, indent=2)

    return content

def fullFileRef(path, folder, type):
    for root, dirs, files in os.walk(folder):
        for file in files:
            filepath = os.path.join(root, file)
            if file in path:
                with open(filepath) as f:
                    content = f.read()
                    json_content = json.loads(content) 
                    try:
                        props = json_content['properties']
                        if type == 'inline':
                            new_content = ''
                            for prop in props:
                                new_content = new_content + '"{}": '.format(prop) + json.dumps(props[prop]) + ','
                            content = new_content
                        elif type == 'object':
                            content = json.dumps(props)
                    except:
                        pass

    return content

def partialRef(ref, folder, type):

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

    try:
        pattern = re.compile('(\{\s*\"\$ref\"\:\s*\"([^\"]+)\"\s*\})')
        refs = re.findall(pattern, json_content)
        refs_count = len(refs)
        type = 'object'

        if refs_count == 0:
            raise Exception()
        else:
            for ref in refs:
                element = ref[0]
                path = ref[1]

                if json_content == element:
                    type = 'empty file'

                if path.endswith('.json') or path.endswith('.json#/'):
                    content = fullFileRef(path, folder, type)
                    json_content = json_content.replace(element, content)
                elif '.json' in path:
                    content = partialRef(path, folder, type)
                    json_content = json_content.replace(element, content)
                else:
                    content = sameFileRef(path, filepath, folder, type)
                    json_content = json_content.replace(element, content)
    except:
        try:
            pattern = re.compile('(\"\$ref\"\:\s*\"([^\"]+)\"\s*,)')
            refs = re.findall(pattern, json_content)
            refs_count = len(refs)
            type = 'inline'
            if refs_count == 0:
                raise Exception()
            else:
                for ref in refs:
                    element = ref[0]
                    path = ref[1]

                    if path.endswith('.json') or path.endswith('.json#/'):
                        content = fullFileRef(path, folder, type)
                        json_content = json_content.replace(element, content)
                    elif '.json' in path:
                        content = partialRef(path, folder, type)
                        json_content = json_content.replace(element, content)
                    else:
                        content = sameFileRef(path, filepath, folder, type)
                        json_content = json_content.replace(element, content)
        except:
            sys.exit('Reference pattern not found')
    
    j = json.loads(json_content)
    return j

def formatJSON(folder, json_output_folder):

    table_list = []
    ignored = []

    for root, dirs, files in os.walk(folder, topdown=False):
        for file in files:
            filepath = os.path.join(root, file)
            if filepath.endswith('.json'):
                with open(filepath, 'r') as f:
                    json_content = f.read()

                    if '{0}shared{0}'.format(os.sep) in filepath or '{0}archive{0}'.format(os.sep) in filepath:
                        report = 'JSON file {} ignored'.format(file)
                        ignored.append(report)

                    else:
                        format_pattern = re.compile('"format":\s*"[^\"]+"')

                        while '$ref' in json_content:
                            json_content = json.dumps(replaceRefs(json_content, folder, filepath))
            
                        content = json.loads(json_content)
                        
                        try:
                            props = content['properties']

                            table_list.append(file.replace('.json', ''))

                            while re.search(format_pattern, json_content):
                                json_content = replaceFormat(json_content)
                            
                            content = json.loads(json_content)
                            with open(json_output_folder + '/' + file, 'w') as j:
                                json.dump(content, j, indent=2, sort_keys=True)
                        
                        except:
                            try:
                                props = content['schema']['properties']
                                json_content = json.dumps(content['schema'])

                                table_list.append(file.replace('.json', ''))

                                while re.search(format_pattern, json_content):
                                    json_content = replaceFormat(json_content)
                                
                                content = json.loads(json_content)
                                with open(json_output_folder + '/' + file, 'w') as j:
                                    json.dump(content, j, indent=2, sort_keys=True)

                            except:
                                report = 'JSON file {} ignored'.format(file)
                                ignored.append(report)
                        

    return [table_list, ignored]