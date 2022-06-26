import requests

header = {'Content-Type': 'application/json'}
item_payload = '{"item_name": "test item"}'
item_payload_upd = '{"item_name": "test item1","is_done": true}'
url = 'http://127.0.0.1:5000'

def test_add_item(h, p):
    resp = requests.post(url+'/additem', data=p, headers=h)
    if resp.status_code == 200:
        print('Add item test successful!')
    else:
        print('Add item test failed!')

def test_get_item(h):
    resp = requests.get(url+'/getitems', headers=h)
    if resp.status_code == 200:
        print('Get item test successful!')
    else:
        print('Get item test failed!')


def test_get_done(h):
    resp = requests.get(url+'/getitems', headers=header)
    resp_json = resp.json()
    for i in resp_json['ToDoList']:
        if i['item_name'] == 'test item':
            id = str((i['id']))
            resp_gd = requests.patch(url + '/getdone/' + id, headers=header)
            if resp_gd.status_code == 200:
                print('Get done test successful!')
            else:
                print('Get done test failed!')

def test_delete(h):
    resp = requests.get(url+'/getitems', headers=header)
    resp_json = resp.json()
    for i in resp_json['ToDoList']:
        if i['item_name'] == 'test item':
            id = str((i['id']))
            resp_gd = requests.patch(url + '/delete/' + id, headers=header)
            if resp_gd.status_code == 200:
                print('Delete test successful!')
            else:
                print('Get done test failed!')


test_add_item(header,item_payload)
test_get_item(header)
test_get_done(header)
test_delete(header)