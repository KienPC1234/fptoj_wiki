import os

# Đường dẫn thư mục chứa các file Markdown
docs_directory = r'C:\Users\kienp\Downloads\vnoi_wiki-master\fptoj_wiki'

# Đường dẫn file log để ghi lại các thay đổi
log_file = 'log.txt'

# Chuỗi cần thay thế và chuỗi thay thế
target_str = r"\*"
replacement = " \\times "  # Thêm khoảng trắng ở đầu và cuối

with open(log_file, 'w', encoding='utf-8') as log:
    # Duyệt qua tất cả các thư mục và file trong docs_directory
    for root, _, files in os.walk(docs_directory):
        for file in files:
            if file.endswith(".md"):  # Chỉ xử lý các file .md
                file_path = os.path.join(root, file)
                
                # Đọc nội dung file
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Thực hiện thay thế
                new_content = content.replace(target_str, replacement)
                
                # Nếu nội dung đã được thay đổi, ghi đè file và ghi log
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    log.write(f"Đã cập nhật file: {file_path}\n")

print("Quá trình thay thế hoàn tất.")
