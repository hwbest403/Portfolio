`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/12/02 11:58:23
// Design Name: 
// Module Name: UDC
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


module UDC(
    input clk, reset, up,
    output reg [3:0] state,
    output reg [6:0] seg,
    output reg dp, view
);

initial
begin
state=0;
seg=0;
dp=1'b1;
view=1'b1;
end

always@(posedge clk)
begin
    if(reset==0)
    begin
        if(clk==0)
        begin
            state=state;
        end
        else if(clk==1)
        begin
            if(up==0)
            begin
                seg[0]=1'b0;
                seg[1]=1'b1;
                seg[2]=1'b1;
                seg[3]=1'b1;
                seg[4]=1'b1;
                seg[5]=1'b0;
                seg[6]=1'b1;
                state<=state-1;
            end
            else if(up==1)
            begin
                seg[0]=1'b0;
                seg[1]=1'b1;
                seg[2]=1'b1;
                seg[3]=1'b1;
                seg[4]=1'b1;
                seg[5]=1'b1;
                seg[6]=1'b0;
                state<=state+1;
            end
        end
    end
    else if(reset==1)
    begin
        state=0;
    end
end
endmodule
