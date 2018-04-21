#include <compilationengine.h>
#include <jacktokenizer.h>
#include <iostream>
#include <QDebug>
#include <QDir>
#include <QXmlStreamWriter>
using namespace std;

void getXmlTokens(const QString& path, QString* xml) {
  JackTokenizer t(path);
  QXmlStreamWriter writer(xml);
  writer.writeStartElement("tokens");
  writer.setAutoFormatting(true);
  writer.setAutoFormattingIndent(0);
  while (t.hasMoreTokens()) {
    t.advance();
    TokenType type = t.tokenType();
    QString tag;
    getStringFromTokenType(type, &tag);
    QString text;
    if (type == TokenType::KEYWORD)
      getStringFromKeyWord(t.keyWord(), &text);
    else if (type == TokenType::SYMBOL)
      text = t.symbol();
    else if (type == TokenType::IDENTIFIER)
      text = t.identifier();
    else if (type == TokenType::INT_CONST)
      text = QString::number(t.intVal());
    else if (type == TokenType::STRING_CONST)
      text = t.stringVal().replace(QRegExp("SPACEINSTRING"), " ");
    else
      Q_ASSERT(false);
    writer.writeTextElement(tag, " " + text + " ");
  }
  writer.writeEndElement();
}

void getXml(const QString& xml_tokens, QString* xml) {
  CompilationEngine engine(xml_tokens, xml);
}

int main(int argc, char** argv) {
  if (argc != 2) Q_ASSERT(argc == 2);
  QFileInfo info(argv[1]);
  Q_ASSERT(info.exists());
  QStringList paths;
  QDir dir;
  if (info.isDir()) {
    dir = QDir(info.absoluteFilePath());
    QFileInfoList infos = dir.entryInfoList();
    for (auto info : infos) {
      QString path = info.absoluteFilePath();
      if (path.endsWith(".jack")) paths << path;
    }
  } else {
    dir = QDir(info.absolutePath());
    paths << info.absoluteFilePath();
  }
  for (auto path : paths) {
    QFileInfo info(path);
    QString xml_tokens;
    getXmlTokens(path, &xml_tokens);
    auto f = [](QFileInfo info, QString tail, QString s) {
      QString out_name = info.baseName() + tail;
      QString out_path = info.absolutePath() + QDir::separator() + out_name;
      QFile out_file(out_path);
      if (out_file.open(QIODevice::WriteOnly)) {
        QTextStream stream(&out_file);
        stream << s;
        out_file.close();
      } else {
        Q_ASSERT(false);
      }
    };
    f(info, "T.output.xml", xml_tokens);
    QString xml;
    getXml(xml_tokens, &xml);
    f(info, ".output.xml", xml);
  }
}
