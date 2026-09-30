
def rot13_proses(teks):
    hasil = ""
    for char in teks:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            # ROT13 selalu menggunakan kunci = 13
            c = (ord(char) - start + 13) % 26 + start
            hasil += chr(c)
        else:
            hasil += char
    return hasil

print("=== Aplikasi ROT13 ===")
pesan_asli = input("Masukkan teks: ")

# Enkripsi
teks_sandi = rot13_proses(pesan_asli)
print(f"Hasil ROT13: {teks_sandi}")

# Dekripsi (ROT13 dua kali menghasilkan teks asli)
teks_kembali = rot13_proses(teks_sandi)
print(f"Dikembalikan: {teks_kembali}")