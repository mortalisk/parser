from lark import Lark
grammar = r"""
WHITESPACE: (" ")+
%ignore WHITESPACE
%ignore COMMENT


%import common.ESCAPED_STRING   -> STRING
%import common.CNAME
%import common.SIGNED_NUMBER    -> NUMBER
%import common.NEWLINE          -> NEWLINE


CHAR: /[.a-zæøå10-9\<\>\/]/
UNQUOTED: CHAR+


arg: CNAME | NUMBER  | STRING | UNQUOTED
arglist: CNAME kw_list

kw_list: "(" [ kw_pair ("," kw_pair)*] ")"
kw_val: CNAME | NUMBER | STRING | UNQUOTED
kw_pair: kw_name "=" kw_val
kw_name: "<" CNAME ">"

COMMENT: /--[^\n]*/

start: instruction+

inst: "FORWARD_MODEL" arglist -> test
    | "DEFINE" kw_name arg -> define
    | CNAME (arg | arglist)* -> undefined


instruction: inst (NEWLINE)


"""
#%import common._STRING_ESC_INNER -> UNQUOTED
with open("snake_oil.ert") as f:
    parser = Lark(grammar, propagate_positions=True)
    tree = parser.parse(f.read())
    print(tree.pretty())