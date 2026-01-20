from textnode import TextNode


def main():
    new_node = TextNode(text="This is some anchor text",text_type="link",url="https://www.boot.dev")
    print(new_node)


if __name__ == "__main__":
    main()
