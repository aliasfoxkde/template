#! /usr/bin/env python

# coding: utf-8

metadata = dict(
	__author__ = "Aliasfox KDE",
	__version__  = "0.0.1",
	__license__ = "MIT License",
	__email__ = "aliasfox@cyopsys.com",
	__status__ = "Work in Progress",
	__url__ = "https://github.com/aliasfoxkde/snippets",
	__summary__ = "Simple but helpful library of snippets for python.",
	__keywords__ = "python, aliasfox, snippets"
)
globals().update(metadata)

__all__ = metadata.keys()

""" This is just a simple library of python "snippits" to either 
    1) make development simplier instead of having to rewrite 
    common or useful code over again, 2) or just clever code 
    I wanted to save while learning python. Also, it might be
    out of scope but I decided to organize my programming progress
    here as well.

    Useful Tools, Libraries, Learning Reference, and Links:
     * https://www.geeksforgeeks.org/10-essential-python-tips-tricks-programmers/
     * https://pythontips.com/2015/04/19/nifty-python-tricks/
     * https://bobbelderbos.com/2016/06/python-tips/
     * https://docs.sympy.org/latest/modules/simplify/simplify.html
     * https://www.w3schools.com/python/python_datetime.asp
     * https://docs.python.org/3/tutorial/modules.html
     * https://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html
     * https://stackoverflow.com/questions/582336/how-can-you-profile-a-python-script
     * https://www.blog.pythonlibrary.org/2014/03/20/python-102-how-to-profile-your-code/
     * https://docs.python.org/2/library/profile.html
	 * https://pypi.org/project/about/
     * https://pymotw.com/2/profile/
     * https://passwordsgenerator.net
     * http://norvig.com/sudoku.html
    
    Useful Notes:
     * "from <module> import <function> as <abbreviation>
     * "from <module> import <function1>, <function2>, ...     
"""
    
def pause():
    return raw_input("Press Enter to continue...")

""" --- Useful list comprehension tricks --- """
def advMap(func, *seqs):
    return [func(*args) for args in zip(*seqs)]
    
def flatten(tuple):
    return sum(tuple, [])

def nthDimList(n, dims):
    lst = [0] * n
    return [[lst for j in range(n)] if dims > 1 else lst for i in range(dims-1)]
    
def remDuplicates(array):
    return sorted(set(array), key=l[::-1].index)[::-1]

def unzip(tuple):
    return zip(*tuple)
    
""" ----- Useful Math Functions ----- """
def cypher(cyper, key):
    return ''.join(chr(i-int(b)+96)for i,b in zip(cyper,str(key)*29))

def factorial(n):
    return eval(str(range(1,n+1))[1:-1].replace(', ','*'))

def fib(n):
    """ Calculate the nth digit of Fibonacci
        0 1 1 2 3 5 8 13 21 34 ... """
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a + b
    return a

