`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/10/07 15:15:49
// Design Name: 
// Module Name: bitcompare
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


module bitcompare(
    input A,
    input B,
    output C,
    output D,
    output E,
    output F
    );
    
    assign C = ~ ( (~A&B) | (A&~B) );
    assign D = (~A&B) | (A&~B);
    assign E = A&~B;
    assign F = ~A & B;
    
endmodule
