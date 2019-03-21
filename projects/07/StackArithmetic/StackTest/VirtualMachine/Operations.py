
class VM:
    file_name = None
    counter = 0
    Commands = {
        "and": '@SP\n'
               'A=M-1\n'
               'D=M\n'
               'A=A-1\n'
               'M=M&D\n'
               '@SP\n'
               'M=M-1\n',

        "sub": '@SP\n'
               'A=M-1\n'
               'D=M\n'
               'A=A-1\n'
               'M=M-D\n'
               '@SP\n'
               'M=M-1\n',

        "add": '@SP\n'
               'A=M-1\n'
               'D=M\n'
               'A=A-1\n'
               'M=M+D\n'
               '@SP\n'
               'M=M-1\n',

        "or": "//or\n"+
            '@SP\n'
              'A=M-1\n'
              'D=M\n'
              'A=A-1\n'
              'M=M|D\n'
              '@SP\n'
              'M=M-1\n',

        "neg": "@SP\n"
               "A=M-1\n"
               "M=-M\n",

        "not":"//not\n" 
                '@0\n'
                'D=A\n'
                '@SP\n'
                'A=M-1\n'
                'M=D-M\n'
                'M=M-1\n'
    }

    outFileName=None
    outFile =None


    def __init__(self, file_name):
        self.file_name = file_name;
        self.outFileName = self.file_name.replace("vm", 'asm')
        self.outFile = open(self.outFileName, 'w+')

    def push(self):
        self.outFile.write("//push\n"
                               "@SP\n" +
                               "A=M\n" +
                               "M=D\n" +
                               "@SP\n" +
                               "M=M+1\n")

    def pop(self):
        self.outFile.write("//pop\n"
                               "@SP\n" +
                               "AM=M-1\n" +
                               "D=M\n")

    def WriteArithmetic(self, command):
        self.counter += 1

        if command == "add":
            self.pop()
            self.outFile.write("//add\n" +
                                   "@SP\n" +
                                   "A=M-1\n" +
                                   "D=M+D\n" +
                                   "M=D\n")
        elif command == "sub":
            self.pop()
            self.outFile.write("//sub\n" +
                                   "@SP\n" +
                                   "A=M-1\n" +
                                   "D=M-D\n" +
                                   "M=D\n")
        elif command == "and":
            self.pop()
            self.outFile.write("//and\n" +
                                   "@SP\n" +
                                   "A=M-1\n" +
                                   "D=M&D\n" +
                                   "M=D\n")
        elif command == "or":
            self.pop()
            self.outFile.write("//or\n"
                                   "@SP\n" +
                                   "A=M-1\n" +
                                   "D=M|D\n" +
                                   "M=D\n")
        elif command == "neg":
            self.outFile.write("//neg\n"
                                   "@SP\n" +
                                   "A=M-1\n" +
                                   "M=-M\n")
        elif command == "not":
            self.outFile.write("//not\n"
                                   "@SP\n" +
                                   "A=M-1\n" +
                                   "M=-M\n" +
                                   "M=M-1\n")
        elif command == "eq":
            self.pop()
            self.outFile.write("//eq\n"
                                   "@SP\n" +
                                   "A=M-1\n" +
                                   "D=M-D\n" +
                                   "@TRUE{}\n".format(self.counter) +
                                   "D;JEQ\n" +
                                   "@SP\n" +
                                   "A=M-1\n" +
                                   "M=0\n" +  # false
                                   "@CONTINUE{}\n".format(self.counter) +
                                   "0;JMP\n" +
                                   "(TRUE{})\n".format(self.counter) +
                                   "@SP\n" +
                                   "A=M-1\n" +
                                   "M=-1\n" +
                                   "(CONTINUE{})\n".format(self.counter))
        elif command == "gt":
            self.pop()
            self.outFile.write("//gt\n"
                                   "@SP\n" +
                                   "A=M-1\n" +
                                   "D=M-D\n" +
                                   "@TRUE{}\n".format(self.counter) +
                                   "D;JGT\n" +
                                   "@SP\n" +
                                   "A=M-1\n" +
                                   "M=0\n" +  # false
                                   "@CONTINUE{}\n".format(self.counter) +
                                   "0;JMP\n" +
                                   "(TRUE{})\n".format(self.counter) +
                                   "@SP\n" +
                                   "A=M-1\n" +
                                   "M=-1\n" +
                                   "(CONTINUE{})\n".format(self.counter))
        elif command == "lt":
            self.pop()
            self.outFile.write("//lt\n"
                                   "@SP\n" +
                                   "A=M-1\n" +
                                   "D=M-D\n" +
                                   "@TRUE{}\n".format(self.counter) +
                                   "D;JLT\n" +
                                   "@SP\n" +
                                   "A=M-1\n" +
                                   "M=0\n" +  # false
                                   "@CONTINUE{}\n".format(self.counter) +
                                   "0;JMP\n" +
                                   "(TRUE{})\n".format(self.counter) +
                                   "@SP\n" +
                                   "A=M-1\n" +
                                   "M=-1\n" +
                                   "(CONTINUE{})\n".format(self.counter))


    def WritePushPop(self, type, segment, idx):
        seg = None
        if (segment != None):
            seg = {
                "this": "THIS",
                "temp": "TEMP",
                "arg": "ARG",
                "lcl": "LCL",
                "that": "THAT",
                "pointer": "POINTER",
                "static": "STATIC",
                "constant": "CONSTANT"
            }[segment]

        if (type == "push"):

            if seg == "CONSTANT":
                self.outFile.write(
                    "@{}\n".format(idx) +
                    "D=A\n"
                )

            elif seg == "LCL" or seg == "ARG" or seg == "THIS" or seg == "THAT":
                self.outFile.write("@{}\n".format(seg)+
                      "D=M\n"
                )
            elif seg == "STATIC":
                self.outFile.write(
                    "@{}.{}\n".format(self.file_name, idx) +
                    "D=A\n"
                )
                idx = 0

            elif seg == "POINTER":
                    self.outFile.write("@R3\n" + "D=A\n")

            elif seg == "TEMP":
                self.outFile.write("@R5\n"
                      "D=A\n"
                )

            if seg != "CONSTANT":
                self.outFile.write("@{}\n".format(idx)+
                                   "A=D+A\n"
                                   "D=M\n"
                                   )
            self.push()

        elif (type == "pop"):

            if seg == "LCL":
                self.outFile.write("@{}\n".format("LCL") +
                                       "D=M\n")
            elif seg == "ARG":
                self.outFile.write("@{}\n".format("ARG") +
                                       "D=M\n")
            elif seg == "THIS":
                self.outFile.write("@{}\n".format("THIS") +
                                       "D=M\n")
            elif seg == "THAT":
                self.outFile.write("@{}\n".format("THAT") +
                                       "D=M\n")
            elif seg == "POINTER":
                self.outFile.write("@{}\n".format("R3") +
                                       "D=A\n")
            elif seg == "TEMP":
                self.outFile.write("@{}\n".format("R5") +
                                       "D=A\n")
            elif seg == "STATIC":
                self.outFile.write("@{}\n".format(self.file_name + "." + idx) +
                                       "D=A\n")
                idx = 0
            self.outFile.write("@{}\n".format(idx) +
                                   "D=D+A\n" +
                                   "@R13\n" +
                                   "M=D\n")
            self.pop()
            self.outFile.write("@R13\n" +
                                   "A=M\n" +
                                   "M=D\n")
