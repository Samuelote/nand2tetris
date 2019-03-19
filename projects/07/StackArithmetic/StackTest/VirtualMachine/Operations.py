
class VM:

    count = 0
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

        "or": '@SP\n'
              'A=M-1\n'
              'D=M\n'
              'A=A-1\n'
              'M=M|D\n'
              '@SP\n'
              'M=M-1\n',

        "neg": "@SP\n"
               "A=M-1\n"
               "M=-M\n",

        "not": "@SP\n"
               "A=M-1\n"
               "D=0\n"
               "A=M-1\n"
               "M=D-M\n"
               'M=M-1\n',
    }


    def push(self):
        return ("@SP\n" +
              "A=M\n" +
              "M=D\n" +
              "@SP\n" +
              "M=M+1\n")


    def pop(self):
        return ("@SP\n" +
              "A=M-1\n" +
              "D=M\n")


    def WriteArithmetic(self, cmd):
        self.count+=1
        command = None
        if (cmd == "gt"):
            command = ("@SP\n"+
                "A=M-1\n"+
                "D=M\n"+
                "A=A-1\n"+
                "D=M-D\n"+
                "@TRUE{}\n".format(self.count) +
                "D;JGT\n"
                "M=0\n"
                "@R13\n"
                "(TRUE{})\n".format(self.count) +
                "M= -1\n")

        elif cmd == "eq":
            command = ("@SP\n"
                "A=M-1\n"
                "D=M\n"
                "A=A-1\n"
                "D=M-D\n"
                "@TRUE{}\n".format(self.count) +
                "D;JEQ\n"
                "M=0\n"
                "@R13\n"
                "(TRUE{})\n".format(self.count) +
                "M= -1\n")

        elif (cmd == "lt"):
                command = ("@SP\n"
                "A=M-1\n"
                "D=M\n"
                "A=A-1\n"
                "D=M-D\n"
                "@TRUE{}\n".format(self.count) +
                "D;JLT\n"
                "M=0\n"
                "@R13\n"
                "(TRUE{})\n".format(self.count) +
                "M= -1\n")
        else:
            command = self.Commands[cmd]

        print(command)


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
                print(
                    "@{}\n".format(idx) +
                    "D=A\n"
                    +self.push()
                )
            else:
                print(
                    "@{}\n".format(idx)+
                    "D=A\n"
                    "@{}\n".format(seg)+
                    "A=A+D \n"  #ADDS IDX AND SEGMENT TO GET PROPER CELLL
                    "D=M\n"
                    + self.push()
                )

        elif (type == "pop"):
            print(
                "@{} \n".format(idx)+
                "D=A \n"
                "@{} \n".format(seg)+
                "A=A+D \n"  #ADDS IDX AND SEGMENT TO GET PROPER CELLL
                "D=M\n" 
                
                "@R13\n"
                "M=D\n" #ASSIGNS R13 TO SEGMENT INDEX

                +self.pop()+ #PUSHES TOP OF STACK TO D

                "@R13\n" 
                "A=D\n") #ASSIGNS SEGMENT INDEX TO TOP OF STACK
        else:
            self.WriteArithmetic(type)

