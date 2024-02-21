`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/09/30 15:25:45
// Design Name: 
// Module Name: fourAOI
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


module fourAOI(
    input A,
    input B,
    input C,
    input D,
    inout E,
    inout F,
    output G
    );
    
    assign E = A & B;
    assign F = C & D;
    assign G = ~(E | F);
    
endmodule
