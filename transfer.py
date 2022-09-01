import json

def kirimuang(asal, tujuan, uang):
    f = open('nasabah.json')
    data = json.load(f)
    idtujuan = cekidrektujuan(tujuan)
    indexasal = asal
    indextujuan = idtujuan
    if data['datanasabah'][indexasal]['id']>=0:
        if data['datanasabah'][indexasal]['saldo']>=uang:
            data['datanasabah'][indexasal]['saldo'] = data['datanasabah'][indexasal]['saldo'] - uang
            data['datanasabah'][indextujuan]['saldo'] = data['datanasabah'][indextujuan]['saldo'] + uang
            with open('nasabah.json', 'w') as j:
                json.dump(data, j)
                sukses = "Sukses transfer sejumlah Rp "+str(uang)
                sisa = "Sisa saldo anda Rp "+str(data['datanasabah'][indexasal]['saldo'])
                hasil = sukses + "\n" + sisa
                return hasil
        else:
            error = "Saldo tidak mencukupi"
            return error
        

def cekidrektujuan(rek):
    f = open('nasabah.json')
    data = json.load(f)
    for i in data['datanasabah']:
        if i['no_rek']==rek:
            return i['id']
