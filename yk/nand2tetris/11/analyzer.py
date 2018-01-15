#!/usr/bin/env python3
import glob
import os
import re
import sys
import xml.etree.ElementTree as ET


class JackAnalyzer:
    def __init__(self):
        argv1 = sys.argv[1]  # Gets command line argument.
        if not os.path.exists(argv1):  # Ensures file existence.
            raise Exception("File not exists.")
        path_abs = os.path.abspath(argv1)  # Gets absolute path.
        print("abspath =", path_abs)
        isdir = os.path.isdir(path_abs)

        def f(path_abs):
            """Processes a file."""
            basename = os.path.basename(path_abs)
            print(basename)
            dirname = os.path.dirname(path_abs)
            root, ext = os.path.splitext(basename)
            path_output = "{}/{}.output.xml".format(dirname, root)
            print("path_output =", path_output)
            path_output_t = "{}/{}T.output.xml".format(dirname, root)
            print("path_output_t =", path_output_t)
            path_output_vm = "{}/{}.output.vm".format(dirname, root)
            print("path_output_vm =", path_output_vm)
            t = JackTokenizer(path_abs)
            tokens = f_tokens(t)
            s = f_xml_tokens(tokens)

            with open(path_output_t, "w") as f:  # Token list xml.
                f.write(s)

            e = CompilationEngine(tokens, path_output)
            tokens2 = e.tokens()
            s = f_xml_tokens2(tokens2)

            with open(path_output, "w") as f:  # Parsed tree xml.
                f.write(s)

            s = append_symbol_desc(s)
            x = CompilationEngine2(s)
            s = str(x)

            with open(path_output_vm, "w") as f:  # .vm file.
                f.write(s)

        if not isdir:  # Process a file.
            f(path_abs)
        else:          # Process files in a directory.
            s = "{}/*.jack".format(path_abs)  # Gets all .jack files.
            paths = glob.glob(s)

            for path in paths:
                f(path)


class JackTokenizer:
    _keywords = ("class constructor function method field static var int char "
                 "boolean void true false null this let do if else while "
                 "return".split())
    _symbols = "{ } ( ) [ ] . , ; + - * / & | < > = ~".split()

    def __init__(self, path_input):
        """Breaks the string in a file path_input into a list."""
        with open(path_input, "r") as f:
            s = f.read()

        # Removes comments.
        s = re.sub("/\*.*?\*/", "", s, flags=re.DOTALL)  # /* ... */ -> None
        s = re.sub("//.*\n", "\n", s)  # // ...    -> None
        # Removes empty lines.
        s = "\n".join([s for s in s.splitlines() if s.strip() != ""])
        print(s)
        is_inside = False
        s2 = ""

        # Replaces spaces in string literals to an escape sequence.
        for c in s:
            if c == '"':
                is_inside = not is_inside
            if is_inside and c == " ":
                s2 += "SPACEINSTRING"  # Replaces to an escape sequence.
            else:
                s2 += c

        s = s2
        # Places spaces on left and right of a symbol.
        s = re.sub("([\{\}\(\)\[\]\.,;\+\-\*/&|<>=~])", r" \1 ", s)
        s2 = ""

        # Removes false spaces in string literals.
        for c in s:
            if c == '"':
                is_inside = not is_inside
            if is_inside and c == " ":
                s2 += ""  # Removes space.
            else:
                s2 += c

        s = s2
        # Replaces multiple continuous space into one.
        s = re.sub(" +", " ", s)
        ss = s.splitlines()  # [line_0, line_1, ..., line_n]
        ss = [s.strip() for s in ss]     # Trims spaces.
        ss = [s for s in ss if s != ""]  # Removes empty lines.
        s = "\n".join(ss)         # One string again.
        ss = re.split(" |\n", s)  # Splits to tokens.
        self._tokens = ss
        self._index_token = -1

    def _token(self):
        """Returns the current token."""
        return self._tokens[self._index_token]

    def hasMoreTokens(self):
        """Returns if there is more tokens."""
        return (self._index_token + 1) < len(self._tokens)

    def advance(self):
        """Goes on to the next token."""
        self._index_token += 1

    def tokenType(self):
        """Returns the token type. There are 5 types."""
        s = self._token()

        if s in self._keywords:
            return "KEYWORD"
        if s in self._symbols:
            return "SYMBOL"
        if s.isdigit():
            return "INT_CONST"
        if s.startswith('"'):
            return "STRING_CONST"

        return "IDENTIFIER"

    def keyWord(self):
        """Returns the keyword if tokenType() == KEYWORD."""
        s = self._token()
        return s.upper()

    def symbol(self):
        """Returns the symbol character if tokenType() == SYMBOL."""
        return self._token()

    def identifier(self):
        """Returns the identifier if tokenType() == IDENTIFIER."""
        return self._token()

    def intVal(self):
        """Returns the integer value if tokenType() == INT_CONST."""
        return int(self._token())

    def stringVal(self):
        """Returns the string if tokenType() == STRING_CONST."""
        return self._token()[1:-1]


