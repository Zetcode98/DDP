import math

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def pangkat(a):
    return a**2

def kali(a, b):
    return a * b

def bagi(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Pembagian oleh nol"
    
def akar(a):
    return math.sqrt(a)

def log(angka):
    return math.log(angka)

def sin(sudut):
    return math.sin(math.radians(sudut))

def cos(sudut):
    return math.cos(math.radians(sudut))

def tan(sudut):
    return math.tan(math.radians(sudut))