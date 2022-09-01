import json

def tarik(asal, uang):
    f = open('nasabah.json')
    data = json.load(f)
    
    indexasal = asal
    
    if data['datanasabah'][indexasal]['id']>=0:
        if data['datanasabah'][indexasal]['saldo']>=uang:
            data['datanasabah'][indexasal]['saldo'] = data['datanasabah'][indexasal]['saldo'] - uang
            with open('nasabah.json', 'w') as j:
                json.dump(data, j)
                sukses = "Silahkan ambil uang anda"
                sisa = "Sisa saldo anda Rp "+str(data['datanasabah'][indexasal]['saldo'])
                hasil = sukses + "\n" + sisa
                return hasil
        else:
            error = "Saldo tidak mencukupi"
            return error


def setor(asal, uang):
    f = open('nasabah.json')
    data = json.load(f)
    
    indexasal = asal
    
    if data['datanasabah'][indexasal]['id']>=0:
        
        data['datanasabah'][indexasal]['saldo'] = data['datanasabah'][indexasal]['saldo'] + uang
        with open('nasabah.json', 'w') as j:
            json.dump(data, j)
            sukses = "Sukses setor sejumlah Rp "+str(uang)
            sisa = "Sisa saldo anda Rp "+str(data['datanasabah'][indexasal]['saldo'])
            hasil = sukses + "\n" + sisa
            return hasil
        
 