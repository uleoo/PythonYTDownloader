# PythonYTDownloader
Programa escrito em python com objetivo de baixar arquivos .mp3(músicas) e arquivos .mp4 (vídeos) com resoluções ajustáveis - versão sem GUI

Conceitos inclusos:
  Classes abstratas (POO);
  Herança.
Funções:
  Rename(para renomear arquivos de qualquer extensão);
  Conversor mp4 para mp3;
  Mesclar vídeo com áudio utilizando ffmpeg.


O sistema de resoluções ajustáveis foi feito por meio de stream_itags, disponibilizados pela biblioteca pytube:
https://pytube.io/en/latest/user/streams.html#working-with-streams-and-streamquery


Por ter sido criado com virtual env, há alguns requisitos, infelizmente ainda não sei mexer bem com isso, então talvez nem todos sejam necessários
Após baixar os arquivos completos, basta baixar as dependências:

pip install -r requirements.txt

Talvez haja a necessidade de instalar o software ffmpeg na sua máquina para o download de .mp4
