import os
import re

# Đường dẫn tới thư mục chứa các file Markdown
docs_directory = r'C:\Users\kienp\Downloads\vnoi_wiki-master\fptoj_wiki'

# Biểu thức chính quy nhận diện các dòng tiêu đề trong Markdown
header_pattern = re.compile(r'^(#{1,})(\s*)(.*)$')

for root, dirs, files in os.walk(docs_directory):
    for filename in files:
        if filename.endswith('.md'):
            file_path = os.path.join(root, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            changed = False
            new_lines = []
            first_header_removed = False  # Cờ đánh dấu đã xóa header đầu tiên hay chưa

            for line in lines:
                match = header_pattern.match(line)
                if match and not first_header_removed:
                    # Nếu dòng này là header và chưa xóa header đầu tiên thì bỏ qua dòng này
                    first_header_removed = True
                    changed = True
                    continue  # Bỏ qua dòng header đầu tiên
                else:
                    new_lines.append(line)

            if changed:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.writelines(new_lines)
                print(f"Đã cập nhật: {file_path}")
