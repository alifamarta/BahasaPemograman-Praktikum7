from menu.add import add,update
from menu.view import show
from menu.delete import delete

while True:

    print("\n")
    print("================================")
    print("      Program input nilai       ")
    print("================================\n")

    print("[1] Lihat Data")
    print("[2] Tambah Data")
    print("[3] Ubah Data")
    print("[4] Hapus Data")
    print("[5] Keluar")

    x = input("> PILIH MENU : ")

    print("\n")

    if x == '1':
        show()
    elif x == '2':
        add()
    elif x == '3':
        update()
    elif x == '4':
        delete()

    elif x == '5':
        print("==========================================================================")
        print('\n')
        print("> You exit the code                        ")
        print("\n")
        print("==========================================================================")

        exit()

    else:
        print("            KODE YANG ANDA MASUKKAN TIDAK VALID !!!!!!!!!!!")