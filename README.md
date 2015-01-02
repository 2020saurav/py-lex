CS335A: Compiler Design
======================
Assignment 1
------------

* Source Language: Python
* Target Language: MIPS Assembly
* Implementation Language: Python

* Lex-Yacc Tool Used: <a href="http://www.dabeaz.com/ply/" target="_blank"> PLY</a>

PLY Overview
------------
PLY consists of two separate modules; lex.py and yacc.py, both of which are found in a Python package called ply. The lex.py module is used to break input text into a collection of tokens specified by a collection of regular expression rules. yacc.py is used to recognize language syntax that has been specified in the form of a context free grammar. yacc.py uses LR parsing and generates its parsing tables using either the LALR(1) (the default) or SLR table generation algorithms.

The two tools are meant to work together. Specifically, lex.py provides an external interface in the form of a token() function that returns the next valid token on the input stream. yacc.py calls this repeatedly to retrieve tokens and invoke grammar rules. The output of yacc.py is often an Abstract Syntax Tree (AST). However, this is entirely up to the user. If desired, yacc.py can also be used to implement simple one-pass compilers.
More on <a href="http://www.dabeaz.com/ply/ply.html" target="_blank"> PLY </a>