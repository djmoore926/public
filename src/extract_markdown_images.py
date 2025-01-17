import re

def extract_markdown_images(text):
    alt_text = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    url = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    result = []
    print(url)
    for i in range(len(alt_text)):
        result.append((alt_text[i], url[i]))
    return result