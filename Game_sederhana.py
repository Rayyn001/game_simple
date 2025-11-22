import os

#dibawah adalah program untuk login 

ussername = "rayyan"
password = 1234567
nama_pengguna = input("masukan ussername kamu:")
kode = input("masukan pasword kamu: ")

if nama_pengguna == ussername:
    if kode == str(password):   #str digunakan untuk menggubah anggka menjadi string
        print("login berhasil")
    else:
        print('password salah')
        exit()          #exit disisni digunakan agar program berhenti dan tidak lanjut berjalan
else:
    print("ussername salah")
    exit()


def menu():
    while True:  #while digunkan untuk membuat perulangan
        os.system('cls')
        print('''  SELAMAT DATANG DI GAME ADVENTURE ON PYTHON''')
        nama_player = input("masukan ussername karakter game kamu: ")
        print(f"halo {nama_player} pilih karakter dalam game mu:")
        print("0.keluar")
        print("1.Ahli pedang")
        print("2.tongkat magis")
        print("3.Perisai")
        #Disini prgram untuk pemain untuk memilih weapon/senjata yang ingin digunkan
        pilihan_player = int(input("masukan pilihan kamu:"))
        if pilihan_player == 1:
            print("pilihan kamu adalah ahli pedang")
            break
        elif pilihan_player == 2:
         print("pilihan kamu adalah kekuatan magis ")
         break
        elif pilihan_player == 3:
         print("pilihan kamu adalah perisai ")
         break
        
        elif pilihan_player == 0:
            exit()
        else:
         print("ulangi lagi")
        os.system('pause')
         
menu()

#dibwah adalah pilihan apa yang kamu ingin lakukan di kota

def kota():
  while True:
    os.system('cls')
    print("kamu sekarang berada di sebuah kota yang cukup terkenal")
    print("kamu bisa menjelajahi kota ini")
    print("di sini kamu bisa membeli beberapa perlengkapan yangkamu butuhkan ")
    print("atau kamu bisa mendaftar ke suah guild petualan ")
    print("atau kamu bisa makan sejenak untuk mengisi tenagamu")
    print("1.Menjelajai kota")
    print("2.Membeli perlengkapan")
    print("3.Mendaftar guild")
    print("4.Memesan makanan")
    print("5.keluar dari petualangan")
    
    jelajah_kota = int(input("masukan pilihan kamu:"))
    if jelajah_kota == 1:
        print("di kota kamu melihat hal-hal baru yang belum pernah kamu lihat")
        print("dan kamu pun seorang petualang lain")
        print("kamu mencoba mengajaknya bicara untuk mendapat beberapa informasi")
        input('''
petualang:
Kamu pendatang baru''')     #ini adalh salah satu percakaon di kota kamu bisa memsaukan apa saja akan teteapi npc tetap akan menjawab sama
        input(":")
        print('''
peualang:
selamt datang di kota py''')
        input(":")
        print('''
petualang:
bersenang-senanglah aku pergi dulu''')
        break
    else:
        print("selamat tunggal")
    if jelajah_kota ==  2:
        print('''
pemilik toko:
sSelamat datang silahkan pilih apa yang kamu butuhkan''') #percakapan bila kamu memasuki sebuah toko di kota
        print("1.pedang")
        print("2.zirah")
        print("3.ramuan penyembuh")
        print("4.pisau kecil")
        print("5.keluar dari toko")
        
        toko_senjata = int(input("masukan pilihanmu"))
        if toko_senjata == 1:
            print(toko_senjata)
            print("terimakasih sudah membeli")
        elif toko_senjata == 2:
            print(toko_senjata)
        elif toko_senjata == 3:
            print(toko_senjata)
        elif toko_senjata == 4:
            print(toko_senjata)
        elif toko_senjata == 5:
            print(toko_senjata)
            break
        else:
            print("keluarlah")
    if jelajah_kota == 3:
        print('''
resepsionis:
Selamat datang apa yang kamu inginkan ''')
        print("1.mendaftar")
        print("2.mencari info monster")
        print("3.keluar")
        
        pilihan_guild = int(input("masukan pilihan mu:"))
        
        if pilihan_guild == 1:
            print("jika kamuninngin mendaftar masukan identitasmu")#jika kamu tertarik dengan guild atau klan
            indentitas = ("masukan identitasmu:")
            nama = input("nama kamu:")
            umur = int(input())
            if indentitas:
                print(f"selamat kamu diteriama {nama} dan umur mu adalah {umur}")
                break
            else:
                print("keluarlah")
        elif pilihan_guild:
            print("lihat di papan informasi")
            break
        else:
            ("dahlah")
    if jelajah_kota == 4:
        print('''
pemilik toko:
apa yang kamu pesan''')
        input("")
        print("nimati maknanmu")
        break
    elif jelajah_kota == 5:
        exit()
    else:
        print("kemblai menjelajah kota")
        os.system('pause')
        
