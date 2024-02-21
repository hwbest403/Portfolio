`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/12/02 11:58:56
// Design Name: 
// Module Name: UDC_tb
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


module UDC_tb;

    reg rreset, cclk, uup;
    wire [3:0] sstate;
    wire [6:0] sseg;
    wire ddp, vview;
    
UDC u_UDC(
    .clk(cclk), 
    .reset(rreset), 
    .up(uup),
    .state(sstate),
    .seg(sseg),
    .dp(ddp),
    .view(vview)
);

initial 
begin
cclk = 1'b0;
rreset = 1'b0;
uup=1'b0;
end

always @(cclk or rreset or uup) 
begin
cclk<=#10 ~cclk;
uup<=#250 ~uup;
rreset<=#500 ~rreset;
end

endmodule
