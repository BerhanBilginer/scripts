#!/usr/bin/env python3
import re
import argparse
import pandas as pd

def count_unique_names_in_range(file_path: str, cell_range: str, sheet_name=0) -> int:
    """
    Excel'den tek bir sütundaki belirli hücre aralığını (örneğin "D2:D1571")
    okuyup içindeki benzersiz string değerleri sayar.
    """
    # Hücre aralığını parse et (aynı sütun)
    m = re.match(r'^([A-Z]+)(\d+):\1(\d+)$', cell_range.upper())
    if not m:
        raise ValueError("Hücre aralığı 'D1:D1571' formatında ve aynı sütun olmalı.")
    col_letter, start_row, end_row = m.group(1), int(m.group(2)), int(m.group(3))

    # usecols ile sadece ilgili sütunu oku; header=0 ile ilk satırı başlık olarak al
    df = pd.read_excel(
        file_path,
        sheet_name=sheet_name,
        usecols=col_letter,
        header=0
    )

    # Gerçek sütun adını al ve slice et
    col_name = df.columns[0]
    series = df[col_name].iloc[start_row - 1 : end_row]

    # NaN değilse string'e çevirip kırp
    names = [str(v).strip() for v in series if pd.notna(v)]
    unique = set(names)

    print(f"Found {len(unique)} unique names in range {cell_range}:")
    for name in sorted(unique):
        print(f"- {name}")

    return len(unique)


def main():
    parser = argparse.ArgumentParser(
        description="Excel dosyasındaki tek bir sütundaki hücre aralığındaki "
                    "benzersiz isimleri sayar."
    )
    parser.add_argument(
        '--excel_file', '-f',
        required=True,
        help="Excel dosya yolu (ör. /path/to/file.xlsx)"
    )
    parser.add_argument(
        '--cell_range', '-r',
        required=True,
        help="Tarayacağınız hücre aralığı (örn. D2:D1571)"
    )
    parser.add_argument(
        '--sheet', '-s',
        default=0,
        help="Sayfa adı veya indeksi (default=0).",
        # eğer girdi rakamsa int'e çevir, değilse olduğu gibi bırak
        type=lambda x: int(x) if x.isdigit() else x
    )

    args = parser.parse_args()
    count_unique_names_in_range(
        file_path=args.excel_file,
        cell_range=args.cell_range,
        sheet_name=args.sheet
    )


if __name__ == "__main__":
    main()
