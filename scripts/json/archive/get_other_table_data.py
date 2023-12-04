import os, frontmatter, pandas, yaml

errors = []
file_count = 0

elements = []
issues = []

def getSchemaData(file):
    parse = frontmatter.load(file)
    data = parse.metadata
    for i in data:
        if i not in elements:
            elements.append(i)

for root, dirs, files in os.walk('../../../_integration-schemas'):
    for file in files:
        if file.endswith('.md') and file != 'foreign-keys.md':
            file_count += 1
            file = os.path.join(root, file)
            try:
                getSchemaData(file)
            except:
                issues.append(file)
                pass

print(issues)
print(*elements, sep='\n')