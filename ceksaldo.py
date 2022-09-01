import json

def ceksaldo(id):
    f = open('nasabah.json')
    data = json.load(f)
    for i in data['datanasabah']:
        if i['id']==id:
            return i['saldo']
    