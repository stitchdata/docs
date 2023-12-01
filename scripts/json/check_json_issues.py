def fixProperty(property):
    # Adds a `properties` element to that contains the child elements in objects that don't have it

    # List elements that are expected to be present directly in an object
    expected_properties = ['multipleOf','additionalProperties', 'type', 'additional_properties', 'description', 'patternProperties', 'enum', 'title', 'required', 'exclusiveMaximum', 'exclusiveMinimum', 'maximum', 'minimum', 'x-looker-deprecated', 'default', 'format', 'selected']
    
    # List elements that contain child elements
    nested = ['anyOf', 'properties', 'items']

    # Get the content of the current property and check if is an object
    for prop in property:
        issues = 0
        new_content = {}
        content = property[prop]
        if type(content) == dict:

            # If it contains a 'properties' element, repeat the same function on that element
            if 'properties' in content and content['properties'] != None:
                properties = content['properties']
                properties = fixProperty(properties)

            # If the element contains 'anyOf', check each the 'properties' in the 'items' element, or just 'items' if there is no 'properties' element
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
                                fixProperty(item)
            
            # If the element contains 'items', check each the 'properties' in the 'items' element, or just 'items' if there is no 'properties' element
            elif 'items' in content:
                item_list = content['items']
                if len(item_list) > 0:
                    if 'items' in item_list and 'type' in item_list and len(item_list) == 2:
                        content['items'] = content['items']['items']
                        item_list = content['items']
                    if 'properties' in item_list:
                        p = item_list['properties']
                        p = fixProperty(p)
                    else:
                        fixProperty(content)    

            # If the current property contains it child elements directly, get all elements and add them in a 'properties' element, and add the 'object' type to the parent      
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
    # Run the checks on the input JSON content and return the fixed JSON
    
    props = json_content['properties']
    props = fixProperty(props)
    
    return json_content