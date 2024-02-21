`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/12/02 11:08:05
// Design Name: 
// Module Name: RC_tb
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


module RC_tb;

    reg rreset, cclk;
    wire [3:0] sstate;
    
RC u_RC(
    .clk(cclk), 
    .reset(rreset),
    .state(sstate)
);

initial 
begin
cclk = 1'b0;
rreset = 1'b0;
end

always @(cclk or rreset) 
begin
cclk<=#50 ~cclk;
rreset<=#500 ~rreset;
end

endmodule
