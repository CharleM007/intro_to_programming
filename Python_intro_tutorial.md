#Python 2014 Intro Tutorial
AN emphasis on creating several small programs and expanding them.


##Core Novice Tutorial Topics
Mention these are from "Introducing Python"
-  Variables, Assignment & Basic data types
    +  Variables
        *  defined
        *  naming rules
    +  Basic Data Types
        *  What's a "data type" and why do you care?
            -  data types will influence how you work with an object
            -  knowing what data types a function requires and gives back is also important
        *  Our first function: the `type()` function
            -  >>> type(10)
                <type 'int'>
                >>> type(10.0)
                <type 'float'>
                >>> type(10.)
                <type 'float'>
    +  Numbers
        +   Int
        +   Float
    +   Strings
        *   str
        *   2nd function: `len()`
    +   Two new functions: `help()` and `dir()`
    +   Bool
    +  When/How to use them

-  Collection types
    +  List; Tuple; Dictionary; Set
    +  When/how to use them


##Basic target apps: these will form the structure of the class
+  process a text file
    *  CSVs are ubiquitious
+  process an Excel file
+  pull JSON from the web and process it
    *  learn the YouTube JSON structure
+  process the contents of a directory
    *  use OS module to make this easier?
+  process Images? Use Pillow
    *  It may be too difficult to get installed for novices
    *  Usage guide is [here](https://pillow.readthedocs.org/en/latest/guides.html)

##My Goals/needs
-  Enhance my OWN Python skills
    +  OO code
    +  web stuff with Flask, Django
-  Prepare my two talks for PyTexas
    +  spend more time with Excel stuff
-  RaspberryPi