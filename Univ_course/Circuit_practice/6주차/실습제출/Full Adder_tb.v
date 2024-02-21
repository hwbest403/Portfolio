`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/10/14 15:16:11
// Design Name: 
// Module Name: FA_tb
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


module FA_tb;
reg AA, BB, CCin;
wire CCout, SS;
FA u_FA(
    .A(AA),
    .B(BB),
    .Cin(CCin),
    .Cout(CCout),
    .S(SS) );
initial 
begin
    AA=1'b0;
    BB=1'b0;
    CCin=1'b0;
end
always @(AA or BB or CCin)
begin
    AA<=#100 ~AA;
    BB<=#200 ~BB;
    CCin<=#400 ~CCin;
end
endmodule
