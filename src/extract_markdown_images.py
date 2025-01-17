import re

def extract_markdown_images(text):
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    result = []
    for i in range(len(images)):
        result.append(images[i])
    if result == []:
        return None
    return result

def extract_markdown_links(text):
    urls = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    result = []
    for i in range(len(urls)):
        result.append(urls[i])
    if result == []:
        return None
    return result
