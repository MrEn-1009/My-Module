from module1 import *
while True:
    print('Z=arithmetic, X= is_year_leap,C=square,V=season,A=xor_cipher')
    v=input()
    if v.upper()=='Z':
        arv1=float(input('Arv1:'))
        arv2=float(input('Arv 2:'))
        sym=input('Tehe:')
        rezult=arithmetic(arv1,arv2,sym)
        print(rezult)
    elif v.upper()=='X':
        a=int(input('Sisesta aasta: '))
        rezult=is_year_leap(a)
        print(rezult)
    elif v.upper()=='C':
        a=float(input('Ruudu külk: '))
        rezult=square(a)
        print(rezult)
    elif v.upper()=='V':
        a=int(input('Sisesta aastaajad'))
        rezult=season(a)
        print(rezult)
    elif v.upper()=='B':
        a=float(input('Sisesta summa miline tahate sisse panna'))
        y=int(input('Mitu aastad deposiit kehtib'))
        rezult=bank(a,y)
        print(rezult)
    elif v.upper()=='A':
        print('Kodeerimine'.center(60,'*'))
        rezult=xor_cipher(input('Sisesta text: '),input('Sisesta võti:'))
        print(rezult)
        print('Dekodeerimine'.center(60,'*'))
        de_rezult=xor_uncipher(rezult, input('Sisesta võti: '))
        print(de_rezult)
    elif v.upper()=='N':
        a=int(input('Sisesta number: '))
        rezult=is_prime(a)
        print(rezult)
    elif v.upper()=='M':
        pass