kota()
#disina adalah menu utama atau saya sebut dengan rintangan
#saya menggunakan if elif dan else untuk menentukan pilihan
def rintangan():
    while True:
        print("kamu mulai menjelajah sekrang tentukan pilihan tujuanmu ")
        print("1.menjelajahi hutan terlarang ")
        print("2.Langsung mencoba melawan monster")
        print("3.Pergi ke desa magis")
        print("4.mengahiri petualangan")
        
        memilih_tantangan = int(input("pilih salah satu tantangan di atas:"))
        if memilih_tantangan == 1:
            print("kamu mulai memasuki hutan")
            print("didalam hutan kamu menemukan berbagai hal yang sebelumnya belum pernah kamu lihat")
            print("kamu pun mulai menyusuri hutan semakin dalam ")
            print('''kamu pun berbagai macam seprti tanaman langka dan 
                  hewan yang jarang kamu lihat sebelumnya''')
            print("kemudian kamu bertemu monster yanng mecoba memangsamu")
            perlawanan = input("apkah kamu ingin melawannya?[ya/tidak]:")
            if perlawanan == "ya":
                print("kamu pu mencoba menahannya menggunakan senjata yang kamu miliki")
                print("dia mencoba menyerang mu lagi ")
                # saya menggunakan program untuk serangan 
                # (serangan_count) digunakan umtuk menghitung jumlah serangan yang kita lancarkan
                # saya juga memberikan pilihan untuk kabur atau menyerang
                serangan_count = 0


                while serangan_count < 3:
                    aksi = input("Pilih aksi (serang/kabur): ").strip().lower()

                    if aksi == "serang":
                        serangan_count += 1
                        print(f"kamu melancarkan Serangan ke-{serangan_count}.")
                    elif aksi == "kabur" and serangan_count == 1:
                        print("kamu kalah karna monsster menyerang dan menerkam mu dari belakang")
                        if serangan_count == 3:
                            print("kamu mengalahkannya dengan gg")
                            break
                    elif aksi == "kabur" and serangan_count == 2:
                            print("kamu memilih untuk kabur dan mati")
                            break
                    else:
                         print("yang bener woi")

                if serangan_count < 3 and aksi != "kabur":
                     print("Pemain tidak berhasil mengalahkan musuh.")
                else:
                    print("masukan pilihan")

                print("kamu mendapat luka ringan")
                print("kamu ingat bahwa kamu memiliki ramuan penyembuahan")
                
                penyembuhan = input("apakh kamu ingin menggunaknnya? [ya/tidak]:")
                if penyembuhan == "ya":
                    print("kamu pulih kembali")
                elif penyembuhan == "no":
                    print("kamu berpikir menyimpnnya untuk nanti")
                else:
                    print("pilihlah sesuai piliahn di atas")
                    
            elif perlawanan == "tidak":
                 print("kamu lebih memilih kabur dan kembali ke desa")
            else:
                print("kamu matiiii")
            
            print("kamu pun berhasil selamat dari hutan tersebut dan memutuskan untuk kembali ke desa")
            
            
        if memilih_tantangan == 2:
            print("kamu pun langsung mencoba melawan monster yang kuat")
            print("kemudian kamu pergi mencari sanggat jauh dari desa")
            print("kamu bertemu monster yang cukup kuat")
            
            lawan =  input("apakah kamu yakin [ya/tidak]")
            if lawan == "ya":
                print("kamu pun mencoba melawannya ")
                print("dia melwanmu dengan kekuatan penuh")
                print("kamu pun mendapat kekuatan yang taek terduga dari senjatamu")
                
                
                serangan_satge_ke2 = 0


                while serangan_satge_ke2 < 3:
                    aksi = input("Pilih aksi (serang/menyerah): ").strip().lower()

                    if aksi == "serang":
                        serangan_satge_ke2 += 1
                        print(f"kamu melancarkan Serangan ke-{serangan_satge_ke2}.")
                    elif aksi == "menyerah" and serangan_satge_ke2 == 1:
                        print("kamu kelah karena ketakutan")
                        if serangan_satge_ke2 == 3:
                            print("gg bang menang")
                            print("apakah kamu ingin melanjutkan pencarain melawan monster")
                    else:
                        print("masukan pilihan")
                        
                        
                        lanjutkah = input("ketik ya jika kamu ingin meneruskannya")
                        if lanjutkah == "ya":
                                print("kamu mencari monster yang lebih kuat dari sebelumnya")
                                print("setelah beberapa saat kamu pun bertemu dengan moster yang lebih kuat")
                                print("apakah kamu ingin melwannya")
                                lawan_kah = int(input("apakah kamu ingin melwannya ketik 1 jika ya dan 2 jika tidak"))
                                if lawan_kah == 1:
                                    print("kamu menyerang monster lagi karena kamu mendapat buff setelah mengalahkan monster sebelumnya")
                                    print("ketika kamu menyerangnya monster belum siap dan mengamuk")
                                    print("kamu menyerangnya dengan kekuatan penuh")
                                    
                                    serangan_count3 = 0


                                    while serangan_count3 < 3:
                                        aksi = input("Pilih aksi (serang/kabur): ").strip().lower()

                                        if aksi == "serang":
                                             serangan_count += 1
                                             print(f"kamu melancarkan Serangan ke-{serangan_count}.")
                                        elif aksi == "kabur" and serangan_count3 == 1:
                                            print("kamu kalah karna monsster menyerang dan menerkam mu dari belakang")
                                            if serangan_count3 == 3:
                                             print("kamu mengalahkannya dengan gg")
                                             print("kamu memutuskan untuk pulang dan beristirahat")
                                             istirahat = input("tekan ya untuk jika ingin beristirahat")
                                             if istirahat == "ya":
                                                 print("kamu memutuskan untuk beristirahat")
                                             else:
                                                 print("kamu mati kelelahan")
                                             
                                            elif aksi == "kabur" and serangan_count3 == 2:
                                             print("kamu memilih untuk kabur dan mati")
                                             break
                                            else:
                                             print("yang bener woi")

                                    
                            
                                        elif aksi == "menyerah" and serangan_count3 == 2:
                                             print("kamu menyerah karena sudah putus asa")
                                             break
                                        else:
                                             print("yang bener woi")
                                                                                  
                                else:
                                    print("kamu pulang ke desa")
                        else:
                                print("kamu kembali ke rumah")
                                
            elif lawan == "tidak":
                print("kamu pergi melanjutkan perjalanan")  
            else:
                print("kamu pulang ke rumah")
                #di desa megis terdapat beberapa percakapan yang saya tambahkan namun 
                # tidak ada pertarungan dengan monster dan juga terdapat tokoyang bisa di kunjungi
        if memilih_tantangan == 3:
            print("kamu memasuki desa magis")
            print("kamu bertemu dengan dengan warga sekitar ")
            print("di desa tersebut terdapat berbagai macam ras ")
            print("dan ras ras tersebut mahir memakai sihir")
            print("ada elf dwarf monster yang monster setengah manusia")
            print("kamupun bertemu salah satu warga desa tersebut")
            percakan_desa_magis = ("keik ya jika kamu ingin memulai percakan[ya/tidak]")
            if percakan_desa_magis == "ya":
                print("halo selamat datang di desa magis")
                print("disini kamu akan banyak hal yang menarik ")
                print('1.apakah aku bisa mendapat kekuatan magis di sini?')
                print("2.apakah aku bisa mendapat benda magis yang keren?")
                print("3.apa saja larangan di desa ini dan apa yang terjadi jika aku melanggar nya?")
                percakpan1 = int(input("masukan pilihan di atas"))
                if percakpan1 == 1:
                    print("tentu kemu bisa berlatih dengan warga yang terampil")
                elif percakpan1 == 2:
                    print("tentu kami meyediakannya di toko di desa")
                elif percakpan1 == 3:
                    print("tentu ada, dan jika kamu kamu melanggarnya kamu akan dikeluarkan dari desa")
                else:
                    print("masukan pilihanmu")
            elif percakan_desa_magis == "tidak":
                print("kamu langsung menyusuri desa")
            else:
                print("masukan pilihanmu")
            
            print("kamupun menelajahi desa tersebut dan menemukan hal hal menarik ")
            
            print("kamu bertemu dengan salah satu warga desa tersebut")
            print("apkah kamu ingin mengajaknya bicara")
            percakapan2 = input("ketik ya jika kamu ingin mengajaknya bicara [ya/tidak]:")
            if percakapan2 == "ya":
                print("halo apakabar apa kamu baru datang ke desa kami ")
                input(":")
                print("perkenalkan aku salah satu warga desa namaku sarah")
                input(":")
                print("apa yang kamu lakukan di desa ini?")
                input("")
                print("karena kamu telah berbicara denganku aku akan memberimu hadiah ")
                input(":")
                print("dah selamat tinggal terima kasih telah berbicara denganku")
            elif percakapan2 == "tidak":
                print("kamu melnjutkan perjalanan di desa")
            else:
                print("kamu melanjutkan menyusuri desa")
            print("didesa tersebut kamu menemukan sebuah toko yang cukup unik")
            print("apakah kamu tertarik masuk ke toko tersenut")
            masuk_toko = input("ketik masuk jika kamu ingin memasuki toko tersebut")
            if masuk_toko == "ya":
                print("selamat datang di toko magisgisgis")
                print("apa yang kamu butuhkan, kamu bisa melihat-lihat terlebih dahulu ")
                print("1.ramuan penembuh")
                print("2.jimat penambah kekuatan")
                print("3.batu penambah kekuatan untuk senjata")
                print("4.junbah anti sihir")
                print("5.sepatu menambah kecepatan")
                print("6.keluar dari toko")
                toko_magis = int(input("masukan pilihan kamu:"))
                if toko_magis == 1:
                    print("terimakasih sudah membeli ")
                elif toko_magis == 2:
                    print("terimakasih sudah membeli")
                elif toko_magis == 3:
                    print("terimakasih sudah membeli ")
                elif toko_magis == 4:
                    print("terimakasih sudah membeli ")
                elif toko_magis == 5:
                    print("terimakasih sudah membeli ")
                elif toko_magis == 6:
                    print("kamu pergi meninggalkan toko")
                else:
                    ("pilih yang benar")
            elif masuk_toko == "tidak":
                print("kamu menyusuri desa")
            else:
                print("ayo masukan yang benar")
            
            print("setelah itu kamu mendapatkan kekuatan baru dan kembali melanjutkan peetualanganmu ")
            print('''                   PERJALANAN DI DESA MAGISPUN BERAKHIR         ''')
            exit()
        else:
            print("permainan selesai silahkan mulai kembali")        
                
        if memilih_tantangan == 4:
            print("kamu memutuskan mangahiri permainan")
            exit()    
        else:
            print()    
            exit()
                        
rintangan()  

# program berakhir di sini
#RAYYAN INDRA MARDHANI
#5240411126