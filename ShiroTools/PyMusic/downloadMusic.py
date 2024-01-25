from pytube import YouTube, Playlist
from pydub import AudioSegment
from time import time_ns
import os
import pytube.request
import re

pytube.request.default_range_size = 2 * 1024 * 1024 # 每 2 MB 回傳一次 on_progress

class Downloader:
    def __init__(self, installPath, tempPath, batch):
        self.installPath = installPath
        self.tempPath = tempPath
        self.batch = batch
    
    def remove_special_characters(self, text):
        pattern = r'[<>:"/\\|?*]'  # 匹配不允許的符號
        cleaned_text = re.sub(pattern, '', text)
        return cleaned_text
    
    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        downloaded = total_size - bytes_remaining
        pct = round(downloaded / total_size * 100, 1)
        progress_pct = round(downloaded / total_size * 30)
        print("[" + "="*progress_pct + (">" if progress_pct < 30 else "=") + " "*(30-progress_pct) + "]" + f"({pct}%)", end = "\r" if progress_pct < 30 else "\n")
    
    def check_is_list(self, url=None):
        if url:
            if "list=" in url:
                videos = Playlist(url)
                videos_count = len(videos.video_urls)
                print("List:", videos.title)
                for c, video in enumerate(videos.video_urls):
                    print(f"({(c+1)}/{videos_count})")
                    self.download(video, self.batch)
            else:
                print("(1/1)")
                self.download(url)
    
    def download(self, url=None, sub_folder = "", format="mp3"):
        if url:
            print("Downloading audio from", url)
            filename = os.path.join(self.tempPath, sub_folder, str(time_ns()) + ".webm")
            print("Getting audio...")
            
            # https://pytube.io/en/latest/api.html?highlight=on_progress#pytube.YouTube.register_on_progress_callback
            yt = YouTube(url, on_progress_callback=self.on_progress)
            # yt.register_on_progress_callback(self.on_progress)
            self.print_info(yt)
            
            
            # https://pytube.io/en/latest/user/streams.html#filtering-for-audio-only-streams
            # for t in yt.streams.filter(file_extension="webm", type="audio"):
            #     print("Mime type:", t)
            
            # print("By Itag:", yt.streams.get_by_itag(251))
            print("Getting stream...")
            audio = yt.streams
            
            print("Downloading...")
            audio = audio.get_by_itag(251)
            print("Size:", audio.filesize_mb, "MB")
            default_filename = audio.default_filename.split(".")[0]
            default_filename = self.remove_special_characters(default_filename)
            audio.download(filename=filename)
            self.temp_to_mp3(filename, os.path.join(self.installPath, sub_folder), default_filename, format)
            return filename, default_filename + "." + format
        return False
    
    def print_info(self, yt: YouTube):
        print("-"*12 + " Sone Info " + "-"*12)
        print("Title:", yt.title)
        print("Author:", yt.author)
        print("Length:", yt.length)
        print("Publish Date:", yt.publish_date)
        print("-"*35)
    
    def temp_to_mp3(self, temp_path, mp3_folder, default_filename, format="mp3"):
        if os.path.isfile(temp_path):
            if not os.path.isdir(mp3_folder):
                os.makedirs(mp3_folder)
            print("Reading...")
            audio = AudioSegment.from_file(temp_path, format="webm")
            print("Saving...")
            audio.export(os.path.join(mp3_folder, default_filename + "." + format), format=format)
            print("Removing temp...")
            os.remove(temp_path)
            print("Save to:", os.path.join(os.getcwd(), default_filename + "." + format))
        else:
            print("Error")
            
    def check_folder_exist(self):
        if not os.path.isdir(self.installPath):
            os.makedirs(self.installPath)
        if not os.path.isdir(self.tempPath):
            os.makedirs(self.tempPath)
        
if __name__ == "__main__":
    Downloader().check_is_list(input("Input YT Link: "))
    