def f_tokens(t):
    """Returns a token list from the given tokenizer.
    e.g. [("keyword", "class"), ...]."""
    tokens = []

    while t.hasMoreTokens():
        t.advance()
        type = t.tokenType()

        if type == "KEYWORD":
            elem = t.keyWord().lower()
        elif type == "SYMBOL":
            elem = t.symbol()
        elif type == "IDENTIFIER":
            elem = t.identifier()
        elif type == "INT_CONST":
            elem = str(t.intVal())
        elif type == "STRING_CONST":
            elem = t.stringVal()
        else:
            raise Exception("Unknown token type.")

        type2 = type.lower()

        if type2 == "int_const":
            type2 = "integerConstant"
        elif type2 == "string_const":
            type2 = "stringConstant"
            elem = elem.replace("SPACEINSTRING", " ")  # Decodes escaped ones.

        tokens.append((type2, elem))

    return tokens


def f_xml_tokens(tokens):
    """Returns a xml string represents given tokens.
    [("keyword", "class"), ...] ->
    "<tokens>\\n<keyword> class </keyword> ... </tokens>" """
    def encode_html(s):
        return (s.replace("&", "&amp;").replace("<", "&lt;")
                .replace(">", "&gt;"))
    s = "<tokens>\n"
    for tag, elem in tokens:
        s += "<{0}> {1} </{0}>\n".format(tag, encode_html(elem))
    s += "</tokens>\n"
    return s


def f_xml_tokens2(tokens):
    """Returns a xml string represents given structure.
    [("begin", "class"), ...] ->
    "<class>\\n<keyword> class </keyword> ... </class>" """
    def encode_html(s):
        return (s.replace("&", "&amp;").replace("<", "&lt;")
                .replace(">", "&gt;"))

    def f():
        nonlocal s
        s += "  " * n
    s = ""
    n = 0  # n_indent
    for tag, elem in tokens:
        if tag == "begin":
            f()
            s += "<{}>\n".format(elem)
            n += 1
        elif tag == "end":
            n -= 1
            f()
            s += "</{}>\n".format(elem)
        else:
            f()
            s += "<{0}> {1} </{0}>\n".format(tag, encode_html(elem))
    return s


