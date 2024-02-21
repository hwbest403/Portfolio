`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/10/14 15:30:58
// Design Name: 
// Module Name: BCDCONV
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


module BCDCONV(
    input A,
    input B,
    input C,
    input D,
    output E,
    output F,
    output G,
    output H
    );
    assign E=A|(B&D)|(B&C);
    assign F=(B&~D)|A|(B&C);
    assign G=(~B&C)|A|(B&~C&D);
    assign H=D;
endmodule
