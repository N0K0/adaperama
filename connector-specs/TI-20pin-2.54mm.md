# TI 20-pin JTAG Connector (2.54mm pitch) - Legacy

## Overview
The TI 20-pin JTAG connector is an older debugging interface used with Texas Instruments processors before the introduction of the Compact TI 20-pin (cTI) connector. This legacy connector uses standard 2.54mm (0.1") pitch and was found on earlier TI DSPs and microcontrollers.

**Note:** This is a legacy connector. For new TI designs, use the TI 14-pin 2.54mm connector or the Compact TI 20-pin (cTI 1.27mm) connector instead.

## Physical Specifications
- **Connector Type:** 2x10 pin header (dual row)
- **Pitch:** 2.54mm (0.1")
- **Pin Count:** 20 pins
- **Orientation:** 2 rows of 10 pins
- **Keying:** Pin 6 typically removed for mechanical keying
- **Standard:** Legacy TI JTAG
- **Status:** Legacy - superseded by TI 14-pin and cTI 20-pin connectors

## Common Part Numbers

### Board Headers
**Generic 2x10 headers:**
- Samtec: TSW-110-07-G-D (dual row, through hole)
- Samtec: TSM-110-01-G-D-06 (surface mount, keyed)
- Sullins: SBH11-PBPC-D10-ST-BK (standard 2x10)
- Harwin: M20-9770346 (dual row)

### IDC Connectors
- 3M: 3420-6000 (20-pin female IDC socket)
- Amphenol: T812120A101CEU (ribbon cable connector)
- TE Connectivity: 1-102202-0 (ribbon cable connector)

## Pinout

### Signal Table
| Pin | Signal | Pin | Signal | Description |
|-----|--------|-----|--------|-------------|
| 1   | VTref  | 2   | VTref  | Target Reference Voltage (both pins) |
| 3   | nTRST  | 4   | TDIS   | Test Reset / TDI Status |
| 5   | TDI    | 6   | KEY    | Test Data In / Keyed (pin removed) |
| 7   | TMS    | 8   | GND    | Test Mode Select / Ground |
| 9   | TCK    | 10  | GND    | Test Clock / Ground |
| 11  | RTCK   | 12  | GND    | Return Test Clock / Ground |
| 13  | TDO    | 14  | GND    | Test Data Out / Ground |
| 15  | nRESET | 16  | GND    | System Reset / Ground |
| 17  | NC     | 18  | GND    | Not Connected / Ground |
| 19  | NC     | 20  | GND    | Not Connected / Ground |

### Pin Diagram (Top View)
```
 ╔═══════════════════════╗
 ║  1  3  5  7  9 11 13 15 17 19  ║ Odd pins (signals)
 ║  2  4  6  8 10 12 14 16 18 20  ║ Even pins (KEY at 6, GND)
 ╚═══════════════════════╝
      ↑ Pin 6 KEY (removed)
```

## Electrical Specifications

### Voltage Levels
- **VTref Range:** 1.2V to 5.0V (typically 1.8V, 3.3V, or 5V)
- **Signal Levels:** All signals match VTref voltage
- **I/O Type:** CMOS compatible
- **Maximum Current per Pin:** 10mA (typical JTAG signals)

### Signal Characteristics
- **TCK Frequency:** DC to 50MHz (device dependent)
- **Rise/Fall Times:** < 3ns (typical)
- **Input Capacitance:** ~10pF per input

## Signal Descriptions

### JTAG Signals
- **TMS (Pin 7):** Test Mode Select - Controls TAP state machine
- **TDI (Pin 5):** Test Data In - Serial data into device
- **TDO (Pin 13):** Test Data Out - Serial data from device
- **TCK (Pin 9):** Test Clock - JTAG clock signal
- **nTRST (Pin 3):** Test Reset (active low) - Resets TAP controller
- **RTCK (Pin 11):** Return Test Clock - For adaptive clocking

### TI-Specific Signals
- **TDIS (Pin 4):** TDI Status
  - Some devices use this for additional debugging features
  - May be NC (Not Connected) on many targets
  - Device-specific functionality - consult datasheet

- **nRESET (Pin 15):** System Reset (active low)
  - Resets the target processor
  - May be bidirectional (debugger can reset target, target can signal reset state)

### Power and Ground
- **VTref (Pins 1, 2):** Target voltage reference - supplied by target board (both pins connected together)
- **GND (Pins 8, 10, 12, 14, 16, 18, 20):** Ground connections - provides good signal integrity
- **KEY (Pin 6):** Mechanically removed for proper orientation
- **NC (Pins 17, 19):** Not Connected - reserved for future use or device-specific features

## Comparison with Other TI Connectors

### vs. TI 14-pin 2.54mm (Recommended)
The TI 14-pin is the preferred standard for modern TI designs:
- **Similarities:** Both include basic JTAG signals, TDIS, and GND pins
- **14-pin advantages:**
  - Smaller footprint
  - Includes EMU0/1 pins for advanced debugging
  - Current standard for most TI debuggers
  - Better defined pinout
- **20-pin legacy advantages:**
  - More ground pins (better SI)
  - Dual VTref sensing
  - Familiar to users of older TI hardware

### vs. Compact TI 20-pin (cTI 1.27mm)
The cTI connector is the modern compact option:
- **cTI advantages:**
  - Smaller pitch (1.27mm) - space savings
  - Includes EMU0-3 pins (4 EMU pins vs. none)
  - Modern standard for compact designs
  - Better signal integrity at high speeds
- **Legacy 20-pin advantages:**
  - Standard 2.54mm pitch - easier to hand-solder
  - Compatible with generic ribbon cables
  - Existing tool support

### vs. ARM 20-pin 2.54mm
**Different pinouts!** These are NOT compatible:
- ARM 20-pin: VTref on pin 1, GND on all even pins
- TI 20-pin legacy: VTref on pins 1&2, TDIS on pin 4, KEY on pin 6
- Always verify pinout before connecting!

## Design Considerations

### Pull-up/Pull-down Requirements
The following signals typically require pull-up resistors (10kΩ to VTref):
- TMS (Pin 7) - Required
- TDI (Pin 5) - Recommended
- nTRST (Pin 3) - Required
- nRESET (Pin 15) - Recommended

### Series Resistors
Recommended series resistors (33Ω) on high-speed signals:
- TCK (Pin 9) - For signal integrity
- TMS (Pin 7) - For protection
- TDO (Pin 13) - For protection

### Board Layout
- **Dual VTref:** Both pins 1 and 2 should be connected to VTref
- **Pin 6 KEY:** Remove this pin from the header for mechanical keying
- **Ground distribution:** All GND pins should be connected to solid ground plane
- **Signal routing:** Keep JTAG traces short and away from noisy signals

## Usage Notes

### When to Use This Connector
- **Legacy TI hardware** - Maintaining existing designs with this connector
- **Adapter boards** - Converting between TI connector standards
- **Historical reference** - Understanding older TI development systems

### When NOT to Use This Connector
- **New designs** - Use TI 14-pin or cTI 20-pin instead
- **Maximum feature support** - Missing EMU pins for advanced debugging
- **ARM compatibility** - Completely different pinout

### EMU Pin Limitation
Unlike modern TI connectors, this legacy 20-pin connector **does not include EMU pins**:
- No EMU0/1 for Wait in Reset
- No cross-core triggering support
- Limited advanced debugging features
- Consider upgrading to TI 14-pin or cTI for full functionality

## Migration Guide

### Upgrading to TI 14-pin
To migrate from legacy TI 20-pin to TI 14-pin:

**Signal mapping:**
| Legacy 20-pin | TI 14-pin | Notes |
|---------------|-----------|-------|
| 1,2 (VTref)   | 5 (VTref) | Combine dual VTref |
| 3 (nTRST)     | 2 (nTRST) | Different pin number |
| 4 (TDIS)      | 4 (TDIS)  | Same function |
| 5 (TDI)       | 3 (TDI)   | Different pin number |
| 7 (TMS)       | 1 (TMS)   | Different pin number |
| 9 (TCK)       | 11 (TCK)  | Different pin number |
| 11 (RTCK)     | 9 (RTCK)  | Different pin number |
| 13 (TDO)      | 7 (TDO)   | Different pin number |
| 15 (nRESET)   | *not on connector* | May need separate connection |
| 8,10,12,14,16,18,20 (GND) | 8,10,12 (GND) | Fewer GND pins |
| N/A           | 13,14 (EMU0/1) | New feature - add support |

### Upgrading to cTI 20-pin
To migrate to Compact TI 20-pin:
- Verify board space for 1.27mm pitch connector
- Map basic JTAG signals (pinout differs - see cTI spec)
- Add support for EMU0-3 pins for full feature set
- Update cables and adapters to 1.27mm pitch

## Troubleshooting

### Common Issues
1. **Confusion with ARM 20-pin**
   - Verify you have the correct connector type
   - Check pin 1 and pin 2 - TI has dual VTref, ARM has VTref and NC/VDD
   - Never assume a 20-pin connector is compatible without checking!

2. **Missing EMU Functionality**
   - This legacy connector doesn't have EMU pins
   - Cannot use Wait in Reset or cross-core triggering
   - Consider upgrading to TI 14-pin or cTI for these features

3. **TDIS Pin**
   - May or may not be used depending on device
   - Consult device datasheet for TDIS functionality
   - Often can be left NC if not supported

### Debug Steps
1. Verify VTref present on both pins 1 and 2
2. Check continuity from connector to device JTAG pins
3. Verify pull-up resistors on TMS, TDI, nTRST
4. Confirm KEY pin (6) is removed/blocked
5. Use oscilloscope to check TCK signal integrity

## Historical Context

### Why This Connector Existed
- **Early TI standard** - Before 14-pin and cTI connectors were developed
- **Similarity to ARM** - Same 2x10 format (but different pinout)
- **Adequate ground pins** - Good signal integrity with multiple GND connections

### Why It Was Superseded
- **No EMU pins** - Critical limitation for TI's advanced debugging features
- **Better alternatives available:**
  - TI 14-pin: Smaller, includes EMU0/1
  - cTI 20-pin: Compact, includes EMU0-3
- **Standardization** - TI consolidated on 14-pin for standard pitch
- **Confusion with ARM** - Same physical format but incompatible pinout

## Related Connectors

### Modern TI Alternatives
- **TI 14-pin 2.54mm** - Current standard for TI JTAG (recommended)
- **Compact TI 20-pin (cTI)** - Modern compact version with EMU pins
- **TI 60-pin MIPI** - For high-speed trace (Sitara, advanced processors)

### Similar ARM Connectors (NOT Compatible)
- **ARM 20-pin 2.54mm** - Different pinout, not compatible!
- **ARM 20-pin 1.27mm** - Compact ARM JTAG (different pinout)

### Adapter Considerations
When creating adapters:
1. **Never connect directly to ARM 20-pin** - Different pinouts!
2. Map signals carefully to TI 14-pin or cTI
3. Consider adding EMU pin support if upgrading
4. Verify TDIS handling for target device

## Recommendations

### For Legacy Hardware
If you must support this legacy TI 20-pin connector:
1. Clearly document the lack of EMU pins
2. Verify TDIS usage for your specific device
3. Consider adding a modern TI connector in parallel
4. Test with intended TI debugger/emulator

### For New Designs
**Do not use this connector for new TI designs.** Instead:
- **Use TI 14-pin 2.54mm** - Best for standard pitch, includes EMU0/1
- **Use cTI 20-pin 1.27mm** - Best for compact designs, includes EMU0-3
- Consult TI's current documentation for recommended debug connectors
- Consider your processor family's specific requirements

## Additional Resources

### TI Documentation
- TI XDS Target Connection Guide
- Emulation and Trace Headers Technical Reference Manual
- Device-specific datasheets for JTAG/emulation requirements

### Important Warning
This connector shares the same **physical format** as the ARM 20-pin 2.54mm connector but has a **completely different pinout**. Never assume compatibility! Always verify pinouts before connecting debug probes to avoid damaging equipment.

## Summary

The TI 20-pin 2.54mm legacy connector was an early TI JTAG standard that has been superseded by the TI 14-pin and Compact TI 20-pin (cTI) connectors. While it provides basic JTAG functionality, it lacks the EMU pins necessary for TI's advanced debugging features. This specification is provided for legacy hardware support and historical reference only.
