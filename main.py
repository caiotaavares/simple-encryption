#
################################
# Criptografia - RSA           #
# Caio Gabriel Santana Tavares #
################################

import math
from time import time

def calc_totiente(p, q):
    result = (p - 1) * (q - 1)
    return result


def ultimo_primo(N):
    # Let A be an array of Boolean values, indexed by integers 2 to n, initially all set to true.
    A = list(range(2, N))

    # for i = 2, 3, 4, ..., not exceeding √n:
    for i in range(2, int(math.sqrt(N) + 1)):

        # if A[i] is true:
        if i in A:

            # for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n:
            for j in range(i ** 2, N, i):

                # A[j] := false.
                if j in A: A.remove(j)

    # print(A)
    return A.pop()


def find_d(public_key, totiente):
    i = 1
    while True:
        if public_key * i % totiente == 1:
            # print(i)
            return i
        else:
            i += 1


def cript(M, public_key, n):
    c = pow(M, public_key, n)
    return c


def RSA(message):
    # --- Escolha dois números primos ---
    print('Escolhendo primos...')
    p = 251  # 3
    q = 331  # 11

    # --- Calcular o produto dos dois números do passo anterior ---
    print('Calculando produto dos primos...')
    n = p * q

    # --- Calcular a função totiente de Euler ---
    print('Calculando a totiente de Euler...')
    totiente = calc_totiente(p, q)

    # --- Escolha um número “e” que seja um dos coprimos de n ---
    print('Calculando a chave pública...')
    public_key = ultimo_primo(totiente)
    print('Chave pública: ', public_key)
    # public_key = 17

    # --- Calculando o “d” da chave privada ---
    print('Calculando a chave privada...')
    # e = ultimo primo = chave pública
    # totiente = totiente
    private_key = find_d(public_key, totiente)
    print('Chave privada: ', private_key)

    # --- Temos tudo que precisamos para criptografar o RSA ---

    # --- Criptografando com EULER ---
    print('Criptografando...')

    # ESCOLHA A MENSAGEM
    print('MENSAGEM INSERIDA: ', message)

    cript_message = cript(message, public_key, n)
    print('Mensagem criptografada', cript_message)


def DiffieHelman(primo, gerador):
    # Número confiencial de A
    a = 15
    # Número confidencia de B
    b = 13

    # Resultado público de A
    PublicResultA = pow(gerador, a, primo)
    print('Resultado público de A', PublicResultA)

    # Resultado público de B
    PublicResultB = pow(gerador, b, primo)
    print('Resultado público de B', PublicResultB)

    # Segredo compartilhado recebido por A
    secretKeyA = pow(PublicResultB, a, primo)

    # Segredo compartilhdo recebido por B
    secretKeyB = pow(PublicResultA, b, primo)

    print('Segredo Compartilhado', secretKeyA)
    print('Segredo Compartilhado', secretKeyB)


message = int(input('Mensagem: '))

start = time()
RSA(message)
end = time()
print('Total time: %.2f seconds' % (end - start))
