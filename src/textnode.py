
from enum import Enum
from htmlnode import HTMLNode 


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


    def text_node_to_html_node(self):
        match self.text_type:
            case TextType.TEXT:
                return HTMLNode(tag=None,
                                value=self.text,
                                children=None,
                                props=None)
            case TextType.BOLD:
                return HTMLNode(tag="b",
                                value=self.text,
                                children=None,
                                props=None)
            case TextType.ITALIC:
                return HTMLNode(tag="i",
                                value=self.text,
                                children=None,
                                props=None)
            case TextType.CODE:
                return HTMLNode(tag="code",
                                value=self.text,
                                children=None,
                                props=None)
            case TextType.LINK:
                return HTMLNode(tag="a",
                                value=self.text,
                                children=None,
                                props={"href":self.url})
            case TextType.IMAGE:
                return HTMLNode(tag="img",
                                value=None,
                                children=None,
                                props={"src":self.url,"alt":self.text})
            case _:
                raise ValueError("not a valid text_type")

