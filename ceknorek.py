import json

def cekrek(id):
    f = open('nasabah.json')
    data = json.load(f)
    for i in data['datanasabah']:
        if i['id']==id:
            return i['no_rek']
    