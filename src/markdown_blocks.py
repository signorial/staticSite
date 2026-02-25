from enum import Enum
from textnode import TextNode, text_node_to_html_node,TextType
from htmlnode import LeafNode,ParentNode
from inline_markdown import text_to_textnodes
import re


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"


def block_to_block_type(block):
    # print(markdown.startswith("#"))
    # print(markdown)
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if re.search(r"/```([\s\S]*?)```/gs",block):
        return BlockType.CODE
    if quote_block_is_valid(block): 
        return BlockType.QUOTE
    if unordered_list_is_valid(block):
        return BlockType.ULIST
    if ordered_list_is_valid(block):
        return BlockType.OLIST
    return BlockType.PARAGRAPH

def quote_block_is_valid(block):
    lines = block.split("\n")
    valid = True
    for line in lines:
        if not line.startswith(">"):
            valid = False
        print(f"quoteline: {line} valid{valid}")
    return valid

def unordered_list_is_valid(block):
    lines = block.split("\n")
    valid = True
    for line in lines:
        if not line.startswith("- "):
            valid = False
    return valid

def ordered_list_is_valid(block):
    lines = block.split("\n")
    valid = True
    line_number = 0
    for line in lines:
        line_number+=1
        if not line.startswith(f"{line_number}. "):
            valid = False
    return valid



def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = [] 
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.QUOTE:
            children.append(quote_block_to_html(block))
        if block_type == BlockType.ULIST:
            children.append(unordered_list_block_to_html(block))
        if block_type == BlockType.OLIST:
            children.append(ordered_list_block_to_html(block))
        if block_type == BlockType.CODE:
            children.append(code_block_to_html(block))
        if block_type == BlockType.HEADING:
            children.append(heading_block_to_html(block))
        if block_type == BlockType.PARAGRAPH:
            children.append(paragraph_block_to_html(block))
    return children


def quote_block_to_html(block):
    children = block.replace(">\n"," ")
    children = children.replace(">","")
    return ParentNode(tag="blockquote",children=children)

def unordered_list_block_to_html(block):
    lines = block.split("\n")
    html_items = []
    for line in lines:
        parts = line.split("- ",1)
        test = parts[1]
        children = text_to_children(test)
        html_items.append(LeafNode(tag="li",value=children))
    return ParentNode("ul",html_items)

def ordered_list_block_to_html(block):
    lines = block.split("\n")
    html_items = []
    for line in lines:
        parts = line.split(". ", 1)
        text = parts[1]
        children = text_to_children(text)
        html_items.append(LeafNode(tag="li",value=children))
    return ParentNode("ol",html_items)

def code_block_to_html(block):
    text = block[4:-3]
    text_node = TextNode(text,TextType.TEXT) 
    children =  text_node_to_html_node(text_node)
    code = ParentNode(tag="code",children=children)
    return  ParentNode(tag="pre",children=code)

def heading_block_to_html(block):
    count = 0
    for char in block:
        if char == "#":
            count+=1
        else:
            break
    children = text_to_children(block[count+1:])
    return ParentNode(tag=f"h{count}",children=children) 

def paragraph_block_to_html(block):
    stripped_block = block.replace("\n"," ")
    children = text_to_children(stripped_block)
    return ParentNode(tag="p",children=children)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return children

