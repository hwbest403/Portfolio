`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/10/28 15:39:26
// Design Name: 
// Module Name: twobitcompare
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


module twobitcompare(
    input A1,
    input A2,
    input B1,
    input B2,
    output F1,
    output F2,
    output F3
    );
    
    assign F1 = (A1&~B1) | (A2&~B1&~B2) | (A1&A2&~B2);
    assign F2 = ~((~A1&B1)|(A1&~B1)) & ~((~A2&B2) | (A2&~B2));
    assign F3 = (~A1&B1)|(~A2&B1&B2)|(~A1&~A2&B2);
    
endmodule
