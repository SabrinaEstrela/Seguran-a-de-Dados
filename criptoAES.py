import os
import base64
import random
import struct
import hashlib

from cryptography.fernet import Fernet 

#Receber arquivo e ler arquivo
arquivo_original = input("Digite o nome do arquivo: ")
arquivo_original2 = open('arquivo_original', 'rb').read()

#Criar chave
chave = Fernet.generate_key()
chave_cripto = Fernet(chave)

#test
print(chave)
print(chave_cripto)

#Criptografar arquivo
arquivo_criptografado = chave_cripto.encrypt(arquivo_original2)

#Escrever arquivo criptografado
with open('arquivo_criptografado', 'wb') as cripto:
    cripto.write(arquivo_criptografado)

#Recuperar arquivo
with open('arquivo_criptografado', 'r') as arquivo_cripto:
    with open('arquivo_recuperado' 'wb') as arquivo_rec:
        senha = input('Digite a chave para descriptografar: ')
        arquivo = senha.decrypt(str.encode(arquivo_cripto.read()))
        arquivo_rec.write(arquivo)


