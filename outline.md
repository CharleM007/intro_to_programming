#Outline

<pre>If there's still a need for tutorials, I'd be interested in leading a tutorial for new programmers.  I'm calling it "Antifragile Python: Learning HOW to learn Python for new programmers".

The focus is on learning the best ways to teach yourself the language, based on ideas from the book "Antifragile" and my own experiences teaching myself how to make software that actually WORKS (solves your particular problem) in Python.

After going through a couple of simple programs I've written that highlight some basics of Python, I'll turn to the students and start guiding them on how they can attack their own problems in Python.

I'd be looking to focus on new programmers, as I'd think more experienced programmers may already know most of these things and would be bored. I'm not that advanced a coder myself, but I AM an experienced teacher. I started my teaching career at A&M, teaching for a semester in 1999.

I can send along a syllabus/outline if needed. Just let me know.
</pre>

##Key Points
-  Writing multiple, small programs, like in "Introduction to Python"
    -  BONUS: Can I design them such that we can link them together, as modules in a larger program? **THAT** would be *AWESOME*!
-  4 Hours
    -  3 hours to match PyTexas time slots
    -  1 hour for Q&A and helping people start on designing their OWN programs

##Core Novice Tutorial Topics
###Basic target apps: these will form the structure of the class
+  process a text file
    *  CSVs are ubiquitious
+  process an Excel file
+  pull JSON from the web and process it
    *  learn the YouTube JSON structure
+  process the contents of a directory
    *  use OS module to make this easier?
+  process Images? Use Pillow
    *  It may be too difficul to get installed for novices
    *  Usage guide is [here](https://pillow.readthedocs.org/en/latest/guides.html)

-  Basic data types
    +  Numbers; String; Bool?
    +  Variables
    +  When/How to use them

-  Collection types
    +  List; Tuple; Dictionary; Set
    +  When/how to use them
-  Using my Excel processing code as an example app
    +  One reason people want to learn to code is to work with all the data that's now available
-  GUI basics?
    +  after we build a basic app, add some GUI elements for picking files or URLs to process
    +  PyQT comes with Anaconda

##Which Python Environment?
-  Enthought Canopy
    +  plus: an editor w/ lint and interactive shell all in ONE place.
    +  minus: might change people's default environment
    +  minus: Python 2.7
-  Anaconda
    +  I need to learn more about this
    +  probably use the Python 3 version of this
-  Miniconda
-  Plain Python/IDLE + Sublime Text
    +  Idle would solve the "copy/paste into the interactive shell" issue that may come up with JUST CLI tools.
-  If I take a command line focus, that should "level the playing field", but I'll need to make sure I can get things working on Windows machines as well.

##Py2 vs Py3
-  I need to make a list of "major" modules not supported by Python 3 from https://python3wos.appspot.com

##Variant Class ideas
-  Intro to Python for aspiring Serious Programmers
    -  Text Editor
    -  Git
    -  Basic data structures
    -  IRC & contributing to projects
-  Intro to Python for Casual Progamming and Useful Everyday Stuff
    -  Python for people who aren't sure WHAT to do with Python
    -  Programming is about Problem Solving
    -  Fun, useful stuff