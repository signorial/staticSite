from textnode import TextNode, TextType
import shutil
import os
from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)
    



# ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # print(ROOT_DIR)
    # PUBLIC_DIR = ROOT_DIR+"/public"
    # SRC_DIR =  ROOT_DIR+"/src"
    #
    # node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    # print(node)
    # delete_public_directory(PUBLIC_DIR)
    # copy_src_to_public_directroy(SRC_DIR,PUBLIC_DIR)
    # generate_page("content/index.md","template.html","public/index.html")
    # generate_page_recursive("content","template.html","public")
    #






# def delete_public_directory(PUBLIC_DIR):
#     if os.path.exists(PUBLIC_DIR):
#         files = os.listdir(PUBLIC_DIR)
#         for file in files:
#             print(f"filename: {file}")
#         print("deleting files")
#         shutil.rmtree(PUBLIC_DIR)
#
#     if not os.path.exists(PUBLIC_DIR):
#         os.mkdir(PUBLIC_DIR)
#
# def copy_src_to_public_directroy(SRC_DIR,PUBLIC_DIR):
#      if (os.path.exists(SRC_DIR),os.path.exists(SRC_DIR)):
#         print(f"copy file")
#         files = os.listdir(SRC_DIR)
#         for file in files:
#             source_path = os.path.join(SRC_DIR,file)
#             print(f"file: {source_path}")
#             print(f"isfile: {os.path.isfile(source_path)}")
#             if os.path.isfile(source_path):
#                 print(f"copying file {file}")
#                 shutil.copy(source_path,PUBLIC_DIR)
#             if os.path.isdir(source_path):
#                 print(f"copying file {file}")
#                 public_dir_folder = os.path.join(PUBLIC_DIR,file)
#                 os.mkdir(public_dir_folder)
#                 print(f"filepath {source_path} publicdir {public_dir_folder}")
#                 copy_src_to_public_directroy(source_path,public_dir_folder)
#
    

main() 

