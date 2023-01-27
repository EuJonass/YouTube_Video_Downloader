from pytube import YouTube
import tkinter as tk
from tkinter import simpledialog, messagebox

ROOT = tk.Tk

# Função criada para colar o link e caso queira colar o caminho da pasta desejada
def input_data(title, prompt):
    result = simpledialog.askstring(title=title, prompt=prompt)
    return result

# Aba para colar o Link do vídeo desejado
video_link = input_data('Link Vídeo', 'Insira o Link do Vídeo:')
yt = YouTube(video_link)

# Printa Informaçoes como Título e o Autor
print(f'Título: {yt.title}')
print(f'Autor: {yt.author}')

# Resolução - lowest ou + highest
yd = yt.streams.get_lowest_resolution()

# Caminha para aonde o Download sera enviado
yd.download("C:\\users\\jonas\\PycharmProjects\\PythonProjects\\Videos")

# Mensagem final
messagebox.showinfo('Menssagem', 'Download Concluído')