class CompilationEngine:
    """Returns parsed structure from the given token list.
    [("keyword", "class"), ...] -> [("begin", "class"), ...]
    Returns (tag, elem) for tokens, but (begin/end, tag) for structure."""
    def __init__(self, tokens, path_output):
        self._tokens = tokens
        self._index = 0
        self._tokens2 = []

        if self._get() == ("keyword", "class"):
            self.compileClass()
        else:
            raise Exception("First token is not keyword class.")

    def _d(self):  # For debug.
        print(f_xml_tokens2(self._tokens2))

    def _add(self, x):
        """Adds x to the structure."""
        self._tokens2.append(x)

    def _add2(self):
        """Adds the current token into the structure."""
        self._add(self._get())
        self._succ()

    def _get(self):
        """Returns the current token."""
        return self._tokens[self._index]

    def _get_next(self):
        """Returns the next token."""
        return self._tokens[self._index + 1]

    def _succ(self):
        """Selects the next token."""
        self._index += 1

    def compileClass(self):
        """Compiles a complete class."""
        self._add(("begin", "class"))
        self._add2()    # "class"
        self._add2()    # className
        self._add2()    # "{"
        tag, elem = self._get()

        while elem != "}":
            if elem in ["static", "field"]:
                self.compileClassVarDec()
            elif elem in ["constructor", "function", "method"]:
                self.compileSubroutine()
            else:
                raise Exception(elem)

            tag, elem = self._get()

        self._add2()    # "}"
        self._add(("end", "class"))

    def compileClassVarDec(self):
        self._add(("begin", "classVarDec"))
        self._add2()    # "static" | "field"
        self._add2()    # type
        self._add2()    # varName
        tag, elem = self._get()
        while elem == ",":
            self._add2()    # ","
            self._add2()    # varName
            tag, elem = self._get()
        self._add2()    # ";"
        self._add(("end", "classVarDec"))

    def compileSubroutine(self):
        self._add(("begin", "subroutineDec"))
        self._add2()    # "constructor" | "function" | "method"
        self._add2()    # "void" | type
        self._add2()    # subroutineName
        self._add2()    # "("
        self.compileParameterList()
        self._add2()    # ")"
        self._add(("begin", "subroutineBody"))
        self._add2()    # "{"
        tag, elem = self._get()

        while elem == "var":
            self.compileVarDec()
            tag, elem = self._get()

        self.compileStatements()
        self._add2()    # "}"
        self._add(("end", "subroutineBody"))
        self._add(("end", "subroutineDec"))

    def compileParameterList(self):
        self._add(("begin", "parameterList"))
        tag, elem = self._get()

        while elem != ")":
            self._add2()    # type
            self._add2()    # varName
            tag, elem = self._get()
            if elem == ",":
                self._add2()    # ","
                tag, elem = self._get()
        self._add(("end", "parameterList"))

    def compileVarDec(self):
        self._add(("begin", "varDec"))
        self._add2()    # "var"
        self._add2()    # type
        self._add2()    # varName
        tag, elem = self._get()

        while elem != ";":
            self._add2()    # ","
            self._add2()    # varName
            tag, elem = self._get()

        self._add2()    # ";"
        self._add(("end", "varDec"))

    def compileStatements(self):
        self._add(("begin", "statements"))
        tag, elem = self._get()

        while True:
            if elem == "let":
                self.compileLet()
            elif elem == "if":
                self.compileIf()
            elif elem == "while":
                self.compileWhile()
            elif elem == "do":
                self.compileDo()
            elif elem == "return":
                self.compileReturn()
            else:
                break

            tag, elem = self._get()

        self._add(("end", "statements"))

    def compileDo(self):
        self._add(("begin", "doStatement"))
        self._add2()    # "do"
        self._compileSubroutineCall()
        self._add2()    # ";"
        self._add(("end", "doStatement"))

    def compileLet(self):
        self._add(("begin", "letStatement"))
        self._add2()    # "let"
        self._add2()    # varname
        tag, elem = self._get()

        if elem == "[":
            self._add2()    # "["
            self.compileExpression()
            self._add2()    # "]"

        self._add2()    # "="
        self.compileExpression()
        self._add2()    # ";"
        self._add(("end", "letStatement"))

    def compileWhile(self):
        self._add(("begin", "whileStatement"))
        self._add2()    # "while"
        self._add2()    # "("
        self.compileExpression()
        self._add2()    # ")"
        self._add2()    # "{"
        self.compileStatements()
        self._add2()    # "}"
        self._add(("end", "whileStatement"))

    def compileReturn(self):
        self._add(("begin", "returnStatement"))
        self._add2()    # "return"
        tag, elem = self._get()

        if elem != ";":
            self.compileExpression()

        self._add2()    # ";"
        self._add(("end", "returnStatement"))

    def compileIf(self):
        self._add(("begin", "ifStatement"))
        self._add2()    # "if"
        self._add2()    # "("
        self.compileExpression()
        self._add2()    # ")"
        self._add2()    # "{"
        self.compileStatements()
        self._add2()    # "}"
        tag, elem = self._get()

        if elem == "else":
            self._add2()    # "else"
            self._add2()    # "{"
            self.compileStatements()
            self._add2()    # "}"

        self._add(("end", "ifStatement"))

    def compileExpression(self):
        self._add(("begin", "expression"))
        self.compileTerm()
        tag, elem = self._get()

        while elem in ["+", "-", "*", "/", "&", "|", "<", ">", "="]:
            self._add2()    # op
            self.compileTerm()
            tag, elem = self._get()

        self._add(("end", "expression"))

    def compileTerm(self):
        self._add(("begin", "term"))
        tag, elem = self._get()

        if tag in ["integerConstant", "stringConstant", "keyword"]:
            self._add2()
        elif elem in ["-", "~"]:
            self._add2()    # "-" | "~"
            self.compileTerm()
        elif elem == "(":
            self._add2()    # "("
            self.compileExpression()
            self._add2()    # ")"
        else:
            tag2, elem2 = self._get_next()

            if elem2 in ["(", "."]:
                self._compileSubroutineCall()
            elif elem2 == "[":
                self._add2()    # varName
                self._add2()    # "["
                self.compileExpression()
                self._add2()    # "]"
            else:
                self._add2()    # varName

        self._add(("end", "term"))

    def compileExpressionList(self):
        self._add(("begin", "expressionList"))
        tag, elem = self._get()

        if elem != ")":
            self.compileExpression()
            tag, elem = self._get()

            while elem == ",":
                self._add2()    # ","
                self.compileExpression()
                tag, elem = self._get()

        self._add(("end", "expressionList"))

    def _compileSubroutineCall(self):
        tag, elem = self._get_next()

        if elem == "(":
            self._add2()    # subroutineName
            self._add2()    # "("
            self.compileExpressionList()
            self._add2()    # ")"
        else:
            self._add2()    # className | varName
            self._add2()    # "."
            self._add2()    # subroutineName
            self._add2()    # "("
            self.compileExpressionList()
            self._add2()    # ")"

    def tokens(self):
        return self._tokens2


