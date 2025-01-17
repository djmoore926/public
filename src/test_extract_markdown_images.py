import unittest
from extract_markdown_images import extract_markdown_images

class TestExtractMarkdownImages(unittest.TestCase):
    def test_single(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("rick roll", "https://i.imgur.com/aKaOqIh.gif")])

    def test_multiple(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_no_images(self):
        text = "This text does not contain any images or anything that we are looking for with our function."
        result = extract_markdown_images(text)
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()