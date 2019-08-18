from html.parser import HTMLParser

class CustomParser(HTMLParser):
    def handle_comment(self, comment):
        comment = comment.strip()

        if '\n' in comment:
            print('>>> Multi-line Comment\n{}'.format(comment))

        else:
            print('>>> Single-line Comment\n{}'.format(comment))

    def handle_data(self, data):
        if '\n' in data:
            return

        print('>>> Data\n{}'.format(data))


code = '\n'.join(input().strip() for _ in range(int(input().rstrip())))

parser = CustomParser()
parser.feed(code)
