import os
import re
import requests

def check_md_image_links(directory, log_file):
    img_url_pattern = re.compile(r'!\[.*?\]\((https://.*?)\)')
    
    with open(log_file, 'w', encoding='utf-8') as log:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".md"):  # Chỉ kiểm tra file .md
                    file_path = os.path.join(root, file)
                    
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    img_urls = img_url_pattern.findall(content)
                    
                    for url in img_urls:
                        try:
                            response = requests.head(url, timeout=5)
                            if response.status_code != 200:
                                log.write(f"Lỗi ảnh ({response.status_code}): {url} trong file {file_path}\n")
                        except requests.RequestException as e:
                            log.write(f"Không thể truy cập ảnh: {url} trong file {file_path} - Lỗi: {e}\n")

# Thư mục chứa các file Markdown
docs_directory = 'C:\\Users\\kienp\\Downloads\\vnoi_wiki-master\\fptoj_wiki'
log_file_path = 'log_image_errors.txt'

# Gọi hàm kiểm tra và lưu log
check_md_image_links(docs_directory, log_file_path)
print(f"Log lỗi ảnh đã được lưu vào {log_file_path}")