def amdahl_hesapla(paralel_oran, islemci_sayisi):
    seri_oran = 1 - paralel_oran
    hizlanma = 1 / (seri_oran + (paralel_oran / islemci_sayisi))
    return hizlanma

def main():
    print("--- Amdahl Yasası Simülatörü ---")
    print("Bir programın ne kadarının paralel yapılabildiğine göre,")
    print("işlemci sayısını artırmanın performansa etkisini hesaplar.\n")
    
    try:
        p_input = float(input("Programın paralel yapılabilir kısmı (% olarak, örn: 70 için 70 yazın): "))
        paralel_oran = p_input / 100
        
        # Farklı işlemci sayıları için senaryolar
        senaryolar = [1, 2, 4, 8, 16, 32, 128, 1000]
        
        print(f"\n{'Çekirdek Sayısı (N)':<20} | {'Teorik Hızlanma (Speedup)':<25}")
        print("-" * 50)
        
        for n in senaryolar:
            sonuc = amdahl_hesapla(paralel_oran, n)
            print(f"{n:<20} | {sonuc:.2f}x")
            
        max_hizlanma = 1 / (1 - paralel_oran)
        print("-" * 50)
        print(f"\n DİKKAT: Sonsuz sayıda işlemciniz olsa bile,")
        print(f"programın seri kısmı ({100-p_input}%) yüzünden")
        print(f"ulaşabileceğiniz MAKSİMUM hızlanma: {max_hizlanma:.2f}x olacaktır.")
        
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz.")

if __name__ == "__main__":
    main()