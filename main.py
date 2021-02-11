import Types
from Person import Person

touristTypes = Types.Types().types
output = ''

if __name__ == '__main__':
    ans = input("Does the person wears black clothes? (y/n) \n")
    clothed = 'black'

    if ans == 'n':
        input("Does the person wears white clothes? (y/n) \n")
        clothed = 'white'

    ans = input("Is the person tall? (y/n) \n")
    height = 'tall'

    if ans == 'n':
        input("Is the person short? (y/n) \n")
        height = 'short'

    ans = input("Does the person supports socialism? (y/n) \n")
    political = 'socialist'

    if ans == 'n':
        input("Does the person supports capitalism? (y/n) \n")
        political = 'capitalist'

    ans = input("Does the person have expensive accesories? (y/n) \n")
    wealth = 'rich'

    if ans == 'n':
        input("Does the person have average accesories? (y/n) \n")
        wealth = 'average'

    personInQuestion = Person(clothed, height, political, wealth)

    for type in touristTypes:
        if personInQuestion == type:
            print('The tourist in question is: ' + type.return_type())
            output = type.return_type()

    if not output:
        print('The tourist did not match any type, it"s most probably a Loonie')