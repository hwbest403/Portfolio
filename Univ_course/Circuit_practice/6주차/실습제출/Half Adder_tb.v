`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/10/14 15:09:29
// Design Name: 
// Module Name: HA_tb
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


module HA_tb;
reg AA, BB;
wire CC, SS;
HA u_HA(
    .A(AA),
    .B(BB),
    .C(CC),
    .S(SS) );
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
