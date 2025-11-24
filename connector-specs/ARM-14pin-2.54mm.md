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
| 1   | VTref    | 2   | GND        | Target Reference / Ground |
| 3   | nTRST    | 4   | GND        | Test Reset (active low) |
| 5   | TDI      | 6   | GND        | Test Data In |
| 7   | TMS      | 8   | GND        | Test Mode Select |
| 9   | TCK      | 10  | GND        | Test Clock |
| 11  | TDO      | 12  | SRST       | Test Data Out / System Reset |
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
- **TDO (Pin 11):** Test Data Out - Serial data from device
- **TCK (Pin 9):** Test Clock - JTAG clock signal
- **nTRST (Pin 3):** Test Reset (active low) - Resets TAP controller
- **RTCK:** Return Test Clock - **Not available on this connector** (no adaptive clocking support)

### System Signals
- **SRST (Pin 12):** System Reset (active low) - Resets the target processor
- **VTref (Pins 1, 13):** Target voltage reference - supplied by target board (dual sensing)
- **GND (Pins 2, 4, 6, 8, 10, 14):** Ground connections

## Comparison with ARM 20-Pin

### Missing Signals
Compared to the standard ARM 20-pin connector, this legacy 14-pin version **does not include:**
- **RTCK (Return Test Clock)** - No adaptive clocking support
- Additional NC/Debug pins

### Key Limitation
**The absence of RTCK means this connector cannot support adaptive clocking,** which is required for:
- ARM9 and ARM11 processors
- Devices with variable or gated debug clocks
- Systems where TCK must be synchronized with the target

However, this connector **does include TDO**, so it supports full JTAG debugging for devices that don't require adaptive clocking.

### Migration Path
To upgrade from ARM 14-pin to ARM 20-pin:
1. Add RTCK connection if adaptive clocking is needed
2. Verify pin numbering differences
3. Consider adding additional ground pins for better signal integrity

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
- **Dual VTref (Pins 1, 13):** Provides voltage reference sensing on both ends
- **Multiple GND connections:** Better signal integrity compared to minimal ground designs

## Usage Notes

### When to Use This Connector
- **Legacy hardware support** - Maintaining existing designs
- **Adapter boards** - Converting to modern connectors
- **Historical reference** - Understanding older ARM systems

### When NOT to Use This Connector
- **New designs** - Use ARM 20-pin or Cortex 10-pin instead
- **ARM9/ARM11 processors** - Requires RTCK for adaptive clocking
- **Devices needing adaptive clocking** - Missing RTCK pin

### Adapter Considerations
When creating adapters from this legacy connector:
1. **RTCK must be sourced elsewhere** if adaptive clocking is needed
2. Verify SRST vs nRESET naming conventions
3. Pin numbering differs from ARM 20-pin - map carefully
4. Consider signal integrity on longer connections

## Troubleshooting

### Common Issues
1. **Adaptive Clocking Problems**
   - This connector lacks RTCK
   - Will not work with ARM9/ARM11 processors that require adaptive clocking
   - Use ARM 20-pin or add RTCK separately if needed

2. **Power Issues**
   - Check VTref is present on both pins 1 and 13
   - Ensure adequate ground connections on all GND pins
   - Verify dual VTref connections are properly wired

3. **Signal Integrity**
   - Good ground distribution with multiple GND pins
   - Keep connections short for best performance
   - Verify all ground pins are connected

## Historical Context

### Why This Connector Existed
- **Cost reduction** - Fewer pins than 20-pin connector
- **Space savings** - Smaller footprint on target board
- **Simplified manufacturing** - Easier to hand-solder in prototyping

### Why It Was Superseded
- **Missing RTCK** - Cannot support adaptive clocking (required for ARM9/ARM11)
- **Limited expandability** - No room for additional debug features
- **Standardization** - Industry moved to 20-pin for maximum compatibility
- **Fewer pins** - Less flexible than 20-pin standard

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
This connector specification is provided for **legacy hardware support only**. The absence of RTCK means it cannot support adaptive clocking (required for ARM9/ARM11 processors), and this connector should not be used for new designs.
