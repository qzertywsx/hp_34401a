"""Module providing an interface to the HP 34401A 6 1/2 digit multimeter"""
from enum import Enum

class HP34401A():
    """Class to represent the HP 34401A 6œ digit multimeter"""
    def __init__(self, _gpib, addr):
        self.address = addr
        self.gpib = _gpib
        self.first_time = True
        self.disp_mode = self._displayMode.NORMAL
        self._pre_command()

    class _displayMode(Enum):
        """Enum with the display mode"""
        NORMAL = 0
        TEXT   = 1

    class Resolution(Enum):
        """Enum with the resolution of the instrument"""
        DIGIT_AUTO = 0
        DIGIT_4    = 1
        DIGIT_5    = 2
        DIGIT_6    = 3

    class Function(Enum):
        """Enum with the function of the instrument"""
        VOLTAGE_DC       = 0
        VOLTAGE_DC_RATIO = 1
        VOLTAGE_AC       = 2
        CURRENT_DC       = 3
        CURRENT_AC       = 4
        RESISTANCE_2W    = 5
        RESISTANCE_4W    = 6
        FREQUENCY        = 7
        PERIOD           = 8
        CONTINUITY       = 9
        DIODE            = 10

    class VoltageRange(Enum):
        """Enum with the voltage range"""
        RANGE_AUTO  = 0
        RANGE_0V1   = 1
        RANGE_1V    = 2
        RANGE_10V   = 3
        RANGE_100V  = 4
        RANGE_1000V = 5

    class CurrentRange(Enum):
        """Enum with the current range"""
        RANGE_AUTO = 0
        RANGE_0A01 = 1
        RANGE_0A1  = 2
        RANGE_1A   = 3
        RANGE_3A   = 4

    class ResistanceRange(Enum):
        """Enum with the resistance range"""
        RANGE_AUTO = 0
        RANGE_100R = 1
        RANGE_1K   = 2
        RANGE_10K  = 3
        RANGE_100K = 4
        RANGE_1M   = 5
        RANGE_10M  = 6
        RANGE_100M = 7

    class NPLC(Enum):
        """Enum with the available NPLC"""
        NPLC_DEFAULT = 0
        NPLC_0_02    = 1
        NPLC_0_2     = 2
        NPLC_1       = 3
        NPLC_10      = 4
        NPLC_100     = 5

    def __str__(self):
        return "HP 34401A address: " + str(self.address)

    def _pre_command(self):
        """Command to be executed before every other command"""
        if self.gpib.address != self.address or self.first_time:
            self.first_time = False
            self.gpib.set_address(self.address)
            self.gpib.write("++eor 2")

    def get_idn(self):
        """Return the *IDN? of the instrument"""
        return self.gpib.get_idn()

    def reset(self):
        """Reset the instrument to the default state"""
        self._pre_command()
        self.gpib.write("*CLS")

    def set_function(self, function, sel_range=0, resolution=0):
        """Set the function"""
        self._pre_command()
        if function   == self.Function.VOLTAGE_DC:
            list_range = ["DEF", "0.1", "1", "10", "100", "1000"]
            list_res = [["DEF", "DEF", "DEF", "DEF"],["DEF", "1e-5", "1e-6", "1e-7"],\
                ["DEF", "1e-4", "1e-5", "1e-6"],["DEF", "1e-3", "1e-4", "1e-5"],\
                ["DEF", "1e-2", "1e-3", "1e-4"],["DEF", "1e-1", "1e-2", "1e-3"]]
            self.gpib.write(f"CONF:VOLT:DC {list_range[sel_range.value.value]:s},\
                            {list_res[sel_range.value][resolution.value]:s}")
        elif function == self.Function.VOLTAGE_DC_RATIO:
            list_range = ["DEF", "0.1", "1", "10", "100", "1000"]
            list_res = [["DEF", "DEF", "DEF", "DEF"],["DEF", "1e-5", "1e-6", "1e-7"],\
                ["DEF", "1e-4", "1e-5", "1e-6"],["DEF", "1e-3", "1e-4", "1e-5"],\
                ["DEF", "1e-2", "1e-3", "1e-4"],["DEF", "1e-1", "1e-2", "1e-3"]]
            self.gpib.write(f"CONF:VOLT:DC:RATIO {list_range[sel_range.value]:s},\
                            {list_res[sel_range.value][resolution.value]:s}")
        elif function == self.Function.VOLTAGE_AC:
            list_range = ["DEF", "0.1", "1", "10", "100", "750"]
            list_res = [["DEF", "DEF", "DEF", "DEF"],["DEF", "1e-5", "1e-6", "1e-7"],\
                ["DEF", "1e-4", "1e-5", "1e-6"],["DEF", "1e-3", "1e-4", "1e-5"],\
                ["DEF", "1e-2", "1e-3", "1e-4"],["DEF", "1e-1", "1e-2", "1e-3"]]
            self.gpib.write(f"CONF:VOLT:AC {list_range[sel_range.value]:s},\
                            {list_res[sel_range.value][resolution.value]:s}")
        elif function == self.Function.CURRENT_DC:
            list_range = ["DEF", "0.01", "0.1", "1", "3"]
            list_res = [["DEF", "DEF", "DEF", "DEF"],["DEF", "1e-6", "1e-7", "1e-8"],\
                ["DEF", "1e-5", "1e-6", "1e-7"],["DEF", "1e-4", "1e-5", "1e-6"],\
                ["DEF", "1e-3", "1e-4", "1e-5"]]
            self.gpib.write(f"CONF:CURR:DC {list_range[sel_range.value]:s},\
                            {list_res[sel_range.value][resolution.value]:s}")
        elif function == self.Function.CURRENT_AC:
            list_range = ["DEF", "0.01", "0.1", "1", "3"]
            list_res = [["DEF", "DEF", "DEF", "DEF"],["DEF", "1e-6", "1e-6", "1e-6"],\
                ["DEF", "1e-5", "1e-6", "1e-6"],["DEF", "1e-4", "1e-5", "1e-6"],\
                ["DEF", "1e-3", "1e-4", "1e-5"]]
            self.gpib.write(f"CONF:CURR:AC {list_range[sel_range.value]:s},\
                            {list_res[sel_range.value][resolution.value]:s}")
        elif function == self.Function.RESISTANCE_2W:
            list_range = ["DEF", "1e2", "1e3", "1e4", "1e5", "1e6", "1e7", "1e8"]
            list_res = [["DEF", "DEF", "DEF", "DEF"],["DEF", "1e-2", "1e-3", "1e-4"],\
                ["DEF", "1e-1", "1e-2", "1e-3"],["DEF", "1e0",  "1e-1", "1e-2"],\
                ["DEF", "1e1",  "1e0",  "1e-1"],["DEF", "1e2",  "1e1",  "1e0"],\
                ["DEF", "1e3",  "1e2",  "1e1"],["DEF", "1e4",  "1e3",  "1e2"]]
            self.gpib.write(f"CONF:RES {list_range[sel_range.value]:s},\
                            {list_res[sel_range.value][resolution.value]:s}")
        elif function == self.Function.RESISTANCE_4W:
            list_range = ["DEF", "1e2", "1e3", "1e4", "1e5", "1e6", "1e7", "1e8"]
            list_res = [["DEF", "DEF", "DEF", "DEF"],["DEF", "1e-2", "1e-3", "1e-4"],\
                ["DEF", "1e-1", "1e-2", "1e-3"],["DEF", "1e0",  "1e-1", "1e-2"],\
                ["DEF", "1e1",  "1e0",  "1e-1"],["DEF", "1e2",  "1e1",  "1e0"],\
                ["DEF", "1e3",  "1e2",  "1e1"],["DEF", "1e4",  "1e3",  "1e2"]]
            self.gpib.write(f"CONF:FRES {list_range[sel_range.value]:s},\
                            {list_res[sel_range.value][resolution.value]:s}")
        elif function == self.Function.FREQUENCY:
            list_res = ["DEF", "1e2", "1e1", "1e0"]
            self.gpib.write(f"CONF:FREQ MAX,{list_res[resolution.value]:s}")
        elif function == self.Function.PERIOD:
            list_res = ["DEF", "1e2", "1e1", "1e0"]
            self.gpib.write(f"CONF:PER MAX,{list_res[resolution.value]:s}")
        elif function == self.Function.CONTINUITY:
            self.gpib.write("CONF:CONT")
        elif function == self.Function.DIODE:
            self.gpib.write("CONF:DIOD")

    def measure(self, sleep=0.2): #For frequency and period we need 1.2 sec of sleep
        """Take a measurement"""
        self._pre_command()
        self.gpib.write("READ?", sleep)
        try:
            return float(self.gpib.query("++read", sleep))
        except (ValueError, AttributeError):
            return False

    def set_nplc(self, cycles):
        """Set the number of NPLC"""
        list_nplc = ["1e1", "2e-2", "2e-1", "1e0", "1e1", "1e2"]
        self._pre_command()
        self.gpib.write(f"VOLT:DC:NPLC {list_nplc[cycles.value]:s}")

    def get_nplc(self):
        """Return the number of NPLC or False in case of problem"""
        self._pre_command()
        self.gpib.write("VOLT:DC:NPLC?")
        t = self.gpib.query("++read")
        if t == "+2.00000000E-02":
            return self.NPLC.NPLC_0_02
        if t == "+2.00000000E-01":
            return self.NPLC.NPLC_0_2
        if t == "+1.00000000E+00":
            return self.NPLC.NPLC_1
        if t == "+1.00000000E+01":
            return self.NPLC.NPLC_10
        if t == "+1.00000000E+02":
            return self.NPLC.NPLC_100
        return False

    def beep(self):
        """Emit a beep"""
        self._pre_command()
        self.gpib.write("SYST:BEEP")

    def set_display_state(self, on):
        """Switch the display on or off"""
        self._pre_command()
        if on:
            self.gpib.write("DISP:STATE ON")
        else:
            self.gpib.write("DISP:STATE OFF")

    def set_display_normal(self):
        """Set the display to normal mode (Show the measured value)"""
        self._pre_command()
        self.gpib.write("DISP:TEXT:CLEAR")

    def set_display_text(self, text):
        """Set a custom text on the display (Max 12 character)"""
        self._pre_command()
        self.gpib.write(f"DISP:TEXT \"{text}\"")

    def get_display_text(self):
        """Get the custom text currently on the display"""
        self._pre_command()
        self.gpib.write("DISP:TEXT?")
        return self.gpib.query("++read").replace('"', '')

    def get_error(self):
        """Get the last error"""
        self._pre_command()
        self.gpib.write("SYST:ERR?")
        return self.gpib.query("++read")

    def local(self):
        """Go to local mode (Reenable the front panel control)"""
        self._pre_command()
        self.gpib.local()
