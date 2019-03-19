from Code import Code


class Parser:

    def __init__(self, cmd):
        self.cmd = cmd
        self.cmd = self.remove_white_space()
        self.cmd = self.remove_comments()

    def remove_white_space(self):
        self.cmd = self.cmd.strip()
        return self.cmd.replace(" ", "")

    def remove_comments(self):

        if "//" in self.cmd:
            return self.cmd[0:self.cmd.index("//")]
        else: return self.cmd


    def commandType(self):
        if len(self.cmd) == 0: return
        split_cmd = list(self.cmd)

        if (split_cmd[0] == "@"):
            # self.symbol("A", split_cmd)
            return "A_COMMAND"

        elif (split_cmd[0] == "("):
            # self.symbol("L", split_cmd)
            return "L_COMMAND"

        elif ";" in split_cmd or "=" in split_cmd:
            return "C_COMMAND"


    def symbol(self, type):
        if (type == "A_COMMAND"):
            return self.cmd.replace("@", "")
        elif(type == "L_COMMAND"):
            cmd = self.cmd.replace("(", "")
            cmd= cmd.replace(")", "")
            return cmd

    def dest(self):
        if "=" in self.cmd:
            dest = self.cmd.split("=")[0]

            return dest;
        else:
            return ""

    def comp(self):
        split = list(self.cmd)
        if "=" in split:
            index = split.index("=")
            comp = "".join(split[index+1:])
            # print(len(comp), comp)
            return comp
        else:
            return ''

    def jmp(self):

        split = list(self.cmd)
        if ";" in split:
            index = split.index(";")
            jmp = "".join(split[0:index])
            return jmp

        else: return ''




# d = Parser("JNE;M-D")
# d.jmp()
