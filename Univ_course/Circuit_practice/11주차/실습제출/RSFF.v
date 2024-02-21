`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/11/18 15:35:57
// Design Name: 
// Module Name: RSFF
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


module RSFF(R,S,clk,Q,nQ);
    input R, S, clk;
    output Q, nQ;

    assign Q = ~(nQ|(R&clk));
    assign nQ = ~(Q|(S&clk));
    
endmodule
