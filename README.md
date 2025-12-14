## &nbsp;			---Description---



Selamlar! 👋Bu depoda, İşletim Sistemleri dersinde gördüğümüz Multiprocessing (Çoklu İşlem), Multithreading (Çoklu İş Parçacığı) ve Amdahl Yasası konularını pekiştirmek için yazdığım Python kodları bulunuyor.



Derste gördüğümüz teorik örnekleri ("Hello World" yazdırmak gibi) alıp, gerçek hayatta bu teknolojilerin nerede ve neden kullanıldığını simüle eden küçük projelere dönüştürdüm.



#### **1. Dosya İndirme Simülasyonu (Threading)**

**Dosya:** threading\_download\_sim.py



**Ben Neyi Değiştirdim?** Sayı yazdırmak yerine sanal bir "Dosya İndirme" senaryosu kurdum.



**Neden?** Thread'lerin asıl gücü işlemciyi (CPU) kullanmak değil, bekleme (I/O) gerektiren işleri yönetmektir. Biri internetten veri beklerken program donmasın, diğer dosya inmeye devam etsin istedim.



**Sonuç:** time.sleep() kullanarak internet gecikmesini taklit ettim. Thread'ler sayesinde tüm dosyalar aynı anda iniyormuş gibi oldu.

#### 

#### **2. İşlemciyi Yorma Testi (Multiprocessing)**

**Dosya:** multiprocessing\_cpu\_crunch.py



**Ben Neyi Değiştirdim?** İşlemciye kasten çok ağır matematiksel işlemler (milyonluk döngüler) yaptırdım.



**Neden?** Basit bir çarpma işlemi çok hızlı bittiği için "Paralel Çalışma"nın farkı anlaşılmıyordu. İşlemciyi gerçekten yorarak, çok çekirdekli çalışmanın tek çekirdeğe göre ne kadar hızlı olduğunu kanıtladım.



**Sonuç:** Her işlem (Process) bilgisayarın farklı bir çekirdeğinde çalıştı ve işler çok daha hızlı bitti.



#### **3. Yarış Simülasyonu (Thread vs Process)**

**Dosya:** benchmark\_thread\_vs\_process.py



**Amaç:** "Hangisi daha iyi?" sorusunun cevabının "Duruma göre değişir" olduğunu kanıtlamak.



**Neyi Test Ettim?** Aynı matematik işlemini hem Thread hem de Process kullanarak yaptırdım ve süreleri yarıştırdım.



**Sonuç:** Python'da ağır matematik işlemlerinde Process çok daha hızlı çünkü tüm çekirdekleri kullanıyor. Thread ise tek çekirdeğe sıkışıyor (GIL muhabbeti yüzünden).



#### **4. Amdahl Yasası Hesaplayıcı**

**Dosya:** 4\_amdahls\_law\_calculator.py



**Konu:** Bir bilgisayara 1000 tane de işlemci taksak, programımız neden 1000 kat hızlanmaz?



**Mantık:** Bu kod, bir programın ne kadarının paralelleştirilebileceğine bakarak, donanım eklemenin (Scale-up) sınırlarını hesaplıyor.



**Örnek:** Kodun %50'si seri (tek tek) çalışmak zorundaysa, dünyanın en güçlü bilgisayarını da getirsen maksimum 2 kat hızlanabilirsin. Bunu hesaplayan bir araç yazdım.





















