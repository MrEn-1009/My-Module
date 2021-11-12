from math import *
def arithmetic(a:float,b:float,c:str):
    '''Lithne kalkulaator
    + - liitmine,, - - laahutamine, * - korrutamine, / - jagamine
    :param float a: Esimene arv
    :param float b: Teine arv
    :param str c: Aritmeetiline tehing
    :rtype var: Märamata tüüb
    '''
    if c=='+':
        r=a+b
    elif c=='-':
        r=a-b
    elif c=='*':
        r=a*b
    elif c=='/':
        if b!=0:
            r=a/b
        else:
            r='Div/0'
    else:
        r='Tundmatu sym'
    return r
def is_year_leap(a:int)->str:
    '''Liigaasta leidmine
    Tagastab true kui aasta on liigaasta ja False kui ei ole
    :param int aasta: Aasta number
    :rtype bool: Funktsioni vastus loogilises formaadis
    '''
    if type(a/4)==int:
        print('True')
    elif type(a/4)==float:
        print('False')
    return r
def square(a:float)->float:
    '''
    '''
    d=sqrt(a**2+a**2)
    p=4*a
    s=a*a
    r=(p,s,d)
    return r
def season(a:int):
    if a==12 or 0<a<3:
        print('Talv')
    elif 2<a<6:
        print('Kevad')
    elif 5<a<9:
        print('Suvi')
    elif 8<a<12:
        print('Sügis')
    else:
        print('Kirjuta ainult aastaajad')
    return a
def bank(a:float,y:int):
    '''
    '''
    for i in range(y):
        a=((1.1*1/100)*a)*100
    return a
def is_prime(a:int):
    '''
    '''
    z=2
    while a%z!=0:
        z+1
    return z==a
def date(d:int,m:int,y:int):
    if type(y/4)==int:
        if m==1 and d<32:
            print(f'Päev:{d} /nKuu:{m} /nAasta:{y}')
        elif m==2 and d<29:
            print(f'Päev:{d} /nKuu:{m} /nAasta:{y}')
        elif m==3 and d<32:
            print(f'Päev:{d} /nKuu:{m} /nAasta:{y}')
        elif m==4 and d<31:
            print(f'Päev:{d} /nKuu:{m} /nAasta:{y}')
        elif m==5 and d<32:
            print(f'Päev:{d} /nKuu:{m} /nAasta:{y}')
        elif m==6 and d<31:
            print(f'Päev:{d} /nKuu:{m} /nAasta:{y}')
        elif m==7 and d<32:
            print(f'Päev:{d} /nKuu:{m} /nAasta:{y}')
        elif m==8 and d<32:
            print(f'Päev:{d} /nKuu:{m} /nAasta:{y}')
        elif m==9 and d<31:
            print(f'Päev:{d} /nKuu:{m} /nAasta:{y}')
        elif m==10 and d<32:
            print(f'Päev:{d} /nKuu:{m} /nAasta:{y}')
        elif m==11 and d<31:
            print(f'Päev:{d} /nKuu:{m} /nAasta:{y}')
        elif m==12 and d<32:
            print(f'Päev:{d} /nKuu:{m} /nAasta:{y}')
        else:
            print('Viga')
    elif type(y/4)==float:
        if m==1 and d<32:
            print(f'Päev:{d} /nKuu:{m} /nAasta:{y}')
        elif m==2 and d<28:
            print(f'Päev:{d} /nKuu:{m} /nAasta:{y}')
        elif m==3 and d<32:
            print(f'Päev:{d} /nKuu:{m} /nAasta:{y}')
        elif m==4 and d<31:
            print(f'Päev:{d} /nKuu:{m} /nAasta:{y}')
        elif m==5 and d<32:
            print(f'Päev:{d} /nKuu:{m} /nAasta:{y}')
        elif m==6 and d<31:
            print(f'Päev:{d} /nKuu:{m} /nAasta:{y}')
        elif m==7 and d<32:
            print(f'Päev:{d} /nKuu:{m} /nAasta:{y}')
        elif m==8 and d<32:
            print(f'Päev:{d} /nKuu:{m} /nAasta:{y}')
        elif m==9 and d<31:
            print(f'Päev:{d} /nKuu:{m} /nAasta:{y}')
        elif m==10 and d<32:
            print(f'Päev:{d} /nKuu:{m} /nAasta:{y}')
        elif m==11 and d<31:
            print(f'Päev:{d} /nKuu:{m} /nAasta:{y}')
        elif m==12 and d<32:
            print(f'Päev:{d} /nKuu:{m} /nAasta:{y}')
        else:
            print('Viga')
    else:
        print('Viga')


















def xor_cipher(string: str, key:str)->str:
    '''Tavaline sõna kooderitakse
    '''
    result = ''
    temp = int()
    for i in range(len(string)):
        temp = ord(string[i]) #näitab sümboli kood
        for j in range(len(key)):
            temp ^= ord(key[j])
        result +=chr(temp)
    return result
def xor_uncipher(string:str, key:str)->str:
    '''Kodeeritud text dekodeeritakse
    '''
    result = ''
    temp=[]
    for i in range(len(string)):
        temp.append(string[i])
        for j in reversed(range(len(key))):
            temp[i]=chr(ord(key[j]) ^ ord(temp[i]))
        result += temp[i]
    return result