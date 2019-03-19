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
file = open("test.vm", "r")
lines = file.readlines()


def handle(line):
    # gets rid of newline characters
    if "\n" in line:
        line = line.replace("\n", "")

    # handles comments
    if "//" in line:
        return line[0:line.index("//")]
    else:
        return line

VM = VM()
for line in lines:
    line = handle(line)

    if len(line)>3:
        split = line.split(" ")
        cmd = split[0]
        seg = split[1]
        idx = split[2]
        VM.WritePushPop(cmd,seg,idx)
    elif len(line)>1:
        split = line.split(" ")
        cmd = split[0]
        VM.WritePushPop(cmd,None,None)

# VM.WritePushPop("eq",None, None)
# VM.WritePushPop('pop','constant',3)