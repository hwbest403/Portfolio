`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/10/28 16:42:48
// Design Name: 
// Module Name: SevenSeg
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


module SevenSeg(
    
    input A,
    input B,
    input C,
    input D,
    output a,
    output b,
    output c,
    output d,
    output e,
    output f,
    output g,
    output DP,
    output view
    );
    
    assign a = (~B&~D)|(A&~D)|(B&C)|(~A&C)|(A&~B&~C)|(~A&B&D);
    assign b = (~A&~B)|(~B&~D)|(~A&~C&~D)|(A&~C&D)|(~A&C&D);
    assign c = (~A&B)|(A&~B)|(~C&D)|(~A&~C)|(~A&D);
    assign d = (~A&~B&~D)|(A&~C&~D)|(B&~C&D)|(~B&C&D)|(B&C&~D);
    assign e = (~B&~D)|(A&B)|(C&~D)|(A&C);
    assign f = (A&~B)|(~C&~D)|(A&C)|(B&~D)|(~A&B&~C);
    assign g = (A&~B)|(C&~D)|(~B&C)|(A&D)|(~A&B&~C);
    assign DP = 1;
    assign view =1;
    
endmodule
