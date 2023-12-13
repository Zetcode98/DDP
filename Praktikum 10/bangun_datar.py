import math

def lingkaran(r):
    return 22/7 * r**2

def keliling_lingkaran (phi,r): 
    return phi * r**2

def segitiga (alas,tinggi): 
    return alas * tinggi/2

def keliling_segitiga (a,b,c):
    return a+b+c

def persegi(sisi):
    return sisi * sisi

def keliling_persegi(sisi):
    return 4* sisi

def persegi_panjang(panjang,lebar):
    return panjang*lebar

def keliling_persegipanjang (panjang,lebar): 
    return 2 * panjang + lebar

def jajargenjang(alas,tinggi):
    return alas * tinggi

def keliling_jajargenjang (a,b):
    return 2 * a + b

def belahketupat(diagonal1, diagonal2):
    return diagonal1 * diagonal2 * 1/2

def keliling_belahketupat(sisi):
    return 4 * sisi

def trapesium(tinggi):
    return 1/2 * tinggi

def keliling_trapesium(a,b,c,d):
    return a + b + c + d