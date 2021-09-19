import os
import re

from pytube import YouTube


class YouTubeDownloader:

    def __init__(self, link):
        self.url = link
        self.video_trigger = None

    def run(self):
        video = self.video_init()
        self.user_choice(video)

    def user_choice(self, video):
        while True:
            print('Что скачать?')
            user_choice = input('1. Видео 2. Аудио: ')
            if user_choice == '1':
                self.video_trigger = 1
            elif user_choice == '2':
                self.video_trigger = None
            else:
                print('Введите корректные данные!')
                continue
            self.downloader(video)
            break

    def audio_downloader(self, youtube_url):
        file = youtube_url.streams.filter(only_audio=True).first()
        file.download(output_path='files/audio')
        print(file.title)
        os.rename(f'/files/audio/{file.title}.mp4',
                  f'/files/audio/{file.title}.mp3')

    def video_downloader(self, youtube_url):
        file = youtube_url.streams.filter(progressive=True).desc().first()
        file.download(output_path='files/videos')

    def downloader(self, video):
        if self.video_trigger:
            self.video_downloader(video)
        else:
            self.audio_downloader(video)
        print('Файл скачан успешно!')

    def video_init(self):
        youtube = YouTube(url=self.url)
        print(youtube.title)
        return youtube


class GetLink:
    re_url = re.compile(r'(?:https?:\/\/)?(?:www\.)?(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|playlist\?|'
                        r'watch\?v=|watch\?.+(?:&|&#38;);v=))([a-zA-Z0-9\-_]{11})?(?:(?:\?|&|&#38;)'
                        r'index=((?:\d){1,3}))?(?:(?:\?|&|&#38;)?list=([a-zA-Z\-_0-9]{34}))?(?:\S+)?')

    def get_url(self):
        while True:
            url_from_user = input('Вставьте ссылку: ')
            match = re.match(self.re_url, url_from_user)
            if match:
                self.url = url_from_user
                return self.url
            else:
                print('Вставьте корректную ссылку!')
                continue


if __name__ == '__main__':
    link = GetLink().get_url()
    downloader = YouTubeDownloader(link)
    downloader.run()
