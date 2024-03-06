from bs4 import BeautifulSoup
import requests
from PIL import Image
import os
import zipfile


class Sticker:
    def __init__(self):
        self.progress = 0
        self.total = 0
    
    @classmethod
    def download(self, url):
        self.progress = 0
        self.total = 0
        res = requests.get(url)
        soup = BeautifulSoup(res.content, "html.parser")
        stickerBase = soup.find_all("span", "FnPreviewBase")
        stickerOverlay = soup.find_all("span", "FnPreviewOverlay")
        
        title = soup.find("p", "mdCMN38Item01Ttl")
        title = "" if not title else title.text
        
        author = soup.find("a", "mdCMN38Item01Author")
        author = "" if not author else author.text
        

        if not stickerBase:
            stickerBase = soup.select("div.FnPreviewImage span")

            if not stickerBase:
                return False

        cnt = len(stickerBase)
        self.total = cnt
        self.progress = 0
        print("Sticker count:", cnt)
        
        stickers_prefix = "stickers-" + str(url.replace("//", "/").split("/")[4])
        
        if not os.path.isdir(f"./static/line_stickers/imgs"):
            os.mkdir("static/line_stickers/imgs")

        if not os.path.isdir(f"./static/line_stickers/imgs/{stickers_prefix}"):
            os.mkdir("static/line_stickers/imgs/" + stickers_prefix)

            for i in range(cnt):
                base_image_url = None
                overlay_image_url = None
                baseStyle = None
                overlayStyle = None
                base_background_image = None
                overlay_background_image = None
                
                if stickerBase:
                    baseStyle = stickerBase[i].get('style')
                    
                if stickerOverlay:
                    overlayStyle = stickerOverlay[i].get('style')
                
                if baseStyle:
                    start_index = baseStyle.index('url(') + 4
                    end_index = baseStyle.index('?', start_index)
                    base_image_url = baseStyle[start_index:end_index]
                    base_background_image = Image.open(requests.get(base_image_url, stream=True).raw).convert("RGBA")
                
                if overlayStyle:
                    start_index = overlayStyle.index('url(') + 4
                    end_index = overlayStyle.index('?', start_index)
                    overlay_image_url = overlayStyle[start_index:end_index]
                    overlay_background_image = Image.open(requests.get(overlay_image_url, stream=True).raw).convert("RGBA")    
                
                if overlay_background_image and base_background_image:
                    base_background_image.paste(overlay_background_image, (0, 0), overlay_background_image)
                
                if base_background_image:
                    base_background_image.save(f"static/line_stickers/imgs/{stickers_prefix}/{i+1}.png")
                
                self.progress += 1
                    
                print("Downloaded:", f"({i+1}/{cnt})")
                print("Base URL:", base_image_url)
                print("Overlay URL:", overlay_image_url)
            self.zip_folder(f"static/line_stickers/imgs/{stickers_prefix}", f"static/line_stickers/imgs/{stickers_prefix}.zip")
        return [title, author, [f"/static/line_stickers/imgs/{stickers_prefix}/{i+1}.png" for i in range(cnt)], f"/static/line_stickers/imgs/{stickers_prefix}.zip"]
    
    @classmethod
    def zip_folder(self, folder_path, output_path):
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, folder_path)  # 在壓縮文件中的相對路徑
                    zipf.write(file_path, arcname=arcname)
    
    @classmethod  
    def get_progress_bar(self):
        return self.progress / max(1, self.total) * 100