class SymbolTable:
    def __init__(self):
        self._scope_class = []
        self._scope_sub = []

    def d(self, table_repr):
        d = {"arg": "ARG", "var": "LOCAL", "static": "STATIC", "field": "THIS"}
        writer_repr = d[table_repr]
        return writer_repr

    def has(self, name):
        try:
            self.tupleOf(name)
            return True
        except KeyError:
            return False

    def print(self):
        s = ""
        s += "==== {:=<35}\n".format("scope class ")

        for n, t, k, i in self._scope_class:
            s += "{: <14} {: <9} {: <9} {}\n".format(n, t, k, i)

        s += "==== {:=<35}\n".format("scope subroutine ")

        for n, t, k, i in self._scope_sub:
            s += "{: <14} {: <9} {: <9} {}\n".format(n, t, k, i)

        s += "=" * 40
        print(s)

    def tupleOf(self, name):
        for x in self._scope_sub + self._scope_class:
            n, type_, kind, index = x
            if n == name:
                return x

        raise KeyError(name)

    def startSubroutine(self):
        self._scope_sub.clear()

    def define(self, name, type_, kind):
        count = self.varCount(kind)

        if kind in ["static", "field"]:
            lis = self._scope_class
        elif kind in ["arg", "var"]:
            lis = self._scope_sub
        else:
            raise Exception("Unknown kind.")

        lis.append((name, type_, kind, count))

    def varCount(self, kind):
        count = 0

        for _, _, k, _ in self._scope_sub + self._scope_class:
            if k == kind:
                count += 1

        return count

    def kindOf(self, name):
        name, type_, kind, index = self.tupleOf(name)
        return kind

    def typeOf(self, name):
        name, type_, kind, index = self.tupleOf(name)
        return type_

    def indexOf(self, name):
        name, type_, kind, index = self.tupleOf(name)
        return index


