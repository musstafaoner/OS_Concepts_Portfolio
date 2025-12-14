import threading
import time
import random

def dosya_indir(dosya_adi, boyut_mb):
    print(f"<>  [{dosya_adi}] indirilmeye başlandı... (Boyut: {boyut_mb} MB)")
    
    indirme_suresi = boyut_mb / 100  
    time.sleep(indirme_suresi) 
    
    print(f">|<  [{dosya_adi}] indirme tamamlandı! (Geçen süre: {indirme_suresi} sn)")

def main():
    baslangic = time.time()
    
    dosyalar = [
        ("Veri_Seti_1.csv", 300),
        ("Gorsel_Paketi.zip", 500),
        ("Sunucu_Loglari.txt", 200),
        ("Egitim_Videosu.mp4", 400)
    ]
    
    threads = []
    
    print("--- Thread (İş Parçacığı) Tabanlı İndirme Başlıyor ---\n")
    
    for ad, boyut in dosyalar:
        t = threading.Thread(target=dosya_indir, args=(ad, boyut))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
        
    bitis = time.time()
    print(f"\n|=| Tüm indirmeler tamamlandı. Toplam Süre: {bitis - baslangic:.2f} saniye")

if __name__ == "__main__":
    main()