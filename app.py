import re

from pytube import YouTube


class YouTubeDownloader:
    re_url = re.compile(r'(?:https?:\/\/)?(?:www\.)?(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|playlist\?|'
                        r'watch\?v=|watch\?.+(?:&|&#38;);v=))([a-zA-Z0-9\-_]{11})?(?:(?:\?|&|&#38;)'
                        r'index=((?:\d){1,3}))?(?:(?:\?|&|&#38;)?list=([a-zA-Z\-_0-9]{34}))?(?:\S+)?')

    def __init__(self, url):
        self.url = url

    def run(self):
        self.user_choice()

    def user_choice(self):
        print('Что скачать?')
        user_choice = input('1. Видео 2. Аудио: ')
        # todo засунуть проверку ввода пользователя
        if user_choice == '1':
            self.video_downloader()
        if user_choice == '2':
            self.audio_downloader()

    def check_url(self):
        match = re.match(self.re_url, self.url)
        if match:
            return self.url
        else:
            print('Вставьте корректную ссылку!')

    def video_downloader(self):
        video_url = self.check_url()
        youtube = YouTube(url=video_url)
        video = youtube.streams.filter(progressive=True).desc().first()
        video.download()
        print('Видео скачано успешно!')

    def audio_downloader(self):
        video_url = self.check_url()
        youtube = YouTube(url=video_url)
        audio = youtube.streams.filter(only_audio=True).first()
        audio.download()
        # todo изменить расширение файла на .mp3
        print('Аудио скачано успешно!')


if __name__ == '__main__':
    # 'https://www.youtube.com/watch?v=Hk4eMIswunQ'
    url = input('Вставьте ссылку: ')
    download = YouTubeDownloader(url=url)
    download.run()
