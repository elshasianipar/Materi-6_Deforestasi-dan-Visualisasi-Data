import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILE_DATA = ROOT / "data" / "perubahan_tutupan_lahan.csv"
FOLDER_OUTPUT = ROOT / "outputs"
FOLDER_OUTPUT.mkdir(exist_ok=True)


def main():
    area_berubah = []
    with FILE_DATA.open(newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            try:
                luas = float(row["luas_ha"])
                if luas < 0:
                    raise ValueError
            except (ValueError, KeyError):
                print("Baris dilewati karena luas tidak valid:", row)
                continue

            if row["kelas_2021"] != row["kelas_2024"]:
                area_berubah.append({
                    "id_area": row["id_area"],
                    "kelas_2021": row["kelas_2021"],
                    "kelas_2024": row["kelas_2024"],
                    "luas_ha": luas
                })

    total_luas = sum(row["luas_ha"] for row in area_berubah)
    hutan_ke_terbuka = sum(
        row["luas_ha"] for row in area_berubah
        if row["kelas_2021"] == "Hutan"
        and row["kelas_2024"] == "Lahan Terbuka"
    )

    print("=== ANALISIS PERUBAHAN TUTUPAN LAHAN ===")
    print("Jumlah area berubah:", len(area_berubah))
    print(f"Total luas berubah: {total_luas:.2f} ha")
    print(f"Hutan menjadi lahan terbuka: {hutan_ke_terbuka:.2f} ha")
    for row in area_berubah:
        print(f"- {row['id_area']}: {row['kelas_2021']} -> {row['kelas_2024']} ({row['luas_ha']:.2f} ha)")

    output = FOLDER_OUTPUT / "rincian_perubahan.csv"
    with output.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=[
            "id_area", "kelas_2021", "kelas_2024", "luas_ha"
        ])
        writer.writeheader()
        writer.writerows(area_berubah)
    print(f"Rincian disimpan ke: {output}")
    print("Catatan: perubahan kelas tidak otomatis membuktikan penyebab deforestasi.")


if __name__ == "__main__":
    main()
