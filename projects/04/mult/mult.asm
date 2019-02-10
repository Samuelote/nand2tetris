
// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
@R2
M = 0
@R0
D=M
@16
D;JEQ
(LOOP)
    @R1
    D=M
    @R2
    M=D+M
    @R0
    D=1
    M=M-D
    D=M
    @LOOP
    D;JNE
