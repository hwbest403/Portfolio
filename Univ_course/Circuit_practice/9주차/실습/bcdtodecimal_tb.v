`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/11/04 16:28:52
// Design Name: 
// Module Name: bcdtodecimal_tb
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


module bcdtodecimal_tb;
reg AA0, AA1, AA2, AA3;
wire BB1, BB2, BB3, BB4, BB5, BB6, BB7, BB8, BB9;
bcdtodecimal u_bcdtodecimal(
    .A0(AA0),
    .A1(AA1),
    .A2(AA2),
    .A3(AA3),
    .B1(BB1),
    .B2(BB2),
    .B3(BB3),
    .B4(BB4),
    .B5(BB5),
    .B6(BB6),
    .B7(BB7),
    .B8(BB8),
    .B9(BB9)
    );
initial 
begin
    AA0=1'b0;
    AA1=1'b0;
    AA2=1'b0;
    AA3=1'b0;
end
always @(AA0 or AA1 or AA2 or AA3)
begin
    AA0<=#50 ~AA0;
    AA1<=#100 ~AA1;
    AA2<=#200 ~AA2;
    AA3<=#400 ~AA3;
end
endmodule

