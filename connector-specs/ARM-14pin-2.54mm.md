# ARM 14-pin JTAG Connector (2.54mm pitch) - Legacy

## Overview
The ARM 14-pin JTAG connector is an older, compact debugging interface that was used with some ARM processors before the standardization on the 20-pin connector. This connector is primarily found on legacy hardware and some cost-sensitive designs where the full 20-pin connector was not needed.

**Note:** This is a legacy connector. For new designs, use the ARM 20-pin (2.54mm or 1.27mm) or ARM Cortex 10-pin connectors instead.

## Physical Specifications
- **Connector Type:** 2x7 pin header (dual row)
- **Pitch:** 2.54mm (0.1")
- **Pin Count:** 14 pins
- **Orientation:** 2 rows of 7 pins
- **Standard:** Legacy ARM JTAG
- **Status:** Legacy - superseded by ARM 20-pin connectors

## Common Part Numbers

### Board Headers
**Generic 2x7 headers:**
- Samtec: TSW-107-07-G-D (dual row, through hole)
- Sullins: SBH11-PBPC-D07-ST-BK (standard 2x7)
- Harwin: M20-9770746 (dual row)

### IDC Connectors
- 3M: 3420-5000 (14-pin female IDC socket)
- Amphenol: T812114A101CEU (ribbon cable connector)

## Pinout

### Signal Table
| Pin | Signal   | Pin | Signal     | Description |
|-----|----------|-----|------------|-------------|
| 1   | VTref    | 2   | Vsupply    | Target Reference / Supply Voltage |
| 3   | nTRST    | 4   | GND        | Test Reset (active low) |
| 5   | TDI      | 6   | GND        | Test Data In |
| 7   | TMS      | 8   | GND        | Test Mode Select |
| 9   | TCK      | 10  | GND        | Test Clock |
| 11  | RTCK     | 12  | nRESET     | Return Test Clock / System Reset |
| 13  | VTref    | 14  | GND        | Target Reference / Ground |

### Pin Diagram (Top View)
```
 ╔════════════════════╗
 ║ 1  3  5  7  9 11 13 ║ Odd pins (mostly signals)
 ║ 2  4  6  8 10 12 14 ║ Even pins (mostly GND)
 ╚════════════════════╝
```

## Electrical Specifications

### Voltage Levels
- **VTref Range:** 1.8V to 5.0V (typically 3.3V)
- **Vsupply (Pin 2):** Optional supply from debugger (or NC)
- **Signal Levels:** All signals match VTref voltage
- **I/O Type:** CMOS compatible
- **Maximum Current per Pin:** 10mA (typical JTAG signals)

### Signal Characteristics
- **TCK Frequency:** DC to 20MHz (typical for this connector)
- **Rise/Fall Times:** < 5ns (typical)
- **Input Capacitance:** ~10pF per input

## Signal Descriptions

### JTAG Signals
- **TMS (Pin 7):** Test Mode Select - Controls TAP state machine
- **TDI (Pin 5):** Test Data In - Serial data into device
- **TDO:** Test Data Out - **Not available on this connector**
- **TCK (Pin 9):** Test Clock - JTAG clock signal
- **nTRST (Pin 3):** Test Reset (active low) - Resets TAP controller
- **RTCK (Pin 11):** Return Test Clock - For adaptive clocking

### System Signals
- **nRESET (Pin 12):** System Reset (active low) - Resets the target processor
- **VTref (Pins 1, 13):** Target voltage reference - supplied by target board
- **Vsupply (Pin 2):** Optional power supply from debugger (may be NC)
- **GND (Pins 4, 6, 8, 10, 14):** Ground connections

## Comparison with ARM 20-Pin

### Missing Signals
Compared to the standard ARM 20-pin connector, this legacy 14-pin version **does not include:**
- **TDO (Test Data Out)** - Critical limitation!
- Additional NC/Debug pins

### Key Limitation
**The absence of TDO makes this connector unsuitable for full JTAG debugging.** It may have been used for:
- Manufacturing/programming only (write-only operations)
- Systems with alternative debug methods
- Very early ARM designs with different debug architectures

### Migration Path
To upgrade from ARM 14-pin to ARM 20-pin:
1. Add TDO connection (essential for debugging)
2. Add proper ground pins for signal integrity
3. Consider pin compatibility when designing adapters

## Design Considerations

### Pull-up/Pull-down Requirements
The following signals typically require pull-up resistors (10kΩ to VTref):
- TMS (Pin 7) - Required
- TDI (Pin 5) - Recommended
- nTRST (Pin 3) - Required
- nRESET (Pin 12) - Recommended (may be driven by debugger)

### Series Resistors
Recommended series resistors (33Ω) on:
- TCK (Pin 9) - For signal integrity
- TMS (Pin 7) - For protection

### Power Considerations
- **Pin 2 (Vsupply):** May be connected to debugger power output or left NC
  - If connected: Typically provides 3.3V or 5V from debugger
  - Maximum current: Usually limited to 100-200mA
  - Use for level shifting or isolated target power only
- **Dual VTref (Pins 1, 13):** Provides voltage reference sensing on both ends

## Usage Notes

### When to Use This Connector
- **Legacy hardware support** - Maintaining existing designs
- **Adapter boards** - Converting to modern connectors
- **Historical reference** - Understanding older ARM systems

### When NOT to Use This Connector
- **New designs** - Use ARM 20-pin or Cortex 10-pin instead
- **Full JTAG debugging** - Missing TDO pin
- **Production debugging** - Limited functionality

### Adapter Considerations
When creating adapters from this legacy connector:
1. **TDO must be sourced elsewhere** or debugging will be limited
2. Check if pin 2 (Vsupply) is used or NC on target
3. Verify nRESET functionality (some boards use different reset schemes)
4. Consider signal integrity on longer connections

## Troubleshooting

### Common Issues
1. **No Debug Connection - Missing TDO**
   - This is expected - connector does not have TDO
   - Cannot perform full JTAG boundary scan
   - May work for programming-only operations

2. **Power Issues**
   - Verify if pin 2 (Vsupply) should be connected or NC
   - Check VTref is present on both pins 1 and 13
   - Ensure adequate ground connections

3. **Signal Integrity**
   - Limited ground pins compared to 20-pin connector
   - Keep connections short
   - May need additional ground wiring for longer cables

## Historical Context

### Why This Connector Existed
- **Cost reduction** - Fewer pins than 20-pin connector
- **Space savings** - Smaller footprint on target board
- **Simplified manufacturing** - Easier to hand-solder in prototyping

### Why It Was Superseded
- **Missing TDO** - Fatal flaw for full JTAG debugging
- **Limited expandability** - No room for additional debug features
- **Standardization** - Industry moved to 20-pin for compatibility
- **Signal integrity** - Insufficient ground pins

## Related Connectors

### Modern Alternatives
- **ARM 20-pin 2.54mm** - Full-featured, industry standard
- **ARM 20-pin 1.27mm** - Compact version with all signals
- **ARM Cortex 10-pin 1.27mm** - Modern SWD/JTAG connector
- **TI 14-pin 2.54mm** - Different pinout, includes TDO and EMU pins

### Adapter Availability
Some debug probe manufacturers offered adapters from:
- ARM 20-pin to ARM 14-pin (limited functionality)
- Custom solutions for specific legacy hardware

## Recommendations

### For Legacy Hardware
If you must support this connector:
1. Document the limitations clearly
2. Consider adding a proper 20-pin connector in parallel
3. Verify what functionality is actually available
4. Test thoroughly with intended debugger

### For New Designs
**Do not use this connector for new designs.** Instead:
- Use ARM 20-pin 2.54mm for maximum compatibility
- Use ARM 20-pin 1.27mm for space-constrained boards
- Use ARM Cortex 10-pin 1.27mm for modern ARM Cortex-M devices
- Use TI 14-pin 2.54mm if targeting TI processors (different pinout!)

## Additional Resources

### Documentation
- ARM Application Notes on JTAG debugging
- Legacy debugger manuals that supported this connector
- Migration guides to modern ARM debug connectors

### Important Note
This connector specification is provided for **legacy hardware support only**. The absence of TDO severely limits debugging capabilities, and this connector should not be used for new designs.
