class Person(object):
    def __init__(self, clothing, height, political, wealth):
        self.clothing = clothing
        self.height = height
        self.political = political
        self.wealth = wealth

    def __eq__(self, other):
        if (isinstance(other, Person)):
            return self.clothing == other.clothing and self.height == other.height and self.political == other.political and self.wealth == other.wealth