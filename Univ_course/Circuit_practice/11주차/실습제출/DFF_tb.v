`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/11/18 16:06:36
// Design Name: 
// Module Name: DFF_tb
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
reg DD,cclk;
wire QQ,nQQ;
DFF tb(
    .D(DD), 
    .clk(cclk), 
    .Q(QQ), 
    .nQ(nQQ));
initial begin
cclk = 1'b1;
DD = 1'b0;
end
always @(DD or cclk)
begin
cclk <=#100 ~cclk;
DD <=#250 ~DD;
end
endmodule
