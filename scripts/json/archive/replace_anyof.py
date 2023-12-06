import json
from jsonpath_ng import parse

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