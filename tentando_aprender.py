from datetime import datetime


def hora():
    comecar = int(input('digite 0 para começar seu teste, ou digite 1 para começar mais tarde: '))
    while comecar >= 1:
        comecar = int(input('quando quiser começar, digite 0: '))

    hora_atual= datetime.now()
    if comecar == 0:

        print('seu teste começou as {}' .format(hora_atual.strftime('%H:%M:%S')))

if __name__ == '__main__':
    hora()

nome = input('Digite seu nome: ')
resultado = int(input('quanto é 5 + 5?: '))
if resultado == 10:
    print(nome,'você acertou a questão')
else:
    print(nome, 'você errou a questão')

def hora_finalizada():
    hora_final = datetime.now()
    print('você concluiu seu teste às: {}' .format(hora_final.strftime('%H:%M:%S')))

if __name__ == '__main__':
    hora_finalizada()

