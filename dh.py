def DiffieHelman(primo, gerador):
    # Número confiencial de A
    a = 82499  # 82499
    # Número confidencia de B
    b = 82493  # 82493

    # Resultado público de A
    PublicResultA = pow(gerador, a, primo)
    print('Resultado público de A', PublicResultA)

    # Resultado público de B
    PublicResultB = pow(gerador, b, primo)
    print('Resultado público de B', PublicResultB)

    # Segredo compartilhado recebido por A
    secretKeyA = pow(PublicResultB, a, primo)

    # Segredo compartilhado recebido por B
    secretKeyB = pow(PublicResultA, b, primo)

    print('Segredo Compartilhado', secretKeyA)
    print('Segredo Compartilhado', secretKeyB)

    return secretKeyA