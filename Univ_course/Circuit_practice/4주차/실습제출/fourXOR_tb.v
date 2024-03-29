`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/09/30 15:21:54
// Design Name: 
// Module Name: fourXOR_tb
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


module fourXOR_tb;
reg AA, BB, CC, DD;
wire EE, FF, GG;

fourXOR u_fourXOR(
    .A(AA),
    .B(BB),
    .C(CC),
    .D(DD),
    .E(EE),
    .F(FF),
    .G(GG) );
initial 
begin
    AA=1'b0;
    BB=1'b0;
    CC=1'b0;
    DD=1'b0;
end
always @(AA or BB or CC or DD)
begin
    AA<=#50 ~AA;
    BB<=#100 ~BB;
    CC<=#200 ~CC;
    DD<=#400 ~DD;
end
        
endmodule
