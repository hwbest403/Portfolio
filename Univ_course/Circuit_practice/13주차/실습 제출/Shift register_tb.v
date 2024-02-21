`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/12/02 10:44:08
// Design Name: 
// Module Name: SR_tb
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


module SR_tb;

    reg rreset, cclk, iin;
    wire [3:0] sstate;
    
SR u_SR(
    .clk(cclk), 
    .reset(rreset),
    .in(iin),
    .state(sstate)
);

initial 
begin
iin = 1'b0;
cclk = 1'b0;
rreset = 1'b0;
end

always @(cclk or rreset or iin) 
begin
cclk<=#10 ~cclk;
iin<=#100 ~iin;
rreset<=#500 ~rreset;
end

endmodule
