import random
import math
 
def Modo():
    print("Seja Bem Vindo!")
    print()
    print("Selecione a operação desejada:")
    print()
    print("Criptografar um texto (1)")
    print("Descriptografar um texto (2)")
    print()
    operacao = input("-> ")
 
    if operacao == "1":
        Cripto()
    elif operacao == "2":
        Descripto()
 
        exit()
    else:
        Modo()
 
 
def FuncaoTotiente(numero):
    if (Primo(numero)):
        return numero - 1
    else:
        return False
 
 
def Primo(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
 
    if (n % 2 == 0 or n % 3 == 0):
        return False
 
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i += 6
    return True
 
 
def CalcE(num):
    def mdc(n1, n2):
        resto = 1
        while (n2 != 0):
            resto = n1 % n2
            n1 = n2
            n2 = resto
        return n1
 
    while True:
        p2 = random.randrange(2, num)
        if (mdc(num, p2) == 1):
            return p2
 
 
def mod(a, b):
    if (a < b):
        return a
    else:
        c = a % b
        return c
 
 
def Concatenar(list):
    resultado= ''
    for element in list:
        resultado += str(element)
    return resultado
    
 
def Dividir(lista):
    half = len(lista)//2
    return lista[:half], lista[half:]
 
 
def Criptografar(palavras, p2, p1):
    tam = len(palavras)
    c = 0
    lista = []
    while (c < tam):
        letter = palavras[c]
        s = ord(letter)
        s = s ** p2
        d = mod(s, p1)
        lista.append(d)
        c += 1
    return lista
 
 
def KeyPublica(toti, p2):
    KeyPub = 0
    while (mod(KeyPub * p2, toti) != 1):
        KeyPub += 1
    return KeyPub
 
 
def KeyPrivada():
    while True:
        x = random.randrange(1, 100)
        if (Primo(x) == True):
            return x
 
 
def Repetir(texto, frase):
    opcao1 = input(texto)
    if opcao1 == "Sim" or opcao1 == "SIM":
        frase()
    elif opcao1 == "Não" or opcao1 == "NÃO":
        Modo()
    else:
        Repetir(texto, frase)
 
 
def Cripto():
    mensagem = input("Digite que o texto deseja criptografar: ")
    k1 = KeyPrivada()
    k2 = KeyPrivada()
    p1 = k1 * k2
    t1 = FuncaoTotiente(k1)
    t2 = FuncaoTotiente(k2)
    Totiente = t2 * t1
    p2 = CalcE(Totiente)
    KeyPub = (p1, p2)
 
    print("Sua key pública gerada:", KeyPub)
    Mensacrip = Criptografar(mensagem, p2, p1)
 
    print("Seu texto após o processo de criptografia é: ", (" ").join(str(x) for x in Mensacrip))
 
    KeyPub = KeyPublica(Totiente, p2)
    print("Sua key privada gerada é:", KeyPub)
    print()
    Repetir("Pronto! Deseja seguir criptografando outro texto (Sim ou Não)? -> ", Cripto)
 
 
def Descriptografar():
    txtcifrado = [int(x) for x in input("Digite o texto criptografado: ").split()]
    KeyPriv = int(input("Digite a key privada: "))
    p1=int(input("Digite o conjunto números que foi gerado antes da virgula na key pública (****): "))
 
    c = 0
    tamanho = len(txtcifrado)
    while c < tamanho:
        resultado = txtcifrado[c] ** KeyPriv
        texto = mod(resultado, p1)
 
        letra = chr(texto)
        txtcifrado.append(letra)
        c = c + 1
    return txtcifrado
 
 
def Descripto():
    Mensagem = Descriptografar()
    B, C = Dividir(Mensagem)
    C = (Concatenar(C))
    print("O texto descriptografado é:", C)
    print()
    Repetir("Pronto! Deseja descriptografar outro texto  (Sim ou Não)? -> ", Descripto)
 
Modo()
 

  
