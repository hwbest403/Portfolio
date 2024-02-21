`timescale 1ns / 1ps


module TC(
    input reset, clk,
    output reg [1:0] state
);

initial
begin
    state=0;
end

always@(posedge clk)
begin
    if(reset == 1)
        state=0;
    else if(reset == 0) 
        if(clk == 1)
            state=state+1;
        else if(clk==0)
            state=state;
end

endmodule
