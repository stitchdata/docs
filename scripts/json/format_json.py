import json, re, os, sys
from check_json_issues import checkJSONIssues

def getType(format):
    # Get the data type to used based on the value of the format element

    # Formats that should be used as type
    type_formats = ['date-time', 'date', 'time', 'any']

    # Formats that should have the types number, string, or integer
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
    # For elements that have a type and a format, the type should be updated and the format should be removed

    # Find the format and type (can be formatted differently in different JSON files, so multiple patterns are needed)
    pattern_single_type = re.compile('("type":\s*"(string|integer)",\s*"format":\s*"([^\"]+)")')
    pattern_multi_types_v1 = re.compile('(("type":\s*\[[^\]]*")(string|integer)("[^\]]*\]),\s*"format":\s*"([^\"]+)")')
    pattern_multi_types_v2 = re.compile('("format":\s*"([^\"]+)",\s*("type":\s*\[[^\]]*")(string|integer)("[^\]]*\]))')

    single_dt = re.findall(pattern_single_type, json_content)
    multi_dt_v1 = re.findall(pattern_multi_types_v1, json_content)
    multi_dt_v2 = re.findall(pattern_multi_types_v2, json_content)

    # Find the patterns in the JSON files
    if re.search(pattern_single_type, json_content) or re.search(pattern_multi_types_v1, json_content) or re.search(pattern_multi_types_v2, json_content):

        # If the element has only one data type: get the full string, isolate the format, and get the corresponding data type
        for i in single_dt:
            full = i[0]
            format = i[2]
            type = getType(format)

            # Replace the string with a new string with the correct data type
            new_single_type = '"type": "{}"'.format(type)
            json_content = json_content.replace(full, new_single_type)

        # If the element has multiple data types, get the full string:
        # - isolate the format and the parts that come before and after the data type to replace
        # - find the correct data type
        # - recreate the string with the new data type

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
    # Replace a $ref that points to an element in the same file

    # Get the path to the element and the length of the path
    split_ref = split_ref = ref.split('/')
    steps = len(split_ref)

    if steps > 1:
        ref_index = 1
    else:
        ref_index = 0

    # Open the file and find the element referenced 
    with open(filepath) as f:
        file_content = json.load(f)
        try:
            path = file_content[split_ref[ref_index]]
            status = 'found'
            if '$ref' in path:
                raise Exception()
        except:

            # If the path is not found as is, check in 'properties' and 'definitions' elements
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

                    # If the element is still not found, the path may be a reference to another file.
                    # In that case, check is a file exists
                    split_ref[ref_index] = split_ref[ref_index] + '.json'
                    out_ref = '/'.join(split_ref)
                    for root, dirs, files in os.walk(folder):
                        for file in files:
                            if file == split_ref[ref_index]:
                                status = 'external_file'

                                # If the external file is found, use the other functions to replace the reference
                                if steps == 1:
                                    content = fullFileRef(split_ref[ref_index], folder, type)
                                else:
                                    content = partialRef(out_ref, folder, type)

        if status == 'external_file':
            pass
        elif status == 'found':

            # If the path has multiple elements, iterate on each step to find the element, then replace the reference with the referenced content
            step = ref_index + 1
            while step < steps :
                path = path[split_ref[step]]
                step +=1

            content = json.dumps(path, indent=2)

    return content

def fullFileRef(path, folder, type):
    # Replace a $ref that points to a full JSON file

    # Find the file in the tap folder and get the content
    for root, dirs, files in os.walk(folder):
        for file in files:
            filepath = os.path.join(root, file)
            if file in path:
                with open(filepath) as f:
                    content = f.read()
                    json_content = json.loads(content) 
                    try:

                        # If the target file has a 'properties' element, get the content of 'properties', otherwise use the full file
                        props = json_content['properties']

                        # For the rare case where a reference is 'inline' (i.e.: not in a separate object):
                        # Get each element from the referenced content and replace the ref with those elements
                        if type == 'inline':
                            new_content = ''
                            for prop in props:
                                new_content = new_content + '"{}": '.format(prop) + json.dumps(props[prop]) + ','
                            content = new_content
                        elif type == 'object':
                            content = json.dumps(props)
                        elif type == 'empty file':
                            content = content
                    except:
                        pass

    return content

