`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/10/14 15:11:48
// Design Name: 
// Module Name: FA
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


module FA(
    input A,
    input B,
    input Cin,
    output S,
    output Cout
    );
    
    assign S = (~((~A&B)|(A&~B))&Cin)|(((~A&B)|(A&~B))&~Cin);
    assign Cout = ((~A&B)|(A&~B))&Cin | (A&B);
    
endmodule
