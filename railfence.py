
def rail_fence_encrypt(plainteks, k):
    # Menghilangkan spasi untuk transposisi murni
    plainteks = plainteks.replace(" ", "").upper()
    rail = [['\n' for _ in range(len(plainteks))] for _ in range(k)]
    
    arah_bawah = False
    baris, kolom = 0, 0
    
    for i in range(len(plainteks)):
        if (baris == 0) or (baris == k - 1):
            arah_bawah = not arah_bawah
        rail[baris][kolom] = plainteks[i]
        kolom += 1
        baris += 1 if arah_bawah else -1
        
    cipherteks = []
    for i in range(k):
        for j in range(len(plainteks)):
            if rail[i][j] != '\n':
                cipherteks.append(rail[i][j])
    return "".join(cipherteks)

print("=== Aplikasi Rail Fence Transposisi ===")
pesan = input("Masukkan plainteks: ")
kunci = int(input("Masukkan jumlah baris (misal: 3): "))

hasil_cipher = rail_fence_encrypt(pesan, kunci)
print(f"Cipherteks: {hasil_cipher}")