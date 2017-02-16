from html.parser import HTMLParser
from urllib.request import urlopen
import re


class MyHTMLParser(HTMLParser):
    is_print = False

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            if re.match(r'.*python-events/\d+/$', attrs[0][1]):
                print('event name:')
                self.is_print = True
            elif tag == 'time':
                print('event time:')
                self.is_print = False
            elif tag == 'span':
                if re.match(r'.*event-location.*', attrs[0][1]):
                    print('event location:')
                    self.is_print = False
            else:
                self.is_print = False
            pass

    # def handle_startendtag(self, tag, attrs):
    #     print('<%s/>' % tag)
    #
    # def handle_comment(self, data):
    #     print('<!--', data, '-->')

    def handle_data(self, data):
        if self.is_print:
            print(data.strip())
            #
            # def handle_entityref(self, name):
            #     print('&%s;' % name)
            #
            # def handle_endtag(self, tag):
            #     print('</%s>' % tag)
            #
            # def handle_charref(self, name):
            #     print('&#%s;' % name)


parser = MyHTMLParser()

parser.feed(urlopen('https://www.python.org/events/python-events/').read().decode('utf-8'))
