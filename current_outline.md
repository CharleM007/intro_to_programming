#Python 2014 Intro Tutorial
AN emphasis on creating several small programs and expanding them.


##Core Novice Tutorial Topics
Mention these are from "Introducing Python"

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
            <pre>
            >>> type(10)
            <type 'int'>
            >>> type(10.0)
            <type 'float'>
            >>> type(10.)
            <type 'float'>
            </pre>
    +  Numbers
        +   Int
        +   Float
        +   Math
            *   Division: `/` vs `//` vs `%`
            *   Exponents: `2 ** 3 = 8`
    +   Strings
        *   str
        *   2nd function: `len()`
        *   Math
            -   ''
    +   Two new functions: `help()` and `dir()`
    +   Bool
    +  When/How to use them

-  Collection types
    +  List; Tuple; Dictionary; Set
    +  When/how to use them


##Basic target apps: these will form the structure of the class
+  process a text file
    *  CSVs are ubiquitous
+  process an Excel file
+  pull JSON from the web and process it
    *  learn the YouTube JSON structure
+  process the contents of a directory
    *  use OS module to make this easier?
+  process Images? Use Pillow (included with Anaconda)
    *  It may be too difficult to get installed for novices
    *  Usage guide is [here](https://pillow.readthedocs.org/en/latest/guides.html); I'll need to learn more about it
*  GUI tools
    -  convert the small console apps into GUI apps
    -  Which GUI library or toolkit to use? I'll need to pick one. What's included with Anaconda?
        +  PyQT

##What's Next?
-  30 Day Github Challenge: Gamify your progress

##My Goals/needs
-  Enhance my OWN Python skills
    +  OO code
    +  web stuff with Flask, Django
-  Prepare my two talks for PyTexas
    +  spend more time with Excel stuff
-  RaspberryPi
