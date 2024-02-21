`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/11/04 15:32:38
// Design Name: 
// Module Name: DeMUX
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


module DeMUX(
    input A, S0, S1,
    output O1, O2, O3, O4
    );
    
    assign O1=A&~S0&~S1;
    assign O2=A&S0&~S1;
    assign O3=A&~S0&S1;
    assign O4=A&S0&S1;
endmodule
