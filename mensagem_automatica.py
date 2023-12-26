import pyautogui
import time

pyautogui.PAUSE = 0.5

# Passo 1: Abrir o navegador Chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)

# Passo 2: Acessar o WhatsApp Web
url = "https://web.whatsapp.com/"
pyautogui.write(url)
pyautogui.press("enter")
time.sleep(10)  # Espere tempo suficiente para escanear o código QR

# Passo 3: Enviar uma mensagem
# Encontre a posição do ícone de pesquisa e clique nele
pyautogui.click(x=172, y=256)
time.sleep(1)

# Digite o nome ou número da pessoa
pyautogui.write("Heloisa Cardoso Fatec")
time.sleep(1)

# Clique no resultado da pesquisa para abrir a conversa
pyautogui.click(x=207, y=427)
time.sleep(1)

# Digite a mensagem que você deseja enviar
pyautogui.write(
    "Olá Helo, meu nome é python vim a pedido do victor te dizer que ele "
    "me programou para escrever essa msg.")

# Pressione Enter para enviar a mensagem
pyautogui.press("enter")
