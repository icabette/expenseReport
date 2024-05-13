from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.is_strong = False

    def handle_starttag(self, tag, attrs):
        if tag == 'strong':  # <strong> 태그 시작
            self.is_strong = True

    def handle_endtag(self, tag):
        if tag == 'strong':  # </strong> 태그 닫힘
            self.is_strong = False

    def handle_data(self, data):
        if self.is_strong:  # <strong>~</strong> 구간인 경우
            print(data)     # 데이터를 출력


with open('LG 유플러스 이메일 청구서입니다..html', encoding='UTF8') as f:
    parser = MyHTMLParser()
    parser.feed(f.read())