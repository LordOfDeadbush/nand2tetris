// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

// see: https://www.nand2tetris.org/_files/ugd/44046b_d70026d8c1424487a451eaba3e372132.pdf


    @R2
    M=0 // setting the sum mem point to 0
    @count
    M=0
(LOOP)
    @count
    D=M // storing count in D
    @R1
    D=D-M // = count - R1 for loop check
    D=D+1
    @END
    D;JGT // if our count is equal to R1 then we go to end
    @R0
    D=M // D = R1
    @R2
    M=M+D // adding R0 to R2
    @count
    M=M+1 // incrementing count
    @LOOP
    0;JMP // looping

(END)
    @END
    0;JMP
