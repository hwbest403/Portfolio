`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/11/04 15:15:47
// Design Name: 
// Module Name: twofourdecoder
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


module twofourdecoder(
    
    input A, B,
    output D0,
    output D1, 
    output D2,
    output D3
    );
    
    assign D0=~A&~B;
    assign D1=~A&B;
    assign D2=A&~B;
    assign D3=A&B;
    
endmodule
