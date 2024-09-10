
link pws : http://cahya-bagus-gegeshop2.pbp.cs.ui.ac.id/

1.  - Pertama saya membuat folder gegeshop 
    - Saya menginisialisasi virtual environ dengan nama venv (berguna untuk meletakkan lib yang saya install)
    - Membuat .gitignore agar venv dan cache python tidak di push ke github
    - Membuat requirements.txt untuk menginstall lib-lib yang ada di venv (di github berfungsi memberi tahu orang lain dependancy proyek ini)
    - Menginstall lib dari requirements.txt
    - Menjalankan "django-admin startproject gege-shop . " untuk membuat projek django, titik ada agar projek berada di folder ini bukan membuat folder baru 
    - Menjalankan "python manage.py startapp main" untuk membuat aplikasi main yang di projek ini digunakan      untuk penampilan dan pendaftaran produk
    - Mempush progress ke github dan pws lalu menambahkan allowed host, agar bisa diakses lokal dan link pws
    - Merouting projek dengan app main dengan menambah "main" ke installed apps dan menambahkan 
      path('', include('main.urls')) ke urlspattern agar defaultnya django bisa mengakses urls.py yang ada di app main (saat dijalankan belum ada)
    - Menambahkan BASE_DIR / "templates" agar template main bisa mengextend template base.html
    - Membuat urls.py dalam app main brfungsi untuk memetakan tampilan projek utama dengan views.py 
    - Membuat model sesuai ketentuan dan melakukan migrasi agar bentuk database berubah
    - Membuat folder templates yang berisi .html untuk tampilan web
    - Membuat views.py agar dapat merubah tampilan html sehingga tidak statis
    - Membuat forms.py untuk merekan input yang nantinya akan disampaikan ke database
    - Menjalankan server


2. 

  User -> urls.py -> views.py -> html <- models.py 
                                    
  html -> User
  

    Jadi untuk projek ini normalnya User ke url show_main (karena "" jadinya default kesana) nanti manggil funsgi
    show_main nya views.py nanti ngembaliin html yang diberi isi nama,npm dan kelas oleh views.py dan model Produk dari models.py yang berisi name,price,description 
  
  
  User -> urls.py -> views.py -> html -> forms.py -> db.sqlite3

   Jika User ingin mendaftarkan produk maka akan mengklik tombol buat produk yang mengarahkan ke url create-product yang berisi fungsi create_product dari views.py akan menampilkan html create_product sambil merekan input user ke kelas ProductForm forms.py, forms.py akan mengubah isi database

   snapshot adalah keadaan suatu projek pada saat tertentu 
3. git berfungsi untuk mengontrol versi suatu projek dengan perintah git add(untuk melacak perubahan),commit(untuk menyimpan snapshot ke local),push(untuk menyimpan snapshot ke server git) kita dapat menyimpan snapshot suatu projek dan mengambil snapshot projek dengan git pull(untuk mencoba mengambil dan menyatukan suatu versi ke projek yang dikerjakan) atau git clone(untuk mengubah seluruh isi projek diganti dengan suatu versi snapshit)

4. Mungkin karena django diimplementasika dengan python dan python sendiri merupakan bahasa yang mudah dipahami selain itu mungkin karena django "Batteries included" semua yang dibutuhkan dalam web development sudah ada di django dan mungkin karena perusahaan besar menggunakan django (spotify,youtube,instagram)

5. Karena database di django menggunakan object relational mapping dengan sql, jadi membuat program lebih cepat dan mudah digunakan untuk developer dan user
