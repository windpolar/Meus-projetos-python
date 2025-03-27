#Biblioteca random
from random import choice

#Biblioteca tempo
from time import sleep

print ('=-=' * 20)

#Variável pergunta
pergunta_usuário = str (input ('Você gostaria de tirar um versículo?: ')).strip().upper()

print ('=-=' * 20)

print ('PROCESSANDO...')
sleep (3)

#Variáveis 1
n1 = ('Filipenses 4:13\n Posso todas as coisas naquele que me fortalece.')
n2 = ('Salmos 23:1\n O senhor é meu pastor e nada me faltará.')
n3 = ('Isaías 41:10\n Não temas, porque eu sou contigo; não te assombres, porque eu sou o teu Deus; eu te fortaleço e te ajudo, e te sustento com a destra da minha justiça.')
n4 = ('Romanos 8:28\n Sabemos que todas as coisas cooperam para o bem daqueles que amam a Deus, daqueles que são chamados segundo o seu propósito.')
n5 = ('2 Coríntios 12:9\n A minha graça te basta, porque o meu poder se aperfeiçoa na fraqueza.')

#Lista pras variáveis 1
lista = [n1, n2, n3, n4, n5]
escolhido = choice (lista)

if pergunta_usuário == 'SIM':
    print (escolhido)

else:
    print ('Poxa, que pena, mesmo assim, que Deus te abençoe infinitamente!')