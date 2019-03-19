from Code import Code


class Parser:

    def __init__(self, cmd):
        self.cmd = cmd
        self.cmd = self.remove_white_space()
        self.cmd = self.remove_comments()
        print("Command:", self.cmd)

    def remove_white_space(self):
        return self.cmd.replace(" ", "")

    def remove_comments(self):
        if "//" in self.cmd:
            return self.cmd[0:self.cmd.index("//")]
        else: return self.cmd


    def commandType(self):
        split_cmd = list(self.cmd)
        if (split_cmd[0] == "@"):
            self.symbol()
            return "A_COMMAND"

        elif (split_cmd[0] == "(" and split_cmd[len(split_cmd)-1] == ")"):
            self.symbol()
            return "L_COMMAND"

        elif ";" in split_cmd or "=" in split_cmd:
            return "C_COMMAND"


    def symbol(self):
        split_cmd = list(self.cmd)
        # A command
        if (split_cmd[0] == "@"):
            return "".join(split_cmd[1:])
        # L command
        elif(split_cmd[0] == "("):
            split_cmd.pop()
            return "".join(split_cmd[1:])

    def dest(self):
        if "=" in self.cmd:
            dest = self.cmd.split("=")[0]
            //Gets binary
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
            // Gets binary
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
            // Gets binary
            code = Code()
            code.jmp(jmp)
            return jmp

        else: return ''



test = Parser("JGT;A")
