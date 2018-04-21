#ifndef COMPILATIONENGINE_H
#define COMPILATIONENGINE_H

#include <QDebug>
#include <QString>
#include <QStringList>
#include <QXmlStreamWriter>

class CompilationEngine {
 public:
  CompilationEngine(const QString& xml_tokens, QString* xml);
  void compileClass();
  void compileClassVarDec();
  void compileSubroutine();
  void compileParameterList();
  void compileVarDec();
  void compileStatements();
  void compileDo();
  void compileLet();
  void compileWhile();
  void compileReturn();
  void compileIf();
  void compileExpression();
  void compileTerm();
  void compileExpressionList();
 private:
  int m_i;
  QStringList m_tags;
  QStringList m_texts;
  QString& m_xml;
  QXmlStreamWriter m_writer;
  void compileSubroutineCall();
  void copy(int n = 1);
  QString* tag();
  QString* text();
  void write(QString* tag, QString* text);
};

#endif // COMPILATIONENGINE_H
