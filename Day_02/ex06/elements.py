from elem import Elem, Text


class Html(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='html', attr=attr)


class Head(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='head', attr=attr)


class Body(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='body', attr=attr)


class Title(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='title', attr=attr)


class Meta(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='meta', attr=attr, tag_type='simple')


class Img(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='img', attr=attr, tag_type='simple')


class Table(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='table', attr=attr)


class Th(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='th', attr=attr)


class Tr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='tr', attr=attr)


class Td(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='td', attr=attr)


class Ul(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='ul', attr=attr)


class Ol(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='ol', attr=attr)


class Li(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='li', attr=attr)


class H1(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='h1', attr=attr)


class H2(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='h2', attr=attr)


class P(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='p', attr=attr)


class Div(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, attr=attr)


class Span(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='span', attr=attr)


class Hr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='hr', attr=attr, tag_type='simple')


class Br(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='br', attr=attr, tag_type='simple')


def generate_boilerplate_html():
    meta1 = Meta(attr={"charset": "UTF-8"})
    meta2 = Meta(attr={"http-equiv": "X-UA-Compatible", "content": "IE=edge"})
    meta3 = Meta(attr={'name': "viewport",
                 'content': "width=device-width, initial-scale=1.0"})
    title = Title(content=Text("Document"))
    head = Head(content=[meta1, meta2, meta3, title])

    h1 = H1(content=Text("Hello world!"))
    p = P(content=Text("This is a test, do not panic."))
    body = Body(content=[h1, p])

    html = Html(content=[head, body])

    return html


def generate_pdf_test_html():
    title = Title(content=Text(r"\"Hello Ground\""))
    head = Head(content=title)

    h1 = H1(content=Text(r"\"Oh no, not again!\""))
    img = Img(attr={"src": "http://i.imgur.com/pfp3T.jpg"})
    body = Body(content=[h1, img])

    html = Html(content=[head, body])

    return html


if __name__ == "__main__":

    html = generate_pdf_test_html()
    print(html)
