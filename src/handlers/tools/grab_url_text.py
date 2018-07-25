from urllib2 import urlopen
from bs4 import BeautifulSoup
from bs4.element import Comment


class UrlGrabber(object):
    """
    Code from: https://stackoverflow.com/questions/1936466/beautifulsoup-grab-visible-webpage-text
    """

    not_content_tags = ['details', 'figcaption', 'figure', 'footer', 'header', 'mark', 'nav', 'section',
                        'summary', 'time', 'style', 'script', 'head', 'title', 'meta', 'aside', '[document]']

    @staticmethod
    def tag_visible(element):
        if element.parent.name in UrlGrabber.not_content_tags:
            return False
        if isinstance(element, Comment):
            return False

        return True


    @staticmethod
    def text_from_html(body):
        soup = BeautifulSoup(body, 'html.parser')

        # Remove tags that should not have significant content
        for tag in UrlGrabber.not_content_tags:
            [s.extract() for s in soup(tag)]

        texts = soup.findAll(text=True)
        visible_texts = filter(UrlGrabber.tag_visible, texts)
        return u" ".join(t.strip() for t in visible_texts)

    @staticmethod
    def get_text_from_url(url):
        html = urlopen(url).read()
        return UrlGrabber.text_from_html(html)
