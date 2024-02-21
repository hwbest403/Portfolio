`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/11/04 15:53:59
// Design Name: 
// Module Name: MUX_tb
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


module MUX_tb;
reg AA, BB, CC, DD, SS0, SS1;
wire OO;
MUX u_MUX(
    .A(AA),
    .B(BB),
    .C(CC),
    .D(DD),
    .S0(SS0),
    .S1(SS1),
    .O(OO)
    );
initial 
begin
    AA=1'b0;
    BB=1'b0;
    CC=1'b0;
    DD=1'b0;
    SS0=1'b0;
    SS1=1'b0;
end
always @(AA or BB or CC or DD or SS0 or SS1)
begin
    AA<=#480 ~AA;
    BB<=#240 ~BB;
    CC<=#120 ~CC;
    DD<=#60 ~DD;
    SS0<=#30 ~SS0;
    SS1<=#15 ~SS1;
end
endmodule
