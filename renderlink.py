import os
import re

def convert_syntax(text):
    # Regex để tìm các pattern [[...]]
    pattern = r'\[\[(.+?)\]\]'
    
    def repl(match):
        content = match.group(1)
        # Kiểm tra cú pháp có chứa dấu |
        if '|' in content:
            alt_text, link = content.split('|', 1)
            alt_text = alt_text.strip()
            link = link.strip()
        else:
            alt_text = link = content.strip()
        
        # Nếu link kết thúc bằng .png thì chuyển thành ảnh, ngược lại là link
        if link.lower().endswith('.png'):
            # Nếu alt_text trùng với link, thì render ảnh mà không cần alt
            # Bạn có thể điều chỉnh nếu muốn hiển thị alt luôn
            return f'![{alt_text}]({link})'
        else:
            return f'[{alt_text}]({link})'
    
    return re.sub(pattern, repl, text)

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = convert_syntax(content)
    
    # Ghi đè file (hoặc bạn có thể lưu ra file mới)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'Processed: {filepath}')

def process_directory(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.lower().endswith('.md'):
                filepath = os.path.join(dirpath, filename)
                process_file(filepath)

if __name__ == '__main__':
    docs_dir = 'C:\\Users\\kienp\Downloads\\vnoi_wiki-master\\fptoj_wiki\\docs'  # Thư mục chứa các file Markdown
    process_directory(docs_dir)
