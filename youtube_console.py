import argparse

from app import YouTubeDownloader

parser = argparse.ArgumentParser(description='Video downloader')
parser.add_argument('link', type=str, help='Lin to videos')
args = parser.parse_args()
print(args.link)


# downloader = YouTubeDownloader()
#
# parser = argparse.ArgumentParser(
#     prog='Youtube Downloader',
#     description='Youtube Downloader',
# )
# subparser = parser.add_subparsers()
#
# """Video download"""
# video_downloader = subparser.add_parser(
#     '-v',
#     help='Video download. Command: python youtube_console.py <video_link> -v')
# video_downloader.set_defaults(func=downloader.video_downloader)
#
# """Audio download"""
# audio_downloader = subparser.add_parser(
#     '-a',
#     help='Video download. Command: python youtube_console.py <video_link> -a')
# audio_downloader.set_defaults(func=downloader.audio_downloader)
#
# args = parser.parse_args()
# args.func()
