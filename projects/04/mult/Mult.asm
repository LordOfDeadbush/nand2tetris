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

// first we need to create our variables

// @R0 would be R0, @R1 would be R1, @R2 would be R2
// we want to multiply @0 by @1 to get @2
// to do this, we need to make a loop with a counter that will break once it reaches @1, 
// in which we will have a variable that will be increased by @0 every loop iteration


// for reference, how to add 2 numbers:

// @0
// D=M
// @1
// D=D+M
// @2
// M=D

// M is what is stored in the selected memory
// D is our variable
