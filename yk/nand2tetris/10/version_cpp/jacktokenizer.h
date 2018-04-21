#ifndef JACKTOKENIZER_H
#define JACKTOKENIZER_H

#include <QString>
#include <QStringList>

enum class TokenType { KEYWORD, SYMBOL, IDENTIFIER, INT_CONST, STRING_CONST };
enum class KeyWord {
  CLASS, METHOD, FUNCTION, CONSTRUCTOR, INT, BOOLEAN, CHAR, VOID, VAR,
  STATIC, FIELD, LET, DO, IF, ELSE, WHILE, RETURN, TRUE_, FALSE_, NULL_, THIS
};

void getStringFromTokenType(TokenType x, QString* s);
void getStringFromKeyWord(KeyWord x, QString* s);
KeyWord getKeyWordFromString(const QString& s);

class JackTokenizer {
 public:
  JackTokenizer(const QString& path);
  bool hasMoreTokens();
  void advance();
  TokenType tokenType();
  KeyWord keyWord();
  QChar symbol();
  QString identifier();
  int intVal();
  QString stringVal();
 private:
  static QStringList m_keywords;
  static QStringList m_symbols;
  int m_index;
  QStringList m_tokens;
};

#endif // JACKTOKENIZER_H
