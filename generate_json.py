import json
import os

paths = []
for root, dirs, files in os.walk('C:/Users/Pinge/Desktop/001'):
    for name in files:
        file_path = os.path.join(root, name)
        paths.append(file_path)

print(paths)

files = []
for i in paths[0:2]:
    f = open(i, "r", encoding="utf-8")
    lines = f.read()
    # print(lines)
    files.append(lines)

# print(files)
# print(json.dumps(files, ensure_ascii=False))

with open('data.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(files, ensure_ascii=False))
    
