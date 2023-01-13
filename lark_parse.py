from lark import Lark
grammar = r"""

%import common.ESCAPED_STRING   -> STRING
%import common.CNAME
%import common.SIGNED_NUMBER    -> NUMBER
%import common.NEWLINE          -> NEWLINE


arg: CNAME | NUMBER | arglist | STRING 

arglist: CNAME kw_list
kw_list: "(" [ kw_pair ("," kw_pair)*] ")"
kw_val: arg
kw_pair: kw_name "=" kw_val
kw_name: "<" CNAME ">"

COMMENT: "--" /[^\n]*/

start: instruction+

inst: "TEST" arg* -> test
    | "DEFINE" kw_name arg -> define

instruction: inst NEWLINE

WHITESPACE: (" ")+
%ignore WHITESPACE
%ignore COMMENT

"""
#%import common._STRING_ESC_INNER -> UNQUOTED
with open("snake_oil.ert") as f:
    parser = Lark(grammar, propagate_positions=True)
    tree = parser.parse(f.read())
    print(tree.pretty())