#include "compilationengine.h"
#include <QDebug>
#include <QXmlStreamReader>

CompilationEngine::CompilationEngine(const QString& xml_tokens, QString* xml) :
    m_xml(*xml), m_writer(xml) {
  QXmlStreamReader reader(xml_tokens);
  if (reader.readNextStartElement()) {
    Q_ASSERT(reader.name() == "tokens");
    while (reader.readNextStartElement()) {
      QString text = reader.readElementText().trimmed();
      m_tags << reader.name().toString();
      m_texts << text;
    }
  }
  m_i = 0;
  Q_ASSERT(m_tags[m_i] == "keyword" && m_texts[m_i] == "class");
  compileClass();
  xml->replace(QRegExp("\n *<dummy> dummy </dummy>\n"), "\n");
}

void CompilationEngine::compileClass() {
  m_writer.writeStartElement("class");
  m_writer.setAutoFormatting(true);
  m_writer.setAutoFormattingIndent(2);
  copy(3);  // "class" className "{"
  while (*text() != "}") {
    if (*text() == "static" || *text() == "field") {
      compileClassVarDec();
    } else if (*text() == "constructor" || *text() == "function" ||
             *text() == "method") {
      compileSubroutine();
    } else {
      Q_ASSERT(false);
    }
  }
  copy();  // "}"
  m_writer.writeEndElement();
}

void CompilationEngine::compileClassVarDec() {
  m_writer.writeStartElement("classVarDec");
  copy(3);  // ("static" | "field") type varName
  while (*text() == ",") copy(2);  // "," varName
  copy();  // ";"
  m_writer.writeEndElement();
}

void CompilationEngine::compileSubroutine() {
  m_writer.writeStartElement("subroutineDec");
  // ("constructor" | "function" | "method") ("void" | type) subroutineName "("
  copy(4);
  compileParameterList();
  copy();  // ")"
  m_writer.writeStartElement("subroutineBody");
  copy();  // "{"
  while (*text() == "var") compileVarDec();
  compileStatements();
  copy();  // "}"
  m_writer.writeEndElement();
  m_writer.writeEndElement();
}

void CompilationEngine::compileParameterList() {
  m_writer.writeStartElement("parameterList");
  QString d("dummy");
  write(&d, &d);
  while (*text() != ")") {
    copy(2);  // type varName
    if (*text() == ",") copy();  // ","
  }
  m_writer.writeEndElement();
}

void CompilationEngine::compileVarDec() {
  m_writer.writeStartElement("varDec");
  copy();  // "var" type varName
  while (*text() != ";") copy(2);  // "," varName
  copy();  // ";"
  m_writer.writeEndElement();
}

void CompilationEngine::compileStatements() {
  m_writer.writeStartElement("statements");
  while (true) {
    if (*text() == "let")
      compileLet();
    else if (*text() == "if")
      compileIf();
    else if (*text() == "while")
      compileWhile();
    else if (*text() == "do")
      compileDo();
    else if (*text() == "return")
      compileReturn();
    else
      break;
  }
  m_writer.writeEndElement();
}

void CompilationEngine::compileDo() {
  m_writer.writeStartElement("doStatement");
  copy();  // "do"
  compileSubroutineCall();
  copy();  // ";"
  m_writer.writeEndElement();
}

void CompilationEngine::compileLet() {
  m_writer.writeStartElement("letStatement");
  copy(2);  // "let" varname
  if (*text() == "[") {
    copy();  // "["
    compileExpression();
    copy();  // "]"
  }
  copy();  // "="
  compileExpression();
  copy();  // ";"
  m_writer.writeEndElement();
}

void CompilationEngine::compileWhile() {
  m_writer.writeStartElement("whileStatement");
  copy(2);  // "while" "("
  compileExpression();
  copy(2);  // ")" "{"
  compileStatements();
  copy();  // "}"
  m_writer.writeEndElement();
}

void CompilationEngine::compileReturn() {
  m_writer.writeStartElement("returnStatement");
  copy();  // "return"
  if (*text() != ";") compileExpression();
  copy();  // ";"
  m_writer.writeEndElement();
}

void CompilationEngine::compileIf() {
  m_writer.writeStartElement("ifStatement");
  copy(2);  // "if" "("
  compileExpression();
  copy(2);  // ")" "{"
  compileStatements();
  copy();  // "}"
  if (*text() == "else") {
    copy(2);  // "else" "{"
    compileStatements();
    copy();  // "}"
  }
  m_writer.writeEndElement();
}

void CompilationEngine::compileExpression() {
  static QStringList ss = QString("+ - * / & | < > =").split(" ");
  m_writer.writeStartElement("expression");
  compileTerm();
  if (ss.contains(*text())) {
    copy();  // op
    compileTerm();
  }
  m_writer.writeEndElement();
}

void CompilationEngine::compileTerm() {
  m_writer.writeStartElement("term");
  if (*tag() == "integerConstant" || *tag() == "stringConstant" ||
      *tag() == "keyword") {
    copy();
  } else if (*text() == "-" || *text() == "~") {
    copy();  // ("-" | "~")
    compileTerm();
  } else if (*text() == "(") {
    copy();  // "("
    compileExpression();
    copy();  // ")"
  } else {
    QString* next = &m_texts[m_i + 1];
    if (*next == "(" || *next == ".") {
      compileSubroutineCall();
    } else if (*next == "[") {
      copy(2);  // varName "["
      compileExpression();
      copy();  // "]"
    } else {
      copy();  // varName
    }
  }
  m_writer.writeEndElement();
}

void CompilationEngine::compileExpressionList() {
  m_writer.writeStartElement("expressionList");
  QString d("dummy");
  write(&d, &d);
  if (*text() != ")") {
    compileExpression();
    while (*text() == ",") {
      copy();  // ","
      compileExpression();
    }
  }
  m_writer.writeEndElement();

}

void CompilationEngine::compileSubroutineCall() {
  QString* next = &m_texts[m_i + 1];
  if (*next == "(") {
    copy(2);  // subroutineName "("
    compileExpressionList();
    copy();  // ")"
  } else {
    copy(4);  // (className | varName) "." subroutineName "("
    compileExpressionList();
    copy();  // ")"
  }
}

void CompilationEngine::copy(int n) {
  for (int i = 0; i < n; ++i) {
    write(tag(), text());
    ++m_i;
  }
}

QString* CompilationEngine::tag() {
  return &m_tags[m_i];
}

QString* CompilationEngine::text() {
  return &m_texts[m_i];
}

void CompilationEngine::write(QString* tag, QString* text) {
  m_writer.writeTextElement(*tag, " " + *text + " ");
}
