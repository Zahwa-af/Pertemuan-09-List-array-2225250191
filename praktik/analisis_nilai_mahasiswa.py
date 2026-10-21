"""
Program: Analisis Nilai Mahasiswa (praktik/analisis_nilai_mahasiswa.py)
Mata Kuliah: Algoritma dan Pemrograman - S1 Pendidikan Matematika Untirta
"""

def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)

def nilai_lulus(data, batas=60):
    hasil = []
    for x in data:
        if x >= batas:
            hasil.append(x)
    return hasil

def main():
    print("=" * 50)
    print("      PRAKTIK 9: ANALISIS NILAI MAHASISWA")
    print("=" * 50)
    
    nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]
    
    jumlah_total = len(nilai)
    total_nilai = sum(nilai)
    avg_nilai = rata_rata(nilai)
    min_nilai = min(nilai)
    max_nilai = max(nilai)
    
    lulus = nilai_lulus(nilai, batas=60)
    jumlah_lulus = len(lulus)
    jumlah_belum_lulus = jumlah_total - jumlah_lulus
    
    print(f"Data Nilai        : {nilai}")
    print("-" * 50)
    print(f"Banyak Data       : {jumlah_total}")
    print(f"Total Nilai       : {total_nilai}")
    print(f"Rata-rata         : {avg_nilai:.2f}")
    print(f"Nilai Minimum     : {min_nilai}")
    print(f"Nilai Maksimum    : {max_nilai}")
    print("-" * 50)
    print(f"Daftar Nilai Lulus: {lulus}")
    print(f"Jumlah Lulus      : {jumlah_lulus} mahasiswa")
    print(f"Jumlah Belum Lulus: {jumlah_belum_lulus} mahasiswa")
    print("=" * 50)

if __name__ == "__main__":
    main()