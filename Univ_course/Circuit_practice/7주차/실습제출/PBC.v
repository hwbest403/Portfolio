`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/10/28 16:22:48
// Design Name: 
// Module Name: PBC
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module PBG(
    input A,
    input B,
    input C,
    input D,
    input P,
    output PEC
    );
    
   
    
    assign PEC = ( ((~((~A&B)|(A&~B)) & ((~C&D)|(C&~D))) | (((~A&B)|(A&~B)) & ~((~C&D)|(C&~D)))) & ~P ) | (~((~((~A&B)|(A&~B)) & ((~C&D)|(C&~D))) | (((~A&B)|(A&~B)) & ~((~C&D)|(C&~D)))) & P);
    
endmodule
