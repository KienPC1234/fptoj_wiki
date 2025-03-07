import os
import re

# Đường dẫn tới thư mục chứa các file Markdown
docs_directory = r'C:\Users\kienp\Downloads\vnoi_wiki-master\fptoj_wiki'

# Biểu thức chính quy để nhận diện các dòng tiêu đề trong Markdown
# Nhóm 1: dãy dấu '#' liên tục
# Nhóm 2: khoảng trắng (nếu có)
# Nhóm 3: phần nội dung tiêu đề
header_pattern = re.compile(r'^(#{1,})(\s*)(.*)$')

for root, dirs, files in os.walk(docs_directory):
    for filename in files:
        if filename.endswith('.md'):
            file_path = os.path.join(root, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            changed = False
            new_lines = []
            for line in lines:
                match = header_pattern.match(line)
                if match:
                    hashes = match.group(1)
                    space = match.group(2)
                    content = match.group(3)
                    
                    # Đảm bảo có ít nhất một khoảng trắng sau dấu #
                    if space == '':
                        space = ' '
                        changed = True
                        
                    # Nếu cấp độ tiêu đề (số lượng dấu '#') ít hơn 6, tăng cấp độ bằng cách thêm thêm một dấu '#'
                    if len(hashes) < 6:
                        hashes = '#' + hashes
                        changed = True

                    new_line = f"{hashes}{space}{content}\n"
                    new_lines.append(new_line)
                else:
                    new_lines.append(line)

            if changed:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.writelines(new_lines)
                print(f"Đã cập nhật: {file_path}")
