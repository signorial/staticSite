import unittest
from markdown_blocks import (BlockType, 
                                markdown_to_blocks,
                                block_to_block_type,
                                markdown_to_html_node,
                                extract_title,
                                generate_page)


class testmarkdowntohtml(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """this is **bolded** paragraph

this is another paragraph with _italic_ text and `code` here
this is the same paragraph on a new line

- this is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "this is **bolded** paragraph",
                "this is another paragraph with _italic_ text and `code` here\nthis is the same paragraph on a new line",
                "- this is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """this is **bolded** paragraph




this is another paragraph with _italic_ text and `code` here
this is the same paragraph on a new line

- this is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "this is **bolded** paragraph",
                "this is another paragraph with _italic_ text and `code` here\nthis is the same paragraph on a new line",
                "- this is a list\n- with items",
            ],
        )

    def test_markdown_block_type_heading(self):
        md = """#### this is a heading for the test
"""
        blocks = block_to_block_type(md)
        self.assertEqual(blocks,BlockType.HEADING)


    
    def test_paragraph(self):
        md = """This is **bolded** paragraph
text in a p
tag here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """> This is a
> blockquote block

this is paragraph text

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
           html,
           "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )
    

    def test_code(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_extract_title_valid(self):
        md = """# This is the heading

```
the **same** even with inline stuff
```
"""
        heading = extract_title(md)
        self.assertEqual(heading,"This is the heading")

    def test_extract_title_invalid(self):
        md = """This is not a heading

```
the **same** even with inline stuff
```
"""
    
        with self.assertRaises(Exception) as context:
            extract_title(md)
        self.assertIn("no title found",str(context.exception))


        
    def test_generate_page(self):
        generate_page("content/index.md","template.html","public/index.html")

    
if __name__ == "__main__":
    unittest.main()

