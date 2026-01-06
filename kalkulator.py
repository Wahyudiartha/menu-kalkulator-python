def kalkulator():
    while True:
        print("===== MENU KALKULATOR =====")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Keluar")

        menu = int(input("Pilih menu (1-5): "))

        if menu == 5:
            print("Program selesai")
            break

        a = float(input("Masukkan bilangan pertama: "))
        b = float(input("Masukkan bilangan kedua: "))

        if menu == 1:
            print("Hasil penjumlahan:", a + b)
        elif menu == 2:
            print("Hasil pengurangan:", a - b)
        elif menu == 3:
            print("Hasil perkalian:", a * b)
        elif menu == 4:
            if b == 0:
                print("Tidak bisa dibagi nol")
            else:
                print("Hasil pembagian:", a / b)
        else:
            print("Menu tidak valid")

        print()

kalkulator()