`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/11/04 16:01:54
// Design Name: 
// Module Name: DeMUX_tb
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

module DeMUX_tb;
reg AA, SS0, SS1;
wire OO1, OO2, OO3, OO4;
DeMUX u_DeMUX(
    .A(AA),
    .S0(SS0),
    .S1(SS1),
    .O1(OO1),
    .O2(OO2),
    .O3(OO3),
    .O4(OO4)
    );
initial 
begin
    AA=1'b0;
    SS0=1'b0;
    SS1=1'b0;
end
always @(AA or SS0 or SS1)
begin
    AA<=#400 ~AA;
    SS1<=#200 ~SS1;
    SS0<=#100 ~SS0;
end
endmodule
