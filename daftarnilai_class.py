from os import system

class Mahasiswa:
	nim=''
	nama=''
	tugas=''
	uts=''
	uas=''
	akhir=''

pilih = 0
dataSiswa = []

def menu():
	system('cls')
	print("Menu Aplikasi Data Mahasiswa");
	print("-------------------------------------------")
	print("1. Input Data Mahasiswa")
	print("2. Tampilkan Data Mahasiswa")
	print("3. Update Data Mahasiswa")
	print("4. Hapus Data Mahasiswa")
	print("5. Keluar Aplikasi")
	pilih = int(input("Masukkan pilihan anda : "))
	if pilih == 1 :
		pilih1()
		menu()
	elif pilih == 2:
		tampil()
		input("kembali menu utama")
		menu()
	elif pilih == 3:
		index_update=-1
		tampil()
		id_edit = int(input("Input Nim yang akan di update ")) 
		for a in range(0, len(dataSiswa)): 
			if id_edit == dataSiswa[a].nim: 
					index_update = a 
					break 
		if(index_update > -1): 
			print("INPUT DATA YANG DI UPATE ") 
			siswa = Mahasiswa() 
			siswa.nim = (int(input("masukkan nim : "))) 
			siswa.nama = (input("masukkan nama siswa : "))
			siswa.tugas = (float(input("Masukkan Nilai Tugas : ")))
			siswa.uts = (float(input("Masukkan Nilai UTS : ")))
			siswa.uas = (float(input("Masukkan Nilai UAS : ")))
			siswa.akhir= siswa.tugas * 0.30 + siswa.uts * 0.35 + siswa.uas * 0.35
			dataSiswa[index_update] = siswa 
			print("berhasil update data siswa") 
		else : print("nim tidak ditemukan") 
		input("kembali menu utama") 
		menu()
	elif pilih ==4:
		system('cls') 
		tampil()
		index_delete=-1
		id_hapus = int(input("Input Nim yang akan di hapus : ")) 
		for a in range(0, len(dataSiswa)): 
			if id_hapus == dataSiswa[a].nim:
					index_delete = a
					break
		if(index_delete > -1):
			del dataSiswa[index_delete]
			print("Data Telah di hapus") 
		else : print("nim tidak ditemukan")
		input("kembali menu utama") 
		menu()
		menu()
	elif pilih == 5 :
		exit()

def tampil():
	system('cls');
	print("DATA MAHASISWA")
	for data in dataSiswa:
		print("Nim : "+str(data.nim)) 
		print("Nama : "+data.nama)
		print("Nilai Tugas : "+str(data.tugas))
		print("Nilai UTS : "+str(data.uts))
		print("Nilai UAS : "+str(data.uas))
		print("Nilai Akhir : "+str(data.akhir))
		print("----------------------")
		

def pilih1():
	ulang = 'Y'
	while ulang in('y', 'Y'):
		system('cls')
		siswaBaru = Mahasiswa() 
		print("INPUT DATA MAHASISWA ") 
		siswaBaru.nim = (int(input("Masukkan NIM : "))) 
		siswaBaru.nama = (input("Masukkan Nama Mahasiswa : "))
		siswaBaru.tugas = (float(input("Masukkan Nilai Tugas : ")))
		siswaBaru.uts = (float(input("Masukkan Nilai UTS : "))) 
		siswaBaru.uas = (float(input("Masukkan Nilai UAS : ")))
		siswaBaru.akhir = siswaBaru.tugas * 0.30 + siswaBaru.uts * 0.35 + siswaBaru.uas * 0.35
		dataSiswa.append(siswaBaru)
		ulang = input("Apakah Anda Ingin Mengulang (Y/ T)? ")		

menu()