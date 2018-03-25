import os

from CompilationEngine import CompilationEngine

class JackAnalyzer:
    def __init__(self, input_files):
        self.input_files = input_files
        return

    def analyze(self):
        if os.path.isdir(self.input_files):
            input_files = os.listdir(self.input_files)
            for input_file in input_files:
                if os.path.isdir(input_file):
                    continue
                else:
                    input_path = self.input_files + os.sep + input_file
                    root, ext = os.path.splitext(input_path)

                    if ext == '.jack':
                        print(input_path)
                        self._analyze_file(input_path)

        else:
            self._analyze_file(self.input_files)


    def _analyze_file(self, input_file):
        output_file = ('.').join(input_file.split('.')[:-1]) + '.xml'
        ce = CompilationEngine(input_file, output_file)
        while ce.hasMoreNonTerminal():
            ce.advance()
            type = ce.checkCompileType()
            if type == 'CLASS':
                ce.compileClass()
