`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/09/16 15:58:23
// Design Name: 
// Module Name: threeand_tb
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


module threeand_tb;

reg AA, BB, CC;

wire DD, EE;

threeand u_threeand(
    .A(AA),
    .B(BB),
    .C(CC),
    .D(DD),
    .E(EE) );
    
initial 
begin
    AA=1'b0;
    BB=1'b0;
    CC=1'b0;
end

always @(AA or BB or CC)

begin
    AA<=#100 ~AA;
    BB<=#200 ~BB;
    CC<=#400 ~CC;
end
        
endmodule