def getIntegral(c, e):
    return "%sx^%s" % (c/(e+1) if c%(e+1)!=0 else c//(e+1), e+1)
    
def hamming(n):
    """ A *Hamming number* is a positive integer of the form 2i3j5k,
        See: https://en.wikipedia.org/wiki/Regular_number """
    h = sorted(2**i*3**j*5**k for i in range(33) for j in range(21) for k in range(15))
    return h[n-1]

def longest_consec(string_array, n):
    return max([''.join(i) for i in zip(*[string_array[i:] for i in range(n)])]+[''], key=len)
    
def pi(position, precision):
    return
    
def sqrt(n):
    return n**.5
    
""" ---- Econding Conversions ---- """
def ascii2bin(string):
    return

def ascii2hex(string):
    return
    
def bin2Ascii(bin):
    from binascii import unhexlify
    return str(unhexlify('%x' % int(str(bin), 2)))[2:-1]

def bin2hex(n):
    return hex(int(str(bin), 2))[2:]

def bin2dec(bin):
    return int(str(bin), 2)
	
def altBin2Dec(bin):
    ''' # Alternative binary calculator: I saw the formula one time for '111' as
    (1 x 2^2) + (1 x 2^1) + (1 x 2^0) = 7 and thought it was awesome, so I made a python
    function. Maybe not the most efficient but it adds a level of intuitiveness. '''
    return sum(int(str(bin)[i])*2**i for i in range(len(str(bin))))

def int2bin(n):
    return ''.join(str((n & (1 << i)) and 1) for i in range(len(str(n))*8,-1,-1)).lstrip('0')

def hex2bin(hex_string):
    return ''.join(bin(ord(x))[2:].rjust(8,'0')[::-1] for x in hex_string)

""" ----- "Fun" Functions I've written ---- """
def zodiac(month, day, year):
    zodiac = [ "Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", 
               "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio",
               "Sagittarius" ]
    cutoff = [22, 20, 19, 21, 20, 21, 21, 23, 23, 23, 23, 22]
    
    if day < cutoff[month]: 
        month -= 1
    
    return zodiac[month%12]

def chinese_zodiac(year):
    zodiac = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", 
              "Rabbit", "Dragon", "Snake", "Horse", "Goat" ]
    return zodiac[year%12]

def increment_string(string):
    # See: https://www.codewars.com/kata/string-incrementer
    for i in range(5,0,-1):
        if len(string) > i-1 and string[-i].isdigit():
            return string[:-i] + str(int(string[-i:])+1).zfill(i) 
    return string+'1'
    
def numerology(month, day, year, name=''):     
    nList = name.lower().split()
    numbers = [sum(ord(j)-96 for j in nList[i])%9 for i in range(len(nList))]+[(month+day+year)%9]
    return numbers
    
def n_friday_the_13ths(y):    
    # My CodWars @ https://www.codewars.com/kata/56eb0be52caf798c630013c0
    count = 0 # Clean & Pure Math Example      
    for m in range(3,15):
        if m == 13: y-=1            
        if (y%100+(y%100//4)+(y//100)//4-2*(y//100)+26*(m+1)//10+12)%7==5:
            count += 1
    return count

def luhn(card):
    """ Credit Card Validator with Mod 10, or Luhn algorithm
    refering to it's creator 'Hans Peter Luhn' """
    # return sum(map(int, str(card)[1::2]+str(card)[0::2]*2))%10==0
    card=str(card).replace(' ','')
    return (sum(map(int, str(card)[1::2])) + \
            sum(sum(map(int, str(i*2))) for i in \
            map(int, str(card)[0::2]))) % 10 == 0

def piedPiper(town):
    """ How many rats are there?
    See: https://www.codewars.com/kata/598106cb34e205e074000031 
    Example: ~O~O~O~OP~O~OO~ has 2 deaf rats """
    return town.replace(' ', '')[::2].count('O')
    
""" ------ Puzzle and Game Related --------- """        
def piCross_solver(grid):
    return
    
def baccarat_simulator():
    return
    
def suduko_solver(grid):
    return
    
""" ---- File tools ---- """
def stripFile(filename, seperator='\n'):
    # "Parse a file into a list of strings, separated by seperator."
    return file(filename).read().strip().split(seperator)
    
""" ------ Sorting Algorithms --------- """
def bubblesort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return(array)
    
def is_turing_equation(s):
    # See https://www.codewars.com/kata/simple-fun-number-384-is-turings-equation
    return int(s[::-1].split('=')[0]) == sum(map(int, s[::-1].split('=')[1].split('+')))

""" --------- Other --------- """
def f2c(ferinheight=0):
    return ferinheight * 9/5 + 32 # celsius

def c2f(celsius=0):
    return (celsius - 32)* 5/9 # ferinheight

def is_anagram(str1, str2):
    return all(i in str2 for i in map(str, str1))

def inspect(object):
    return dir(object)

def debug():
    import pdb
    return pdb.set_trace()

def unitTests(level):
    """ Automated Unit tests and script profiling """
    return
