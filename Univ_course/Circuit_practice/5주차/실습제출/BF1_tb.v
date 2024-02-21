`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/10/07 15:09:24
// Design Name: 
// Module Name: BF1_tb
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


module BF1_tb;
reg AA, BB, CC;
wire DD, EE;
BF1 u_BF1(
    .A(AA),
    .B(BB),
    .C(CC),
    .D(DD),
    .E(EE) );
initial 
begin
    AA=1'b0;
    BB=1'b0;
    CC=1'b0;
end
always @(AA or BB or CC)
begin
    AA<=#100 ~AA;
    BB<=#200 ~BB;
    CC<=#400 ~CC;
end
endmodule
