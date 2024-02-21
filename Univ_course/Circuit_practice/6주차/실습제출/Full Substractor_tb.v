`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/10/14 15:27:50
// Design Name: 
// Module Name: FS_tb
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


module FS_tb;
reg AA, BB, BBrin;
wire BBrout, DD;
FS u_FS(
    .A(AA),
    .B(BB),
    .Brin(BBrin),
    .Brout(BBrout),
    .D(DD) );
initial 
begin
    AA=1'b0;
    BB=1'b0;
    BBrin=1'b0;
end
always @(AA or BB or BBrin)
begin
    AA<=#100 ~AA;
    BB<=#200 ~BB;
    BBrin<=#400 ~BBrin;
end
endmodule
