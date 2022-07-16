from pytube import YouTube
from pytube import Playlist
import argparse
import math

parser = argparse.ArgumentParser(description='Program untuk mendownload Youtube video')

parser.add_argument('--url', metavar='url', required=True, help='Masukan Youtube URL atau Link')
parser.add_argument('-p', '--playlist', metavar='playlist', const=True, nargs='?', help='Kalau playlist pake argument ini')
args = parser.parse_args()

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    percentage = str(math.trunc(percentage_of_completion))
    print(f"Download in progress: {percentage}%")

url = args.url
if args.playlist == True:
    playlist = Playlist(url)
    for video in playlist.videos:
        video.register_on_progress_callback(on_progress)
        file = video.streams.get_highest_resolution().download()
        print(f"File yang kamu download ada disini: {file}")
else:
    video = YouTube(url)
    video.register_on_progress_callback(on_progress)
    video_streams = video.streams.filter(file_extension='mp4')
    file = video_streams.get_highest_resolution().download()
    print(f"File yang kamu download ada disini: {file}")
    