#!/usr/bin/env python3
import glob
import os
import re
import sys
import xml.etree.ElementTree as ET
from xml.dom import minidom

class JackAnalyzer:
    def __init__(self):
        argv1 = sys.argv[1]
        if not os.path.exists(argv1):
            raise Exception("File not exists.")
        path_abs = os.path.abspath(argv1)
        print("abspath =", path_abs)
        isdir = os.path.isdir(path_abs)
        
        def f(path_abs):
            basename = os.path.basename(path_abs)
            print(basename)
            dirname = os.path.dirname(path_abs)
            root, ext = os.path.splitext(basename)
            path_output = "{}/{}.output.xml".format(dirname, root)
            print("path_output =", path_output)
            path_output_t = "{}/{}T.output.xml".format(dirname, root)
            print("path_output_t =", path_output_t)
            t = JackTokenizer(path_abs)
            tokens = f_tokens(t)
            s = f_xml_tokens(tokens)
            
            with open(path_output_t, "w") as f:
                f.write(s)
            
            e = CompilationEngine(tokens, path_output)
            tokens2 = e.tokens()
            s = f_xml_tokens2(tokens2)
            
            with open(path_output, "w") as f:
                f.write(s)
            
            s = append_symbol_desc(s)
            s = f_vm(s)
            print(s)
        
        if not isdir:
            f(path_abs)
        else:
            s = "{}/*.jack".format(path_abs)
            paths = glob.glob(s)
            
            for path in paths:
                f(path)

class JackTokenizer:
    _keywords = "class constructor function method field static var int char boolean void true false null this let do if else while return".split()
    _symbols = "{ } ( ) [ ] . , ; + - * / & | < > = ~".split()
    
    def __init__(self, path_input):
        with open(path_input, "r") as f:
            s = f.read()
        
        s = re.sub("/\*.*?\*/", "", s, flags=re.DOTALL) # /* ... */ -> None
        s = re.sub("//.*\n", "\n", s) # // ...    -> None
        is_inside = False
        s2 = ""
        
        for c in s:
            if c == '"':
                is_inside = not is_inside
            if is_inside and c == " ":
                s2 += "SPACEINSTRING"
            else:
                s2 += c
        
        s = s2
        s = re.sub("([\{\}\(\)\[\]\.,;\+\-\*/&|<>=~])", r" \1 ", s)
        s = re.sub(" +", " ", s)
        ss = s.splitlines()
        ss = [s.strip() for s in ss]
        ss = [s for s in ss if s != ""] # Removes empty lines.
        s = "\n".join(ss)
        ss = re.split(" |\n", s)
        self._tokens = ss
        self._index_token = -1
    
    def _token(self):
        return self._tokens[self._index_token]
    
    def hasMoreTokens(self):
        return (self._index_token + 1) < len(self._tokens)
    
    def advance(self):
        self._index_token += 1
    
    def tokenType(self):
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
        s = self._token()
        return s.upper()
    
    def symbol(self):
        return self._token()
    
    def identifier(self):
        return self._token()
    
    def intVal(self):
        return int(self._token())
    
    def stringVal(self):
        return self._token()[1:-1]

def f_tokens(t):
    """Returns a token list from the given tokenizer."""
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
            elem = elem.replace("SPACEINSTRING", " ")
        
        tokens.append((type2, elem))
    
    return tokens

def f_xml_tokens(tokens):
    def encode_html(s):
        return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = "<tokens>\n"
    for tag, elem in tokens:
        s += "<{0}> {1} </{0}>\n".format(tag, encode_html(elem))
    s += "</tokens>\n"
    return s

