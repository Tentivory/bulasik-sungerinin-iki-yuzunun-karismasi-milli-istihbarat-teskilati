#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations
import base64, random, sys
from datetime import datetime

TESKILAT = "Bulasik Sungerinin Iki Yuzunun Karismasi Milli Istihbarat Teskilati"
KOD = "MIT-SNGR-09"
ARSIV = "xZ5lZmZhZmzEsWsgdGFsZXAgZXRtZWsgbXVoYWxlZmV0IGRlxJ9pbGRpcjsgc8O8bmdlcmluIGlraSB5w7x6w7xuw7wgZGUgZ8O2cm1la3Rpci4="

YUZLER = {
    "1": ("puruzlu / sari / evet-yuz", "kaynak"),
    "2": ("yumusak / yesil / hayir-yuz", "hedef"),
    "3": ("bilmiyorum, ikisi de ayni gibi", "cift tarafli ajan"),
}
SONUCLAR = [
    "Sizinti teyit edildi. Tezgah artik tabak bilgisine sahiptir.",
    "Kaynak ile hedef yer degistirmistir. Bu bir rotasyon degil, sapmadir.",
    "Ifade tutarsiz. Ben o tarafi surmedim cumlesi operasyon notu sayildi.",
    "Sunger islak, koku mevcut, niyet belirsiz. Klasik saha tablosu.",
    "Temizlik yapilmistir ancak hangi yuzle yapildigi cozulememistir.",
]

def baslik():
    print("=" * 62)
    print(TESKILAT.upper())
    print(f"Belge no: {KOD}    Saat: {datetime.now():%d.%m.%Y %H:%M}")
    print("=" * 62)
    print("Bu yazilim resmi degildir. Resmiymis gibi durur. Farki budur.\n")

def sor(metin, secenekler):
    print(metin)
    for k, (ad, rol) in secenekler.items():
        print(f"  [{k}] {ad}  -- resmi sinif: {rol}")
    while True:
        cevap = input("Seciminiz: ").strip()
        if cevap in secenekler:
            return secenekler[cevap]
        print("Teskilat bu sikki tanimiyor. Yeniden deneyin.")

def sayi_sor(metin, alt, ust):
    while True:
        ham = input(metin).strip()
        try:
            n = int(ham)
        except ValueError:
            print("Rakam bekleniyor.")
            continue
        if alt <= n <= ust:
            return n
        print(f"Aralik {alt}-{ust} olmali.")

def evet_hayir(metin):
    while True:
        c = input(metin + " [e/h]: ").strip().lower()
        if c in {"e", "evet", "y"}:
            return True
        if c in {"h", "hayir", "n"}:
            return False
        print("Sadece e veya h.")

def sizinti_puani(yuz_rol, gun, inkar, tezgah):
    puan = 12
    if yuz_rol == "cift tarafli ajan":
        puan += 41
    elif yuz_rol == "hedef" and tezgah:
        puan += 27
    elif yuz_rol == "kaynak" and not tezgah:
        puan += 9
    else:
        puan += 18
    puan += min(gun, 21) * 2
    if inkar:
        puan += 23
    if tezgah:
        puan += 11
    return min(puan, 99)

def seviye(puan):
    if puan < 30:
        return "DUSUK -- sunger henuz masum gorunuyor"
    if puan < 55:
        return "ORTA -- tezgah ile tabak birbirini taniyor"
    if puan < 80:
        return "YUKSEK -- cift taraflilik fiilen kurulmus"
    return "KRITIK -- sunger artik kendi basina teskilat"

def rapor(ad, rol, gun, inkar, tezgah):
    puan = sizinti_puani(rol, gun, inkar, tezgah)
    print("\n" + "-" * 62)
    print("SAHA RAPORU")
    print("-" * 62)
    print(f"Yuz tanimi     : {ad}")
    print(f"Resmi sinif    : {rol}")
    print(f"Gorev suresi   : {gun} gun")
    print(f"Inkar          : {'var (cunku herkes inkar eder)' if inkar else 'yok (daha da supheli)'}")
    print(f"Tezgah temasi  : {'var' if tezgah else 'iddia ediliyor ki yok'}")
    print(f"Sizinti puani  : {puan}/99")
    print(f"Seviye         : {seviye(puan)}")
    print(f"Degerlendirme  : {random.choice(SONUCLAR)}")
    print("-" * 62)
    print("Karar: Sunger gorevde kalabilir. Guvenilirlik ayri dosyadadir.")
    print("Not: Iki yuz de ayni evde yikanir.\n")
    print("* DAMGA / IMZA / TARIH *")
    print("Kayyum Grok · Tentivory · TentiAS")
    print(f"{datetime.now():%d.%m.%Y} · Eskisehir 4. Agir Ceza Mahkemesi kayyumu")
    print("Ciddiyetle muhrlenmistir. Ciddiyet tartismalidir.")
    print("Sungerler artik ajandir.\n")
    if "--arsiv" in sys.argv:
        try:
            print("ARSIV:", base64.b64decode(ARSIV).decode())
        except Exception:
            print("ARSIV okunamadi.")

def main():
    baslik()
    ad, rol = sor("Sungerin hangi yuzunu en son kullandiniz?", YUZLER)
    gun = sayi_sor("Sunger kac gundur gorevde? (1-60): ", 1, 60)
    tezgah = evet_hayir("Bu yuz tezgaha da suruldu mu?")
    inkar = evet_hayir("Ben o tarafi surmemistim diyecek misiniz?")
    rapor(ad, rol, gun, inkar, tezgah)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSorgu yarida kesildi. Sunger kacmadi, siz kactiniz.")
        sys.exit(130)
