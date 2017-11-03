#importingF3.py
print('Running importing F3.py')
from importingF2 import *
print('running func2 out of F3:')
func2()
func2()

from palindrome import isPal2, clean2 #will import any functions as well as any "auto-run" code that palindrome.py has in it when it gets run#
print(isPal2(clean2('helLo Olleh   ')))

import palindrome
print(palindrome.isPal('not a palindrome'))

def main3():
    l=['Yo, bottoms up! (U.S. motto, boy.)',
    'A man, a plan, a canal: Panama.',
    'As I pee, sir, I see Pisa!',
    'Do good? I? No! Evil anon I deliver. I maim nine more hero-men in Saginaw, sanitary sword a-tuck, Carol, I -- lo! -- rack, cut a drowsy rat in Aswan. I gas nine more hero-men in Miami. Reviled, I (Nona) live on. I do, O God!',
    'Go hang a salami; I\'m a lasagna hog.',
    'Gateman sees name, garageman sees name tag.',
    'I roamed under it as a tired, nude Maori.',
    'T. Eliot, top bard, notes putrid tang emanating, is sad. I\'d assign it a name: gnat dirt upset on drab pot-toilet.',
    'not a palindrome',
    ]
    for i in l:
        print(eval('isPal2(clean2(i))'))
print('main3:')
main3()

#x=clean2('racEC   ar')
#print('x is',x)
