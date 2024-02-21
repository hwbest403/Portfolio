`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2021/12/09 15:12:00
// Design Name: 
// Module Name: SD
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


module SD(
    input reset, clk, in,
    output reg [0:1] state,
    output reg out
    );
    
    initial
    begin
        state=2'b00;
    end
    
    always@(posedge clk)
    begin
        if(reset==1)
        begin
            state=2'b00;
            out=0;
        end
        else if(reset==0)
        begin
            if(state==2'b00)
            begin
                if(in==0)
                begin
                    state<=2'b00;
                    out<=0;
                end
                else if(in==1)
                begin
                    state<=2'b01;
                    out<=0;
                end
            end
            else if(state==2'b01)
            begin
                if(in==0)
                begin
                    state<=2'b00;
                    out<=0;
                end
                else if(in==1)
                begin
                    state<=2'b10;
                    out<=0;
                end
            end
            else if(state==2'b10)
            begin
                if(in==0)
                begin
                    state<=2'b11;
                    out<=0;
                end
                else if(in==1)
                begin
                    state<=2'b10;
                    out<=0;
                end
            end
            else if(state==2'b11)
            begin
                if(in==0)
                begin
                    state<=2'b00;
                    out<=0;
                end
                else if(in==1)
                begin
                    state<=2'b01;
                    out<=1;
                end
            end
        end
    end
    
endmodule
