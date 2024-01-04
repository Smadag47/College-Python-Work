import os


def add_header(file_path, header):
    try:
        with open(file_path, 'a+') as file:
            content = file.read()

            file.seek(0)

            file.write(header + '\n' + content)

            file.truncate()

    except FileNotFoundError:
        print("File not found")


def main():
    file_path = input("Enter the file path for the markdown file: ")
    title = input("Enter a title for this assignment without spaces: ")
    header = f'''
    ---
    title: "{title}"
    author: [Grant Adams]
    date: "1947912 | HCCYSE23-G-1FA"
    titlepage: true,
    titlepage-background: "background6.pdf"
    toc: true,
    toc-own-page: true,
    ...

    '''
    add_header(file_path, header)

    try:
        os.system(f"pandoc {file_path} -o {title}.pdf --from markdown --template eisvogel --listings")
    except Exception as e:
        print(f"Error executing command: {e}")







