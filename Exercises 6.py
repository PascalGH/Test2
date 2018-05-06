from math import *
from turtle import *
a = ''

def inverse(chaine):
    i = len(chaine) -1
    nouvelle_chaine = ""
    while i >= 0:
        nouvelle_chaine += chaine[i]
        i -= 1
    return(nouvelle_chaine)

def printList(t):
    length = len(t)
    i = 0
    while i <length:
        print(t[i], end = " ")
        i += 1
    print('')
    
t1 = [31, 28, 31, 30, 31,30, 31, 31, 30, 31, 30, 31]
t2 = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
t3 = []

i = 0
length = len(t1)
while i < length:
    t3.append(t2[i])
    t3.append(t1[i])
    i += 1
# printList(t1)
# printList(t2)
# printList(t3)   

        
b = []
petits = []
grands = []
a= ''
max = 0
i = 0
while a != '':
    a = input('Veuillez entrer la vitesse en miles / heure: ')
    if a != '':
        km_h = float(a)*1.609
        m_s = km_h / 3.6
        print(a, 'Miles par heures valent ', m_s, ' mètres par seconde, et ',km_h, ' kilomètres par heure')


# l = float(input('Entrer la longueur du pendule: '))
# T = 2 * pi * sqrt(l/g)
# print(T)

# forward(120)
# left(90)
# color('red')
# forward(80)

# a = 0
# write('Hello World')
# while a < 12:
#    a += 1
#    forward(150)
#    left(150)

a = input('a: ')
b = input('b: ')
i = 1

while i <= b:
    print(i)
    i += 1




   
