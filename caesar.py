def caesar_cipher_encrypt(plainteks, k):
    cipherteks = ""
    for char in plainteks:
        if char.isalpha(): # Hanya memproses huruf alfabet saja
            start = ord('A') if char.isupper() else ord('a')
            c = (ord(char) - start + k) % 26 + start
            cipherteks += chr(c)
        else:
            cipherteks += char
    return cipherteks

def caesar_cipher_decrypt(cipherteks, k):
    plainteks = ""
    for char in cipherteks:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            c = (ord(char) - start - k) % 26 + start
            plainteks += chr(c)
        else:
            plainteks += char
    return plainteks

print("=== Aplikasi Caesar Cipher ===")
pesan = input("Ketikkan pesan: ")
kunci = int(input("Masukkan jumlah pergeseran kunci (0-25): "))

terenkripsi = caesar_cipher_encrypt(pesan, kunci)
print(f"Cipherteks: {terenkripsi}")
print(f"Hasil dekripsi: {caesar_cipher_decrypt(terenkripsi, kunci)}")