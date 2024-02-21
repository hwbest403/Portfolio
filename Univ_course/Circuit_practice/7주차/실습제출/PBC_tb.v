`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/10/28 16:25:53
// Design Name: 
// Module Name: PBC_tb
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



module PBC_tb;
reg AA, BB, CC, DD, PP;
wire PEE;
PBG u_PBG(
    .A(AA),
    .B(BB),
    .C(CC),
    .D(DD),
    .P(PP),
    .PEC(PEE)
    );
initial 
begin
    AA=1'b0;
    BB=1'b0;
    CC=1'b0;
    DD=1'b0;
    PP=1'b0;
end
always @(AA or BB or CC or DD or PP)
begin
    AA<=#400 ~AA;
    BB<=#200 ~BB;
    CC<=#100 ~CC;
    DD<=#50 ~DD;
    PP<=#25 ~PP;
end
endmodule
