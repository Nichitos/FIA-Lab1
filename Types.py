from Person import Person

class Types:
    def __init__(self):
        self.types = [AsianHuman(), EuropeanHuman(), AmericanHuman(), AfricanHuman(), MoldovanHuman(), SouthAmericanHuman(), ArabHuman(), IndianHuman(), AustralianHuman()]

class AsianHuman(Person):
    def __init__(self):
        super().__init__('white', 'short', 'socialist', 'average')
    def return_type(self):
            return "AsianHuman"

class EuropeanHuman(Person):
    def __init__(self):
        super().__init__('white', 'tall', 'capitalist', 'rich')
    def return_type(self):
            return "EuropeanHuman"

class AmericanHuman(Person):
    def __init__(self):
        super().__init__('black', 'short', 'capitalist', 'rich')
    def return_type(self):
            return "AmericanHuman"

class AfricanHuman(Person):
    def __init__(self):
        super().__init__('black', 'tall', 'socialist', 'average')
    def return_type(self):
            return "AfricanHuman"

class MoldovanHuman(Person):
    def __init__(self):
        super().__init__('black', 'short', 'capitalist', 'average')
    def return_type(self):
            return "MoldovanHuman"

class SouthAmericanHuman(Person):
    def __init__(self):
        super().__init__('white', 'tall', 'socialist', 'average')
    def return_type(self):
            return "SouthAmericanHuman"

class ArabHuman(Person):
    def __init__(self):
        super().__init__('black', 'short', 'socialist', 'average')
    def return_type(self):
            return "ArabHuman"

class IndianHuman(Person):
    def __init__(self):
        super().__init__('black', 'tall', 'capitalist', 'average')
    def return_type(self):
            return "IndianHuman"

class AustralianHuman(Person):
    def __init__(self):
        super().__init__('white', 'tall', 'socialist', 'rich')
    def return_type(self):
            return "AustralianHuman"