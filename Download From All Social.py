import yt_dlp
import uuid
import os

def download_video(video_url):
    # Generate a random filename with .mp4 extension
    random_filename = str(uuid.uuid4()) + '.mp4'
    output_path = os.path.join(os.getcwd(), random_filename)
    
    ydl_opts = {
        'format': 'best',
        'outtmpl': output_path,
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([video_url])
            print(f"Video downloaded successfully as {random_filename}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter URL: ")
    download_video(video_url)
