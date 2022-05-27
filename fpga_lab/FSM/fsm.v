/* Machine-generated using Migen */
module fsm(
	input [1:0] money,
	output reg product,
	input sys_clk,
	input sys_rst
);

reg [2:0] state = 3'd0;
reg [2:0] next_state;
reg product_next_value;
reg product_next_value_ce;

// synthesis translate_off
reg dummy_s;
initial dummy_s <= 1'd0;
// synthesis translate_on


// synthesis translate_off
reg dummy_d;
// synthesis translate_on
always @(*) begin
	next_state <= 3'd0;
	product_next_value <= 1'd0;
	product_next_value_ce <= 1'd0;
	next_state <= state;
	case (state)
		1'd1: begin
			if ((money == 1'd0)) begin
				product_next_value <= 1'd0;
				product_next_value_ce <= 1'd1;
				next_state <= 2'd2;
			end else begin
				if ((money == 1'd1)) begin
					product_next_value <= 1'd0;
					product_next_value_ce <= 1'd1;
					next_state <= 2'd3;
				end else begin
					if ((money == 2'd2)) begin
						product_next_value <= 1'd1;
						product_next_value_ce <= 1'd1;
						next_state <= 1'd0;
					end else begin
						product_next_value <= 1'd0;
						product_next_value_ce <= 1'd1;
						next_state <= 1'd1;
					end
				end
			end
		end
		2'd2: begin
			if ((money == 1'd0)) begin
				product_next_value <= 1'd0;
				product_next_value_ce <= 1'd1;
				next_state <= 2'd3;
			end else begin
				if ((money == 1'd1)) begin
					product_next_value <= 1'd0;
					product_next_value_ce <= 1'd1;
					next_state <= 3'd4;
				end else begin
					if ((money == 2'd2)) begin
						product_next_value <= 1'd1;
						product_next_value_ce <= 1'd1;
						next_state <= 1'd0;
					end else begin
						product_next_value <= 1'd0;
						product_next_value_ce <= 1'd1;
						next_state <= 2'd2;
					end
				end
			end
		end
		2'd3: begin
			if ((money == 1'd0)) begin
				product_next_value <= 1'd0;
				product_next_value_ce <= 1'd1;
				next_state <= 3'd4;
			end else begin
				if ((money == 1'd1)) begin
					product_next_value <= 1'd1;
					product_next_value_ce <= 1'd1;
					next_state <= 1'd0;
				end else begin
					if ((money == 2'd2)) begin
						product_next_value <= 1'd1;
						product_next_value_ce <= 1'd1;
						next_state <= 1'd0;
					end else begin
						product_next_value <= 1'd0;
						product_next_value_ce <= 1'd1;
						next_state <= 2'd3;
					end
				end
			end
		end
		3'd4: begin
			if ((money == 1'd0)) begin
				product_next_value <= 1'd1;
				product_next_value_ce <= 1'd1;
				next_state <= 1'd0;
			end else begin
				if ((money == 1'd1)) begin
					product_next_value <= 1'd1;
					product_next_value_ce <= 1'd1;
					next_state <= 1'd0;
				end else begin
					if ((money == 2'd2)) begin
						product_next_value <= 1'd1;
						product_next_value_ce <= 1'd1;
						next_state <= 1'd0;
					end else begin
						product_next_value <= 1'd0;
						product_next_value_ce <= 1'd1;
						next_state <= 3'd4;
					end
				end
			end
		end
		default: begin
			if ((money == 1'd0)) begin
				product_next_value <= 1'd0;
				product_next_value_ce <= 1'd1;
				next_state <= 1'd1;
			end else begin
				if ((money == 1'd1)) begin
					product_next_value <= 1'd0;
					product_next_value_ce <= 1'd1;
					next_state <= 2'd2;
				end else begin
					if ((money == 2'd2)) begin
						product_next_value <= 1'd1;
						product_next_value_ce <= 1'd1;
						next_state <= 1'd0;
					end else begin
						product_next_value <= 1'd0;
						product_next_value_ce <= 1'd1;
						next_state <= 1'd0;
					end
				end
			end
		end
	endcase
// synthesis translate_off
	dummy_d <= dummy_s;
// synthesis translate_on
end

always @(posedge sys_clk) begin
	state <= next_state;
	if (product_next_value_ce) begin
		product <= product_next_value;
	end
	if (sys_rst) begin
		product <= 1'd0;
		state <= 3'd0;
	end
end

endmodule
