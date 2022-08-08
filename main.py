import ffmpeg
from pytube import YouTube
from moviepy.editor import *
import os
from abc import ABC


youtube_url = YouTube(input("Digite o url: "))
name = youtube_url.title.replace('|', '')
stream_itag = input("formato: ")


class Download(ABC):

    def __init__(self, url):
        self.url = url
        video_audio = self.url
        video_audio.title = 'video'
        stream_video_audio = video_audio.streams.get_by_itag(stream_itag)
        stream_video_audio.download()


def rename(file, extension):
    directory = os.path.abspath(os.getcwd())
    file_oldname = os.path.join(directory, file)
    file_newname = os.path.join(directory, f"{name}.{extension}")
    try:
        os.rename(file_oldname, file_newname)
    except:
        print("O nome da música não pôde ser definido automaticamente por motivos de caracteres especiais.")
        file_newname = os.path.join(directory, f"{input('Qual é o nome da música? ')}.{extension}")
        os.rename(file_oldname, file_newname)

    os.remove('video.mp4')


def mp4_to_mp3(mp4, mp3):
    mp4_without_frames = AudioFileClip(mp4)
    mp4_without_frames.write_audiofile(mp3)
    mp4_without_frames.close()


class DownloadVideo(Download, ABC):
    def __init__(self, url):
        super().__init__(url)


class DownloadMusic(Download):
    def __init__(self, url):
        super().__init__(url)
        mp4_to_mp3(f"{url.title}.mp4", "audio.mp3")


if stream_itag == 'mp4':
    quality = int(input("Resolução:"))
    stream_itag = 140
    print(f"Fazendo o download de: {youtube_url.title}, visto {youtube_url.views} vezes.")
    youtube_audio_url1 = DownloadMusic(youtube_url)
    os.remove('video.mp4')
    if quality == 1080:
        stream_itag = 137
    elif quality == 720:
        stream_itag = 22
    elif quality == 480:
        stream_itag = 135
    elif quality == 360:
        stream_itag = 134
    elif quality == 240:
        stream_itag = 133
    else:
        stream_itag = 160
    youtube_video_url = DownloadVideo(youtube_url)
    video_stream = ffmpeg.input('video.mp4')
    audio_stream = ffmpeg.input('audio.mp3')
    ffmpeg.output(audio_stream, video_stream, 'out.mp4').overwrite_output().run()
    rename('out.mp4', 'mp4')
    os.remove('audio.mp3')
else:
    stream_itag = 140
    print(f"Fazendo o download de: {youtube_url.title}, visto {youtube_url.views} vezes.")
    youtube_audio_url = DownloadMusic(youtube_url)
    rename('audio.mp3', 'mp3')
