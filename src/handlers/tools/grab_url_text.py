from StringIO import StringIO
from urllib2 import urlopen

from PyPDF2 import PdfFileReader
from bs4 import BeautifulSoup
from bs4.element import Comment


class UrlGrabber(object):
    """
    This class is used for grabbing text from websites and remote pdf files.
    Part of code from: https://stackoverflow.com/questions/1936466/beautifulsoup-grab-visible-webpage-text
    """

    # Tags that should not have significant content
    not_content_tags = ['details', 'figcaption', 'figure', 'footer', 'header', 'mark', 'nav', 'section',
                        'summary', 'time', 'style', 'script', 'head', 'title', 'meta', 'aside', '[document]']

    @staticmethod
    def tag_visible(element):
        """
        Check whether the passed tag is significant or not
        :param element: the tag to be examined
        :return: true if the tag is significant
        """
        if element.parent.name in UrlGrabber.not_content_tags:
            return False
        if isinstance(element, Comment):
            return False

        return True

    @staticmethod
    def text_from_html(body):
        """
        Gets text from html code
        :param body: The html code
        :return: The text grabbed
        """
        soup = BeautifulSoup(body, 'html.parser')

        # Remove tags that should not have significant content
        for tag in UrlGrabber.not_content_tags:
            [s.extract() for s in soup(tag)]

        texts = soup.findAll(text=True)
        visible_texts = filter(UrlGrabber.tag_visible, texts)
        return u" ".join(t.strip() for t in visible_texts)

    @staticmethod
    def get_text_from_url(url):
        """
        Opens an URL and grab the content
        :param url: The URL to be opened and examined
        :return: The content
        """
        html = urlopen(url).read()
        return UrlGrabber.text_from_html(html)

    @staticmethod
    def get_text_from_first_page_pdf(url):
        """
        Get the content from a remote pdf file. 
        For efficiency reasons, only the content from the first page is grabbed.
        :param url: The pdf URL
        :return: The first pdf page content
        """
        remote_file = urlopen(url).read()
        memory_file = StringIO(remote_file)
        pdf_file = PdfFileReader(memory_file)
        first_page = pdf_file.getPage(0).extractText().strip().encode('utf-8')
        return first_page
