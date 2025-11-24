# TI 14-pin JTAG Connector (2.54mm pitch)

## Overview
The TI 14-pin JTAG connector is Texas Instruments' standard debugging interface for many DSP and microcontroller families including C2000, C5000, C6000, and some Sitara processors. It features EMU0/1 pins for advanced debugging features like cross-core triggering and Wait in Reset capabilities.

## Physical Specifications
- **Connector Type:** 2x7 pin header (dual row)
- **Pitch:** 2.54mm (0.1") pin and row pitch
- **Pin Count:** 14 pins
- **Orientation:** 2 rows of 7 pins
- **Keying:** Pin 6 typically removed for mechanical keying
- **Standard:** TI proprietary

## Common Part Numbers

### Board Headers
**Samtec:**
- TSW-107-01-L-D-006 (unshrouded, through hole)
- TSM-107-01-L-DV-006 (unshrouded, surface mount)
- TST-107-01-G-D-06 (shrouded, through hole)

**Don Connex:**
- C03-14-A-G-1-G

**Amphenol/FCI:**
- 98401-101-14LF (SMT - surface mount)
- 77313-101-14LF (TH - through hole)

### Debug Probe Connectors
**Samtec:**
- IDSD-07-S-04.00-P06 (cable assembly, without strain relief)

**Don Connex:**
- A01-14-B-G-A-1-G (with strain relief)
- A01c-14-B-G-B-1-G (without strain relief)

**Amphenol/FCI:**
- 66900-214 (with strain relief)
- 66900-314 (without strain relief)

## Pinout

### Signal Table
| Pin | Signal | Pin | Signal | Description |
|-----|--------|-----|--------|-------------|
| 1   | TMS    | 2   | nTRST  | Test Mode Select / Test Reset |
| 3   | TDI    | 4   | TDIS   | Test Data In / TDI Status |
| 5   | VTref  | 6   | KEY    | Target Reference Voltage / Keyed |
| 7   | TDO    | 8   | GND    | Test Data Out / Ground |
| 9   | RTCK   | 10  | GND    | Return Test Clock / Ground |
| 11  | TCK    | 12  | GND    | Test Clock / Ground |
| 13  | EMU0   | 14  | EMU1   | Emulation pins for triggering/debug |

### Pin Diagram (Top View)
```
 ╔═══════════════════╗
 ║ 1  3  5  7  9 11 13 ║ Odd pins (signals)
 ║ 2  4  6  8 10 12 14 ║ Even pins
 ╚═══════════════════╝
      ↑ Pin 6 KEY (removed)
```

## Electrical Specifications

### Voltage Levels
- **VTref Range:** 1.2V to 5.0V (typically 1.8V or 3.3V)
- **Signal Levels:** All signals match VTref voltage
- **I/O Type:** CMOS compatible
- **Maximum Current per Pin:** 10mA (typical JTAG signals)

### Signal Characteristics
- **TCK Frequency:** DC to 100MHz (device dependent)
- **Rise/Fall Times:** < 3ns (typical)
- **Input Capacitance:** ~10pF per input
- **Output Drive:** ~4mA minimum

## Signal Descriptions

### JTAG Signals
- **TMS (Pin 1):** Test Mode Select - Controls TAP state machine
- **TDI (Pin 3):** Test Data In - Serial data into device
- **TDO (Pin 7):** Test Data Out - Serial data from device
- **TCK (Pin 11):** Test Clock - JTAG clock signal
- **nTRST (Pin 2):** Test Reset (active low) - Resets TAP controller
- **RTCK (Pin 9):** Return Test Clock - For adaptive clocking

### TI-Specific Signals
- **EMU0 (Pin 13):** Emulation pin 0
  - Cross-core triggering (one device halts, signals others)
  - Wait in Reset capability (device dependent)
  - Advanced Event Triggering
  - See device datasheet/TRM for specific usage

- **EMU1 (Pin 14):** Emulation pin 1
  - Similar functionality to EMU0
  - Can be used together for complex trigger scenarios
  - Some devices use for trace information

- **TDIS (Pin 4):** TDI Status
  - Some devices use this for additional debugging features
  - May be NC (Not Connected) on some targets

### Power and Ground
- **VTref (Pin 5):** Target voltage reference - supplied by target board
- **GND (Pins 8, 10, 12):** Ground connections
- **KEY (Pin 6):** Mechanically removed for proper orientation

## Design Considerations

### Pull-up/Pull-down Requirements
The following signals typically require pull-up resistors (10kΩ to VTref):
- TMS (Pin 1) - Required
- TDI (Pin 3) - Recommended
- nTRST (Pin 2) - Required
- EMU0 (Pin 13) - Recommended
- EMU1 (Pin 14) - Recommended

### Series Resistors
Recommended series resistors (33Ω) on high-speed signals:
- TCK (Pin 11) - For signal integrity
- TMS (Pin 1) - For protection
- TDO (Pin 7) - For protection

### Trace Routing Guidelines
1. **Keep traces short** - Especially TCK and RTCK
2. **Match impedance** - Use 50Ω controlled impedance for high-speed designs
3. **Avoid stubs** - Minimize trace stubs on JTAG signals
4. **Ground planes** - Provide solid ground reference
5. **Separation** - Keep JTAG traces away from noisy signals

## Adapter Usage

### Conversion to Other Standards
This connector can be adapted to:
- **20-pin ARM:** Via TMDSADPEMU-20T (maps nRESET, buffers TCK/RTCK)
- **Compact TI 20-pin:** For boards with cTI connectors
- **XDS560 Legacy:** For older debug probes

### Buffer/Termination
For multi-device scan chains or long cable runs:
- TCK and RTCK should be buffered
- Termination may be required for high-speed operation
- See TI's "Emulation and Trace Headers TRM" Chapter 11

## Target Requirements

### Minimum Connection
For basic JTAG debugging, minimum required signals:
- TMS, TDI, TDO, TCK, nTRST
- VTref, GND
- nRESET (recommended but not on this connector)

### EMU Pin Usage
- **C2000 DSPs:** EMU0/1 used for Wait in Reset
- **C5000 DSPs:** EMU0/1 used for cross-core triggering
- **C6000 DSPs:** EMU0/1 used for advanced triggering
- **Sitara (some):** May use EMU pins for trace data

## Device Family Support

### Primary Usage
- **C2000 DSPs:** TMS320F28x, TMS320C28x families
- **C5000 DSPs:** TMS320C54x, TMS320C55x families
- **C6000 DSPs:** TMS320C64x, TMS320C674x families
- **Sitara AM3x/AM4x:** When not using ARM standard connectors
- **OMAP/DaVinci:** Legacy support

### Alternate Header Note
For newer devices, TI recommends:
- **SimpleLink (MSP432, CC series):** Use 10-pin or 20-pin ARM
- **Sitara with trace:** Use 60-pin MIPI connector
- **ARM compatibility needed:** Use ARM 20-pin connector

## Troubleshooting

### Common Issues
1. **No JTAG Connection**
   - Verify VTref is present and correct voltage
   - Check all ground connections
   - Confirm nTRST pull-up resistor installed

2. **Intermittent Connection**
   - Check cable quality and length
   - Verify series resistor values (should be 33Ω, not higher)
   - Ensure good mechanical connection at connector

3. **Slow Operation**
   - Check for excessive capacitance on JTAG lines
   - Reduce TCK frequency in debugger settings
   - Verify RTCK is properly connected for adaptive clocking

### Debug Steps
1. Measure VTref voltage at connector
2. Check continuity from connector to device JTAG pins
3. Verify pull-up resistors with multimeter
4. Use oscilloscope to check TCK signal integrity
5. Confirm device is not held in reset

## Additional Resources

### TI Documentation
- **XDS Target Connection Guide:** Detailed connection information
- **Emulation and Trace Headers Technical Reference Manual:** Electrical specs
- **Device-specific datasheets:** For EMU pin functionality
- **Debugging JTAG Connectivity Problems:** Troubleshooting guide

### Related Connectors
- **Compact TI 20-pin (cTI):** Smaller pitch version with more EMU pins
- **ARM 20-pin:** Industry standard, no EMU pins
- **ARM 10-pin:** Compact ARM SWD/JTAG connector

## Notes

1. **EMU Pin Functionality:** EMU0/1 behavior is device-specific. Always consult the device datasheet for exact functionality.

2. **Adaptive Clocking:** RTCK (Pin 9) is used for adaptive clocking, where the target device provides a return clock signal. This is required for some ARM9/ARM11 cores.

3. **Compatibility:** While this connector is TI-specific, adapters are available to connect to ARM standard debuggers. However, EMU pin functionality will be lost.

4. **Obsolescence:** For new designs, consider using the Compact TI 20-pin (cTI) connector for better feature support, or ARM 20-pin for maximum debugger compatibility.

5. **Scan Path Linker:** If your design uses plug-in cards or dynamic JTAG configurations, consider the TI SN74ACT8997 Scan Path Linker device.
