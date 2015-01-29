CS335A: Compiler Design (Assignment 1)
========================================

* Source Language: *Python*
* Target Language: *MIPS Assembly*
* Implementation Language: *Python*

* Tool Used : PLY (Python Lex and Yacc)

### Running Instruction
_______________________
1. Run the makefile 
```
make
```
2. To run the lexer, pass the path of filename as argument.
```
bin/lexer path/to/file
```
3. To clean the executables, run make clean.
```
make clean
```

### Directory Structure
_______________________
* bin:
	* lex.py [Python source file from PLY for lexing]
	* lexer [Python bytecode for lexer.py]
	* lexer.py [Python source file to specify language lexemes]
* src:
	* lex.py [Python source file from PLY for lexing]
	* lexer.py [Python source file to specify language lexemes]
* test:
	* test#.py [Test files]
* Makefile [To move the source files to bin directory and compile bytecode for lexer and making it executable]
* README.md
