`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/11/04 16:12:54
// Design Name: 
// Module Name: fourtwoencoder_tb
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


module fourtwoencoder_tb;
reg AA, BB, CC, DD;
wire EE0, EE1;
fourtwoencoder u_fourtwoencoder(
    .A(AA),
    .B(BB),
    .C(CC),
    .D(DD),
    .E0(EE0),
    .E1(EE1)
    );
initial 
begin
    AA=1'b0;
    BB=1'b0;
    CC=1'b0;
    DD=1'b0;
end
always @(AA or BB or CC or DD)
begin
    AA<=#400 ~AA;
    BB<=#200 ~BB;
    CC<=#100 ~CC;
    DD<=#50 ~DD;
end
endmodule
