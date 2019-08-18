import re

langs = r'C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC'.replace(':', '|')

for _ in range(int(input())):
    match = re.match(r'^\d+\s(?:{})$'.format(langs), input())

    if match:
        print('VALID')

    else:
        print('INVALID')
