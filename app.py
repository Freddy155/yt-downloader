import click
from pytube import YouTube

@click.command()
@click.option('--url', prompt='Enter the YouTube video URL', help='URL of the video to download')
def download_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        title = yt.title
        filename = title + '.mp4'
        print(f"Downloading: {title}")
        stream.download(output_path='downloads', filename=filename)
        print('Download completed.')
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    download_video()
