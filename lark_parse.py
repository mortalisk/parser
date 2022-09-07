from lark import Lark
grammar = """
statement: name arg* COMMENT?
arg: name | number | arglist | string | path

path: 

arglist: name kw_list
kw_list: "(" [ kw_pair ("," kw_pair)*] ") 
kw_pair: kw_name "=" string
kw_name: "<" name ">"

COMMENT: "//" /[^\n]*/ NEWLINE
NEWLINE: "\n"

%import common.ESCAPED_STRING   -> string
%import common.CNAME -> name
%import common.SIGNED_NUMBER    -> number
"""

parser = Lark()