`timescale 1ns / 1ps


module DC2421_tb;

    reg rreset, cclk;
    wire [3:0] sstate;
    
DC2421 u_DC2421(
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
cclk<=#20 ~cclk;
rreset<=#500 ~rreset;
end

endmodule
