`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/10/28 15:57:34
// Design Name: 
// Module Name: twobitcompare_tb
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


module twobitcompare_tb;
reg AA1, AA2, BB1, BB2;
wire FF1, FF2, FF3;
twobitcompare u_twobitcompare(
    .A1(AA1),
    .A2(AA2),
    .B1(BB1),
    .B2(BB2),
    .F1(FF1),
    .F2(FF2),
    .F3(FF3)
    );
initial 
begin
    AA1=1'b0;
    AA2=1'b0;
    BB1=1'b0;
    BB2=1'b0;
end
always @(AA1 or AA2 or BB1 or BB2)
begin
    AA1<=#400 ~AA1;
    AA2<=#200 ~AA2;
    BB1<=#100 ~BB1;
    BB2=#50 ~BB2;
end
endmodule
