`timescale 1ns / 1ps


module DC(
    input reset, clk,
    output reg [3:0] state
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
        if(clk==1)
            if(state==4'b1001)
                state=0;
            else
                state=state+1;
        else if(clk==0)
            state=state;
end

endmodule
