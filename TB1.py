def decode_matrix(matriks, n, m):
    string_terdekripsi = ""
    simbol_di_belakang = ""


    for kolom in range(m):
        for baris in range(n):
            if kolom < len(matriks[baris]):
                karakter = matriks[baris][kolom]

                if karakter.isalnum():
                    if string_terdekripsi and not string_terdekripsi[-1].isalnum():

                        string_terdekripsi = string_terdekripsi[:-1] + ' '
                    string_terdekripsi += karakter
                else:

                    if not string_terdekripsi or not string_terdekripsi[-1].isalnum():
                        simbol_di_belakang += karakter
                    else:

                        string_terdekripsi += karakter


    if string_terdekripsi and not string_terdekripsi[-1].isalnum():
        simbol_di_belakang = string_terdekripsi[-1] + simbol_di_belakang
        string_terdekripsi = string_terdekripsi[:-1]


    string_terdekripsi = ' '.join(string_terdekripsi.split())


    string_terdekripsi += simbol_di_belakang

    return string_terdekripsi


def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        matriks = [line.strip() for line in file]
    return matriks


def main():
    filenames = ['data1.txt', 'data2.txt']
    for filename in filenames:
        matriks = read_matrix_from_file(filename)
        n = len(matriks)
        m = max(len(baris) for baris in matriks)


        pesan_terdekripsi = decode_matrix(matriks, n, m)
        print(f"Hasil decoding matriks dari {filename} adalah:")
        print(pesan_terdekripsi)
        print()


if __name__ == "__main__":
    main()