class VMWriter:
    def __init__(self):
        self._seg0 = "CONST ARG LOCAL STATIC THIS THAT POINTER TEMP".split()
        # p. 145
        self._seg1 = (
            "constant argument local static this that pointer temp".split())
        self._d = dict(zip(self._seg0, self._seg1))
        self._s = ""
        self.indent = 0

    def _p(self, s):
        # self._s += "    " * self.indent + s + "\n"
        self._s += s + "\n"

    def writePush(self, segment, index):
        if segment not in self._seg0:
            raise Exception(segment)

        segment = self._d[segment]
        self._p("push {} {}".format(segment, index))

    def writePop(self, segment, index):
        if segment not in self._seg0:
            raise Exception(segment)

        segment = self._d[segment]
        self._p("pop {} {}".format(segment, index))

    def writeArithmetic(self, command):
        command = command.lower()

        if command in "add sub neg eq gt lt and or not".split():
            self._p("{}".format(command.lower()))
        else:
            raise Exception(command)

    def writeLabel(self, label):
        self._p("label {}".format(label))

    def writeGoto(self, label):
        self._p("goto {}".format(label))

    def writeIf(self, label):
        self._p("if-goto {}".format(label))

    def writeCall(self, name, nArgs):
        self._p("call {} {}".format(name, nArgs))

    def writeFunction(self, name, nLocals):
        self._p("function {} {}".format(name, nLocals))

    def writeReturn(self):
        self._p("return")

    def close(self):
        return self._s


def append_symbol_desc(xml):
    """Appends attributes to the identifier tags."""
    depth = 0
    info = ()
    n = 0

    def f(elem):
        """Processes an element recursively."""
        nonlocal depth, info, n

        if elem.tag == "class":
            info = ("class", "defined", "na", -1)
        elif elem.tag == "subroutineDec":
            info = ("subroutine", "defined", "na", -1)
        elif elem.tag == "parameterList":
            info = ("argument", "defined", "argument", 1)
            n = 1  # argument (without "this")
        elif elem.tag == "subroutineBody":
            info = ("var", "defined", "var", 1)
            n = 0  # var
        elif elem.tag == "statements":
            info = ("?", "used", "?", -1)
        elif elem.tag == "identifier":
            elem.attrib["appear"] = info[1]
            if info[1] != "used":
                elem.attrib["cat"] = info[0]
                elem.attrib["kind"] = info[2]
            if info[3] != -1:
                elem.attrib["n"] = str(n)
                n += 1

        depth += 1

        for child in elem:
            f(child)

        depth -= 1

    root = ET.fromstring(xml)
    f(root)
    xml = ET.tostring(root).decode("utf-8")
    return xml


def debug_print_xml(xml, start=0, stop=-1, step=1):
    s = ""
    depth = 0

    def f(elem):
        nonlocal depth, s
        attrib = elem.attrib if elem.attrib else ""
        s += "{}{} {} {}\n".format(
            "  " * depth, elem.tag, elem.text.strip(), attrib)
        depth += 1

        for child in elem:
            f(child)

        depth -= 1
    root = ET.fromstring(xml)
    f(root)
    ss = s.splitlines()
    len_before = len(ss)
    s = "\n".join(ss[start:stop:step])
    ss = s.splitlines()
    len_after = len(ss)
    x = "[{}:{}:{}] ({:.0f}%) ".format(
        start, stop, step, len_after / len_before * 100)
    x = "==== {:=<75}".format(x)
    print(x)
    print(s)
    print(x)


