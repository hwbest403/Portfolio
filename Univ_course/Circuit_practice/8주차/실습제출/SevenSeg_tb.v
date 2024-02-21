`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/10/28 16:53:52
// Design Name: 
// Module Name: SevenSeg_tb
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


module SevenSeg_tb;
reg AA, BB, CC, DD;
wire aa, bb, cc, dd, ee, ff, gg, DDP, vview;
SevenSeg u_SevenSeg(
    .A(AA),
    .B(BB),
    .C(CC),
    .D(DD),
    .a(aa),
    .b(bb),
    .c(cc),
    .e(ee),
    .f(ff),
    .g(gg),
    .d(dd),
    .DP(DDP),
    .view(vview)
    );
initial 
begin
    AA=1'b0;
    BB=1'b0;
    CC=1'b0;
    DD=1'b0;
end
always @(AA or BB or CC or DD)
begin
    AA<=#400 ~AA;
    BB<=#200 ~BB;
    CC<=#100 ~CC;
    DD<=#50 ~DD;
end
endmodule
