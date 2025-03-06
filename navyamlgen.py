import os
import markdown
from markdown.treeprocessors import Treeprocessor
from markdown.extensions.toc import TocExtension

# Hàm để lấy tiêu đề H1 đầu tiên trong một file markdown
def extract_first_h1_from_md(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Sử dụng markdown để phân tích cú pháp
    md = markdown.Markdown(extensions=[TocExtension()])
    html = md.convert(content)

    # Tìm tiêu đề H1 đầu tiên
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    h1 = soup.find('h1')

    if h1:
        return h1.get_text()
    return os.path.splitext(os.path.basename(file_path))[0]  # Nếu không có H1, dùng tên file

# Hàm duyệt qua thư mục và tạo cấu trúc nav
def generate_nav_from_directory(directory):
    nav = []
    for root, dirs, files in os.walk(directory):
        # Bỏ qua thư mục gốc (docs) nếu không phải root thư mục
        if root == directory:
            continue
        
        # Lấy tên thư mục và thay đổi nó thành tiêu đề
        folder_name = os.path.relpath(root, directory)
        folder_name = folder_name.replace(os.sep, " / ")  # Chuyển đường dẫn thành tên thư mục

        # Tạo cấu trúc nav cho thư mục này
        folder_nav = {folder_name: []}
        
        # Duyệt qua các file .md trong thư mục
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.relpath(os.path.join(root, file), directory)
                title = extract_first_h1_from_md(os.path.join(root, file))
                file_nav = {title: file_path.replace(os.sep, "/")}
                folder_nav[folder_name].append(file_nav)

        if folder_nav:
            nav.append(folder_nav)

    return nav

# Hàm in ra cấu trúc nav theo định dạng YAML
def print_nav_in_yaml(nav):
    import yaml
    print(yaml.dump({"nav": nav}, allow_unicode=True, default_flow_style=False))

# Đường dẫn đến thư mục chứa các file Markdown
docs_directory = 'docs'  # Đảm bảo rằng thư mục docs chứa các file markdown của bạn
nav = generate_nav_from_directory(docs_directory)

# In ra cấu trúc nav dưới dạng YAML
print("Cấu trúc nav của MkDocs dưới dạng YAML:")
print_nav_in_yaml(nav)
