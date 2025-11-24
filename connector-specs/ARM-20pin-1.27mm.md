# ARM 20-pin JTAG Connector (1.27mm pitch)

## Overview
The ARM 20-pin compact JTAG connector is a space-saving version of the standard 2.54mm ARM JTAG connector. It uses a 1.27mm (0.05") pitch, making it suitable for compact target boards while maintaining the same signal arrangement.

## Physical Specifications
- **Connector Type:** 2x10 pin header
- **Pitch:** 1.27mm (0.05")
- **Pin Count:** 20 pins
- **Orientation:** 2 rows of 10 pins
- **Keying:** Pin 7 or Pin 14 typically removed for mechanical keying

## Common Part Numbers
- Samtec: FTSH-110-01-L-DV-K (vertical)
- Samtec: FTSH-110-01-L-DV-K-A (with alignment pins)
- Amphenol: 20021121-00010T1LF (low profile)
- 3M: 952520-6800-AR (right angle)

## Pinout

### Signal Table
| Pin | Signal      | Pin | Signal      | Description                          |
|-----|-------------|-----|-------------|--------------------------------------|
| 1   | VTref       | 2   | NC/VDD      | Target reference voltage             |
| 3   | nTRST       | 4   | GND         | Test Reset (active low)              |
| 5   | TDI         | 6   | GND         | Test Data In                         |
| 7   | TMS         | 8   | GND         | Test Mode Select                     |
| 9   | TCK         | 10  | GND         | Test Clock                           |
| 11  | RTCK        | 12  | GND         | Return Test Clock (adaptive clocking)|
| 13  | TDO         | 14  | GND         | Test Data Out                        |
| 15  | nRESET/nSRST| 16  | GND         | System Reset (active low)            |
| 17  | NC          | 18  | GND         | Not Connected                        |
| 19  | NC/DBGRQ    | 20  | GND         | Debug Request (optional)             |

### Pin Diagram (Top View)
```
 ╔═══════════════════════╗
 ║  1  3  5  7  9 11 13 15 17 19  ║ Odd pins (signals)
 ║  2  4  6  8 10 12 14 16 18 20  ║ Even pins (mostly GND)
 ╚═══════════════════════╝
```

## Electrical Specifications

### Voltage Levels
- **VTref Range:** 1.2V to 5.0V (typically 1.8V or 3.3V)
- **Signal Levels:** All signals match VTref voltage
- **I/O Type:** CMOS compatible
- **Maximum Current per Pin:** 10mA (typical JTAG signals)

### Pull Resistor Requirements
| Signal  | Pull Direction | Resistance | Required? | Notes                           |
|---------|----------------|------------|-----------|----------------------------------|
| TMS     | Pull-up        | 10kΩ-47kΩ  | Yes       | Essential for proper operation   |
| TDI     | Pull-up        | 10kΩ-47kΩ  | Yes       | Essential for proper operation   |
| nTRST   | Pull-up        | 10kΩ-47kΩ  | Recommended| Prevents floating               |
| nRESET  | Pull-up        | 10kΩ-47kΩ  | Recommended| Prevents accidental reset       |
| TCK     | Pull-down      | 10kΩ-47kΩ  | Optional  | Keeps clock idle when disconnected|
| TDO     | None           | -          | No        | Driven by target                |

### Series Resistors (Optional Protection)
- **Value:** 22Ω - 47Ω on all signal lines
- **Purpose:** Signal integrity, short circuit protection, impedance matching
- **Placement:** Close to connector on debugger side

## Signal Descriptions

### Core JTAG Signals
- **TCK (Test Clock):** Clock signal for JTAG operations, driven by debugger
- **TMS (Test Mode Select):** Controls JTAG state machine, driven by debugger
- **TDI (Test Data In):** Serial data input to target, driven by debugger
- **TDO (Test Data Out):** Serial data output from target, driven by target
- **nTRST (Test Reset):** Asynchronous reset for JTAG TAP controller (optional in IEEE 1149.1)

### System Signals
- **nRESET/nSRST:** System reset for the target processor
- **VTref:** Target voltage reference, used by debugger to set I/O voltage levels
- **RTCK:** Return clock for adaptive clocking (advanced feature for slow targets)

### Optional Signals
- **DBGRQ (Pin 19):** Debug request signal (rarely used)
- **VDD (Pin 2):** Some implementations provide power to target

## Usage Notes

### As Adapter Output
When using this connector as an output on the JTAG adapter:
1. Connect via ribbon cable from input connector (J-Link via ribbon cable)
2. Include pull-up resistors on TMS, TDI, nTRST, nRESET (10kΩ to VTref)
3. Optional pull-down on TCK (10kΩ to GND)
4. VTref must be supplied by target board
5. Series resistors (33Ω) recommended on all signals for basic protection

### Cable Considerations
- Maximum recommended cable length: 150mm for standard JTAG speeds (<10MHz)
- For high-speed operation (>10MHz): Use controlled impedance cable, shorter lengths
- Shield cable or use twisted pairs for EMI reduction in noisy environments
- Ensure good ground connection - multiple GND pins help reduce ground bounce

### Compatibility
- **Forward Compatible:** Can connect to standard 2.54mm JTAG via adapter
- **Common Use:** Modern embedded systems, space-constrained designs
- **SWD Support:** When using pins 2, 4, 6 for SWDIO, SWCLK, SWO (ARM CoreSight)

## Pin Mapping from Standard ARM 20-pin (2.54mm)
The 1.27mm version uses identical pinout to the 2.54mm version, only the physical pitch differs:

| Signal  | 2.54mm Pin | 1.27mm Pin |
|---------|------------|------------|
| VTref   | 1          | 1          |
| nTRST   | 3          | 3          |
| TDI     | 5          | 5          |
| TMS     | 7          | 7          |
| TCK     | 9          | 9          |
| RTCK    | 11         | 11         |
| TDO     | 13         | 13         |
| nRESET  | 15         | 15         |
| GND     | Even pins  | Even pins  |

## Design Recommendations

### For Passive Adapter
1. Use 10kΩ pull-up resistor networks (4x or 5x)
2. Place pull resistors close to connector
3. Add test points for VTref and key signals
4. Use 0603 or 0805 resistor packages for easy hand assembly
5. Add mounting holes for mechanical stability

### PCB Layout
- Keep all JTAG traces short and equal length where possible
- Use ground plane on both sides of board
- Place decoupling capacitor (100nF) near VTref pin
- Route signals on one layer, ground plane on other
- Avoid routing under connector if possible

## Common Issues and Troubleshooting

### Connection Problems
- **No VTref detected:** Check target board is powered
- **Communication fails:** Verify TMS and TCK signals with oscilloscope
- **Intermittent connection:** Check cable seating, inspect for bent pins
- **Target won't reset:** Check nRESET pull-up and target circuit

### Electrical Issues
- **Signal ringing:** Add series resistors (33Ω-47Ω)
- **False triggering:** Ensure proper pull-ups on TMS, TDI
- **Slow operation:** Check RTCK if using adaptive clocking

## References
- ARM Debug Interface Architecture Specification (ADIv5)
- ARM CoreSight Architecture Specification
- JTAG (IEEE 1149.1) Standard
- Segger J-Link / J-Trace User Guide