class CompilationEngine2:
    def __init__(self, xml):
        debug_print_xml(xml, 0, 20)
        root = ET.fromstring(xml)
        self._p = dict(
            (child, parent) for parent in root.iter()
            for child in parent)  # child -> parent dictionary.
        self._s = ""
        self._t = SymbolTable()
        self._w = VMWriter()
        self._n_labels = 0

        if (root.tag == "class"):
            self.compileClass(root)

    def __repr__(self):
        return self._w.close()

    def _new_label(self):
        s = "L{}".format(self._n_labels)
        self._n_labels += 1
        return s

    def _p1(self, e):
        tag = e.tag
        children = ", ".join([x.tag for x in e.findall("./*")])
        print("tag={}, children=({})".format(tag, children))

    def compileClass(self, e):
        self._class = e.find("./identifier").text.strip()

        for x in e.findall("./classVarDec"):
            self.compileClassVarDec(x)

        for x in e.findall("./subroutineDec"):
            self.compileSubroutine(x)

    def compileClassVarDec(self, e):
        kind = e[0].text.strip()
        type_ = e[1].text.strip()
        ids = [x for x in e.findall("./*")[2:] if x.tag == "identifier"]

        for x in ids:
            self._t.define(x.text.strip(), type_, kind)

    def compileSubroutine(self, e):
        self._t.startSubroutine()
        id = e[2].text.strip()
        keyword0 = e[0].text.strip()
        n_locals = 0

        for varDec in e.findall("./subroutineBody/varDec"):
            ids = [
                x for x in varDec.findall("./*")[2:] if x.tag == "identifier"]
            n_locals += len(ids)

        if keyword0 == "function":
            self._w.writeFunction("{}.{}".format(self._class, id), n_locals)
        elif keyword0 == "method":
            self._w.writeFunction(
                "{}.{}".format(self._class, id), n_locals + 1)
            self._w.writePush("ARG", 0)
            self._w.writePop("POINTER", 0)
            self._t.define("self", self._class, "arg")
        elif keyword0 == "constructor":
            self._w.writeFunction("{}.{}".format(self._class, "new"), n_locals)
            n = self._t.varCount("field")  # instance size n (p. 256)
            self._w.writePush("CONST", str(n))
            self._w.writeCall("Memory.alloc", 1)
            self._w.writePop("POINTER", 0)  # p. 262
        else:
            raise Exception(keyword0)

        for i, x in enumerate(e.find("./parameterList")):
            text = x.text.strip()

            if i % 3 == 0:
                type_ = text
            elif i % 3 == 1:
                self._t.define(text, type_, "arg")

        self._w.indent += 1

        for x in e.findall("./subroutineBody/varDec"):
            self.compileVarDec(x)

        x = e.find("./subroutineBody/statements")

        if x:
            self.compileStatements(x)

        self._w.indent -= 1

