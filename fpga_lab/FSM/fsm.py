#!/usr/bin/env python3

#
# @author: Nguyen Duc Quang
#

from migen import *
from migen.fhdl import verilog

class fsm(Module):
    def __init__(self):
        self.money = Signal(2)  # Input
        self.product = Signal() # Output

        fsm = FSM(reset_state = "STATE_0K")
        self.submodules += fsm

        fsm.act(
            "STATE_0K",
            If (
                self.money == 0,    # money = 10k
                NextValue(self.product, 0),
                NextState ("STATE_10K")
            ).Elif (
                self.money == 1,    # money = 20k
                NextValue(self.product, 0),
                NextState("STATE_20K")
            ).Elif(
                self.money == 2,    # money = 50k
                NextValue(self.product, 1),
                NextState("STATE_0K")
            ).Else(
                NextValue(self.product, 0),
                NextState("STATE_0K")
            )
        )

        fsm.act(
            "STATE_10K",
            If (
                self.money == 0,    # money = 10k
                NextValue(self.product, 0),
                NextState ("STATE_20K")
            ).Elif (
                self.money == 1,    # money = 20k
                NextValue(self.product, 0),
                NextState("STATE_30K")
            ).Elif(
                self.money == 2,    # money = 50k
                NextValue(self.product, 1),
                NextState("STATE_0K")
            ).Else(
                NextValue(self.product, 0),
                NextState("STATE_10K")
            )
        )

        fsm.act(
            "STATE_20K",
            If (
                self.money == 0,    # money = 10k
                NextValue(self.product, 0),
                NextState ("STATE_30K")
            ).Elif (
                self.money == 1,    # money = 20k
                NextValue(self.product, 0),
                NextState("STATE_40K")
            ).Elif(
                self.money == 2,    # money = 50k
                NextValue(self.product, 1),
                NextState("STATE_0K")
            ).Else(
                NextValue(self.product, 0),
                NextState("STATE_20K")
            )
        )

        fsm.act(
            "STATE_30K",
            If (
                self.money == 0,    # money = 10k
                NextValue(self.product, 0),
                NextState ("STATE_40K")
            ).Elif (
                self.money == 1,    # money = 20k
                NextValue(self.product, 1),
                NextState("STATE_0K")
            ).Elif(
                self.money == 2,    # money = 50k
                NextValue(self.product, 1),
                NextState("STATE_0K")
            ).Else(
                NextValue(self.product, 0),
                NextState("STATE_30K")
            )
        )

        fsm.act(
            "STATE_40K",
            If (
                self.money == 0,    # money = 10k
                NextValue(self.product, 1),
                NextState ("STATE_0K")
            ).Elif (
                self.money == 1,    # money = 20k
                NextValue(self.product, 1),
                NextState("STATE_0K")
            ).Elif(
                self.money == 2,    # money = 50k
                NextValue(self.product, 1),
                NextState("STATE_0K")
            ).Else(
                NextValue(self.product, 0),
                NextState("STATE_40K")
            )
        )

if __name__ == "__main__":
    from migen.fhdl.verilog import convert
    # convert(fsm()).write("fsm.v")
    module = fsm()
    ios = {module.money, module.product}
    f = open("fsm.v", "w")
    f.write(verilog.convert(module, ios, name="fsm").main_source)
    f.close()