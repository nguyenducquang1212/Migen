#!/usr/bin/env python3

from migen import *

from litex.build.generic_platform import *
from litex.build.altera import AlteraPlatform

# IOs ----------------------------------------------------------------------------------------------

_io = [
    ("user_led",  0, Pins("H17"), IOStandard("LVCMOS33")),
    ("clk50", 0, Pins("Y2"), IOStandard("3.3-V LVTTL"))
]

# Platform -----------------------------------------------------------------------------------------

class Platform(AlteraPlatform):
    default_clk_name   = "clk50"
    default_clk_period = 1e9/100e6

    def __init__(self):
        AlteraPlatform.__init__(self, "EP4CE115F29I7", _io, toolchain="quartus")

    def do_finalize(self, fragment):
        AlteraPlatform.do_finalize(self, fragment)





# from litex.build.generic_platform import *
# from litex.build.xilinx import XilinxPlatform

# # IOs ---------------------------------------------------------------------------------------------- 
# _io = [
#     ("user_led", 0, Pins("AB8"),  IOStandard("LVCMOS15")),

#     ("user_btn_c", 0, Pins("G12"),  IOStandard("LVCMOS25")),

#     ("clk200", 0,
#         Subsignal("p", Pins("AD12"), IOStandard("LVDS")),
#         Subsignal("n", Pins("AD11"), IOStandard("LVDS"))
#     ),

#     # ("clk156", 0,
#     #     Subsignal("p", Pins("K28"), IOStandard("LVDS_25")),
#     #     Subsignal("n", Pins("K29"), IOStandard("LVDS_25"))
#     # ),
#     ("clk156", 0, Pins("K28"), IOStandard("LVDS_25")),

#     ("cpu_reset", 0, Pins("AB7"), IOStandard("LVCMOS15"))
# ]

# # Platform -----------------------------------------------------------------------------------------

# class Platform(XilinxPlatform):
#     default_clk_name   = "clk156"
#     default_clk_period = 1e9/156.5e6

#     def __init__(self):
#         XilinxPlatform.__init__(self, "xc7a100t-csg324-1", _io, toolchain="vivado")

# Design -------------------------------------------------------------------------------------------

# Create our platform (fpga interface)
platform = Platform()

# Create our module (fpga description)
class Switches(Module):
    def __init__(self, platform):
        # Reuse file .v for instance
        platform.add_source('/home/quangnd12/Migen/fpga_lab/test.v')

        # synchronous assignments
        self.sync += []
        led    = platform.request("user_led", 0)
        # clk156 = platform.request("clk156", 0)
        clk156 = ClockSignal();

        # Instance
        self.specials += [
            Instance(
                "test",
                o_user_led = led,
                i_clk = ClockSignal()
            )
        ]


        # combinatorial assignements



module = Switches(platform)

# Build --------------------------------------------------------------------------------------------

platform.build(module)