#    def compileParameterList(self):
#        pass

    def compileVarDec(self, e):
        ids = [x for x in e.findall("./*")[2:] if x.tag == "identifier"]

        for x in ids:
            self._t.define(x.text.strip(), e[1].text.strip(), "var")

    def compileStatements(self, e):
        for x in e.findall("./*"):
            if x.tag == "doStatement":
                self.compileDo(x)
            elif x.tag == "letStatement":
                self.compileLet(x)
            elif x.tag == "ifStatement":
                self.compileIf(x)
            elif x.tag == "returnStatement":
                self.compileReturn(x)
            elif x.tag == "whileStatement":
                self.compileWhile(x)
            else:
                print("compileStatements - {}".format(x.tag))

    def compileDo(self, e):
        self._compileSubroutineCall(e)

    def compileLet(self, e):
        self.compileExpression(e.findall("./*")[-2])
        id = e.find("./identifier").text.strip()
        kind, index = self._t.kindOf(id), self._t.indexOf(id)
        kind = self._t.d(kind)

        n_children = len(e.findall("./*"))

        if n_children == 5:
            self._w.writePop(kind, index)
        elif n_children == 8:
            self._w.writePush(kind, index)
            self.compileExpression(e[3])
            self._w.writeArithmetic("ADD")
            self._w.writePop("POINTER", "1")
            self._w.writePop("THAT", "0")
        else:
            raise Exception(n_children)

    def compileWhile(self, e):  # p. 260
        self._w.indent += 1
        begin = self._new_label() + "_begin_while"
        end = self._new_label() + "_end_while"
        self._w.writeLabel(begin)
        self.compileExpression(e.find("./expression"))
        self._w.writeArithmetic("NOT")
        self._w.writeIf(end)
        self.compileStatements(e.find("./statements"))
        self._w.writeGoto(begin)
        self._w.writeLabel(end)
        self._w.indent -= 1

    def compileReturn(self, e):
        x = e.find("./expression")

        if x:
            self.compileExpression(x)
        else:
            self._w.writePush("CONST", "0")  # p. 262

        self._w.writeReturn()

    def compileIf(self, e):  # p. 260
        self._w.indent += 1
        else_ = self._new_label() + "_if_else"
        end = self._new_label() + "_if_end"
        ss = e.findall("./statements")
        self.compileExpression(e.find("./expression"))
        self._w.writeArithmetic("NOT")
        self._w.writeIf(else_)
        self.compileStatements(ss[0])
        self._w.writeGoto(end)
        self._w.writeLabel(else_)

        if len(ss) == 2:
            self.compileStatements(ss[1])

        self._w.writeLabel(end)
        self._w.indent -= 1

    def compileExpression(self, e):
        for x in e.findall("./term"):
            self.compileTerm(x)

        for x in list(e.findall("./symbol"))[::-1]:
            s = x.text.strip()
            if s == "+":
                self._w.writeArithmetic("ADD")
            elif s == "-":
                self._w.writeArithmetic("SUB")
            elif s == "=":
                self._w.writeArithmetic("EQ")
            elif s == ">":
                self._w.writeArithmetic("GT")
            elif s == "<":
                self._w.writeArithmetic("LT")
            elif s == "&":
                self._w.writeArithmetic("AND")
            elif s == "|":
                self._w.writeArithmetic("OR")
            elif s == "*":
                self._w.writeCall("Math.multiply", 2)  # p. 263
            elif s == "/":
                self._w.writeCall("Math.divide", 2)  # p. 263
            else:
                raise Exception(s)

    def compileTerm(self, e):
        x = e[0]
        tag, text = x.tag, x.text.strip()

        if tag == "integerConstant":
            self._w.writePush("CONST", x.text.strip())
        elif tag == "stringConstant":  # p. 263
            self._w.writePush("CONST", len(text))
            self._w.writeCall("String.new", "1")

            for char in text:
                self._w.writePush("CONST", str(ord(char)))
                self._w.writeCall("String.appendChar", "2")
        elif tag == "keyword":
            if text == "true":  # true == -1 (p. 143)
                self._w.writePush("CONST", "1")
                self._w.writeArithmetic("NEG")  # p. 263
            elif text == "false":
                self._w.writePush("CONST", "0")
            elif text == "null":
                self._w.writePush("CONST", "0")  # p. 263
            elif text == "this":
                self._w.writePush("POINTER", "0")
            else:
                raise Exception(text)
        elif tag == "symbol":
            if text == "(":
                self.compileExpression(e[1])
            elif text in ["-", "~"]:  # unaryOp
                self.compileTerm(e[1])
                self._w.writeArithmetic("NEG" if text == "-" else "NOT")
            else:
                raise Exception(text)
        elif e[-1].tag == "symbol":
            x = e[-1].text.strip()
            if x == ")":
                self._compileSubroutineCall(e)
            elif x == "]":
                id = text
                kind, index = self._t.kindOf(id), self._t.indexOf(id)
                kind = self._t.d(kind)
                self._w.writePush(kind, index)
                self.compileExpression(e[-2])
                self._w.writeArithmetic("ADD")
                self._w.writePop("POINTER", "1")
                self._w.writePush("THAT", "0")
            else:
                raise Exception(x)
        elif tag == "identifier":
            id = text
            kind, index = self._t.kindOf(id), self._t.indexOf(id)
            kind = self._t.d(kind)
            self._w.writePush(kind, index)
        else:
            print("compileTerm - else; {} {}".format(tag, text))

    def compileExpressionList(self, e):
        for x in e.findall("./expression"):
            self.compileExpression(x)

    def _compileSubroutineCall(self, e):
        children = e.findall("./*")

        if e[0].text.strip() == "do":
            children = children[1:-1]  # 'do' subroutineCall ';'

        n_args = len(e.findall("./expressionList/expression"))
        x = [x.text.strip() for x in e.findall("./identifier")]

        if len(x) == 2:
            if self._t.has(x[0]):
                id = x[0]
                kind, index = self._t.kindOf(id), self._t.indexOf(id)
                kind = self._t.d(kind)
                self._w.writePush(kind, index)
                self.compileExpressionList(e.find("./expressionList"))
                type_ = self._t.typeOf(id)
                self._w.writeCall("{}.{}".format(type_, x[1]), n_args + 1)
            else:
                self.compileExpressionList(e.find("./expressionList"))
                self._w.writeCall("{}.{}".format(x[0], x[1]), n_args)
        elif len(x) == 1:
            self._w.writePush("POINTER", 0)
            self.compileExpressionList(e.find("./expressionList"))
            self._w.writeCall("{}.{}".format(self._class, x[0]), n_args + 1)
        else:
            raise Exception(len(x))

        if e[0].text.strip() == "do":
            self._w.writePop("TEMP", 0)


def main():
    JackAnalyzer()


if __name__ == "__main__":
    main()
