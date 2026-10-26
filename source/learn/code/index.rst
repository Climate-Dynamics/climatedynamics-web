Coding for Beginners
====================

.. figure:: img/banner001_ccby_SebastianMutz.jpg
   :align: center

Description
------------

This is a series of exercises to introduce practical coding to absolute beginners. They are available in Fortran (a fast and well-established "compiled" language) and Python (a popular "interpreted" language).

They were developed as part of the `INTEGRATE teaching package <\https://integrate.mutz.science/>`_, which is based on workshops and lectures by Sebastian G. Mutz and supported by the EGU Higher Education Teaching Grant 2020.

If you are unsure about compiled and interpreted languages, see the explanation below.


Compiled or Interpreted
-----------------------

There are a few differences between compiled and interpreted languages. These are highlighted below in a simplified manner, which may (a) help you decide on a language you'd like to use, and (b) exaplain the difference in workflows if you previously used an interpreted language and now want to learn a compiled language (or vice versa).

**Compiled Language**: The whole programme is translated into *machine code* (i.e. your computers "language") by a so-called **compiler**. In the compilation process, a new file is created (separate from the text file you wrote your code into). This (executable) file can be run as a programme without the need of the original code (text file).

- **Analogy**: It can be thought of as the process of translating a poem completely into another language, then reading the translated poem to an audience. The original poem (script) and translator are no longer needed.
- **Examples**: Fortran, C
- **Advantages**: Usually faster performance, easy to control optimisations during compilation.

**Interpreted Language**: The programme does not have to be translated into *machine code* before execution. Instead, when you run your programme, your code (in the text file) is translated line-by-line by a so-called **interpreter**.

- **Analogy**: It can be thought of as someone reading a Bavarian poem and translating it line-by-line into English to an audience. The original poem (script) and translator are still needed.
- **Examples**: Python, JavaScript
- **Advantages**: More convenient, no need for manual compilation.


Exercises
--------

.. toctree::
   :caption: Fortran
   :maxdepth: 1

   E001/f90/E001.rst
   E002/f90/E002.rst
   E003/f90/E003.rst
..    E004/f90/E004.rst

.. toctree::
   :caption: Python
   :maxdepth: 1

   E001/py/E001.rst
   E002/py/E002.rst
   E003/py/E003.rst
..    E004/py/E004.rst
