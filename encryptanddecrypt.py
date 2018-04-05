import pyperclip

pesan = raw_input("Masukkan kata yang mau di encrypt : ")
kunci = input("Masukkan kuncinya : ")
mode = 'encrypt'
HURUF ='ABCDEFGHIJKLMNOPWRSTUVWXYZ'
ubah = ''
pesan = pesan.upper()
for symbol in pesan:
	if symbol in HURUF:
		nomor = HURUF.find(symbol)
		if mode == 'encrypt':
			nomor = nomor + kunci
		elif mode == 'decrypt':
			nomor = nomor - kunci
		#jika pesan yang diproses lebih besar dari atau lebih kecil
		#atau sama dengan nol/tidak ada
		if nomor >= len(HURUF):
			nomor = nomor - len(HURUF)
		elif nomor < 0:
			nomor = nomor + len(HURUF)
		#jumlah symbol pada proses enkripsi/dekripsi ditambahkan
		#pada proses akhir pengubahan
		ubah = ubah + HURUF[nomor]
	else :
		ubah = ubah + symbol
print(ubah)
#menyalin hasil enkripsi/dekripsi pada penyimpanan sementara
pyperclip.copy(ubah)

print "*" * 20
print "Berikut Hasil Decrypt : "

# pesan = 'JOEPOFTJB SBZB'
pesan1 = ubah
#kumpulan HURUF yang digunakan untuk menebak huruf kunci
HURUF = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#coba seluruh kunci yang memungkinkan
for kunci1 in range(len(HURUF)):
	#ubah tetap memiliki string kosong seperti sebelumnya telah dijelaskan
	ubah1 = ''
#bagian akhir dari proram ini hampir sama dengan program asli Caesar Cipher
#kode enkripsi dan dekripsi berjalan dan melakukan tugasnya pada string pesan
	for symbol in pesan1:
		if symbol in HURUF:
			#mencari jumlah simbol dalam huruf
			nomor = HURUF.find(symbol)
			nomor = nomor - kunci1
			#menangani proses dimana jumlah lebih dari 26 atau kurang dari 0
			if nomor < 0:
				nomor = nomor + len(HURUF)
			#tambahkan jumlah simbol pada akhir pengubahan
			ubah1 = ubah1 + HURUF[nomor]
		else:
			#tambahkan symbol tanpa melakukan enkripsi/dekripsi
			ubah1 = uba1h + symbol
#tampilkan kunci yang telah dicoba selama melakukan dekripsi
	print('Key #%s: %s' % (kunci1, ubah1))