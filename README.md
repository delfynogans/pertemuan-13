### Nama    : Muhamad Sofhian Permana
### Kelas   : TI.22.C1
### Prodi   : Teknik Informatika
### Matkul  : Bahasa Pemrograman

# Praktikum Lab 9 Pertemuan 13 Penanganan Eksepsi

Eksepsi (exception) merupakan suatu kesalahan (error) yang terjadi saat proses eksekusi program sedang berjalan, kesalahan ini akan menyebabkan program berakhir dengan tidak normal. Kesalahan-kesalahan ini dapat diidentifikasikan dengan nama tertentu dan direpresentasikan sebagai objek di dalam python.

## Contoh Eksepsi / Exceptions

<img width="960" alt="ss eksepsi 1" src="https://user-images.githubusercontent.com/116411792/208586102-6b90c94d-be3c-4979-9f65-cee24aafc4e4.png">

Contoh program diatas adalah salah satu bentuk dari penanganan eksepsi. Eksepsi yang terjadi saat program di 'run'. 

## Contoh Eksepsi / Exceptions dalam blok try except. 

<img width="960" alt="ss eksepsi 3" src="https://user-images.githubusercontent.com/116411792/208622780-0ab5f5ed-86a5-4d15-95e3-6d2d8aa6786e.png">

<img width="960" alt="ss eksepsi 2" src="https://user-images.githubusercontent.com/116411792/208622709-599c7d71-02d4-41db-84ce-c8212d736435.png">

Berikut adalah perbedaan dari program yang menggunakan try except dan tidak. Pada program yang tidak menggunakan try except, karena sebuah bilangan tidak bisa dibagi dengan 0 akan menghasilkan error ZeroDivision Error yang berarti. dengan menggunakan block try except, maka kita bisa membuat program yang tidak akan error jika angka yang dibagi adalah 0. pada contoh kedua jika bilangan yg dibagi hasilnya 0, maka akan menampilkan text "Input tidak boleh nol" untuk menggantikan peringatan error sebelumnya. 

## Contoh Eksepsi / Exceptions dengan multiple except.

<img width="960" alt="ss eksepsi 6" src="https://user-images.githubusercontent.com/116411792/208633989-c989883c-90ba-4bbe-9fa5-749e1a33c1ea.png">

<img width="960" alt="ss eksepsi 6(1)" src="https://user-images.githubusercontent.com/116411792/208633919-6999772d-44da-4cca-8ea5-ee4a1dca33f8.png">

Program diatas adalah sebuah contoh sederhana pada multiple except. Menggunakan aritmatika faktorial. Jika angka nya sesuai, maka akan mencetak angka dan hasilnya. jika di dalam number_list adalah bilangan negatif, bilangan desimal, ataupun text. maka except akan mencetak error / kesalahannya. 

<img width="960" alt="ss eksepsi 7" src="https://user-images.githubusercontent.com/116411792/208634074-204992c5-9bf9-404c-85e8-a73bdfdfdafb.png">

<img width="960" alt="ss eksepsi 7(1)" src="https://user-images.githubusercontent.com/116411792/208634035-bb1479c6-122e-403a-b208-02fbdfb90298.png">

Berikut adalah contoh jika semua isi di dalam number_list merupakan bilangan bulat. 

## Contoh Eksepsi / Exceptions menggunakan try finally clause.

"Finally" block bisa digunakan di dalam blok try except. Namun tidak bisa digunakan dalam else. Jika ingin menggunakan else maka penggunaan finally setelah perintah else. 

<img width="960" alt="ss eksepsi 8" src="https://user-images.githubusercontent.com/116411792/208636436-86dfb799-7b39-4ef2-9e93-27539d9929af.png">

### Contoh lainnya : 

<img width="960" alt="ss eksepsi 9" src="https://user-images.githubusercontent.com/116411792/208640552-8c21f481-f0df-41f1-ae09-047c5ca58de2.png">

<img width="960" alt="ss eksepsi 9(1)" src="https://user-images.githubusercontent.com/116411792/208640587-8815fedc-a80d-47f1-ab96-78b3d632637b.png">

Jika yang diinput bukan berupa angka. maka akan mengeluarkan text agar menginput data dengan benar. Dan jika sesuai maka akan menampilkan hasil dari pembagian 50. 

## Contoh Eksepsi / Argument of an exceptions. 

Jadi, error yang terjadi bisa dijadikan sebagai teks argumen, tidak seperti biasanya yang berupa teks berwarna merah sebagai peringatan. 

<img width="960" alt="ss eksepsi 10" src="https://user-images.githubusercontent.com/116411792/208643486-99def435-6642-4c1f-a358-b737161111f6.png">

Contoh program diatas adalah salah satu penerapan dari error yang dijadikan argumen. Operasi aritmatika tersebut dijumlahkan serta dibagi 0 yang hasilnya akan error "DivisionByZero". namun dengan perintah argumen maka error tersebut menjadi seperti bukan error. 
Fungsi tersebut berguna untuk mengetahui informasi tambahan daripada sebuah program. 

## Contoh dari Eksepsi / Raising an Exceptions

Raise adalah sebuah perintah untuk memaksa program yang tidak sesuai menjadi eksepsi. 
Contoh seperti di bawah, jika angka yang dimasukkan bilangan positif maka program berjalan normal. namun jika angka negatif yang dimasukkan maka akan mengeluarkan eksepsi / error "This is not a positive number" dan program pun berhenti. Raise juga berfungsi untuk memperlihatkan jenis kesalahan yang muncul tetapi bukan dari kesalahan program.

<img width="960" alt="ss eksepsi 11" src="https://user-images.githubusercontent.com/116411792/208649497-2e6ceb3c-75a9-4331-abff-6699264494b9.png">


## Contoh dari Eksepsi / User defined exceptions

User defined Exceptions adalah eksepsi yang dibuat user dengan menggunakan raise. Program menbak huruf yang jika huruf yang dimasukan melebihi/kurang dari huruf yang ditentukan maka fungsi if akan memproses raise, raise yang nantinya memanggil except di akhir program untuk memberikan pernyataan apakah huruf itu benar atau salah. 


<img width="960" alt="ss eksepsi 12" src="https://user-images.githubusercontent.com/116411792/208656280-a8546df2-4ad2-4a52-9349-48386895a3dd.png">

<img width="960" alt="ss eksepsi 12(1)" src="https://user-images.githubusercontent.com/116411792/208656251-427bd16f-d893-4849-adf1-a4159b8b9982.png">

<img width="960" alt="ss eksepsi 12(2)" src="https://user-images.githubusercontent.com/116411792/208656782-088f2214-a99a-46b1-a3f0-cf41c3820d9c.png">




# TERIMA KASIH :)






