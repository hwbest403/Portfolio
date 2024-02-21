`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/11/04 15:47:07
// Design Name: 
// Module Name: twofourdecoder_tb
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


module twofourdecoder_tb;
reg AA, BB;
wire DD0, DD1, DD2, DD3;
twofourdecoder u_twofourdecoder(
    .A(AA),
    .B(BB),
    .D0(DD0),
    .D1(DD1),
    .D2(DD2),
    .D3(DD3)
    );
initial 
begin
    AA=1'b0;
    BB=1'b0;
end
always @(AA or BB)
begin
    AA<=#500 ~AA;
    BB<=#250 ~BB;
end
endmodule
