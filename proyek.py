# Daftar stasiun MRT
print("=== DAFTAR STASIUN MRT ===")
Stasiuns = ["Lebak Bulus Grab", 
           "Fatmawati Indomaret", 
           "Cipete Raya", "Haji Nawi", 
           "Blok A", 
           "Blok M BCA", 
           "ASEAN", 
           "Senayan Mastercard", 
           "Istora Mandiri", 
           "Bendungan Hilir", 
           "Setiabudi Astra", 
           "Dukuh Atas BNI", 
           "Bundaran HI Bank DKI"
           ]

for i, stasiun in enumerate(Stasiuns):
    print(f"{i+1}. {stasiun}") 

# Input stasiun keberangkatan dan tujuan
Initial = input("Berangkat dari stasiun apa? ")

# Memastikan ketersediaan stasiun keberangkatan
while Initial not in Stasiuns:
    print("Stasiun tidak tersedia!")
    Initial = input("Berangkat dari stasiun apa? ")

Final = input("Mau turun di stasiun apa? ")

# Memastikan ketersediaan stasiun tujuan
while Final not in Stasiuns:
    print("Stasiun tidak tersedia!")
    Final = input("Mau turun di stasiun apa? ")

while Initial == Final:
    print("Stasiun keberangkatan dan tujuan tidak boleh sama!")
    Final = input("Mau turun di stasiun apa? ")
    
Perubahan_stasiun = abs(Stasiuns.index(Final) - Stasiuns.index(Initial))

'''
Misal:
- Durasi antarstasiun 3 menit (tetap)
- Durasi berhenti di tiap stasiun 2 menit
- Harga dasar Rp4000
- Setiap stasiun yang dilewati menambah Rp1000
'''

t_antarstasiun = 3
t_stop_stasiun = 2
Waktu_tempuh = t_antarstasiun * Perubahan_stasiun + t_stop_stasiun * (Perubahan_stasiun - 1)

Harga_per_tiket = 4000 + (Perubahan_stasiun - 1) * 1000
print(f"Harga per tiket adalah Rp{Harga_per_tiket}")
Jumlah_tiket = int(input("Mau beli berapa tiket? (Masukkan angkanya saja): "))
Total_harga = Harga_per_tiket * Jumlah_tiket
print(f"Total harganya adalah Rp{Total_harga}", )
print(f"Perkiraan waktu tempuh adalah {Waktu_tempuh} menit")

Konfirmasi = input("Lanjutkan transaksi? (Ya/Tidak): ")

while Konfirmasi != "Ya" and Konfirmasi != "Tidak":
    print("Pilihan tidak valid")
    Konfirmasi = input("Lanjutkan transaksi? (Ya/Tidak): ")

if Konfirmasi == "Ya":
    print("Silakan lanjut ke pembayaran")
else:
    print("Transaksi dibatalkan")