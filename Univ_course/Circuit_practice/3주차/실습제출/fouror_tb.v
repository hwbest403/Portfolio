`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/09/16 16:36:55
// Design Name: 
// Module Name: fouror_tb
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


module fouror_tb;

reg AA, BB, CC, DD;

wire EE, FF, GG;

fouror u_fouror(
    .A(AA),
    .B(BB),
    .C(CC),
    .D(DD),
    .E(EE),
    .F(FF),
    .G(GG) );
    
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
