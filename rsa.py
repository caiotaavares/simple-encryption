def calc_totiente(p, q):
    result = (p - 1) * (q - 1)
    return result


def ultimo_primo(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]


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


def RSA(message, public_key):
    # --- Escolha dois números primos ---
    print('Escolhendo primos...')
    p = 82499  # 3
    q = 82493  # 11

    # --- Calcular o produto dos dois números do passo anterior ---
    print('Calculando produto dos primos...')
    n = p * q

    # --- Calcular a função totiente de Euler ---
    print('Calculando a totiente de Euler...')
    totiente = calc_totiente(p, q)

    # --- Escolha um número “e” que seja um dos coprimos de n ---
    print('Calculando a chave pública...')
    # public_key = ultimo_primo(totiente)
    # public_key = public_key.pop()
    print('Chave pública: ', public_key)

    # --- Calculando o “d” da chave privada ---
    print('Calculando a chave privada...')
    # ultimo primo = chave pública
    private_key = find_d(public_key, totiente)
    print('Chave privada: ', private_key)

    # --- Temos tudo que precisamos para criptografar o RSA com EULER ---
    print('Criptografando...')

    # ESCOLHA A MENSAGEM
    print('MENSAGEM INSERIDA: ', message)

    cript_message = cript(message, public_key, n)
    print('Mensagem criptografada', cript_message)

