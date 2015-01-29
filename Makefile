lexer: src/lexer.py src/lex.py
	cp src/lexer.py bin/lexer.py
	cp src/lex.py bin/lex.py
	python -m py_compile bin/lex.py bin/lexer.py
	mv bin/lexer.pyc bin/lexer
	chmod +x bin/lexer

clean:
	rm -rf bin/*
