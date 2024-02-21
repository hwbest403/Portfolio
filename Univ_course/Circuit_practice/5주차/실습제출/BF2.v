`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/10/07 15:11:52
// Design Name: 
// Module Name: BF2
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


module BF2(
    input A,
    input B,
    input C,
    output D,
    output E
    );
    
    assign D = (~A & ~B) | ~C;
    assign E = ~( (A | B) & C );
    
endmodule
