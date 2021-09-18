import argparse

from app import YouTubeDownloader

parser = argparse.ArgumentParser(description='Video downloader')
parser.add_argument('link', type=str, help='Lin to videos')
args = parser.parse_args()
print(args.link)

downloader = YouTubeDownloader(args.link)
downloader.run()
