import smtplib
import string
import config
from random import *
from time import sleep


def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS, message)
        server.quit()
        print("Successo! Email enviado!")
    except:
        print("O Envio do Email falhou.")

def pass_gen1(x = 8, y = 16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(choice(characters)for x in range(randint(x,y)))
    return password

def pass_gen2(x = 8, y = 16):
    characters = string.ascii_letters + string.digits
    password2 = ''.join(choice(characters)for x in range(randint(x,y)))
    return password2

def pass_gen3(x = 8, y = 16):
    characters = string.ascii_letters
    password3 = ''.join(choice(characters)for x in range(randint(x,y)))
    return password3

while True:
    subject = str(input('Para qual lugar deseja gerar a senha? '))
    user = str(input('Qual usuário? '))
    print('''[ 1 ] Caracteres/Números/Símbolos
[ 2 ] Caracters/Números
[ 3 ] Caracters''')
    option = int(input('Qual opção deseja? '))
    try:
        x, y = [int(x) for x in input('Escolha o número min/max: ').split()]
        if option == 1:
            pw = pass_gen1(x, y)
        elif option == 2:
            pw = pass_gen2(x, y)
        elif option == 3:
            pw = pass_gen3(x, y)
        else:
            print('Opção inválida.')
    except ValueError:
        x, y = None, None
        if option == 1:
            pw = pass_gen1()
        elif option == 2:
            pw = pass_gen2()
        elif option == 3:
            pw = pass_gen3()
        else:
            print('Opção inválida.')
    print(subject)
    msg = (user, pw)
    print(msg)
    print('Enviando...')
    sleep(1)
    #send_email(subject, msg)
    c = str(input('Gerar outra senha? [S/N] ')).lower().strip()[0]
    if c == 'n':
        break
print('Programa encerrado.')
