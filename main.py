import nyugta
import etlap
import rendeles

levesek = ["Húsleves", "Gyümölcsleves", "Bableves"]
levesek_ar = [1000, 600, 800]
foetelek = ["Rántotthús", "Töltöttkáposzta", "Pörkölt"]
foetele_ar = [2000, 1600, 1800]

etlap.kiir2(); etlap.kiir2("|           LEVESEK:         |", 1); etlap.kiir2()
etlap.kiir(levesek, levesek_ar)
etlap.kiir2(); etlap.kiir2("|           FŐÉTELEK:        |", 1); etlap.kiir2()
etlap.kiir(foetelek, foetele_ar)
etlap.kiir2(); etlap.kiir2("|           RENDELÉS:        |", 1); etlap.kiir2()
rendeles.rendeles1(levesek,levesek_ar,foetelek,foetele_ar)
