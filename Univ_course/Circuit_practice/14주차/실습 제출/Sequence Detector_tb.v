`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/12/09 15:48:01
// Design Name: 
// Module Name: SD_tb
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


module SD_tb;

    reg reset, clk, in;
    wire out;
    wire [1:0]state;
    
SD u_SD(
    .clk(clk), 
    .reset(reset), 
    .in(in),
    .out(out),
    .state(state)
);

initial 
begin
clk = 1'b0;
reset = 1'b0;
in=1'b0;
#20 in=1;
#100 in=0;
#40 in=1;
#240 in=0; 
#40 in=1;
#100 in=0;
#40 in=1;
end

always @(clk or reset) 
begin
clk<=#20 ~clk;
reset<=#500 ~reset;
end

endmodule
