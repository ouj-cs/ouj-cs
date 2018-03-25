from JackTokenizer import JackTokenizer

class CompilationEngine:
    def __init__(self, input_file, output_file):
        self.jt = JackTokenizer(input_file)
        self.f = open(output_file, 'w')
        self.indent = ''

    def hasMoreNonTerminal(self):
        return self.jt.hasMoreTokens()

    def advance(self):
        self.jt.advance()

    def checkCompileType(self):
        keyword = self.jt.keyWord()
        if keyword == 'CLASS':
            return 'CLASS'
        elif keyword == 'STATIC' or\
             keyword == 'FILED':
            return 'CLASS_VAR_DEC'
        elif keyword == 'CONSTRUCTOR' or\
             keyword == 'FUNCTION' or\
             keyword == 'METHOD':
            return 'SUBROUTINE'
        elif keyword == 'VAR':
             return 'VAR_DEC'
        else:
            return 'ERROR'

    def compileClass(self):
        self.f.write('%s<class>\n' % self.indent)
        self.indent = self.indent + '  '
        # 'class'
        self._writeKeyword(self.jt.keyWord())
        self.jt.advance()

        # className
        self._compileClassName()

        # {
        if self.jt.hasMoreTokens() and self.jt.symbol() == '{':
            self._writeSymbol(self.jt.symbol())
            self.jt.advance()

        # ClassVarDec*
        while self.compileClassVarDec():
            pass

        # SubroutineDec*
        while self.checkCompileType() == 'SUBROUTINE':
            self.compileSubroutineDec()

        # }
        if self.jt.symbol() == '}':
            self._writeSymbol(self.jt.symbol())
            self.jt.advance()

        self.indent = self.indent[:-2]
        self.f.write('</class>\n')

        return

    def compileClassVarDec(self):
        # (static | field)
        if (self.jt.tokenType() == 'KEYWORD') and \
           (self.jt.keyWord() == 'STATIC' or self.jt.keyWord() == 'FIELD'):
            self.f.write('%s<classVarDec>\n' % self.indent)
            self.indent = self.indent + '  '

            self._writeKeyword(self.jt.keyWord())
            self.jt.advance()
            # type
            self._compileType()

            # varName
            self._compileVarName()

            #,が続く限り
            while (self.jt.tokenType() == 'SYMBOL') and (self.jt.symbol() == ','):
                # ,
                self._writeSymbol(self.jt.symbol())
                self.jt.advance()
                # varName
                self._compileVarName()

            #;
            if (self.jt.tokenType() == 'SYMBOL') and\
               (self.jt.symbol() == ';'):
                self._writeSymbol(self.jt.symbol())
                self.jt.advance()

            self.indent = self.indent[:-2]
            self.f.write('%s</classVarDec>\n' % self.indent)

            return True
        return False

    def _compileType(self):
        # type
        if self.jt.tokenType() == 'KEYWORD':
            if self.jt.keyWord() == 'INT' or\
               self.jt.keyWord() == 'CHAR' or\
               self.jt.keyWord() == 'BOOLEAN':
                self._writeKeyword(self.jt.keyWord())
                self.jt.advance()
        elif self.jt.tokenType() == 'IDENTIFIER':

            self._writeIdentifier(self.jt.identifier())
            self.jt.advance()

    def compileSubroutineDec(self):
        self.f.write('%s<subroutineDec>\n' % self.indent)
        self.indent = self.indent + '  '

        # TODO: 判定条件
        # constructor, function, method
        if self.jt.hasMoreTokens():
            self._writeKeyword(self.jt.keyWord())
            self.jt.advance()

        # (void | type)
        if (self.jt.tokenType() == 'KEYWORD') and \
           (self.jt.keyWord() == 'VOID'):
            self._writeKeyword(self.jt.keyWord())
            self.jt.advance()
        else:
            self._compileType()

        # subroutineName
        self._compileSubroutineName()

        # (
        if (self.jt.tokenType() == 'SYMBOL') and\
           (self.jt.symbol() == '('):
            self._writeSymbol(self.jt.symbol())
            self.jt.advance()

        # parameterList
        self._compileParameterList()

        # )
        if (self.jt.tokenType() == 'SYMBOL') and\
           (self.jt.symbol() == ')'):
            self._writeSymbol(self.jt.symbol())
            self.jt.advance()

        # subroutineBody
        self._compileSubroutineBody()

        self.indent = self.indent[:-2]
        self.f.write('%s</subroutineDec>\n' % self.indent)

        return

    def _compileParameterList(self):
        self.f.write('%s<parameterList>\n' % self.indent)
        self.indent = self.indent + '  '

        #
        while self.jt.hasMoreTokens() and self.jt.symbol() != ')':
            self._compileType()
            # varName
            self._compileVarName()

            # ,(= 続きがある場合)
            if (self.jt.tokenType() == 'SYMBOL') and\
               (self.jt.symbol() == ','):
                self._writeSymbol(self.jt.symbol())
                self.jt.advance()

        self.indent = self.indent[:-2]
        self.f.write('%s</parameterList>\n' % self.indent)
        return

    def _compileSubroutineBody(self):
        self.f.write('%s<subroutineBody>\n' % self.indent)
        self.indent = self.indent + '  '

        # {
        if self.jt.symbol() == '{':
            self._writeSymbol(self.jt.symbol())
            self.jt.advance()

        # VarDec*
        while (self.jt.tokenType() == 'KEYWORD') and (self.jt.keyWord() == 'VAR'):
            self.compileVarDec()

        # statements
        self._compileStatements()

        # }
        if self.jt.symbol() == '}':
            self._writeSymbol(self.jt.symbol())
            self.jt.advance()

        self.indent = self.indent[:-2]
        self.f.write('%s</subroutineBody>\n' % self.indent)

        return

    def compileVarDec(self):
        self.f.write('%s<varDec>\n' % self.indent)
        self.indent = self.indent + '  '

        # var
        if (self.jt.tokenType() == 'KEYWORD') and\
           (self.jt.keyWord() == 'VAR'):
            self._writeKeyword(self.jt.keyWord())
            self.jt.advance()

        # type
        self._compileType()

        # varName
        self._compileVarName()

        # (',' type varName)*
        while (self.jt.tokenType() == 'SYMBOL') and (self.jt.symbol() == ','):
            # ,
            self._writeSymbol(self.jt.symbol())
            self.jt.advance()

            # varName
            self._compileVarName()

        # ;
        if (self.jt.tokenType() == 'SYMBOL') and\
           (self.jt.symbol() == ';'):
            self._writeSymbol(self.jt.symbol())
            self.jt.advance()

        self.indent = self.indent[:-2]
        self.f.write('%s</varDec>\n' % self.indent)
        return

    def _compileClassName(self):
        if self.jt.tokenType() == 'IDENTIFIER':
            self._writeIdentifier(self.jt.identifier())
            self.jt.advance()
        return

    def _compileSubroutineName(self):
        if self.jt.tokenType() == 'IDENTIFIER':
            self._writeIdentifier(self.jt.identifier())
            self.jt.advance()
        return

    def _compileVarName(self):
        if self.jt.tokenType() == 'IDENTIFIER':
            self._writeIdentifier(self.jt.identifier())
            self.jt.advance()
        return

    # 文
    def _compileStatements(self):
        self.f.write('%s<statements>\n' % self.indent)
        self.indent = self.indent + '  '

        while self._compileStatement():
            pass                # 何も処理しない

        self.indent = self.indent[:-2]
        self.f.write('%s</statements>\n' % self.indent)
        return

    def _compileStatement(self):
        if self._compileLet():
            return True
        elif self._compileIf():
            return True
        elif self._compileWhile():
            return True
        elif self._compileDo():
            return True
        elif self._compileReturn():
            return True
        else:
            return False

    def _compileLet(self):
        if (self.jt.tokenType() == 'KEYWORD') and\
           (self.jt.keyWord() == 'LET'):
            self.f.write('%s<letStatement>\n' % self.indent)
            self.indent = self.indent + '  '

            # let
            self._writeKeyword(self.jt.keyWord())
            self.jt.advance()
            # varName
            self._compileVarName()

            if (self.jt.tokenType() == 'SYMBOL') and\
                  (self.jt.symbol() == '['):
                # [
                self._writeSymbol(self.jt.symbol())
                self.jt.advance()
                # expression
                self._compileExpression()

                # ]
                if (self.jt.tokenType() == 'SYMBOL') and\
                   (self.jt.symbol() == ']'):
                    self._writeSymbol(self.jt.symbol())
                    self.jt.advance()

            # =
            if (self.jt.tokenType() == 'SYMBOL') and\
               (self.jt.symbol() == '='):
                self._writeSymbol(self.jt.symbol())
                self.jt.advance()

            # expression
            self._compileExpression()

            # ;
            if (self.jt.tokenType() == 'SYMBOL') and\
               (self.jt.symbol() == ';'):
                self._writeSymbol(self.jt.symbol())
                self.jt.advance()

                self.indent = self.indent[:-2]
                self.f.write('%s</letStatement>\n' % self.indent)
            return True
        else:
            return False

    def _compileIf(self):
        if (self.jt.tokenType() == 'KEYWORD') and\
           (self.jt.keyWord() == 'IF'):
            self.f.write('%s<ifStatement>\n' % self.indent)
            self.indent = self.indent + '  '

            # if
            self._writeKeyword(self.jt.keyWord())
            self.jt.advance()
            # (
            if (self.jt.tokenType() == 'SYMBOL') and\
                  (self.jt.symbol() == '('):
                self._writeSymbol(self.jt.symbol())
                self.jt.advance()

            # expression
            self._compileExpression()

            # )
            if (self.jt.tokenType() == 'SYMBOL') and\
               (self.jt.symbol() == ')'):
                self._writeSymbol(self.jt.symbol())
                self.jt.advance()

            # {
            if (self.jt.tokenType() == 'SYMBOL') and\
                  (self.jt.symbol() == '{'):
                self._writeSymbol(self.jt.symbol())
                self.jt.advance()

            # statements
            self._compileStatements()

            # }
            if (self.jt.tokenType() == 'SYMBOL') and\
                  (self.jt.symbol() == '}'):
                self._writeSymbol(self.jt.symbol())
                self.jt.advance()

            # else
            if (self.jt.tokenType() == 'KEYWORD') and\
                  (self.jt.keyWord() == 'ELSE'):
                self._writeKeyword(self.jt.keyWord())
                self.jt.advance()

                # {
                if (self.jt.tokenType() == 'SYMBOL') and\
                   (self.jt.symbol() == '{'):
                    self._writeSymbol(self.jt.symbol())
                    self.jt.advance()

                    # statements
                    self._compileStatements()

                    # }
                    if (self.jt.tokenType() == 'SYMBOL') and\
                       (self.jt.symbol() == '}'):
                        self._writeSymbol(self.jt.symbol())
                        self.jt.advance()

            self.indent = self.indent[:-2]
            self.f.write('%s</ifStatement>\n' % self.indent)

            return True
        else:
            return False

    def _compileWhile(self):
        if (self.jt.tokenType() == 'KEYWORD') and\
           (self.jt.keyWord() == 'WHILE'):

            self.f.write('%s<whileStatement>\n' % self.indent)
            self.indent = self.indent + '  '

            # while
            self._writeKeyword(self.jt.keyWord())
            self.jt.advance()

            # (
            if (self.jt.tokenType() == 'SYMBOL') and\
                  (self.jt.symbol() == '('):
                self._writeSymbol(self.jt.symbol())
                self.jt.advance()

            # expression
            self._compileExpression()

            # )
            if (self.jt.tokenType() == 'SYMBOL') and\
               (self.jt.symbol() == ')'):
                self._writeSymbol(self.jt.symbol())
                self.jt.advance()

            # {
            if (self.jt.tokenType() == 'SYMBOL') and\
                  (self.jt.symbol() == '{'):
                self._writeSymbol(self.jt.symbol())
                self.jt.advance()

            # statements
            self._compileStatements()

            # }
            if (self.jt.tokenType() == 'SYMBOL') and\
                  (self.jt.symbol() == '}'):
                self._writeSymbol(self.jt.symbol())
                self.jt.advance()

            self.indent = self.indent[:-2]
            self.f.write('%s</whileStatement>\n' % self.indent)

            return True
        else:
            return False

    def _compileDo(self):
        if (self.jt.tokenType() == 'KEYWORD') and\
           (self.jt.keyWord() == 'DO'):

            self.f.write('%s<doStatement>\n' % self.indent)
            self.indent = self.indent + '  '

            # do
            self._writeKeyword(self.jt.keyWord())
            self.jt.advance()

            # subroutineCall
            self._compileSubroutineCall()

            # ;
            if (self.jt.tokenType() == 'SYMBOL') and\
                  (self.jt.symbol() == ';'):
                self._writeSymbol(self.jt.symbol())
                self.jt.advance()

            self.indent = self.indent[:-2]
            self.f.write('%s</doStatement>\n' % self.indent)

            return True
        else:
            return False

    def _compileReturn(self):
        if (self.jt.tokenType() == 'KEYWORD') and\
           (self.jt.keyWord() == 'RETURN'):

            self.f.write('%s<returnStatement>\n' % self.indent)
            self.indent = self.indent + '  '

            # return
            self._writeKeyword(self.jt.keyWord())
            self.jt.advance()

            # expression
            if (self.jt.tokenType() != 'SYMBOL'):
                self._compileExpression()

            # ;
            if (self.jt.tokenType() == 'SYMBOL') and\
                  (self.jt.symbol() == ';'):
                self._writeSymbol(self.jt.symbol())
                self.jt.advance()

            self.indent = self.indent[:-2]
            self.f.write('%s</returnStatement>\n' % self.indent)

            return True
        else:
            return False

    def _compileExpression(self):
        if self.jt.tokenType() == 'SYMBOL' and\
           self.jt.symbol() == ')':
            return False

        self.f.write('%s<expression>\n' % self.indent)
        self.indent = self.indent + '  '

        # term
        if self._compileTerm() == False:
            return False

        # (op term)*
        while self._compileOp():
            self._compileTerm()

        self.indent = self.indent[:-2]
        self.f.write('%s</expression>\n' % self.indent)

        return True

    def _compileTerm(self):
        self.f.write('%s<term>\n' % self.indent)
        self.indent = self.indent + '  '

        if self.jt.hasMoreTokens():
            token_type = self.jt.tokenType()

            if token_type == 'INT_CONST': # integerConstant
                self._writeIntegerConstant(self.jt.intVal())
                self.jt.advance()
            elif token_type == 'STRING_CONST': # stringConstant
                self._writeStringConstant(self.jt.stringVal())
                self.jt.advance()
            elif token_type == 'KEYWORD': # keywordConstant
                self._writeKeyword(self.jt.keyWord())
                self.jt.advance()
            elif token_type == 'SYMBOL':
                if self.jt.symbol() == '(':
                    # (
                    self._writeSymbol(self.jt.symbol())
                    self.jt.advance()
                    # expression
                    self._compileExpression()
                    # )
                    self._writeSymbol(self.jt.symbol())
                    self.jt.advance()
                elif self.jt.symbol() == '-' or\
                     self.jt.symbol() == '~':
                    # unaryOp
                    self._compileUnaryOp()
                    # term
                    self._compileTerm()
            else:
                # 先読みが必要
                pre_identifier = self.jt.identifier()
                self.jt.advance()

                if self.jt.hasMoreTokens():
                    if self.jt.tokenType() == 'SYMBOL':
                        if self.jt.symbol() == '[': # 配列
                            # varName
                            self._writeIdentifier(pre_identifier)
                            # [
                            self._writeSymbol(self.jt.symbol())
                            self.jt.advance()
                            # expression
                            self._compileExpression()
                            # ]
                            self._writeSymbol(self.jt.symbol())
                            self.jt.advance()
                        elif self.jt.symbol() == '.' or\
                             self.jt.symbol() == '(': # 関数
                            self.jt.retreat()         # 後退
                            self._compileSubroutineCall()
                        else:

                            self._writeIdentifier(pre_identifier)
                else:
                    self._writeIdentifier(pre_identifier)

        self.indent = self.indent[:-2]
        self.f.write('%s</term>\n' % self.indent)

        return True

    def _compileSubroutineCall(self):
        if self.jt.tokenType() == 'IDENTIFIER':
            self._writeIdentifier(self.jt.identifier())
            self.jt.advance()

            # .
            if (self.jt.tokenType() == 'SYMBOL') and\
               (self.jt.symbol() == '.'):
                    self._writeSymbol(self.jt.symbol())
                    self.jt.advance()
                    # SubroutineName
                    self._compileSubroutineName()

            # (
            if self.jt.tokenType() == 'SYMBOL' and\
               self.jt.symbol() == '(':
                self._writeSymbol(self.jt.symbol())
                self.jt.advance()

            # expressionList
            self._compileExpressionList()

            # )
            if self.jt.tokenType() == 'SYMBOL' and\
               self.jt.symbol() == ')':
                self._writeSymbol(self.jt.symbol())
                self.jt.advance()
            return True
        else:
            return False

    def _compileExpressionList(self):
        self.f.write('%s<expressionList>\n' % self.indent)
        self.indent = self.indent + '  '

        while self._compileExpression():
            # ,
            if (self.jt.tokenType() == 'SYMBOL') and\
                  (self.jt.symbol() == ','):
                self._writeSymbol(self.jt.symbol())
                self.jt.advance()
            else:
                break

        self.indent = self.indent[:-2]
        self.f.write('%s</expressionList>\n' % self.indent)

        return

    def _compileOp(self):
        if (self.jt.tokenType() == 'SYMBOL'):
            if (self.jt.symbol() == '+') or\
               (self.jt.symbol() == '-') or\
               (self.jt.symbol() == '*') or\
               (self.jt.symbol() == '/') or\
               (self.jt.symbol() == '&') or\
               (self.jt.symbol() == '|') or\
               (self.jt.symbol() == '<') or\
               (self.jt.symbol() == '>') or\
               (self.jt.symbol() == '='):
                self._writeSymbol(self.jt.symbol())
                self.jt.advance()
                return True

        return False

    def _compileUnaryOp(self):
        if (self.jt.tokenType() == 'SYMBOL'):
            if (self.jt.symbol() == '-') or\
               (self.jt.symbol() == '~'):
                self._writeSymbol(self.jt.symbol())
                self.jt.advance()
                return True
        return False

    def _compileKeywordConstant(self):
        if (self.jt.tokenType() == 'KEYWORD'):
            if (self.jt.keyWord() == 'TRUE') or\
               (self.jt.keyWord() == 'FALSE') or\
               (self.jt.keyWord() == 'NULL') or\
               (self.jt.keyWord() == 'THIS'):
                self._writeSymbol(self.jt.keyWord())
                self.jt.advance()
                return True
        return False

        return



    def _writeKeyword(self, str):
        self.f.write('%s<keyword> %s </keyword>\n' % (self.indent, str.lower()))
        return

    def _writeSymbol(self, str):
        if str == '<':
            str = '&lt;'
        elif str == '>':
            str = '&gt;'
        elif str == '&':
            str = '&amp;'

        self.f.write('%s<symbol> %s </symbol>\n' % (self.indent, str))
        return

    def _writeIntegerConstant(self, i):
        self.f.write('%s<integerConstant> %d </integerConstant>\n' % (self.indent, i))
        return

    def _writeStringConstant(self, str):
        self.f.write('%s<stringConstant> %s </stringConstant>\n' % (self.indent, str))
        return

    def _writeIdentifier(self, str):
        self.f.write('%s<identifier> %s </identifier>\n' % (self.indent, str))
        return
