import re                       # 正規表現

class JackTokenizer:
    def __init__(self, input_file):
        self.tokens = []
        self.index = -1
        self.num_tokens = 0
        # コメントを取り除く
        with open(input_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

            for line in lines:
                sub_str = line

                if sub_str.find('//') != -1:
                    index = sub_str.find('//')
                    sub_str = sub_str[:index]

                while sub_str.find('/*') != -1:
                    index_start = sub_str.find('/*')
                    index_end = sub_str.find('*/', index_start + 2) + 1
                    former = ''
                    latter = ''

                    if index_start > 0:
                        former = sub_str[:index_start]
                    if (index_end + 1) < len(sub_str):
                        latter = sub_str[index_end + 1:]
                    sub_str = former + ' ' + latter

                tokens = self._divide_string(sub_str)
                self.tokens.extend(tokens)

        self.num_tokens = len(self.tokens)

        return

    def _divide_string(self, string):
        len_str = len(string)
        pre_char = False        # 前がスペースかどうか
        string_mode = False
        index_start = 0
        ret = []

        for i in range(len_str):
            c = string[i:i+1]
            if string_mode:     # stringの場合
                if c == '"':
                    ret.append(string[index_start:i+1])
                    string_mode = False
            else:
                if c == ' ' or c == '\t':
                    if pre_char:
                        pre_char = False
                        ret.append(string[index_start:i])
                elif c == '{' or\
                     c == '}' or\
                     c == '(' or\
                     c == ')' or\
                     c == '[' or\
                     c == ']' or\
                     c == '.' or\
                     c == ',' or\
                     c == ';' or\
                     c == '+' or\
                     c == '-' or\
                     c == '*' or\
                     c == '/' or\
                     c == '|' or\
                     c == '<' or\
                     c == '>' or\
                     c == '=' or\
                     c == '~':
                    if pre_char:
                        ret.append(string[index_start:i]) # former
                    ret.append(string[i:i+1]) # symbol
                    pre_char = False
                elif c == '"':
                    index_start = i
                    string_mode = True
                elif c == '\n': # 改行の場合
                    if pre_char:
                        ret.append(string[index_start:i])
                else:           # 文字の場合
                    if pre_char != True:
                        pre_char = True
                        index_start = i

        if pre_char:
            ret.append(string[index_start:])

        return ret

    def hasMoreTokens(self):
        if (self.index + 1) < self.num_tokens:
            return True
        else:
            return False

    def advance(self):
        if (self.index + 1) < self.num_tokens:
            self.index = self.index + 1
        return

    def retreat(self):
        if self.index != -1:
            self.index = self.index - 1
        return

    def tokenType(self):
        if self.index < self.num_tokens:
            token = self.tokens[self.index]
        else:
            return "ERROR"
        if token == 'class' or\
            token == 'constructor' or\
            token == 'function' or\
            token == 'method' or\
            token == 'field' or\
            token == 'static' or\
            token == 'var' or\
            token == 'int' or\
            token == 'char' or\
            token == 'boolean' or\
            token == 'void' or\
            token == 'true' or\
            token == 'false' or\
            token == 'null' or\
            token == 'this' or\
            token == 'let' or\
            token == 'do' or\
            token == 'if' or\
            token == 'else' or\
            token == 'while' or\
            token == 'return':
            return "KEYWORD"
        elif token == '{' or\
             token == '}' or\
             token == '(' or\
             token == ')' or\
             token == '[' or\
             token == ']' or\
             token == '.' or\
             token == ',' or\
             token == ';' or\
             token == '+' or\
             token == '-' or\
             token == '*' or\
             token == '/' or\
             token == '&' or\
             token == '|' or\
             token == '<' or\
             token == '>' or\
             token == '=' or\
             token == '~':
            return "SYMBOL"
        elif token.isdigit():   # 数字
            return "INT_CONST"
        elif token[0:1] == '"' and \
            token[len(token)-1:len(token)] == '"':
            return "STRING_CONST"
        else:                   #
            return "IDENTIFIER"

    def keyWord(self):
        if self.index < self.num_tokens:
            token = self.tokens[self.index]
        else:
            return "ERROR"

        if token == 'class':
            return "CLASS"
        elif token == 'method':
            return "METHOD"
        elif token == 'function':
            return "FUNCTION"
        elif token == 'constructor':
            return "CONSTRUCTOR"
        elif token == 'int':
            return "INT"
        elif token == 'boolean':
            return "BOOLEAN"
        elif token == 'char':
            return "CHAR"
        elif token == 'void':
            return "VOID"
        elif token == 'var':
            return "VAR"
        elif token == 'static':
            return "STATIC"
        elif token == 'field':
            return "FIELD"
        elif token == 'let':
            return "LET"
        elif token == 'do':
            return "DO"
        elif token == 'if':
            return "IF"
        elif token == 'else':
            return "ELSE"
        elif token == 'while':
            return "WHILE"
        elif token == 'return':
            return "RETURN"
        elif token == 'true':
            return "TRUE"
        elif token == 'false':
            return "FALSE"
        elif token == 'null':
            return "NULL"
        elif token == 'this':
            return "THIS"
        else:
            return "ERROR"

    # 1文字だけ
    def symbol(self):
        return self.tokens[self.index]

    def identifier(self):
        return self.tokens[self.index]

    def intVal(self):
        return int(self.tokens[self.index])

    def stringVal(self):
        string = self.tokens[self.index]
        return string[1:-1]     # ""を除くため
