'''
I 1
V 5
X 10
L 50
C 100
D 500
M 1000
'''



if __name__ == '__main__':
    numero_romano = str(input('Digite um algorismo romano:'))
    numero = {'I': 1, 'V': 5 }
    print(numero[numero_romano])