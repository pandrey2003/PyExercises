from bs4 import BeautifulSoup
from bs4.element import Comment
from urllib.request import urlopen


def tag_visible(element):
    if element.parent.name in \
            ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)

    for t in visible_texts:
        print(t)


def output(url):
    html = urlopen(url).read()
    text_from_html(html)
