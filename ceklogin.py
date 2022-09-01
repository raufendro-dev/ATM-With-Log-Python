import json

def cek_login(user, pin):
    f = open('nasabah.json')
    data = json.load(f)
    for i in data['datanasabah']:
        if i['username']==user and i['pin']==pin:
            return i['id']
        else:
            a = "error"
            return a
    
        