def partialRef(ref, folder, type):
    # Replace a $ref that points to part of a JSON file

    # Get the path to the element and the length of the path
    split_ref = ref.split('/')
    path = split_ref[0].replace('#', '')
    steps = len(split_ref)

    # Open the file and find the element referenced 
    for root, dirs, files in os.walk(folder):
        for file in files:
            filepath = os.path.join(root, file)
            if file in path:
                with open(filepath) as f:
                    file_content = json.load(f)
                    try:
                        path = file_content[split_ref[1]]
                    except:

                        # If the element is not found using the path in the $ref, try looking in the 'properties' in case if was omitted
                        path = file_content['properties'][split_ref[1]]

                    # Iterate on the steps to get the element referenced
                    step = 2
                    while step < steps :
                        path = path[split_ref[step]]
                        step +=1

                    # Replace the reference with the content
                    content = json.dumps(path, indent=2)
    
    return content

def replaceRefs(json_content, folder, filepath):
    # Resolve references to JSON content

    try:

        # Find $ref elements
        pattern = re.compile('(\{\s*\"\$ref\"\:\s*\"([^\"]+)\"\s*\})', re.MULTILINE)
        refs = re.findall(pattern, json_content)
        refs_count = len(refs)
        type = 'object'

        if refs_count == 0:
            raise Exception()
        else:
            for ref in refs:

                # Get the path to the element referenced and determine the type of reference
                element = ref[0]
                path = ref[1]

                if json_content.strip() == element:
                    type = 'empty file'

                # Use the function matching the reference type
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

            # Find inline $ref elements, get the path and type, and use the corresponding function
            pattern = re.compile('(\"\$ref\"\:\s*\"([^\"]+)\"\s*,)', re.MULTILINE)
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
    
    # Return the content with the references resolved
    j = json.loads(json_content)
    return j

def formatJSON(folder, json_output_folder, keep):
    # Format JSON files to fit the format supported by the HTML template

    table_list = []

    # Get JSON files in the tap folder
    for root, dirs, files in os.walk(folder, topdown=False):
        for file in files:
            filepath = os.path.join(root, file)
            if filepath.endswith('.json'):
                with open(filepath, 'r') as f:
                    json_content = f.read()
                    output_file = json_output_folder + '/' + file
                    
                    # Ignore files in 'shared' and 'archive' folders, they are either old schemas or files containing content referenced in schemas
                    if file not in keep and ('{0}shared{0}'.format(os.sep) in filepath or '{0}archive{0}'.format(os.sep) in filepath):
                        print('JSON file {} ignored'.format(file))

                    else:

                        # Find '$ref' elements and resolve the references
                        # This uses 'while' to deal with nested references
                        while '$ref' in json_content:
                            json_content = json.dumps(replaceRefs(json_content, folder, filepath))
            
                        # Read JSON content as a dict for the next steps
                        content = json.loads(json_content)
                        
                        try:

                            # Check if there is a properties element and if so, add the file to the list of tables
                            props = content['properties']
                            table_list.append(file.replace('.json', ''))

                            # Find and replace elements with formats
                            format_pattern = re.compile('"format":\s*"[^\"]+"')
                            while re.search(format_pattern, json_content):
                                json_content = replaceFormat(json_content)
                            
                            # Run function from check_json_issues.py to check for missing 'properties' elements
                            content = json.loads(json_content)
                            content = checkJSONIssues(content)

                            # Write updated content to file in the _data/taps/schemas folder
                            with open(output_file, 'w') as j:
                                json.dump(content, j, indent=2, sort_keys=True)
                            
                        except:
                            try:

                                # If the 'properties' element is not found at the root of the file, check for a 'schema' element and if it is found, add the file to the list of tables
                                props = content['schema']['properties']
                                json_content = json.dumps(content['schema'])
                                table_list.append(file.replace('.json', ''))

                                # Find and replace elements with formats
                                while re.search(format_pattern, json_content):
                                    json_content = replaceFormat(json_content)
                                
                                # Run function from check_json_issues.py to check for missing 'properties' elements
                                content = json.loads(json_content)
                                content = checkJSONIssues(content)

                                # Write updated content to file in the _data/taps/schemas folder
                                with open(output_file, 'w') as j:
                                    json.dump(content, j, indent=2, sort_keys=True)
                            except:
                                
                                # Ignore files that don't have 'properties' or 'schema'
                                print('JSON file {} ignored'.format(file))
                        

    return table_list