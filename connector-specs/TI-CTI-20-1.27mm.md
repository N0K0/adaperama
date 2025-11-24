# TI CTI-20 JTAG Connector (1.27mm pitch)

## Overview
The TI CTI-20 (Compact JTAG Interface - 20 pin) connector is Texas Instruments' compact JTAG debugging interface used with XDS debug probes. It features a 1.27mm pitch and includes TI-specific EMU (emulation) pins for enhanced debugging capabilities on TI processors.

## Physical Specifications
- **Connector Type:** 2x10 pin header
- **Pitch:** 1.27mm (0.05")
- **Pin Count:** 20 pins
- **Orientation:** 2 rows of 10 pins
- **Keying:** Often uses shrouded connectors or pin removal

## Common Part Numbers
- Samtec: FTSH-110-01-L-DV-K (vertical)
- Samtec: FTSH-110-01-L-DV-K-TR (tape and reel)
- CNC Tech: 3220-10-0300-00 (with strain relief)
- Amphenol: 20021121-00010T1LF (low profile)

## Pinout

### Signal Table
| Pin | Signal       | Pin | Signal | Description                           |
|-----|--------------|-----|--------|---------------------------------------|
| 1   | TMS          | 2   | GND    | Test Mode Select                      |
| 3   | TDI          | 4   | GND    | Test Data In                          |
| 5   | TDO          | 6   | GND    | Test Data Out                         |
| 7   | TCK          | 8   | GND    | Test Clock                            |
| 9   | nTRST        | 10  | GND    | Test Reset (active low)               |
| 11  | nSRST        | 12  | GND    | System Reset (active low)             |
| 13  | EMU0         | 14  | GND    | Emulation Pin 0 (TI-specific)         |
| 15  | EMU1         | 16  | GND    | Emulation Pin 1 (TI-specific)         |
| 17  | EMU2/TDO_EN  | 18  | GND    | Emulation Pin 2 / TDO Enable          |
| 19  | EMU3         | 20  | GND    | Emulation Pin 3 (TI-specific)         |

### Pin Diagram (Top View)
```
 ╔═══════════════════════╗
 ║  1  3  5  7  9 11 13 15 17 19  ║ Odd pins (signals)
 ║  2  4  6  8 10 12 14 16 18 20  ║ Even pins (all GND)
 ╚═══════════════════════╝
```

## Electrical Specifications

### Voltage Levels
- **VTref Range:** 1.2V to 5.0V (typically 1.8V or 3.3V)
- **VTref Sensing:** Usually sensed separately from the 20-pin connector
- **Signal Levels:** All signals match target I/O voltage
- **I/O Type:** CMOS/TTL compatible
- **Maximum Current per Pin:** 4-8mA (typical)

### Pull Resistor Requirements
| Signal  | Pull Direction | Resistance | Required? | Notes                              |
|---------|----------------|------------|-----------|------------------------------------|
| TMS     | Pull-up        | 4.7kΩ-10kΩ | Yes       | Critical for proper operation      |
| TDI     | Pull-up        | 4.7kΩ-10kΩ | Yes       | Prevents floating inputs           |
| nTRST   | Pull-up        | 4.7kΩ-10kΩ | Yes       | Required by most TI devices        |
| nSRST   | Pull-up        | 4.7kΩ-10kΩ | Yes       | Prevents spurious resets           |
| TCK     | Pull-down      | 4.7kΩ-10kΩ | Optional  | Keeps clock low when idle          |
| TDO     | None           | -          | No        | Driven by target                   |
| EMU0-3  | Pull-up        | 4.7kΩ-10kΩ | Recommended| Target/processor dependent         |

### Series Resistors (Recommended)
- **Value:** 33Ω - 47Ω on all signal lines
- **Purpose:** Current limiting, signal integrity, ESD protection
- **Placement:** Near connector on adapter board

## Signal Descriptions

### Standard JTAG Signals
- **TCK (Test Clock):** Clock for JTAG operations, driven by debugger
- **TMS (Test Mode Select):** Controls JTAG state machine
- **TDI (Test Data In):** Serial data to target
- **TDO (Test Data Out):** Serial data from target
- **nTRST (Test Reset):** Resets JTAG TAP controller (active low)
- **nSRST (System Reset):** Resets target system (active low)

### TI-Specific EMU Signals
The EMU (emulation) pins provide additional debugging and control features:

- **EMU0:** Multi-purpose emulation signal
  - Real-time breakpoint signal
  - Can trigger external events
  - Processor dependent functionality

- **EMU1:** Multi-purpose emulation signal
  - Real-time trace signal
  - Event counter
  - Processor dependent functionality

- **EMU2/TDO_EN:** Dual purpose
  - Emulation signal (some processors)
  - TDO buffer enable control
  - Used to tri-state TDO when needed

- **EMU3:** Additional emulation signal
  - Processor specific features
  - May be NC on some targets

### EMU Pin Usage by Processor Family
| Processor Family | EMU0        | EMU1        | EMU2        | EMU3    |
|------------------|-------------|-------------|-------------|---------|
| C2000           | RTDX        | RTDX        | TDO_EN      | NC      |
| C5000           | BIO         | DX          | CLKMD       | NC      |
| C6000           | RTDXCLK     | RTDX        | TDO_EN      | NC      |
| MSP430          | TEST/SBWTCK | RST/SBWTDIO | NC          | NC      |
| ARM (Sitara)    | EMU0        | EMU1        | NC          | NC      |

## VTref Considerations

Unlike ARM 20-pin connectors, the TI CTI-20 does NOT include VTref on the 20-pin connector. VTref is typically:
1. Sensed on a separate pin on the debug probe connector
2. Provided via the target board's dedicated VTref connection
3. Configured manually in the debugger software

**For adapter design:** Include a VTref sense wire separate from the 20-pin connector, or document that VTref must be configured manually.

## Pin Mapping from ARM 20-pin JTAG

### Signal Correspondence
| Signal  | ARM 20-pin (2.54mm) | TI CTI-20 (1.27mm) | Notes                    |
|---------|---------------------|--------------------|--------------------------|
| TMS     | Pin 7               | Pin 1              | Direct mapping           |
| TDI     | Pin 5               | Pin 3              | Direct mapping           |
| TDO     | Pin 13              | Pin 5              | Direct mapping           |
| TCK     | Pin 9               | Pin 7              | Direct mapping           |
| nTRST   | Pin 3               | Pin 9              | Direct mapping           |
| nRESET  | Pin 15              | Pin 11             | nSRST on TI              |
| VTref   | Pin 1               | (separate)         | Not on CTI-20 connector  |
| RTCK    | Pin 11              | N/A                | Not used on TI           |
| EMU0-3  | N/A                 | Pins 13,15,17,19   | TI-specific additions    |
| GND     | Even pins           | Even pins          | All even pins            |

## Usage Notes

### As Adapter Output
When using this connector as an output on a JTAG adapter:

1. **Required Connections:**
   - All standard JTAG signals (TMS, TDI, TDO, TCK, nTRST, nSRST)
   - Ground on all even pins
   - Pull-ups on TMS, TDI, nTRST, nSRST (4.7kΩ recommended)

2. **EMU Signals:**
   - Can be left unconnected if only basic JTAG is needed
   - Should be connected through for full TI debugging features
   - Add pull-ups (4.7kΩ) if connecting EMU signals

3. **VTref Handling:**
   - Provide separate VTref connection point
   - Label clearly that VTref is NOT on the 20-pin connector
   - Alternative: Document required debugger configuration

4. **Series Resistors:**
   - 33Ω on all signal lines recommended
   - Protects against shorts and improves signal integrity

### Cable Considerations
- Maximum cable length: 150mm recommended for speeds up to 10MHz
- Use ribbon cable with ground every other conductor
- Shield cable in high-EMI environments
- Twisted pair for critical signals (TCK/TMS) in long cables

### Target Board Requirements
TI target boards using CTI-20 must:
- Provide VTref to the debug probe (separate connection)
- Include pull-ups on TMS, TDI, nTRST (if not on adapter)
- Connect appropriate EMU signals based on processor requirements
- Provide solid ground connection

## Compatibility

### Debug Probe Compatibility
- **TI XDS Series:** XDS100v3, XDS110, XDS200, XDS560v2
- **Spectrum Digital:** DSK and EVM boards
- **Third Party:** Various TI-compatible debuggers

### Processor Compatibility
This connector is primarily used with:
- TI C2000 (Piccolo, Delfino, etc.)
- TI C5000 DSPs
- TI C6000 DSPs
- TI MSP430 (with SBW on EMU pins)
- TI Sitara ARM processors
- TI OMAP processors

## Design Recommendations

### For Passive Adapter
1. Use resistor networks for clean layout:
   - 5x10kΩ network for JTAG pull-ups (TMS, TDI, nTRST, nSRST, +spare)
   - 4x47Ω network for series resistors on main signals
2. Place resistors on adapter board, not target
3. Include test points for debugging
4. Add LED indicator on TCK for activity indication (optional)

### PCB Layout
- Keep JTAG signal traces short (<100mm if possible)
- Match trace lengths for TCK and TMS (critical pair)
- Use ground plane on bottom layer
- Place 100nF decoupling capacitor near connector
- Route EMU signals away from JTAG signals if possible

### Labeling
- Clearly mark "TI CTI-20" to avoid confusion with ARM connectors
- Label Pin 1 with square pad or marking
- Note that VTref is NOT included on this connector
- Mark EMU signals if connector is for TI-specific use

## Common Issues and Troubleshooting

### Connection Problems
- **Debugger doesn't detect target:** Check VTref is provided separately
- **Communication fails:** Verify TMS, TCK signals, check pull-ups
- **Works with ARM but not TI:** Pin mapping is different - check adapter wiring
- **EMU features don't work:** Verify EMU pin connections and processor requirements

### Electrical Issues
- **Signal integrity problems:** Add/check series resistors (33Ω-47Ω)
- **False triggers:** Ensure pull-ups on TMS, TDI (4.7kΩ recommended)
- **Cannot reset target:** Check nSRST pull-up and target reset circuit

### Design Issues
- **Wrong connector type:** Verify 1.27mm pitch, not 2.54mm
- **Pin 1 orientation:** Check pinout diagram, easy to reverse
- **Missing VTref:** Remember to provide VTref sensing separately

## References
- TI Debug Probe Connector Specifications
- TI XDS Target Connection Guide
- Code Composer Studio Debug Probe documentation
- IEEE 1149.1 JTAG Standard
- Processor-specific Technical Reference Manuals for EMU pin definitions
