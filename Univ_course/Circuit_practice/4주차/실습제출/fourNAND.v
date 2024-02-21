`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/09/30 15:06:08
// Design Name: 
// Module Name: fourNAND
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


module fourNAND(
    input A,
    input B,
    input C,
    input D,
    inout E,
    inout F,
    output G
    );
    
    assign E = ~(A & B);
    assign F = ~(E & C);
    assign G = ~(F & D);
    
endmodule
