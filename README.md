# HP_34401A
Python module for the HP 34401A 6½ digit multimeter.

You must use my GPIB or GPIB_WIFI module to use this module.

## Supported command:
### get_IDN()
Return the *IDN? of the instrument

### reset()
Reset the instrument to the default state

### setFunction(function, sel_range, resolution)
Set the function
<table>
  <tr><td>function</td><td>Description</td></tr>
  <tr><td>HP_34401A.Function.VOLTAGE_DC</td><td>Measure DC voltage</td></tr>
  <tr><td>HP_34401A.Function.VOLTAGE_DC_RATIO</td><td>Measure DC voltage ratio</td></tr>
  <tr><td>HP_34401A.Function.VOLTAGE_AC</td><td>Measure AC voltage</td></tr>
  <tr><td>HP_34401A.Function.CURRENT_DC</td><td>Measure DC current</td></tr>
  <tr><td>HP_34401A.Function.CURRENT_AC</td><td>Measure AC current</td></tr>
  <tr><td>HP_34401A.Function.RESISTANCE_2W</td><td>Measure 2 wire resistance</td></tr>
  <tr><td>HP_34401A.Function.RESISTANCE_4W</td><td>Measure 4 wire resistance</td></tr>
  <tr><td>HP_34401A.Function.FREQUENCY</td><td>Measure frequency</td></tr>
  <tr><td>HP_34401A.Function.PERIOD</td><td>Measure period </td></tr>
  <tr><td>HP_34401A.Function.CONTINUITY</td><td>Measure continuity</td></tr>
  <tr><td>HP_34401A.Function.DIODE</td><td>Measure diode</td></tr>
</table>

*`resolution`:
  `resolution` is not mandatory.

  Available `resolution`:
  * HP_34401A.Resolution.DIGIT_AUTO
  * HP_34401A.Resolution.DIGIT_4
  * HP_34401A.Resolution.DIGIT_5
  * HP_34401A.Resolution.DIGIT_6

sel_range is not mandatory.

sel_range for voltage:

* HP_34401A.VoltageRange.RANGE_AUTO
* HP_34401A.VoltageRange.RANGE_0V1
* HP_34401A.VoltageRange.RANGE_1V
* HP_34401A.VoltageRange.RANGE_10V
* HP_34401A.VoltageRange.RANGE_100V
* HP_34401A.VoltageRange.RANGE_1000V

sel_range for current:

* HP_34401A.CurrentRange.RANGE_AUTO
* HP_34401A.CurrentRange.RANGE_0A01
* HP_34401A.CurrentRange.RANGE_0A1
* HP_34401A.CurrentRange.RANGE_1A
* HP_34401A.CurrentRange.RANGE_3A
* 
sel_range for resistance:

* HP_34401A.ResistanceRange.RANGE_AUTO
* HP_34401A.ResistanceRange.RANGE_100R
* HP_34401A.ResistanceRange.RANGE_1K
* HP_34401A.ResistanceRange.RANGE_10K
* HP_34401A.ResistanceRange.RANGE_100K
* HP_34401A.ResistanceRange.RANGE_1M
* HP_34401A.ResistanceRange.RANGE_10M
* HP_34401A.ResistanceRange.RANGE_100M

### measure()
Get the output state
<table>
  <tr><td>Return</td><td>Description</td></tr>
  <tr><td>True</td><td>The output is enabled</td></tr>
  <tr><td>False</td><td>The output is disabled</td></tr>
</table>

### setNPLC(cycles)
Set the voltage to `volt`

### getNPLC()
Return the measured voltage or `False` in case of problem

### beep()
Set the current to `amps`

### setDisplay(on)
Switch the display on or off
<table>
  <tr><td>on</td><td>Description</td></tr>
  <tr><td>True</td><td>Switch on the display</td></tr>
  <tr><td>False</td><td>Switch off the display</td></tr>
</table>

### setDisplayNormal()
Set the display to normal mode (Show the measured value) 

### setDisplayText(text)
Set a custom `text` on the display (Max 12 character)

### getDisplayText()
Get the custom text currently on the display

### local()
Go to local mode (Reenable the front panel control)

## Usage:
```python
from GPIB_WIFI import AR488_WIFI
from HP_34401A import HP_34401A

gpib = AR488_WIFI('192.168.178.36', timeout=5)
dmm = HP_34401A( gpib, 3)
dmm.setVoltage(5)
dmm.setCurrent(0.5)
print("Voltage:", dmm.getVoltage(), "V")
print("Current:", dmm.getCurrent(), "A")
dmm.local()
```
## Result of executing the above code (Not done yet):
```
GPIB address: 3, IP: 192.168.178.36
```
