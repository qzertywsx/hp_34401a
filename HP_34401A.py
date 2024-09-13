from enum import Enum

class HP_34401A(object):
	def __init__(self, gpib, addr):
		self.address = addr
		self.gpib = gpib
		self.firstTime = True
		self.dispMode = self.DisplayMode.NORMAL
		self.preCommand()
	
	class Resolution(Enum):
		DIGIT_AUTO = 0
		DIGIT_4    = 1
		DIGIT_5    = 2
		DIGIT_6    = 3
	
	class Function(Enum):
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
		RANGE_AUTO  = 0
		RANGE_0V1   = 1
		RANGE_1V    = 2
		RANGE_10V   = 3
		RANGE_100V  = 4
		RANGE_1000V = 5
	
	class CurrentRange(Enum):
		RANGE_AUTO = 0
		RANGE_0A01 = 1
		RANGE_0A1  = 2
		RANGE_1A   = 3
		RANGE_3A   = 4
	
	class ResistanceRange(Enum):
		RANGE_AUTO = 0
		RANGE_100R = 1
		RANGE_1K   = 2
		RANGE_10K  = 3
		RANGE_100K = 4
		RANGE_1M   = 5
		RANGE_10M  = 6
		RANGE_100M = 7
	
	class NPLC(Enum):
		NPLC_DEFAULT = 0
		NPLC_0_02    = 1
		NPLC_0_2     = 2
		NPLC_1       = 3
		NPLC_10      = 4
		NPLC_100     = 5
	
	def preCommand(self):
		if self.gpib.address != self.address or self.firstTime:
			self.firstTime = False
			self.gpib.set_address(self.address)
			self.gpib.write("++eor 2")
	
	def get_IDN(self):
		return self.gpib.get_IDN()
	
	def reset(self):
		self.preCommand()
		self.gpib.write("*CLS")
	
	def setFunction(self, function, sel_range=0, resolution=0):
		self.preCommand()
		if function   == self.Function.VOLTAGE_DC:
			list_range = ["DEF", "0.1", "1", "10", "100", "1000"]
			list_res = [["DEF", "DEF", "DEF", "DEF"],["DEF", "1e-5", "1e-6", "1e-7"],["DEF", "1e-4", "1e-5", "1e-6"],["DEF", "1e-3", "1e-4", "1e-5"],["DEF", "1e-2", "1e-3", "1e-4"],["DEF", "1e-1", "1e-2", "1e-3"]]
			self.gpib.write("CONF:VOLT:DC {:s},{:s}".format(list_range[sel_range.value.value], list_res[sel_range.value][resolution.value]))
		elif function == self.Function.VOLTAGE_DC_RATIO:
			list_range = ["DEF", "0.1", "1", "10", "100", "1000"]
			list_res = [["DEF", "DEF", "DEF", "DEF"],["DEF", "1e-5", "1e-6", "1e-7"],["DEF", "1e-4", "1e-5", "1e-6"],["DEF", "1e-3", "1e-4", "1e-5"],["DEF", "1e-2", "1e-3", "1e-4"],["DEF", "1e-1", "1e-2", "1e-3"]]
			self.gpib.write("CONF:VOLT:DC:RATIO {:s},{:s}".format(list_range[sel_range.value], list_res[sel_range.value][resolution.value]))
		elif function == self.Function.VOLTAGE_AC:
			list_range = ["DEF", "0.1", "1", "10", "100", "750"]
			list_res = [["DEF", "DEF", "DEF", "DEF"],["DEF", "1e-5", "1e-6", "1e-7"],["DEF", "1e-4", "1e-5", "1e-6"],["DEF", "1e-3", "1e-4", "1e-5"],["DEF", "1e-2", "1e-3", "1e-4"],["DEF", "1e-1", "1e-2", "1e-3"]]
			self.gpib.write("CONF:VOLT:AC {:s},{:s}".format(list_range[sel_range.value], list_res[sel_range.value][resolution.value]))
		elif function == self.Function.CURRENT_DC:
			list_range = ["DEF", "0.01", "0.1", "1", "3"]
			list_res = [["DEF", "DEF", "DEF", "DEF"],["DEF", "1e-6", "1e-7", "1e-8"],["DEF", "1e-5", "1e-6", "1e-7"],["DEF", "1e-4", "1e-5", "1e-6"],["DEF", "1e-3", "1e-4", "1e-5"]]
			self.gpib.write("CONF:CURR:DC {:s},{:s}".format(list_range[sel_range.value], list_res[sel_range.value][resolution.value]))
		elif function == self.Function.CURRENT_AC:
			list_range = ["DEF", "0.01", "0.1", "1", "3"]
			list_res = [["DEF", "DEF", "DEF", "DEF"],["DEF", "1e-6", "1e-6", "1e-6"],["DEF", "1e-5", "1e-6", "1e-6"],["DEF", "1e-4", "1e-5", "1e-6"],["DEF", "1e-3", "1e-4", "1e-5"]]
			self.gpib.write("CONF:CURR:AC {:s},{:s}".format(list_range[sel_range.value], list_res[sel_range.value][resolution.value]))
		elif function == self.Function.RESISTANCE_2W:
			list_range = ["DEF", "1e2", "1e3", "1e4", "1e5", "1e6", "1e7", "1e8"]
			list_res = [["DEF", "DEF", "DEF", "DEF"],["DEF", "1e-2", "1e-3", "1e-4"],["DEF", "1e-1", "1e-2", "1e-3"],["DEF", "1e0",  "1e-1", "1e-2"],["DEF", "1e1",  "1e0",  "1e-1"],["DEF", "1e2",  "1e1",  "1e0"],["DEF", "1e3",  "1e2",  "1e1"],["DEF", "1e4",  "1e3",  "1e2"]]
			self.gpib.write("CONF:RES {:s},{:s}".format(list_range[sel_range.value], list_res[sel_range.value][resolution.value]))
		elif function == self.Function.RESISTANCE_4W:
			list_range = ["DEF", "1e2", "1e3", "1e4", "1e5", "1e6", "1e7", "1e8"]
			list_res = [["DEF", "DEF", "DEF", "DEF"],["DEF", "1e-2", "1e-3", "1e-4"],["DEF", "1e-1", "1e-2", "1e-3"],["DEF", "1e0",  "1e-1", "1e-2"],["DEF", "1e1",  "1e0",  "1e-1"],["DEF", "1e2",  "1e1",  "1e0"],["DEF", "1e3",  "1e2",  "1e1"],["DEF", "1e4",  "1e3",  "1e2"]]
			self.gpib.write("CONF:FRES {:s},{:s}".format(list_range[sel_range.value], list_res[sel_range.value][resolution.value]))
		elif function == self.Function.FREQUENCY:
			list_res = ["DEF", "1e2", "1e1", "1e0"]
			self.gpib.write("CONF:FREQ MAX,{:s}".format(list_res[resolution.value]))
		elif function == self.Function.PERIOD:
			list_res = ["DEF", "1e2", "1e1", "1e0"]
			self.gpib.write("CONF:PER MAX,{:s}".format(list_res[resolution.value]))
		elif function == self.Function.CONTINUITY:
			self.gpib.write("CONF:CONT")
		elif function == self.Function.DIODE:
			self.gpib.write("CONF:DIOD")
		
	def measure(self, sleep=0.2): #For frequency and period we need 1 sec of sleep, I don't know why (Gate time maybe?)
		self.preCommand()
		self.gpib.write("READ?", sleep)
		try:
			return float(self.gpib.query("++read"))
		except:
			return False
	
	def setNPLC(self, cycles):
		list_NPLC = ["1e1", "2e-2", "2e-1", "1e0", "1e1", "1e2"]
		self.preCommand()
		self.gpib.write("VOLT:DC:NPLC {:s}".format(list_NPLC[cycles.value]))
	
	def getNPLC(self):
		self.preCommand()
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
		self.preCommand()
		self.gpib.write("SYST:BEEP")
	
	def setDisplay(self, on):
		self.preCommand()
		if on:
			self.gpib.write("DISP:STATE ON")
		else:
			self.gpib.write("DISP:STATE OFF")
	
	def setDisplayNormal(self):
		self.preCommand()
		self.gpib.write("DISP:TEXT:CLEAR")
	
	def setDisplayText(self, text):
		self.preCommand()
		self.gpib.write(f"DISP:TEXT \"{text}\"")
	
	def getDisplayText(self):
		self.preCommand()
		self.gpib.write("DISP:TEXT?")
		return self.gpib.query("++read").replace('"', '')
	
	def local(self):
		self.preCommand()
		self.gpib.local()
