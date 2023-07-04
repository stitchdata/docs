import json, re, os
from jsonpath_ng import parse

def replaceDatetimeFormat(json_content):
    pattern = re.compile('("type":\s"string",\s*"format":\s"date-time")')

    dt = re.findall(pattern, json_content)

    new = '"type": "date-time"'

    for i in dt:

        json_content = json_content.replace(i, new)
    
    j = json.loads(json_content)
    
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
                if t == 'null':
                    pass
                else:
                    if t not in types:
                        types.append(t)
        elif type(v_types) == str:
            if v_types != 'null':
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

    json_output = json.loads(new_content)

    return json_output

def fullFileRef(path):
    for root, dirs, files in os.walk('schemas'):
        for file in files:
            filepath = os.path.join(root, file)
            if file == path:
                with open(filepath) as f:
                    content = f.read()
    
    return content

def partialRef(ref):

    split_ref = ref.split('/')
    path = split_ref[0].replace('#', '')

    steps = len(split_ref)

    for root, dirs, files in os.walk('schemas'):
        for file in files:
            filepath = os.path.join(root, file)
            if file == path:
                with open(filepath) as f:
                    file_content = json.load(f)
                    path = file_content[split_ref[1]]
                    step = 2
                    while step < steps :
                        path = path[split_ref[step]]
                        step +=1

                    content = json.dumps(path, indent=2)
    
    return content

def replaceRefs(json_content):

    pattern = re.compile('(\{\s*\"\$ref\"\:\s\"([^\"]+)\"\s*\})')

    refs = re.findall(pattern, json_content)

    for ref in refs:
        element = ref[0]
        path = ref[1]

        if path.endswith('.json') or path.endswith('.json#/'):
            content = fullFileRef(path)
            json_content = json_content.replace(element, content)
        else:
            content = partialRef(path)
            json_content = json_content.replace(element, content)
    

    j = json.loads(json_content)
    
    return j

# def removeNull(json_content):


folder = 'schemas'

for root, dirs, files in os.walk(folder, topdown=False):
    for file in files:
        filepath = os.path.join(root, file)
        if filepath.endswith('.json'):
            change = 0
            with open(filepath, 'r') as f:
                json_content = f.read()
                if '$ref' in json_content:
                    json_content = replaceRefs(json_content)
                    change +=1
                if 'anyOf' in json_content:
                    json_content = replaceAnyof(json_content)
                    change +=1
                if '"format": "date-time"' in json_content:
                    json_content = replaceDatetimeFormat(json_content)
                    change +=1
            
            if change > 0:
                with open(filepath, 'w') as j:
                    json.dump(json_content, j, indent=2)