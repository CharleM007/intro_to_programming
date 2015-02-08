#Python 2014 Intro Tutorial
AN emphasis on creating several small programs and expanding them.


##Core Novice Tutorial Topics
Mention these are from "Introducing Python"

###"STUFF": Programming Nouns
-  Variables, Assignment & Basic data types
    +  Variables
        *  defined
        *  naming rules
            *  lowercase letters (a through z)
            *  uppercase letters (A through Z)
            *  digits (0 through 9)
            *  underscore (_)
    +  Basic Data Types
        *  What's a "data type" and why do you care?
            -  data types will influence how you work with an object
            -  knowing what data types a function requires and gives back is also important
        *  Our first function: the `type()` function
            *  `>>> type(10)`
            *  `>>> type(10.0)`
            *  `>>> type(10.)`
    +  Numbers
        +   Int
        +   Float
        +   Math
            *   Division: `/` vs `//` vs `%`
            *   Exponents: `2 ** 3 = 8`
    +   Strings
        *   type `str`
            -   'string' vs "string" vs '''string'''
        *   2nd function: `len()`
        *   String math?
        *   String + Int == Errors!!
        *   1 vs. '1'
            -   converting 1 to '1': `str()`

    +   Two new functions: `help()` and `dir()`

    +   Bool and comparisons: first steps to making decisions
        *  True; False; and, or, in
        *  Equalities
            *  `==` vs `=` 
        *  Inequalities: `!=`, `<=`, `>=`

###What to *DO* with this "STUFF"? Programming Verbs
-  Making decisions: `if`, `else`, `elif`

###Programming is Problem Solving! Our first challenge!
-  CodeBat problem
-  Fizzbuzz Questions


###More Nouns
-  Collection types
    +  List; Tuple(?); Dictionary; Set
    +  When/how to use them
    +  Lists & Tuples
        *  Similarities?
            -  Both are [sequences](https://docs.python.org/3.4/glossary.html#term-sequence)
            -  both can contain items of any type, including mixed types
            -  both can be nested
                +  `[1, "lemon", 3.14]`
                +  `[[10,11,13], [21, 25, 27],[34, 36, 38]]`
                +  `('monkey', 17, [1,2,3,4])`
        *  Differences?
            -  List are mutable; Tuples are immutable
            -  Tuples designed for collections where there *order* of the sequence has some meaning
                +  `("lastName", "firstName", "initial", "xxx-xxx-xxxx")`
            -  Being immutable, tuples have fewer methods than lists
                +  `dir(tuple)` vs. `dir(list)`
        *  Indexing
            -  From left to right, "offsets"
            -  From right to left, "negative counting order"
                    >>> a = 1,2,3,4
                    >>> a
                    (1, 2, 3, 4)
                    >>> a[0]
                    1
                    >>> a[-4]
                    1
                    >>> len(a)
                    4
            -  Why? 
                -  What if you want the last item in a list? The last 2 items?
                -  What if you want to perform an operation involving the last 2 items of a list, then add that result TO the list? What if you want to do it AGAIN?
        +  Slicing: get more than one item from a list
            *  `a[0:2]`
            *  `>>> a[:]`
            *  Steps
                *  `>>> a[::2]`
                *  `>>> a[1::2]`
    *  Dictionary

###More Verbs: Loops
-  For
    +  see [`for.py`](for.py) for examples
-  [While](https://docs.python.org/3/reference/compound_stmts.html#while)
    +  a simple example is used in [writing.py](writing.py)

###Files
-  See [writing.py](writing.py) and [reading.py](reading.py) for code examples that write a file [`scores.txt`](scores.txt), then read that file and process it's contents. 

###Get data from the web!
-  [youtube_stats.py](youtube_stats.py) is the file I demoed at the end of class.

##What's Next?
-  30 Day Github Challenge: Gamify your progress
-  Specific libraries
    +  [OpenPyXL docs](http://openpyxl.readthedocs.org/en/latest/) for working with Excel documents
    +  [Pillow](https://pillow.readthedocs.org/handbook/tutorial.html) for working with images
    +  [os standard module](https://docs.python.org/3/library/os.html) for working with your particular operating system
        *  [st_mtime](https://docs.python.org/3/library/os.html#os.stat_result.st_mtime) and other methods let you look at when files were created or modified. Results vary by OS.
    +  [sys module](https://docs.python.org/3/library/sys.html#module-sys): we only looked at `sys.argv` today. There's a LOT more.
    +  [NumPy](http://www.numpy.org) and [SciPy](http://scipy.org) for sophisticated math, engineering and data analysis
    +  [NLTK](http://www.nltk.org): Natural Language Tool Kit, "for building Python programs to work with human language data."
    +  [PyGame](http://pygame.org/wiki/about), "a set of Python modules designed for writing games."
