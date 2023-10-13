# Fix issue when the parent element doesn't hae "properties" and the child element doesn't either

def fixProperty(property):

    expected_properties = ['multipleOf','additionalProperties', 'type', 'additional_properties', 'description', 'patternProperties', 'enum', 'title', 'required', 'exclusiveMaximum', 'exclusiveMinimum', 'maximum', 'minimum', 'x-looker-deprecated', 'default', 'format']
    nested = ['anyOf', 'properties', 'items']
    for prop in property:
        issues = 0
        new_content = {}
        content = property[prop]
        if type(content) == dict:
            if 'properties' in content and content['properties'] != None:
                properties = content['properties']
                properties = fixProperty(properties)
            elif 'anyOf' in content:
                for item in content['anyOf']:
                    if len(item) == 1 and 'type' in item:
                        pass
                    elif 'items' in item:
                        item_list = item['items']
                        if len(item_list) > 0:
                            if 'properties' in item_list:
                                p = item_list['properties']
                                p = fixProperty(p)
                            else:
                                fixProperty(item_list)
            elif 'items' in content:
                item_list = content['items']
                if len(item_list) > 0:
                    if 'properties' in item_list:
                        p = item_list['properties']
                        p = fixProperty(p)
                    else:
                        fixProperty(item_list)          
            else:
                for item in content:
                    if item not in expected_properties and item not in nested:
                        issues += 1

                if issues > 0:
                    for item in content:
                        new_content[item] = content[item]
                    for item in new_content:
                        content.pop(item)
                    new_content = fixProperty(new_content)
                    content['properties'] = new_content
                    content['type'] = ['object']

    return property

def checkJSONIssues(json_content):
    props = json_content['properties']
    props = fixProperty(props)
    
    return json_content