`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/11/18 15:41:11
// Design Name: 
// Module Name: RSFF_tb
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


module RSFF_tb;
reg RR,SS,cclk;
wire QQ,nQQ;
RSFF tb(
    .R(RR), 
    .S(SS), 
    .clk(cclk), 
    .Q(QQ), 
    .nQ(nQQ));
initial begin
cclk = 1'b1;
RR = 1'b0;
SS = 1'b1;
end
always @(RR or SS or cclk)
begin
cclk <=#100 ~cclk;
RR <=#250 ~RR;
SS <=#500 ~SS;
end
endmodule
