`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/09/16 16:29:57
// Design Name: 
// Module Name: threeor
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


module threeor(
    input A,
    input B,
    input C,
    inout D,
    output E
    );
    
    assign D = A | B;
    assign E = D | C;
    
endmodule
