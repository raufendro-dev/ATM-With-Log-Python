from ceklogin import cek_login
from ceksaldo import ceksaldo
from ceknorek import cekrek
from transfer import kirimuang
from tariksetor import tarik, setor
import logging
from datetime import datetime

global namafile
today = datetime.now()
namafile = str(today)+' transaksi.log'
def login():
    
    nama = input("Masukan username : ")
    pin = input("Masukan pin anda : ")
    global userid
    userid=cek_login(nama, pin)
    
    
    logging.basicConfig(filename=r"log/"+namafile, filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO)
    logging.info("[login] Berhasil login")
    

def atm():
    today = datetime.now()
    login()
    
    if userid=="error":
        print("Username atau pin yang anda masukan salah")
    else:

        menuloop = 1
        while menuloop ==1:
            print("Pilih Menu : ")
            print("1. Informasi Saldo")
            print("2. Informasi Nomor Rekening")
            print("3. Transfer")
            print("4. Tarik Tunai")
            print("5. Setor Tunai")
            print("6. Keluar")
            pilih = int(input("> "))
            print("\n")
            if pilih == 1:
                print("Saldo Anda : Rp ",ceksaldo(userid), "\n", "\n")  
                logging.basicConfig(filename=r"log/"+namafile, filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO)
                logging.info("[1] Cek Saldo : Rp " +str(ceksaldo(userid))) 
            elif pilih == 2:
                print(cekrek(userid), "\n", "\n")
                logging.basicConfig(filename=r"log/"+namafile, filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO)
                logging.info("[2] Cek rekening :  " +str(cekrek(userid))) 
            elif pilih == 3:
                uang = int(input("Berapa yang mau ditransfrer? "))
                rektujuan = int(input("Masukan rekening tujuan : "))
                print("\n")
                print(kirimuang(userid, rektujuan, uang), "\n", "\n")
                logging.basicConfig(filename=r"log/"+namafile, filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO)
                logging.info("[3] Transfer dari userid "+str(userid)+" ke nomor rekening "+str(rektujuan)+" sebesar Rp "+str(uang))
            elif pilih == 4:
                ambil = int(input("Masukan jumlah uang yang ingin diambil : "))
                logging.basicConfig(filename=r"log/"+namafile, filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO)
                logging.info("[4] Berhasil tarik uang sejumlah Rp "+str(ambil))
                print(tarik(userid, ambil))
            elif pilih == 5:
                kasih = int(input())
                print(setor(userid, kasih))
                
                logging.basicConfig(filename=r"log/"+namafile, filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO)
                logging.info("[5] Berhasil setor uang sejumlah Rp "+str(kasih))
            elif pilih == 6:
                
                logging.basicConfig(filename=r"log/"+namafile, filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO)
                logging.info("[6] Berhasil logout") 
                menuloop =0
        
           
                

atm()
