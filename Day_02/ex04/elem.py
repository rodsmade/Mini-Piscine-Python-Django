#!/usr/bin/python3


class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        return super().__str__().replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace('\n', '\n<br />\n').replace("\\&quot;", '"')


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """

    class ValidationError(Exception):
        def __init__(self) -> None:
            super().__init__("incorrect behaviour.")

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """

        # validate tag
        if type(tag) == type('str'):
            self.tag = tag
        else:
            raise Elem.ValidationError

        # validate attr
        if type(attr) == type({}):
            self.attr = attr
        else:
            raise Elem.ValidationError

        # validate tag_type
        if tag_type == 'double' or tag_type == 'simple':
            self.tag_type = tag_type
        else:
            raise Elem.ValidationError

        # validate content
        if content == None:
            self.content = []
        elif Elem.check_type(content):
            if content is None:
                content = []
            else:
                self.content = []
            self.add_content(content)
        else:
            raise Elem.ValidationError

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        if self.tag_type == 'double':
            result = '<' + self.tag + self.__make_attr() + '>' + self.__make_content() + \
                '</' + self.tag + '>'
        elif self.tag_type == 'simple':
            result = '<' + self.tag + self.__make_attr() + ' />'
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """

        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            if str(elem) != '':
                result += str(elem) + '\n'
        if result == '\n':
            result = ''
        else:
            result = "  ".join(line for line in result.splitlines(True))
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))


if __name__ == '__main__':
    text1 = Text(r"\"Hello Ground!\"")
    title = Elem(tag='title', content=[text1])
    head = Elem(tag='head', content=title)
    text2 = Text(r"\"Oh no, not again\"")
    h1 = Elem(tag='h1', content=text2)
    img = Elem(tag='img', tag_type='simple', attr={
               'src': "http://i.imgur.com/pfp3T.jpg"})
    body = Elem(tag='body', content=[h1, img])
    html = Elem(tag='html', content=[head, body])

    print(html)
