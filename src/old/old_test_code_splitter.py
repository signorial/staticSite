
import unittest

from textnode import TextNode, TextType
from code_splitter import split_nodes_delimiter


class TestCodeSplitter(unittest.TestCase):
    def test_split_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        print(f"split list {new_nodes}")
        self.assertEqual(len(new_nodes), 3)
''' 
    def test_split_bold(self):
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], r"**", TextType.BOLD)
        print(f"split list {new_nodes}")
        self.assertEqual(len(new_nodes), 3)
    
    def test_split_italic(self):
        node = TextNode("This is text with a _italic block_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        print(f"split list {new_nodes}")
        self.assertEqual(len(new_nodes), 3)
 
    def test_split_link(self):
        node = TextNode("This is text with a [link block](www.link.com) word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "[", TextType.LINK)
        print(f"split list {new_nodes}")
        self.assertEqual(len(new_nodes), 3)
 
    def test_split_image(self):
        node = TextNode("This is text with a ![image block](www.image.com) word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "![", TextType.IMAGE)
        print(f"split list {new_nodes}")
        self.assertEqual(len(new_nodes), 3)
 
    
    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )
 
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_italic(self):
        node = TextNode("This is a italic node", TextType.ITALIC)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a italic node")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK,"www.link.com")
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props["href"], "www.link.com")

    def test_image(self):
        node = TextNode("This is a image node", TextType.IMAGE, "www.image.com")
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        print(html_node)
        self.assertEqual(html_node.props["src"], "www.image.com")
'''
if __name__ == "__main__":
    unittest.main()

