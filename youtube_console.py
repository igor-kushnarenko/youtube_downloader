import argparse

from app import YouTubeDownloader

parser = argparse.ArgumentParser(description='Video downloader')
parser.add_argument('link', type=str, help='Link to videos')
args = parser.parse_args()

downloader = YouTubeDownloader(args.link)
downloader.run()
