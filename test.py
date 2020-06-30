import json
from models import storage

"""with open("file.json", "r", encoding="utf-8") as f:
    obj = json.load(f)
    for i, v in obj.items():
        for x, y in v.items():
            if (x == 'id'):
                print(y)"""


for i, v in storage.all().items():
    if 'eazrea' in i:
        print('ok')
    print(i)

