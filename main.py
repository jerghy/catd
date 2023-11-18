import requests
import time

url = "https://cdn77.91p49.com//mp43/905405.mp4?st=0cd93b19448d67f916f0201874abcda4"
filename = "video.mp4"

response = requests.get(url, stream=True)
total_size = int(response.headers.get('content-length', 0))
block_size = 1024  # 1KB

with open(filename, "wb") as file:
    start_time = time.time()
    downloaded_size = 0
    for data in response.iter_content(block_size):
        file.write(data)
        downloaded_size += len(data)
        elapsed_time = time.time() - start_time
        if elapsed_time >= 1:
            progress = downloaded_size / total_size * 100
            print(f"已下载：{progress:.2f}%")
            start_time = time.time()

print("文件下载完成")