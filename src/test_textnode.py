import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)


    def test_inequality(self):
        node3 = TextNode("this is a link node",TextType.LINK,"www.go.com")
        node4 = TextNode("this is a link node but not the same",TextType.LINK,"www.go4launch.com")
        self.assertNotEqual(node3,node4)

    def test_url(self):
        node5 = TextNode("this is a link node",TextType.LINK,"www.go.com")
        self.assertTrue(node5.url=="www.go.com")
        node6 = TextNode("this is a link node but not the same",TextType.LINK)
        self.assertTrue(node6.url==None)





if __name__ == "__main__":
    unittest.main()
