import requests as requests
import json

url = 'http://127.0.0.1:8000/'

response = requests.get(url).json()


print(call.data)

# for i in response:
    # for k, v in i.items():
#    print(i['category_name'])

# with open(response) as f:
#     templates = json.loads(response)
#
# print(templates)
#
# for dict_v in response:
#     for k, v in dict_v.items():
#         if k == 'category_name':
#             print(f'{v}')
#         if k == 'id':
#             print(v)
#
#
# actions = {10: sum, 100: product, }
# action = actions.get(x, cube)
# action(x)
