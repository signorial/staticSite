from hmac import new
from pydoc import text
from textnode import TextNode, TextType
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    #print(f"old_nodes {old_nodes}")
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        #print(f"sections: {sections} delimiter: {delimiter}")
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = [] 
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)

        if len(images)==0:
            new_nodes.append(old_node)
            continue

        for label,link in images:
            delimiter = f"![{label}]({link})"
            sections = original_text.split(delimiter)
            if len(sections) !=2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] !="":
                new_nodes.append(TextNode(sections[0],TextType.TEXT))
            new_nodes.append(TextNode(label,TextType.IMAGE,link))
            original_text = sections[1]
        if original_text !="":
            new_nodes.append(TextNode(original_text,TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes



def redo_split_nodes_image(old_nodes):
    new_nodes=[]
    for old_node in old_nodes:
        old_text = old_node.text
        images = extract_markdown_images(old_text)
        for label,url in images:
            delimiter = f"![{label}]({url})"
            sections = old_text.split(delimiter,1)
            if sections[0] !="":
                new_nodes.append(TextNode(text=sections[0],text_type=TextType.TEXT))
            new_nodes.append(TextNode(text=label,text_type=TextType.IMAGE,url=url))
            old_text=sections[1]
    #print("-------------------------------------------------------------")
        #for new_node in new_nodes:
    #    print(f"new_node:  {new_node}")
    #print("-------------------------------------------------------------")
    return new_nodes


def text_to_textnodes(text):
    output= [TextNode(text=text,text_type=TextType.TEXT)]
    #print(output)
    output=split_nodes_delimiter(old_nodes=output,delimiter="**",text_type=TextType.BOLD)
    output=split_nodes_delimiter(old_nodes=output,delimiter="_",text_type=TextType.ITALIC)
    output=split_nodes_delimiter(old_nodes=output,delimiter="`",text_type=TextType.CODE)
    output=split_nodes_image(old_nodes=output)
    output=split_nodes_link(old_nodes=output)
    print("-------------------------------------------------------------")
    for o in output:
        print(f"output:  {o}")
    print("-------------------------------------------------------------")
    return output
