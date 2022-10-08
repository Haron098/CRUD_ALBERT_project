import json
from datetime import datetime

FILE = 'data.json'


# сериализируем json в python
def get_data(ge_price=None, le_price=None, stat=None, page=None, date=None):
    with open(FILE) as file:
        products = json.load(file)
    if page:
        page = int(page)
        products = products[page * 3 - 3:page * 3]
    if ge_price:
        ge_price = int(ge_price)
        products = [i for i in products if i['price'] >= ge_price]
    if le_price:
        le_price = int(le_price)
        products = [i for i in products if i['price'] <= le_price]
    if stat == 'active':
        products = [i for i in products if i['status'] == stat]
    elif stat == 'inactive':
        products = [i for i in products if i['status'] == stat]
    if date:
        products = [i for i in products if date in i['date of creation']]
    return products


# даем id для продукта
def new_id(id_=None):
    id_ = int(input('Введите id Продукта: '))
    products = get_data()
    product = [i for i in products if i['id'] ==id_]
    if products:
        return product[0]
    return 'No such proudct!'


# Создаем продукт
def new_product():
    products = get_data()
    max_id = max(i['id'] for i in products)
    new_id = max_id + 1
    products.append({
        'id': new_id,
        'name': input('Введите название продукта: '),
        'price': int(input('Введите цену нового продукта: ')),
        'date of creation': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'date of update': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'description': input('Введите описание: '),
        'status': 'active'
    })
    json.dump(products, open(FILE, 'w'))
    return 'product created'


# редактируем продукт
def reduct_product():
    print('Редактирования продукта')
    data = get_data()
    id = int(input('Введите id продукта для изменении -> '))
    product = list(filter(lambda x: x['id'] == id, data))
    if not product:
        return 'вы не правильно ввели id продукта'
    index_ = data.index(product[0])
    user = input('Что вы хотите изменить? p.s введите ниже указанные цифры\n1-цену\n2-описание\n3-статус\n')
    if user == '1':
        data[index_]['price'] = int(input('Введите новую цену-> '))
    elif user == '2':
        data[index_]['description'] = input('Измените описание-> ')
    if '3' in user:
            status = input('Выберите статус: active/inactive: ')
            if status.lower() == 'active' or status.lower() == 'inactive':
                product[index_]['status'] = status
    else:
        return 'Такой команды нету!'
    product[data]['date of update'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    json.dump(product, open(FILE, 'w'))
    return 'your product has been successfully modified'

def delete_product():
    data = get_data()
    id = int(input('Введите id для удалении -> '))
    product = list(filter(lambda x:x['id'] == id, data))
    if not product:
        return 'Такого продукта нету!'
    index_ = data.index(product[0])
    data.pop(index_)
    json.dump(data, open(FILE, 'w'))
    return 'product removed!'

def watch_product():
    data = get_data()
    id = int(input('Введите id продукта'))
    product = list(filter(lambda x:x['id'] == id, data))
    
    if product:
        return product[0]
    else:
        return 'no such product!'