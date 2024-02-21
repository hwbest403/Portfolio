`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/10/07 15:19:27
// Design Name: 
// Module Name: bitcompare_tb
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


module bitcompare_tb;
reg AA, BB;
wire CC, DD, EE, FF;
bitcompare u_bitcompare(
    .A(AA),
    .B(BB),
    .C(CC),
    .D(DD),
    .E(EE),
    .F(FF) );
initial 
begin
    AA=1'b0;
    BB=1'b0;
end
always @(AA or BB)
begin
    AA<=#250 ~AA;
    BB<=#500 ~BB;
end
endmodule
