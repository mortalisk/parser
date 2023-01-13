from lark import Lark
grammar = """

%import common.ESCAPED_STRING   -> STRING
%import common.CNAME
%import common.SIGNED_NUMBER    -> NUMBER

start: statement+
statement: CNAME CNAME
arg: CNAME | NUMBER | arglist | STRING 

arglist: CNAME kw_list
kw_list: "(" [ kw_pair ("," kw_pair)*] ")"
kw_pair: kw_name "=" STRING
kw_name: "<" CNAME ">"

comment: "//" STRING*



"""

with open("snake_oil.ert") as f:
    parser = Lark(grammar)
    tree = parser.parse(f.read())
    print(tree)