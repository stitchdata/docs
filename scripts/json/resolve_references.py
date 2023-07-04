import json, re, os

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

folder = 'schemas'

for root, dirs, files in os.walk(folder, topdown=False):
    for file in files:
        filepath = os.path.join(root, file)
        if filepath.endswith('.json'):
            with open(filepath, 'r') as f:
                json_content = f.read()
                new_json = replaceRefs(json_content)
            with open(filepath, 'w') as j:
                json.dump(new_json, j, indent=2)