from time import sleep

#Variável peso (kg)
peso = float (input ('Digite o seu peso em quilogramas: '))

#Variável nível de atividade
atividade = str (input ('Qual é o seu nível de atividade física? Pouco ativo, moderado ou intenso?: ')).strip().upper()

print ('Calculando...')
sleep(2)

print ('Calculando seu peso...')
sleep(2)

print ('Calculando proteina...')
sleep(2)

if atividade == 'POUCO ATIVO':
    print (f'Você deve ingerir cerca de {0.8 * peso}')

if atividade == 'MODERADO':
    print (f'Você deve ingerir cerca de {1.4 * peso}')

if atividade == 'INTENSO':
    print (f'Você deve ingerir cerca de {1.8 * peso} ')