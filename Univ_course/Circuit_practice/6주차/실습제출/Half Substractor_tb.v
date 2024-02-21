`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/10/14 15:22:16
// Design Name: 
// Module Name: HS_tb
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


module HS_tb;
reg AA, BB;
wire BBr, DD;
HS u_HS(
    .A(AA),
    .B(BB),
    .Br(BBr),
    .D(DD) );
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
