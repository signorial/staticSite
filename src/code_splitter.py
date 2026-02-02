from ast import Continue
from enum import Enum
from textnode import TextNode, TextType
import re
import pdb



def split_nodes_delimiter(old_nodes, delimiter, text_type):
    delimiters = ["**","_","`","[","]","![","]"]
    new_list = []
    text = ""
    if delimiter not in delimiters:
        raise Exception(f"{delimiter} is not valid markdown. valid markdown includes {delimiters}")

    for node in old_nodes:
        if node.text_type !=TextType.TEXT:
            new_list.append(node)
        else:
            for text_type in TextType:
                if text_type == TextType.TEXT:
                    continue
                text = node.text
                delimiter = get_delimiter(text_type)
                start =0
                end =0
                while len(text)>0:
                    if text_type == TextType.LINK or text_type == TextType.IMAGE:
                        for match in re.finditer(delimiter,text): 
                            if match:
                                start = match.start() 
                                end =  match.end()
                            else:
                                start = -1
                                end = -1
                            text,new_list =append_list(start,end,text,text_type,new_list)
                    else:
                        print(f"new_list: {new_list}")
                        print(f"delimiter:{delimiter}")
                        print(f"text type:{text_type}")
                        start  = text.find(delimiter)
                        end = text[start +1:].find(delimiter) 
                        print(f" start={start} end={end}")
                        text,new_list =append_list(start,end,text,text_type,new_list)
    return new_list

def append_list(start,end,text,text_type, new_list):
    if start == -1 :
        new_list.append(TextNode(text=text,text_type=TextType.TEXT,url=None))
        text = ""
    if start > 0:
        new_list.append(TextNode(text=text[0:start],text_type=TextType.TEXT,url=None))
        text = text[start+1:]
    if start == 0:
        new_list.append(TextNode(text=text[start+1:end+1],text_type=text_type,url=None))
        text = text[end+2:]
    print(f" print text: {text}")
    return text,new_list

def get_delimiter(text_type):
    
    match text_type:
        case TextType.TEXT:
            return ""
        case TextType.BOLD:
            return "**"
        case TextType.ITALIC:
            return "_"
        case TextType.CODE:
            return "`"
        case TextType.IMAGE:
            return r"!\[([^\[\]]*)\]\(([^\(\)]*)\)" 
        case TextType.LINK:
            return r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
        case _:
            raise ValueError("not a valid text_type")


