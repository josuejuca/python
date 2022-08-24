# Baixando musicas do YouTube com Python #
from pytube import YouTube
import moviepy.editor as mp
import os
import re

# Link do video para salvar o mp3 #
link = input("Digite o link do vídeo que deseja baixa: ")
path = input("Digite o diretório que deseja salvar: ")
yt = YouTube(link)

# https://youtu.be/5WUF6-ikBlM  link teste

# Inicio do Downlad # 
print("Baixando...")
ys = yt.streams.filter(only_audio=True).first().download(path)
print("Arquivo baixado com sucesso!")

# Converte de mp4 para mp3 #
print('Convertendo arquivo...')
for file in os.listdir(path):
    if re.search('mp4',file):
        mp4_path = os.path.join(path, file)
        mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)
print("Sucesso!")
