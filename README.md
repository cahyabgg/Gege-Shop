
link pws : http://cahya-bagus-gegeshop2.pbp.cs.ui.ac.id/

Tugas 2 [x]
## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    - Pertama saya membuat folder gegeshop 
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


## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

  User -> urls.py -> views.py -> html <- models.py 
                                    
  html -> User
  

    Jadi untuk projek ini normalnya User ke url show_main (karena "" jadinya default kesana) nanti manggil funsgi
    show_main nya views.py nanti ngembaliin html yang diberi isi nama,npm dan kelas oleh views.py dan model Produk dari models.py yang berisi name,price,description 
  
  
  User -> urls.py -> views.py -> html -> forms.py -> db.sqlite3

    Jika User ingin mendaftarkan produk maka akan mengklik tombol buat produk yang mengarahkan ke url create-product yang berisi fungsi create_product dari views.py akan menampilkan html create_product sambil merekan input user ke kelas ProductForm forms.py, forms.py akan mengubah isi database

   
## 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!

git berfungsi untuk mengontrol versi suatu projek dengan perintah git add(untuk melacak perubahan),commit(untuk menyimpan snapshot ke local),push(untuk menyimpan snapshot ke server git) kita dapat menyimpan snapshot (snapshot adalah keadaan suatu projek pada saat tertentu )suatu projek dan mengambil snapshot projek dengan git pull(untuk mencoba mengambil dan menyatukan suatu versi ke projek yang dikerjakan) atau git clone(untuk mengubah seluruh isi projek diganti dengan suatu versi snapshot)

## 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Mungkin karena django diimplementasika dengan python dan python sendiri merupakan bahasa yang mudah dipahami selain itu mungkin karena django "Batteries included" semua yang dibutuhkan dalam web development sudah ada di django dan mungkin karena perusahaan besar menggunakan django (spotify,youtube,instagram)

## 5. Mengapa model pada Django disebut sebagai ORM?

Karena database di django menggunakan object relational mapping dengan sql, jadi membuat program lebih cepat dan mudah digunakan untuk developer dan user

Tugas 3 [x]

### 1. Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery diperlukan dalam pengimplementasian platform karena berfungsi untuk memastikan data dapat diakses secara cepat, akurat, dan aman oleh pengguna. Hal ini penting agar aplikasi atau platform dapat beroperasi secara optimal, memungkinkan interaksi real-time, serta mendukung analisis data dan pengambilan keputusan yang efektif. Data delivery juga berperan dalam menjaga integritas dan konsistensi data yang didistribusikan, baik dalam sistem terdistribusi maupun terpusat.

Referensi:  
- Silva, R. et al. (2021). *Data delivery and its importance in distributed systems*. Journal of Information Systems.  
- Stankovic, J. et al. (2020). *Real-time Data Delivery in Modern Applications*. IEEE Communications.


### 2. Mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Antara XML dan JSON, JSON umumnya dianggap lebih baik dalam banyak situasi karena lebih ringkas, mudah dibaca, dan efisien untuk dikirim melalui jaringan. JSON mendukung struktur data yang langsung seperti objek, array, string, dan angka, yang membuatnya cocok untuk pertukaran data dalam aplikasi web modern.

Beberapa alasan JSON lebih populer dibandingkan XML:

  - **Sintaks yang Lebih Sederhana**: JSON menggunakan struktur yang lebih minimalis dan mudah dipahami dibandingkan XML yang memiliki tag pembuka dan penutup.
  - **Ukuran Lebih Kecil**: Data dalam JSON biasanya lebih ringkas dibandingkan XML karena tidak membutuhkan tag berulang.
  - **Kinerja Lebih Baik**: Parsing JSON lebih cepat dan memakan lebih sedikit memori dibandingkan XML, terutama dalam aplikasi web.
  - **Dukungan di JavaScript**: JSON adalah format asli yang didukung oleh JavaScript, sehingga lebih praktis untuk aplikasi berbasis web.

Namun, XML masih berguna dalam situasi tertentu, seperti ketika diperlukan **validasi data** yang lebih kuat melalui DTD atau XML Schema.

**Referensi**:  
- Bray, T. (2014). The JavaScript Object Notation (JSON) Data Interchange Format.  
- W3C. (2015). Extensible Markup Language (XML) 1.0.

### 3. Fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkannya?

Method `is_valid()` pada form Django digunakan untuk memvalidasi data yang dimasukkan oleh pengguna ke dalam form. Method ini:
  - Memeriksa apakah semua field di form sudah diisi sesuai dengan aturan yang ditetapkan (misalnya, format email harus benar, field yang diperlukan tidak boleh kosong, dsb).
  - Mengembalikan `True` jika form valid dan `False` jika tidak valid.
  - Jika valid, method ini juga menyediakan data yang telah dibersihkan (`cleaned_data`) yang siap untuk diproses lebih lanjut (misalnya, disimpan ke database).

