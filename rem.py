import os

def remove_contributor_from_files(directory):
    # Duyệt qua tất cả các file trong thư mục và các thư mục con
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):  # Kiểm tra nếu là file .md
                file_path = os.path.join(root, file)
                # Mở và đọc nội dung file
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Xóa tất cả chuỗi "/contributor" trong nội dung
                new_content = content.replace('/contributor', '')

                # Nếu nội dung có thay đổi thì ghi lại vào file
                if content != new_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Đã xóa '/contributor' trong file: {file_path}")

# Thư mục chứa các file .md
docs_directory = 'docs'

# Gọi hàm để xóa '/contributor' trong tất cả các file .md
remove_contributor_from_files(docs_directory)
