import time
import threading
from multiprocessing import Process
import os

def is_yuku(n):
    while n > 0:
        n -= 1

def run_threads(n, tekrar):
    threads = []
    basla = time.time()
    for _ in range(tekrar):
        t = threading.Thread(target=is_yuku, args=(n,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return time.time() - basla

def run_processes(n, tekrar):
    processes = []
    basla = time.time()
    for _ in range(tekrar):
        p = Process(target=is_yuku, args=(n,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    return time.time() - basla

if __name__ == "__main__":
    yuk_miktari = 10000000 
    tekrar_sayisi = 4      
    
    print(f"--- KARŞILAŞTIRMA BAŞLIYOR ---\nYük: {yuk_miktari} döngü x {tekrar_sayisi} adet\n")
    
    print("|...| Threading Testi yapılıyor...")
    thread_sure = run_threads(yuk_miktari, tekrar_sayisi)
    print(f"   -> Thread Süresi: {thread_sure:.4f} saniye")
    
    print("\n|...| Multiprocessing Testi yapılıyor...")
    process_sure = run_processes(yuk_miktari, tekrar_sayisi)
    print(f"   -> Process Süresi: {process_sure:.4f} saniye")
    
    print("\n--- SONUÇ ANALİZİ ---")
    if process_sure < thread_sure:
        fark = thread_sure / process_sure
        print(f"/ Multiprocessing, Threading'den {fark:.2f} kat daha hızlı çalıştı.")
        print("// Sebep: İşlem CPU odaklı olduğu için Process'ler farklı çekirdekleri kullandı.")
    else:
        print("- Multiprocessing daha yavaş veya eşit çalıştı.")
        print("-- Sebep: İşlem çok kısaysa, Process oluşturma maliyeti (Overhead) avantajı yok etmiş olabilir.")