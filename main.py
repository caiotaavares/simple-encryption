#
################################
# Criptografia - RSA           #
# Caio Gabriel Santana Tavares #
################################

from time import time
import rsa
import dh

# Define P e Q

# Calcula Diffie Helman = chave
# primo = int(input('Escolha um numero primo para Diffie-Helman: '))
# gerador = int(input('Escolha um numero gerador para Diffie-Helman: '))
primo = 82499  # 3
gerador = 82493  # 11
mensagem = 13

print('DIFFIE HELMAN')
chave = dh.DiffieHelman(primo, gerador)
print('chave: ', chave)
public_key = rsa.ultimo_primo(chave)
public_key = public_key.pop()

print('RSA')
print(rsa.RSA(mensagem, public_key))

# chave será usada para escolher os coprimos


# message = int(input('Mensagem: '))
#
# start = time()
# rsa.RSA(message)
# end = time()
# print('Total time: %.2f seconds' % (end - start))