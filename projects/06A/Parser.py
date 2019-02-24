from Code import Code


class Parser:

    def __init__(self, cmd):
        self.cmd = cmd
        self.cmd = self.remove_white_space()
        self.cmd = self.remove_comments()
        print(self.cmd)

    def remove_white_space(self):
        return self.cmd.replace(" ", "")

    def remove_comments(self):
        if "//" in self.cmd:
            return self.cmd[0:self.cmd.index("//")]
        else: return self.cmd



    def commandType(self):
        split_cmd = list(self.cmd)
        if (split_cmd[0] == "@"):
            # self.symbol("A", split_cmd)
            return "A_COMMAND"

        elif (split_cmd[0] == "(" and split_cmd[len(split_cmd)-1] == ")"):
            # self.symbol("L", split_cmd)
            return "L_COMMAND"

        elif ";" in split_cmd or "=" in split_cmd:
            return "C_COMMAND"


    def symbol(self, type, cmd):
        if (type == "A"):
            return "".join(cmd[1:])
        elif(type == "L"):
            cmd.pop()
            return "".join(cmd[1:])

    def dest(self):
        if "=" in self.cmd:
            dest = self.cmd.split("=")[0]
            code = Code()
            code.dest(dest)
            return dest;
        else:
            return ""

    def comp(self):
        split = list(self.cmd)
        if "=" in split:
            index = split.index("=")
            comp = "".join(split[index+1:])
            code = Code()
            code.comp(comp)
            return comp
        else:
            return ''

    def jmp(self):
        split = list(self.cmd)
        if ";" in split:
            index = split.index(";")
            jmp = "".join(split[0:index])
            code = Code()
            print(code.jmp(jmp))
            return jmp

        else: return ''




d = Parser("JNE;M-D")
d.jmp()
