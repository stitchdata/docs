import json, re, os

file = 'first.json'

def fullFileRef(path):
    for root, dirs, files in os.walk("."):
        for file in files:
            if file == path:
                with open(file) as f:
                    content = f.read()
    
    return content

# def partialRef(path):

def replaceRefs(json_content):

    pattern = re.compile('(\{\s+\"\$ref\"\:\s\"([^\"]+)\"\s+\})')

    refs = re.findall(pattern, json_content)

    for ref in refs:
        element = ref[0]
        path = ref[1]

        if path.endswith('.json') or path.endswith('.json#/'):
            content = fullFileRef(path)
            
            json_content = json_content.replace(element, content)
    

    j = json.loads(json_content)
    
    return j

with open(file, 'r') as f:
    json_content = f.read()
    new_json = replaceRefs(json_content)

with open(file, 'w') as j:
    json.dump(new_json, j, indent=4)