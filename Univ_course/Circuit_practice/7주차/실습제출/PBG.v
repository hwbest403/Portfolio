`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/10/28 16:14:23
// Design Name: 
// Module Name: PBG
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
    output E
    );
    
    assign E = (~((~A&B)|(A&~B)) & ((~C&D)|(C&~D))) | (((~A&B)|(A&~B)) & ~((~C&D)|(C&~D)));
    
endmodule
