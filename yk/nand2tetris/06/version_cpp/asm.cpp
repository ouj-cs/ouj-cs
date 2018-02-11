#include <algorithm>
#include <bitset>
#include <cassert>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
using namespace std;


enum CommandType {A_COMMAND, C_COMMAND, L_COMMAND};


class Parser {
private:
    ifstream stream;
    string line_current;
    string line_next;
    string s_dest;
    string s_comp;
    string s_jump;

    void split() {
        string s = line_current;
        s_dest = "null";
        s_jump = "null";
        size_t i = s.find("=");

        // 文字列に「=」が含まれるならば、左側を s_dest、右側を s とする。
        // （そうでなければ、s_dest は null、s は文字列全体である。）
        if (i != string::npos) {
            s_dest = s.substr(0, i);
            s = s.substr(i + 1);
        }

        i = s.find(";");

        // s に「;」が含まれるならば、左側を s、右側を s_jump とする。
        // （そうでなければ、s_jump は null、s はそのまま、である。）
        if (i != string::npos) {
            s_jump = s.substr(i + 1);
            s = s.substr(0, i);
        }

        s_comp = s;
    }
public:
    Parser(const char *path_input) {
        stream.open(path_input);
        assert(!stream.fail());  // ファイルが正常に開けなかった場合。
        advance();  // line_next に最初の行を得る。
    }

    ~Parser() {
        stream.close();
    }

    bool hasMoreCommands() {
        return line_next != "EOF";
    }

    void advance() {
        line_current = line_next;

        do {
            if (stream.peek() == EOF) {  // これ以上読み込むデータがない。
                line_next = "EOF";
            } else {
                getline(stream, line_next);  // 次の行を読み込む。
                // 改行文字がある場合は無害化しておく。
                replace(line_next.begin(), line_next.end(), '\r', ' ');
                size_t i = line_next.find("//");

                if (i == string::npos) {  // コメントを削除する。
                    ;
                } else {
                    line_next = line_next.substr(0, i);
                }

                i = line_next.find_first_not_of(' ');

                if (i == string::npos) {  // 左側の空白を削除する。
                    line_next = "";
                } else {
                    line_next = line_next.substr(i);
                }

                i = line_next.find_last_not_of(' ');

                if (i == string::npos) {  // 右側の空白を削除する。
                    line_next = "";
                } else {
                    line_next = line_next.substr(0, i + 1);
                }
            }
        } while (line_next == "");  // 空行は無視する。

        split();
    }

    CommandType commandType() {
        if (line_current[0] == '@') {  // 「@」で始まる。
            return A_COMMAND;
        } else if (line_current[0] == '(') {  // 「(」で始まる。
            return L_COMMAND;
        } else {
            return C_COMMAND;
        }
    }

    string symbol() {
        CommandType t = commandType();
        if (t == A_COMMAND) {  // 最初の文字「@」を除いて返す。
            return line_current.substr(1);
        } else if (t == L_COMMAND) {  // 左右の丸括弧を除いて返す。
            return line_current.substr(0, line_current.size() - 1).substr(1);
        } else {
            assert(false);
        }
    }

    string dest() { return s_dest; }
    string comp() { return s_comp; }
    string jump() { return s_jump; }
};


class Code {
private:
    // # ニーモニック -> バイナリコード、な連想配列を定義する。
    map<string, string> map_dest {
        {"null", "000"}, {"M", "001"}, {"D", "010"}, {"MD", "011"},
        {"A", "100"}, {"AM", "101"}, {"AD", "110"}, {"AMD", "111"}};
    map<string, string> map_comp {
        {"0", "0101010"}, {"1", "0111111"},
        {"-1", "0111010"}, {"D", "0001100"},
        {"A", "0110000"}, {"!D", "0001101"},
        {"!A", "0110001"}, {"-D", "0001111"},
        {"-A", "0110011"}, {"D+1", "0011111"},
        {"A+1", "0110111"}, {"D-1", "0001110"},
        {"A-1", "0110010"}, {"D+A", "0000010"},
        {"D-A", "0010011"}, {"A-D", "0000111"},
        {"D&A", "0000000"}, {"D|A", "0010101"},
        {"_", "1101010"}, {"_", "1111111"},
        {"_", "1111010"}, {"_", "1001100"},
        {"M", "1110000"}, {"_", "1001101"},
        {"!M", "1110001"}, {"_", "1001111"},
        {"-M", "1110011"}, {"_", "1011111"},
        {"M+1", "1110111"}, {"_", "1001110"},
        {"M-1", "1110010"}, {"D+M", "1000010"},
        {"D-M", "1010011"}, {"M-D", "1000111"},
        {"D&M", "1000000"}, {"D|M", "1010101"}};
    map<string, string> map_jump {
        {"null", "000"}, {"JGT", "00
        1"}, {"JEQ", "010"}, {"JGE", "011"},
        {"JLT", "100"}, {"JNE", "101"}, {"JLE", "110"}, {"JMP", "111"}};
public:
    string dest(string mnemonic) {
        return map_dest[mnemonic];
    }

    string comp(string mnemonic) {
        return map_comp[mnemonic];
    }

    string jump(string mnemonic) {
        return map_jump[mnemonic];
    }
};


class SymbolTable {
private:
    map<string, int> table;  // 連想配列を用意する。シンボル -> アドレス、として用いる。
public:
    SymbolTable() {
        // 定義済みシンボルを登録していく。
        addEntry("SP", 0);
        addEntry("LCL", 1);
        addEntry("ARG", 2);
        addEntry("THIS", 3);
        addEntry("THAT", 4);

        for (int i = 0; i < 16; ++i) {  // R0〜R15 を登録する。
            addEntry("R" + to_string(i), i);
        }

        addEntry("SCREEN", 16384);
        addEntry("KBD", 24576);
    }

    void addEntry(string symbol, int address) {
        table.emplace(symbol, address);
    }

    bool contains(string symbol) {
        return table.find(symbol) != table.end();
    }

    int getAddress(string symbol) {
        return table[symbol];
    }
};


int main(int argc, char **argv) {
    assert(argc == 2);
    char *path_input = argv[1];
    Code code;
    SymbolTable table;
    int address = 0;
    Parser *parser;
    parser = new Parser(path_input);

    // 最初のパスを行う。
    while (parser->hasMoreCommands()) {
        parser->advance();

        CommandType t = parser->commandType();

        if (t == L_COMMAND) {
            string symbol = parser->symbol();
            table.addEntry(symbol, address);
        } else if (t == A_COMMAND || t == C_COMMAND) {
            ++address;
        }
    }

    delete parser;
    parser = new Parser(path_input);
    address = 16;

    // 2 回目のパスを行う。
    while (parser->hasMoreCommands()) {
        parser->advance();
        CommandType t = parser->commandType();
        int integer;
        
        if (t == A_COMMAND) {
            string symbol = parser->symbol();
            if (isdigit(symbol[0])) {  // @Xxx が数字である。
                integer = stoi(symbol);  // 文字列->整数。
            } else {
                if (!table.contains(symbol)) {  // 未登録である。
                    table.addEntry(symbol, address);
                    ++address;
                }

                integer = table.getAddress(symbol);
            }

            // 二進数文字列を出力する
            cout << bitset<16>(integer) << endl;
        } else if (t == C_COMMAND) {
            // comp、dest、jump の各部分を二進数に変換して出力する。
            cout << "111";
            cout << code.comp(parser->comp());
            cout << code.dest(parser->dest());
            cout << code.jump(parser->jump());
            cout << endl;
        }
    }

    delete parser;
    return 0;
}
