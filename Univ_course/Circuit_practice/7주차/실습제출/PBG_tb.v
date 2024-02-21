`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/10/28 16:18:27
// Design Name: 
// Module Name: PBG_tb
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


module PBG_tb;
reg AA, BB, CC, DD;
wire EE;
PBG u_PBG(
    .A(AA),
    .B(BB),
    .C(CC),
    .D(DD),
    .E(EE)
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
