`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/09/30 15:19:12
// Design Name: 
// Module Name: fourXOR
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


module fourXOR(
    input A,
    input B,
    input C,
    input D,
    inout E,
    inout F,
    output G
    );
    
    assign E = (A & ~B) | (~A & B);
    assign F = (E & ~C) | (~E & C);
    assign G = (F & ~D) | (~F & D);
    
endmodule
