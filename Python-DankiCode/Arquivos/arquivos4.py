"""O gmail teve uma atualização recente quanto ao envio de email basicamente agora você terá que informar ao google para criar uma senha específica para você enviar emails estarei ensinando logo abaixo:


Para informar ao google para criar uma senha para o disparo de emails faça o seguinte:


clique no seu perfil > Gerenciar sua conta google


Ao abrir vá em Segurança.


Desça até achar o banner com "Como fazer login no Google"


Primeramete faça a verificação de duas etapas e siga para o próximo passo.


Ao habilitar a verificação em duas etapas clique em senhas de app.


faça o login o login do google.


Selecione o app E-mail e o nome do dispositivo que enviará email. Sugiro colocar em Outro e coloque um nome específico


e clique em gerar. Ao clicar em gerar vai aparecer uma senha, copie ela e cole no campo Password do código que envie logo abaixo:"""


#!/usr/bin/env python
# coding: utf-8


# In[ ]:


import smtplib
import email.message


def enviar_email():


corpo_email = """
<p>Parágrafo1</p>
<p>Parágrafo2</p>
"""


msg = email.message.Message()
msg['Subject'] = "Assunto"
msg['From'] = 'remetente'
msg['To'] = 'destinatario'
password = 'senha'  # COLE AQUI A SENHA DA EXPLICAÇÃO QUE FIZ LOGO ACIMA
msg.add_header('Content-Type', 'text/html')
msg.set_payload(corpo_email)


# lembrando que aqui será adicionado o smtp do gmail,hotmail (cada um possui um diferente)
s = smtplib.SMTP('smtp.gmail.com: 587')
s.starttls()
# Login Credentials for sending the mail
s.login(msg['From'], password)
s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
print('Email enviado')


# In[ ]:


enviar_email()
