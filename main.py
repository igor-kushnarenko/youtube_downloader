from pytube import YouTube


def get_url():
    # todo регуляркой проверять корректность ссылки
    user_input = input('Вставьте ссылку: ')
    return user_input


def download_audio(url):
    youtube = YouTube(url=url)
    audio = youtube.streams.filter(only_audio=True)
    audio.download(output_path='/home/maxim/Загрузки/')


def download_video(url):
    youtube = YouTube(url=url)
    video = youtube.streams.filter(progressive=True).desc().first()
    video.download(output_path='/home/maxim/Загрузки/')
    print('Видео скачано успешно!')


if __name__ == '__main__':
    url = get_url()
    # todo что скачать, аудио или видео?&
    download_video(url)
