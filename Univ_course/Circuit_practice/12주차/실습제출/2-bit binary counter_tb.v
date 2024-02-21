`timescale 1ns / 1ps


module TC_tb;

    reg rreset, cclk;
    wire [1:0] sstate;
    
TC u_TC(
    .clk(cclk), 
    .reset(rreset), 
    .state(sstate)
);

initial 
begin
cclk = 1'b0;
rreset = 1'b0;
end

always @(cclk or rreset) 
begin
cclk<=#50 ~cclk;
rreset<=#500 ~rreset;
end

endmodule
