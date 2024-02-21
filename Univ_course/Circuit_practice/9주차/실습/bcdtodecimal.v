`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/11/04 15:27:27
// Design Name: 
// Module Name: bcdtodecimal
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


module bcdtodecimal(
    input A0, A1, A2, A3,
    output B1, B2, B3, B4, B5, B6, B7, B8, B9
    );
    
    assign B1=A0&~A1&~A2&~A3;
    assign B2=A1&~A0&~A2;
    assign B3=A0&A1&~A2;
    assign B4=A2&~A0&~A1;
    assign B5=A0&A2&~A1;
    assign B6=A1&A2&~A0;
    assign B7=A0&A1&A2;
    assign B8=A3&~A0;
    assign B9=A0&A3;
endmodule