def f_xml_tokens2(tokens):
    def encode_html(s):
        return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    def f():
        nonlocal s
        s += "  " * n
    s = ""
    n = 0 # n_indent
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
    def __init__(self, tokens, path_output):
        self._tokens = tokens
        self._index = 0         # index
        self._tokens2 = []
        
        if self._get() == ("keyword", "class"):
            self.compileClass()
        else:
            print(self._get(), 99)
            raise Exception("First token is not keyword class.")
    
    def _d(self): # For debug.
        print(f_xml_tokens2(self._tokens2))
    
    def _add(self, x):
        self._tokens2.append(x)
    
    def _add2(self):
        self._add(self._get())
        self._succ()
    
    def _get(self):
        return self._tokens[self._index]
    
    def _get_next(self):
        return self._tokens[self._index + 1]
    
    def _succ(self):
        self._index += 1
    
    def compileClass(self):
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
                raise Exception()
            
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
    
    def startSubroutine(self):
        self._scope_sub.clear()
    
    def define(self, name, type, kind):
        count = self.varCount(kind)
        if kind in ["static", "field"]:
            lis = self._scope_class
        elif kind in ["arg", "var"]:
            lis = self._scope_sub
        else:
            raise Exception("Unknown kind.")
        lis.append((name, type, kind, count + 1))
        
    def varCount(self, kind):
        count = 0
        for _, _, k, _ in self._scope_sub + self._scope_class:
            if k == kind:
                count += 1
        return count
        
    def kindOf(self, name):
        for n, t, k, i in self._scope_sub + self._scope_class:
            if name == n:
                return k
    
    def typeOf(self, name):
        for n, t, k, i in self._scope_sub + self._scope_class:
            if name == n:
                return t
    
    def indexOf(self, name):
        for n, t, k, i in self._scope_sub + self._scope_class:
            if name == n:
                return i

class VMWriter:
    def __init__(self):
        self._s = ""
    def _p(self, s):
        self._s += s + "\n"
    def writePush(self, segment, index):
        pass
    def writePop(self, segment, index):
        pass
    def writeArithmetic(self, command):
        self._p(command.lower())
    def writeLabel(self, label):
        pass
    def writeGoto(self, label):
        pass
    def writeIf(self, label):
        pass
    def writeCall(self, name, nArgs):
        pass
    def writeFunction(self, name, nLocals):
        self._p("function {} {}".format(name, nLocals))
    def writeReturn(self):
        pass
    def close(self):
        return self._s

def append_symbol_desc(xml):
    depth = 0
    info = ()
    n = 0
    
    def f(elem):
        nonlocal depth, info, n
        
        if elem.tag == "class":
            info = ("class", "defined", "na", -1)
        elif elem.tag == "subroutineDec":
            info = ("subroutine", "defined", "na", -1)
        elif elem.tag == "parameterList":
            info = ("argument", "defined", "argument", 1)
            n = 1 # argument (without "this")
        elif elem.tag == "subroutineBody":
            info = ("var", "defined", "var", 1)
            n = 0 # var
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
    tree = ET.ElementTree(root)
    xml = ET.tostring(root)
    return xml

def debug_print_xml(xml):
    depth = 0
    def f(elem):
        nonlocal depth
        attrib = elem.attrib if elem.attrib else ""
        print("  " * depth, elem.tag, elem.text.strip(), attrib)
        
        depth += 1
        for child in elem:
            f(child)
        depth -= 1
    root = ET.fromstring(xml)
    f(root)

def f_vm(xml):
    debug_print_xml(xml)
    def is_terminal(s):
        return s in "keyword symbol integerConstant stringConstant identifier".split()
    class_id = None
    sub_id = None
    n_args = None
    def f(elem):
        nonlocal parents, w, class_id, sub_id, n_args
        t, s = elem.tag, elem.text.strip()
        if not is_terminal(t):
            n_args = 0
        else:
            p = parents[elem].tag if elem in parents else "None"
            print("{: <20} {: <20} {: <20}".format(p, t, s))
        
            if p == "class":
                if t == "identifier":
                    class_id = s
            if p == "subroutineDec":
                if t == "identifier":
                    sub_id = s
                if t == "symbol":
                    if s == ")":
                        w.writeFunction("{}.{}".format(class_id, sub_id), n_args)
            if p == "parameterList":
                if t == "identifier":
                    n_args += 1
            if p == "expression":
                if t == "symbol":
                    if s == "+":
                        w.writeArithmetic("ADD")
                    if s == "-":
                        w.writeArithmetic("SUB")
                    if s == "=":
                        w.writeArithmetic("EQ")
                    if s == ">":
                        w.writeArithmetic("GT")
                    if s == "<":
                        w.writeArithmetic("LT")
                    if s == "&":
                        w.writeArithmetic("AND")
                    if s == "|":
                        w.writeArithmetic("OR")
            if p == "term":
                if t == "symbol":
                    if s == "-":
                        w.writeArithmetic("NEG")
                    if s == "~":
                        w.writeArithmetic("NOT")
        
        for child in elem:
            f(child)
    root = ET.fromstring(xml)
    parents = dict((child, parent) for parent in root.iter() for child in parent)
    w = VMWriter()
    f(root)
    return w.close()

def main():
    JackAnalyzer()

if __name__ == "__main__":
    main()
