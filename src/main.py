from textnode import TextNode, TextType
import shutil
import os

def main():
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(ROOT_DIR)
    PUBLIC_DIR = ROOT_DIR+"/public"

    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)
    copy_files_to_public(PUBLIC_DIR)


def copy_files_to_public(PUBLIC_DIR):
    if os.path.exists(PUBLIC_DIR):
        files = os.listdir(PUBLIC_DIR)
        for file in files:
            print(f"filename: {file}")
        print("deleting files")
        shutil.rmtree(PUBLIC_DIR)
    
    if not os.path.exists(PUBLIC_DIR):
        os.mkdir(PUBLIC_DIR)


main()

