`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/12/02 10:35:03
// Design Name: 
// Module Name: SR
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


module SR(
    input clk, reset, in,
    output reg [3:0] state
    );
    
initial
begin
state=0;
end

always@(posedge clk)
begin
    if(reset==0)
    begin
        if(clk==0)
            state=state;
        else if(clk==1)
            state[0]=state[1];
            state[1]=state[2];
            state[2]=state[3];
            state[3]=in;
    end
    else if(reset==1)
        state=0;
end
    
endmodule
