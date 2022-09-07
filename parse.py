import pyparsing as pp

dbl_dash_comment = pp.Regex(r"--(?:\\\n|[^\n])*").set_name("-- comment")

string = pp.quotedString
identifier = pp.Word(pp.identchars + "/", pp.identbodychars + "/-")
keyword = identifier | string

subarg = pp.Literal("<").suppress() + identifier + pp.Literal(">").suppress() + pp.Literal("=").suppress() + string
id_arglist = pp.Group(identifier + pp.Literal("(").suppress() + pp.Group(pp.delimited_list(subarg)) + pp.Literal(")").suppress())
arg = string | id_arglist | identifier | pp.Word(pp.alphanums)

line = keyword + pp.ZeroOrMore(arg) + pp.Suppress(pp.Optional(dbl_dash_comment)) | dbl_dash_comment | pp.empty

line.validate()

with open("snake_oil.ert") as f:
    for l in f.readlines():
        print(f"{l=}")
        res = line.parse_string(l)
        print(res)

 

