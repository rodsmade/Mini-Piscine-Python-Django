import traceback

from elem import Elem
from elements import *

# Page itself is not an Elem.
class Page:
    def __init__(self, contents) -> None:
        if not isinstance(contents, Elem):
            raise TypeError(
                "Argument must be an instance of a subclass of Elem")
        self.contents = contents

    def __str__(self) -> str:
        result = ''
        if isinstance(self.contents, Html):
            result += "<!DOCTYPE html>\n"
        result += str(self.contents)
        return result

    @staticmethod
    def validate_html_elem(elem) -> bool:
        correct_structure = [Head, Body]
        if type(elem) == Html:
            if type(elem.content) != list or len(elem.content) != 2:
                return False

            if type(elem.content[0]) == correct_structure[0] and type(elem.content[1]) == correct_structure[1]:
                return True
            else:
                return False
        else:
            return True

    def validate_body_and_div_elem(elem) -> bool:
        valid_classes = [H1, H2, Div, Table, Ul, Ol, Span, Text]
        if type(elem) == Body or type(elem) == Div:
            for item in elem.content:
                if type(item) not in valid_classes:
                    return False
            return True
        else:
            return True
        
    def validate_single_text_elems(elem) -> bool:
        valid_classes = [Title, H1, H2, Li, Th, Td]
        if type(elem) in valid_classes:
            if (type(elem.content) == list and len(elem.content) == 0) \
                or (type(elem.content) == list and len(elem.content) == 1 and type(elem.content[0]) == Text) \
                or (type(elem.content) != list and type(elem.content) == Text):
                return True
            else:
                return False
        else:
            return True
        
        
    @staticmethod
    def passes_all_elements_validation(elem):
        if Page.validate_html_elem(elem) \
            and Page.validate_body_and_div_elem(elem) \
            and Page.validate_single_text_elems(elem):
            return True
        return False
    
    def is_valid(self):
        valid_classes = [Html, Head, Body, Title, Meta, Img, Table,
                         Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Text]

        if self.contents != list:
            self.contents = [self.contents]

        for elem in self.contents:
            if type(elem) in valid_classes:
                if Page.passes_all_elements_validation(elem):
                    return True
                else:
                    return False
            else:
                return False
        return True

class TestClass(Elem):
    pass


if __name__ == "__main__":
    try:
        # TESTING INITIALISATION
        try:
            page = Page("hello this is wrong")
            raise AssertionError
        except TypeError as e:
            pass

        try:
            page = Page(H1())
        except e:
            raise AssertionError

        print("Initialisation tests: OK!")

        # TESTING STRINGIFICATION
        page = Page(H1(content=Text("Hello world")))
        assert str(page) == '<h1>\n  Hello world\n</h1>'

        page = Page(Html(content=H1(content=Text("Hello world"))))
        assert str(
            page) == '<!DOCTYPE html>\n<html>\n  <h1>\n    Hello world\n  </h1>\n</html>'

        print("Stringification tests: OK!")

        # TESTING IS_VALID()
        page = Page(H1())
        assert page.is_valid() == True
        page = Page(TestClass())
        assert page.is_valid() == False
        page = Page(Html(content=[Head(), Body()]))
        assert page.is_valid() == True
        page = Page(Html(content=[Body()]))
        assert page.is_valid() == False
        page = Page(Body())
        assert page.is_valid() == True
        page = Page(Body(content=H1()))
        assert page.is_valid() == True
        page = Page(Body(content=Title()))
        assert page.is_valid() == False
        page = Page(Div())
        assert page.is_valid() == True
        page = Page(Div(content=H1()))
        assert page.is_valid() == True
        page = Page(Div(content=Title()))
        assert page.is_valid() == False
        
        page = Page(Title())
        assert page.is_valid() == True
        page = Page(Title(content=Text("Hello")))
        assert page.is_valid() == True
        page = Page(Title(content=[Text("Hello")]))
        assert page.is_valid() == True
        page = Page(Title(content=[Text("Hello"), Text("Hello")]))
        assert page.is_valid() == False
        page = Page(Title(content=[H1()]))
        assert page.is_valid() == False
        page = Page(Title(content=H1()))
        assert page.is_valid() == False



        print("Is_valid() tests: OK!")

    except AssertionError as e:
        traceback.print_exc()
        print(e)
        print('Tests failed!')
