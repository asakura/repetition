from html.parser import HTMLParser

class CustomParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)

        for attr in attrs:
            print('-> {} > {}'.format(attr[0], attr[1]))


code = ''.join(input().strip() for _ in range(int(input())))

parser = CustomParser()
parser.feed(code)
