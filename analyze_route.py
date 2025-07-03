#!/usr/bin/env python3
# analyze_route.py

import argparse
import sys
import pandas as pd

def _to_time_series(col: pd.Series) -> pd.Series:
    """
    'SeferSaati' kolonu datetime64 veya object (str) gelebilir.
    Tümü datetime.time tipine çevrilir ve format '%H:%M:%S' kullanılarak parse edilir.
    """
    if pd.api.types.is_datetime64_any_dtype(col):
        return col.dt.time
    cleaned = (col.astype(str)
                  .str.replace(r'Ö[ÖS]', '', regex=True)
                  .str.strip())
    return pd.to_datetime(cleaned, format="%H:%M:%S", errors='coerce').dt.time

def list_all_by_row(df: pd.DataFrame):
    """
    Satır sırasına göre her HatAdi'ni ilk gördüğü anda başlık olarak alır,
    ve o hattın tüm sefer kayıtlarını kronolojik (saat) olarak listeler.
    """
    df2 = df.copy()
    df2['SeferSaati'] = _to_time_series(df2['SeferSaati'])
    df2['ExcelRow'] = df2.index + 2

    seen = set()
    for _, row in df2.iterrows():
        hat = row['HatAdi']
        if pd.isna(hat) or hat in seen:
            continue
        seen.add(hat)
        print(f"\n=== {hat} ===")
        # bu hattın tüm kayıtlarını saat ve satır sırasına göre sırala
        sub = df2[df2['HatAdi'] == hat].copy()
        sub = sub.sort_values(['SeferSaati', 'ExcelRow'], na_position='last')
        for _, r in sub.iterrows():
            t = r.SeferSaati.strftime('%H:%M') if pd.notna(r.SeferSaati) else '??'
            print(f"• Satır {r.ExcelRow}: {r.Yon}, Saat={t}, Süre={r.SeferSuresi}, Plaka={r.AracNo}")
        print()

def analyze_pair(df: pd.DataFrame, hatadi: str, yon: str):
    """
    Belirli bir HatAdi+Yon için seferleri kronolojik (saat) olarak listeler.
    """
    df2 = df.copy()
    df2['SeferSaati'] = _to_time_series(df2['SeferSaati'])
    df2['ExcelRow']   = df2.index + 2

    matches = df2[(df2['HatAdi'] == hatadi) & (df2['Yon'] == yon)].copy()
    if matches.empty:
        print(f"[!] Hiç eşleşme yok: {hatadi} — {yon}")
        return

    # kronolojik olarak sırala
    matches = matches.sort_values(['SeferSaati', 'ExcelRow'], na_position='last')

    print(f"\n=== {hatadi} — {yon} (Toplam {len(matches)}) ===")
    for _, r in matches.iterrows():
        t = r.SeferSaati.strftime('%H:%M') if pd.notna(r.SeferSaati) else '??'
        print(f"• Satır {r.ExcelRow}: Saat={t}, Süre={r.SeferSuresi}, Plaka={r.AracNo}")
    print()

def main():
    parser = argparse.ArgumentParser(
        description="Satır sırasına ve saate göre HatAdi bazlı sefer listesi çıkarır."
    )
    parser.add_argument('-f', '--excel_file', required=True, help="Excel dosyası")
    parser.add_argument('-s', '--sheet_name', default=0, help="Sayfa adı/indeksi (default: 0)")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-r', '--row',    type=int, metavar='SATIR',
                       help="Tek satır numarası (o satırın Hat+Yon’una bak)")
    group.add_argument('-v', '--values', nargs=2, metavar=('HAT','YON'),
                       help='Manuel HatAdi ve Yon, örn. -v "ÇİLEKLİ ZAFANOZ" "Gidiş"')
    group.add_argument('--all', action='store_true',
                       help="Her hattın tüm seferlerini kronolojik sırala ve listeler")

    args = parser.parse_args()

    try:
        df = pd.read_excel(args.excel_file, sheet_name=args.sheet_name)
    except Exception as e:
        sys.exit(f"Dosya okunamadı → {e}")

    if args.all:
        list_all_by_row(df)
        return

    if args.row is not None:
        idx = args.row - 2
        if not 0 <= idx < len(df):
            sys.exit("Satır aralık dışında")
        hatadi, yon = df.at[idx, 'HatAdi'], df.at[idx, 'Yon']
    else:
        hatadi, yon = args.values

    analyze_pair(df, hatadi, yon)

if __name__ == '__main__':
    main()
