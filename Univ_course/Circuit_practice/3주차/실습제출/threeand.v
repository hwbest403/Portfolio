`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/09/16 15:50:25
// Design Name: 
// Module Name: threeand
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


module threeand(
    input A,
    input B,
    input C,
    inout D,
    output E
    );
    
    assign D = A & B;
    assign E = D & C;
    
endmodule
