import requests

request=requests.get('https://餐厅.com/菜单/汉堡')
print(request.json())

new_burger={"名称": "培根汉堡", "价格": 42, "配料": ["牛肉", "培根", "芝士"]}
reponse=requests.post('https://餐厅.com/菜单',json=new_burger)
print(reponse.status_code) #输出201

update_burger={"名称": "双层牛肉汉堡", "价格": 40, "配料": ["牛肉", "生菜", "番茄"]}
reponse=requests.put('https://餐厅.com/菜单/汉堡',json=update_burger)
print(reponse.json())

response = requests.delete("https://餐厅.com/菜单/素食汉堡")
print(response.status_code)