Kita memerlukan `is_valid()` untuk memastikan bahwa data yang akan kita proses benar dan sesuai dengan aturan validasi yang ditetapkan. Ini penting untuk mencegah adanya data yang tidak valid atau berbahaya (seperti input yang tidak diinginkan atau serangan injeksi) masuk ke dalam sistem.

### 4. Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

**CSRF (Cross-Site Request Forgery)** adalah jenis serangan di mana seorang penyerang dapat memaksa pengguna yang telah login ke suatu situs untuk melakukan tindakan yang tidak diinginkan tanpa sepengetahuan mereka. Django menggunakan token CSRF untuk mencegah serangan ini.

- **Mengapa kita membutuhkan `csrf_token`**: Token CSRF adalah token unik yang dihasilkan oleh server untuk setiap permintaan dari form. Token ini dikirimkan bersama form dan harus dicocokkan dengan token yang ada di server. Jika token tidak sesuai, Django akan menolak permintaan tersebut.
  
- **Apa yang dapat terjadi tanpa `csrf_token`**: Jika kita tidak menggunakan `csrf_token`, penyerang bisa mengirimkan permintaan ke aplikasi kita melalui browser korban yang telah login (misalnya dengan cara mengirimkan link berbahaya atau form tersembunyi). Ini memungkinkan penyerang melakukan tindakan yang sah seperti mengubah data atau membuat transaksi tanpa sepengetahuan korban.

- **Bagaimana penyerang dapat memanfaatkan**: Penyerang dapat memanfaatkan kelemahan ini dengan mengirimkan permintaan dari situs berbahaya ke situs kita atas nama pengguna yang sah. Jika tidak ada perlindungan CSRF, permintaan ini akan diterima oleh server seolah-olah dibuat oleh pengguna yang sah. Akibatnya, penyerang dapat mengambil alih fungsi aplikasi secara tidak sah.

### 5. Bagaimana cara mengimplementasikan checklist di atas secara step-by-step?

**Langkah-langkah implementasi**:

1. **Setup Proyek Django**:
   - Inisialisasi proyek Django baru atau masuk ke proyek yang ada.
   - Buat aplikasi baru dengan perintah `python manage.py startapp <app_name>`.

2. **Buat Model dan Form**:
   - Definisikan model (misalnya, untuk menyimpan data pengguna atau produk) dalam file `models.py`.
   - Buat form berdasarkan model tersebut dengan menggunakan `ModelForm` di `forms.py`. Ini akan otomatis membuat form sesuai dengan struktur model.
   
3. **Tambahkan Form ke Views**:
   - Di `views.py`, buat view untuk menampilkan dan memproses form. Gunakan form yang sudah dibuat dan tambahkan logika untuk memeriksa apakah form valid menggunakan method `is_valid()`.
   - Contoh:
     ```python
     from django.shortcuts import render
     from .forms import MyForm
     
     def my_view(request):
         if request.method == 'POST':
             form = MyForm(request.POST)
             if form.is_valid():
                 # proses form
                 return redirect('success_url')
         else:
             form = MyForm()
         return render(request, 'template.html', {'form': form})
     ```

4. **Gunakan CSRF Protection**:
   - Saat membuat template HTML untuk form, tambahkan tag `{% csrf_token %}` di dalam `<form>`. Ini penting agar Django bisa memvalidasi form yang dikirim dengan token CSRF yang dihasilkan.
   - Contoh:
     ```html
     <form method="post">
         {% csrf_token %}
         {{ form.as_p }}
         <button type="submit">Submit</button>
     </form>
     ```

5. **Validasi Form**:
   - Dalam view, pastikan untuk memanggil `is_valid()` agar data pengguna tervalidasi dengan benar sebelum disimpan atau diproses. Jika form tidak valid, tampilkan pesan kesalahan kembali ke pengguna.

6. **Testing**:
   - Uji aplikasi secara menyeluruh dengan berbagai skenario untuk memastikan bahwa form hanya dapat diproses ketika data valid dan dilindungi dari serangan CSRF. Cek juga apakah `csrf_token` bekerja dengan baik.

Setiap langkah di atas bukan hanya mengikuti tutorial, tetapi memerlukan pemahaman konsep dasar dan cara kerja Django serta pentingnya validasi dan keamanan (seperti CSRF). Pemahaman ini membantu dalam mengadaptasi dan memperbaiki aplikasi sesuai kebutuhan real-world.