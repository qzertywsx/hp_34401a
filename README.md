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

* `function`

  `function` is mandatory.
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

* `resolution`:

  `resolution` is not mandatory.

  <table>
    <tr><td>resolution</td><td>Description</td></tr>
    <tr><td>HP_34401A.Resolution.DIGIT_AUTO</td><td>Default number of digit</td></tr>
    <tr><td>HP_34401A.Resolution.DIGIT_4</td><td>4½ digit</td></tr>
    <tr><td>HP_34401A.Resolution.DIGIT_5</td><td>5½ digit</td></tr>
    <tr><td>HP_34401A.Resolution.DIGIT_6</td><td>6½ digit</td></tr>
  </table>

* `sel_range`

  `sel_range` is not mandatory, is mandatory if you want to choose the `resolution`.

  * sel_range for voltage:

    <table>
      <tr><td>sel_range</td><td>Description</td></tr>
      <tr><td>HP_34401A.VoltageRange.RANGE_AUTO</td><td>auto range</td></tr>
      <tr><td>HP_34401A.VoltageRange.RANGE_0V1</td><td>100 mV range</td></tr>
      <tr><td>HP_34401A.VoltageRange.RANGE_1V</td><td>1 V range</td></tr>
      <tr><td>HP_34401A.VoltageRange.RANGE_10V</td><td>10 V range</td></tr>
      <tr><td>HP_34401A.VoltageRange.RANGE_100V</td><td>100 V range</td></tr>
      <tr><td>HP_34401A.VoltageRange.RANGE_1000V</td><td>1000 V range</td></tr>
    </table>

  * sel_range for current:

    <table>
      <tr><td>sel_range</td><td>Description</td></tr>
      <tr><td>HP_34401A.CurrentRange.RANGE_AUTO</td><td>auto range</td></tr>
      <tr><td>HP_34401A.CurrentRange.RANGE_0A01</td><td>10 mA range</td></tr>
      <tr><td>HP_34401A.CurrentRange.RANGE_0A1</td><td>100 mA range</td></tr>
      <tr><td>HP_34401A.CurrentRange.RANGE_1A</td><td>1 A range</td></tr>
      <tr><td>HP_34401A.CurrentRange.RANGE_3A</td><td>3 A range</td></tr>
    </table>

  * sel_range for resistance:

    <table>
      <tr><td>sel_range</td><td>Description</td></tr>
      <tr><td>HP_34401A.ResistanceRange.RANGE_AUTO</td><td>auto range</td></tr>
      <tr><td>HP_34401A.ResistanceRange.RANGE_100R</td><td>100 &Omega; range</td></tr>
      <tr><td>HP_34401A.ResistanceRange.RANGE_1K</td><td>1 k&Omega; range</td></tr>
      <tr><td>HP_34401A.ResistanceRange.RANGE_10K</td><td>10 k&Omega; range</td></tr>
      <tr><td>HP_34401A.ResistanceRange.RANGE_100K</td><td>100 k&Omega; range</td></tr>
      <tr><td>HP_34401A.ResistanceRange.RANGE_1M</td><td>1 M&Omega; range</td></tr>
      <tr><td>HP_34401A.ResistanceRange.RANGE_10M</td><td>10 M&Omega; range</td></tr>
      <tr><td>HP_34401A.ResistanceRange.RANGE_100M</td><td>100 M&Omega; range</td></tr>
    </table>

### measure()
Take a measurement

Return the measurement as real value or `False` in case of problem

### setNPLC(cycles)
Set the number of NPLC
<table>
  <tr><td>cycles</td><td>Description</td></tr>
  <tr><td>HP_34401A.NPLC.NPLC_DEFAULT</td><td>Default number of NPLC</td></tr>
  <tr><td>HP_34401A.NPLC.NPLC_0_02</td><td>0.02 NPLC cycles</td></tr>
  <tr><td>HP_34401A.NPLC.NPLC_0_2</td><td>0.2 NPLC cycles</td></tr>
  <tr><td>HP_34401A.NPLC.NPLC_1</td><td>1 NPLC cycles</td></tr>
  <tr><td>HP_34401A.NPLC.NPLC_10</td><td>10 NPLC cycles</td></tr>
  <tr><td>HP_34401A.NPLC.NPLC_100</td><td>100 NPLC cycles</td></tr>
</table>

### getNPLC()
Return the number of NPLC or `False` in case of problem

### beep()
Emit a beep

### setDisplayState(on)
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

### getError()
Get the last error

### local()
Go to local mode (Reenable the front panel control)

## Usage:
```python
from GPIB_WIFI import AR488_WIFI
from HP_34401A import HP_34401A

gpib = AR488_WIFI('192.168.178.36', timeout=2)
dmm = HP_34401A(gpib, 3)
print(dmm)
dmm.setFunction(HP_34401A.Function.VOLTAGE_AC, HP_34401A.VoltageRange.RANGE_1000V, HP_34401A.Resolution.DIGIT_6)
print("Voltage:", dmm.measure(), "V")
dmm.setFunction(HP_34401A.Function.FREQUENCY, resolution=HP_34401A.Resolution.DIGIT_6)
print("Frequency:", dmm.measure(sleep=2), "Hz")
dmm.local()
```
## Result of executing the above code:
```
HP 34401A address: 3
Voltage: 239.37351 V
Frequency: 50.016148 Hz
```
