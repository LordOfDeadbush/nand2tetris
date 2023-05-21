// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// link for ref: https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm

// Put your code here.

    @8192 // amount of pixels we have because it is NOT a 256 by 512, the book lied
    D=A
    @SCREEN
    D=D+A
    @MAX
    M=D
    @SCREEN
    D=A
    @n
    M=D
(LOOP)
    // if (n == MAX) reset count and go back to top of loop
    @n
    D=M
    @MAX
    D=M-D
    @RESET
    D;JEQ
    // now for the fun stuff
    @KBD
    D=M
    @SETWHITE
    D;JEQ
    @SETBLACK
    0;JMP

(SETBLACK)
    // this is for blk
    @SCREEN
    D=M
    @n
    A=D+M
    M=-1
    @n
    M=M+1
    @LOOP
    0;JMP

(SETWHITE)
    // this is for white
    @SCREEN
    D=M
    @n
    A=D+M
    M=0
    @n
    M=M+1
    @LOOP
    0;JMP

(RESET)
    @SCREEN
    D=A
    @n
    M=D
    @LOOP
    0;JMP
