#include "jacktokenizer.h"
#include <stdexcept>
#include <QDebug>
#include <QDir>

QStringList JackTokenizer::m_keywords = QString(
    "class constructor function method field static var int char boolean "
    "void true false null this let do if else while return").split(" ");
QStringList JackTokenizer::m_symbols = QString(
      "{ } ( ) [ ] . , ; + - * / & | < > = ~").split(" ");

void getStringFromTokenType(TokenType x, QString* s) {
  switch (x) {
    case TokenType::KEYWORD:      { *s = "keyword"; break; }
    case TokenType::SYMBOL:       { *s = "symbol"; break; }
    case TokenType::IDENTIFIER:   { *s = "identifier"; break; }
    case TokenType::INT_CONST:    { *s = "integerConstant"; break; }
    case TokenType::STRING_CONST: { *s = "stringConstant"; break; }
    default:                    { Q_ASSERT(false); }
  }
}

void getStringFromKeyWord(KeyWord x, QString* s) {
  switch (x) {
    case KeyWord::CLASS:       { *s = "class"; break; }
    case KeyWord::CONSTRUCTOR: { *s = "constructor"; break; }
    case KeyWord::FUNCTION:    { *s = "function"; break; }
    case KeyWord::METHOD:      { *s = "method"; break; }
    case KeyWord::FIELD:       { *s = "field"; break; }
    case KeyWord::STATIC:      { *s = "static"; break; }
    case KeyWord::VAR:         { *s = "var"; break; }
    case KeyWord::INT:         { *s = "int"; break; }
    case KeyWord::CHAR:        { *s = "char"; break; }
    case KeyWord::BOOLEAN:     { *s = "boolean"; break; }
    case KeyWord::VOID:        { *s = "void"; break; }
    case KeyWord::TRUE_:       { *s = "true"; break; }
    case KeyWord::FALSE_:      { *s = "false"; break; }
    case KeyWord::NULL_:       { *s = "null"; break; }
    case KeyWord::THIS:        { *s = "this"; break; }
    case KeyWord::LET:         { *s = "let"; break; }
    case KeyWord::DO:          { *s = "do"; break; }
    case KeyWord::IF:          { *s = "if"; break; }
    case KeyWord::ELSE:        { *s = "else"; break; }
    case KeyWord::WHILE:       { *s = "while"; break; }
    case KeyWord::RETURN:      { *s = "return"; break; }
    default:                   { Q_ASSERT(false); }
  }
}

KeyWord getKeyWordFromString(const QString& s) {
  if (s == "class") return KeyWord::CLASS;
  if (s == "constructor") return KeyWord::CONSTRUCTOR;
  if (s == "function") return KeyWord::FUNCTION;
  if (s == "method") return KeyWord::METHOD;
  if (s == "field") return KeyWord::FIELD;
  if (s == "static") return KeyWord::STATIC;
  if (s == "var") return KeyWord::VAR;
  if (s == "int") return KeyWord::INT;
  if (s == "char") return KeyWord::CHAR;
  if (s == "boolean") return KeyWord::BOOLEAN;
  if (s == "void") return KeyWord::VOID;
  if (s == "true") return KeyWord::TRUE_;
  if (s == "false") return KeyWord::FALSE_;
  if (s == "null") return KeyWord::NULL_;
  if (s == "this") return KeyWord::THIS;
  if (s == "let") return KeyWord::LET;
  if (s == "do") return KeyWord::DO;
  if (s == "if") return KeyWord::IF;
  if (s == "else") return KeyWord::ELSE;
  if (s == "while") return KeyWord::WHILE;
  if (s == "return") return KeyWord::RETURN;
  Q_ASSERT(false);
  return KeyWord::CLASS;
}

JackTokenizer::JackTokenizer(const QString& path) {
  QFile file(path);
  QString s;
  if (file.open(QIODevice::ReadOnly)) {
    QTextStream stream(&file);
    s = stream.readAll();
    file.close();
  } else {
    Q_ASSERT(false);
  }
  s = s.remove(QRegExp("//[^\n]*"));
  QRegExp exp("/\\*.*\\*/");
  exp.setMinimal(true);
  s = s.remove(exp);

  QString s2;
  bool inside = false;
  for (auto c : s) {
    if (c == '"') inside = !inside;
    if (inside && c == ' ') s2 += "SPACEINSTRING";
    else
      s2 += c;
  }
  s = s2;

  s = s.replace(QRegExp("([\\{\\}\\(\\)\\[\\]\\.,;\\+\\-\\*/&|<>=~])"), " \\1 ");
  s = s.replace(QRegExp("[\t\r\n]"), " ");
  s = s.replace(QRegExp(" +"), " ");
  s = s.trimmed();
  m_tokens = s.split(" ");
  m_index = -1;
}

bool JackTokenizer::hasMoreTokens() {
  return m_index < m_tokens.size() - 1;
}

void JackTokenizer::advance() {
  ++m_index;
}

TokenType JackTokenizer::tokenType() {
  QString s = m_tokens[m_index];
  if (m_keywords.contains(s)) return TokenType::KEYWORD;
  if (m_symbols.contains(s)) return TokenType::SYMBOL;
  bool is_digit;
  s.toInt(&is_digit);
  if (is_digit) return TokenType::INT_CONST;
  if (s.startsWith('"')) return TokenType::STRING_CONST;
  return TokenType::IDENTIFIER;
}

KeyWord JackTokenizer::keyWord() {
  return getKeyWordFromString(m_tokens[m_index].toLower());
}

QChar JackTokenizer::symbol() {
  return m_tokens[m_index][0];
}

QString JackTokenizer::identifier() {
  return m_tokens[m_index];
}

int JackTokenizer::intVal() {
  return m_tokens[m_index].toInt();
}

QString JackTokenizer::stringVal() {
  QString s = m_tokens[m_index];
  return s.mid(1, s.size() - 2);
}
