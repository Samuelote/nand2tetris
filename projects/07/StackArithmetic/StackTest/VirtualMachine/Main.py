from Operations import VM

# CREATES SEGMENTS
segments = {
    "CONSTANT": [],
    "STATIC": [],
    "POINTER": [],
    "TEMP": [],
    "ARG": [],
    "LCL": [],
    "THIS": [],
    "THAT": [],
}
file = open("StackTest.vm", "r")
lines = file.readlines()


def handle(line):
    line = line.strip()
    # gets rid of newline characters
    if "\n" in line:
        line = line.replace("\n", "")

    # handles comments
    if "//" in line:
        return line[0:line.index("//")]
    else:
        return line

VM = VM("StackTest.vm")
for line in lines:
    line = handle(line)

    if line == "" or line[0] == "/":
        pass
    elif line[0] == "p":
        split = line.split(" ")
        cmd = split[0]
        seg = split[1]
        idx = split[2]
        VM.WritePushPop(cmd,seg,idx)
    else:
        split = line.split(" ")
        cmd = split[0]
        VM.WriteArithmetic(cmd)

# VM.WritePushPop("eq",None, None)
# VM.WritePushPop('pop','constant',3)