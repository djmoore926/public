import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        props = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode("a", "This is a text value", "child object", props)
        self.assertEqual(f"HTMLNode(a, This is a text value, children: child object, {props})", repr(node))

    def test_p2html(self):
        props = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode("a", "This is a text value", "child object", props)
        self.assertEqual(f' href="https://www.google.com" target="_blank"', node.props_to_html())

    def test_p2html_none(self):
        node = HTMLNode("a", "This is a text value", "child object")
        self.assertEqual("", node.props_to_html())

    def test_values(self):
        props = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode("a", "This is a text value", "child object", props)
        self.assertEqual("a", node.tag)
        self.assertEqual("This is a text value", node.value)
        self.assertEqual("child object", node.children)
        self.assertEqual(props, node.props)

    def test_notag(self):
        node = LeafNode(None, "This is a paragraph of text.")
        self.assertEqual("This is a paragraph of text.", node.to_html())

    def test_noprops(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual("<p>This is a paragraph of text.</p>", node.to_html())

    def test_withprops(self):
        node = LeafNode("a", "This is a paragraph of text.", {"href": "https://www.google.com"})
        self.assertEqual('<a href="https://www.google.com">This is a paragraph of text.</a>', node.to_html())

    def test_tohtml_nochildren(self):
        node = LeafNode("a", "This is text.")
        self.assertEqual(node.to_html(), "<a>This is text.</a>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_simple_parent(self):
        node = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "TEXT text"), LeafNode("i", "italic text"), LeafNode(None, "TEXT text")])
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>TEXT text<i>italic text</i>TEXT text</p>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_nested_parent(self):
        node = ParentNode(
            "h", [
                ParentNode(
                    "p", [
                        LeafNode("b", "bold text"), 
                        LeafNode(None, "TEXT text"), 
                        LeafNode("i", "italic text"), 
                        LeafNode(None, "TEXT text.")
                        ]
                        ),
                ParentNode(
                    "p", [
                        LeafNode("f", "footer text")
                        ]
                )
                ]
            )
        self.assertEqual(node.to_html(), "<h><p><b>bold text</b>TEXT text<i>italic text</i>TEXT text.</p><p><f>footer text</f></p></h>")

    def test_parent_props(self):
        node = ParentNode("p", [LeafNode(None, "try this")], {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<p href="https://www.google.com">try this</p>')

if __name__ == "__main__":
    unittest.main()