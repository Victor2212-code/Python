import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import os


usuarios = {'maritor': '210723'}

def verificar_login(usuario, senha):
    if usuario in usuarios and usuarios[usuario] == senha:
        return True
    else:
        return False

def fazer_login():
    print('usuário será mais dificil de acertar então ele vou colocar aqui "maritor", agora a senha é nossa data especial.')
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    return usuario, senha

def login():
    tentativas = 3
    while tentativas > 0:
        usuario, senha = fazer_login()
        if verificar_login(usuario, senha):
            print("Login bem-sucedido!")
            return True
        else:
            print("Usuário ou senha incorretos. Tente novamente.")
            tentativas -= 1
    print("Número máximo de tentativas excedido. Tente novamente mais tarde.")
    return False

def draw_heart():
    t = np.linspace(0, 2*np.pi, 100)
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    return x, y

# Função para animar o coração
def animate_heart():
    fig, ax = plt.subplots()
    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)
    line, = ax.plot([], [], 'r-')

    def init():
        line.set_data([], [])
        return line,

    def animate(i):
        x, y = draw_heart()
        line.set_data(x[:i], y[:i])
        return line,

    def add_text():
        ax.text(0, -2, 'Feliz um ano amor', fontsize=15,  ha='center')

    plt.axis('off')
    plt.gca().set_aspect('equal', adjustable='box')
    num_beats = 3
    frames_per_beat = len(draw_heart()[0])
    total_frames = num_beats * frames_per_beat
    def final_animation(i):
        if i < total_frames:
            return animate( i % frames_per_beat)
        else:
            return animate_beat(i - total_frames)
    def animate_beat(i):
        if i < frames_per_beat // 2:
            return animate(i)
        else:
            return animate(frames_per_beat - i)
    
    ani  = animation.FuncAnimation(fig, final_animation, frames=total_frames + frames_per_beat // 2, init_func=init, interval=50, blit=True)
    ani.event_source.stop()
    add_text()
    plt.show()
    
def show_video():
    input("Pressione Enter para ver o vídeo...")
    os.system('start surpresa_duda/video.mp4')
    
def contrato_eternidade():
    input('Pressione enter para ver o próximo vídeo...')
# Verificar o login antes de executar a animação e o vídeo
if login():
    show_video()
    input('Aperte enter para continuara a surpresa...')
    animate_heart()