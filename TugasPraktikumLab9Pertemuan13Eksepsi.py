#Python user-defined exceptions
class ContohException(Exception):
    """Base class for other exceptions"""
pass
class HurufAtas(ContohException):
    """Raised when the entered alphabet is smaller than the actual one"""
pass
class HurufBawah(ContohException):
    """Raised when the entered alphabet is larger than the actual one"""
pass
# we need to guess this alphabet till we get it right
alphabet = 'l'
while True:
    try:
        tekateki = input("Masukkan alphabet: ")
        if tekateki < alphabet:
            raise HurufBawah
        elif tekateki > alphabet:
            raise HurufAtas
        break
    except HurufAtas :
        print("Kelebihan gaes, tebak lagi!")
        print('')
    except HurufBawah:
        print("Masih belum, ayo tebak lagi!")
        print('')
print("Betul. Selamat 2 juta rupiah anda dapatkan jika bekerja.")