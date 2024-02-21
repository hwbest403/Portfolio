`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/12/02 10:59:58
// Design Name: 
// Module Name: RC
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


module RC(
    input clk, reset,
    output reg [3:0] state
    );
    
initial
begin
   state=8;
end
    
always@(posedge clk)
begin
    if(reset==0)
    begin
        if(clk==0)
            state=state;
        else if(clk==1)
            if(state==0)
            begin
                state=1;
                state[3]<=state[0];
                state[2]<=state[3];
                state[1]<=state[2];
                state[0]<=state[1];
            end
            else
                state[3]<=state[0];
                state[2]<=state[3];
                state[1]<=state[2];
                state[0]<=state[1];
    end
    else if(reset==1)
        state=0;
end
    
endmodule
