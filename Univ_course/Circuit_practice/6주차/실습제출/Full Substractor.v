`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/10/14 15:24:42
// Design Name: 
// Module Name: FS
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


module FS(
    input A,
    input B,
    input Brin,
    output D,
    output Brout
    );
    
    assign D = (~((~A&B)|(A&~B))&Brin)|(((~A&B)|(A&~B))&~Brin);
    assign Brout = ~((~A&B)|(A&~B))&Brin | (~A&B);
    
endmodule
