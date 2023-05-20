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

// Put your code here.


(LOOP)
    @KBD
    D=M
    @KEYSTROKE
    M=D // saving the key state to the keystroke register
    @COUNT
    M=0 // putting our count at 0 makes it so we can count the pixels we use (131072 pixels, so we should max out at 131071)
    @SCREEN
    D=A
    @REGISTER
    M=D
    @UPDATESCREEN
    0;JMP

(UPDATESCREEN)
    @KEYSTROKE
    D=M
    @REGISTER
    A=M
    M=D
    D=A+1
    @REGISTER
    M=D
    @1
    D=M
    @COUNT
    M=M+D
    D=M-131072
    @LOOP
    D;JMP
    @UPDATESCREEN
    0;JMP

    // this brings us back to the top
    @LOOP
    0;JMP