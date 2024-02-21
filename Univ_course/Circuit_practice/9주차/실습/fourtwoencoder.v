`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/11/04 15:17:45
// Design Name: 
// Module Name: fourtwoencoder
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


module fourtwoencoder(
    input A, B, C, D,
    output E0, E1
    );
    
    assign E0=B|D;
    assign E1=C|D;
    
endmodule
