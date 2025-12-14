from multiprocessing import Process, current_process
import time
import os

def agir_hesaplama(sayi):
    process_id = os.getpid()
    process_name = current_process().name
    
    print(f"<>  İşlem Başladı -> PID: {process_id} ({process_name}) | Sayı: {sayi}")
    
    sonuc = 0
    for i in range(1, sayi * 1000000):
        sonuc += i * i
        
    print(f">|<  İşlem Tamamlandı -> PID: {process_id} | Sonuç Hesaplandı.")

def main():
    start_time = time.time()
    
    veriler = [50, 60, 55, 70]
    
    processes = []
    
    print(f"--- Multiprocessing (Çoklu İşlemci) Başlıyor ---\nAna İşlemci (Parent) PID: {os.getpid()}\n")
    
    for veri in veriler:
        p = Process(target=agir_hesaplama, args=(veri,))
        processes.append(p)
        p.start()
        
    for p in processes:
        p.join()
        
    end_time = time.time()
    print(f"\n|=| Tüm hesaplamalar bitti. Toplam Süre: {end_time - start_time:.2f} saniye")

if __name__ == "__main__":
    main()