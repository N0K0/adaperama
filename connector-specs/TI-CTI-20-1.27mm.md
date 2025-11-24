# TI CTI-20 JTAG Connector (1.27mm pitch)

## Overview
The TI CTI-20 (Compact JTAG Interface - 20 pin) connector is Texas Instruments' compact debugging interface used with XDS debug probes. It supports both SWD (Serial Wire Debug) and JTAG modes through dual-function pins, features a 1.27mm pin pitch with 2.54mm row spacing, and includes TI-specific EMU (emulation) pins for enhanced debugging capabilities on TI processors. The connector includes VTref for voltage sensing and RTCK for adaptive clocking support.

## Physical Specifications
- **Connector Type:** 2x10 pin header (dual row)
- **Pin Pitch:** 1.27mm (0.05") - along each row
- **Row Pitch:** 2.54mm (0.1") - between the two rows
- **Pin Count:** 20 pins
- **Orientation:** 2 rows of 10 pins
- **Keying:** Pin 6 is KEY (mechanically keyed, no electrical connection)

## Common Part Numbers
- Samtec: FTSH-110-01-L-DV-K (vertical)
- Samtec: FTSH-110-01-L-DV-K-TR (tape and reel)
- CNC Tech: 3220-10-0300-00 (with strain relief)
- Amphenol: 20021121-00010T1LF (low profile)

## Pinout

### Signal Table
| Pin | Signal       | Pin | Signal     | Description                           |
|-----|--------------|-----|------------|---------------------------------------|
| 1   | SWDIO/TMS    | 2   | nTRST      | SWD Data / Test Mode Select           |
| 3   | TDI          | 4   | TDIS       | Test Data In / TDI State              |
| 5   | VTref        | 6   | KEY        | Target Reference Voltage / Mech. Key  |
| 7   | SWO/TDO      | 8   | GND        | SWO Trace / Test Data Out             |
| 9   | RTCK         | 10  | GND        | Return Test Clock                     |
| 11  | SWCLK/TCK    | 12  | GND        | SWD Clock / Test Clock                |
| 13  | EMU0         | 14  | GND        | Emulation Pin 0 (TI-specific)         |
| 15  | nRESET       | 16  | GND        | System Reset (active low)             |
| 17  | EMU2         | 18  | EMU3       | Emulation Pin 2 / Emulation Pin 3     |
| 19  | EMU4         | 20  | GND        | Emulation Pin 4 (TI-specific)         |

### Pin Diagram (Top View)
```
 ╔════════════════════════════╗
 ║  1  3  5  7  9 11 13 15 17 19  ║ Odd pins (mixed signals)
 ║  2  4  6  8 10 12 14 16 18 20  ║ Even pins (mixed signals/GND)
 ╚════════════════════════════╝
```

## Electrical Specifications

### Voltage Levels
- **VTref Range:** 1.2V to 5.0V (typically 1.8V or 3.3V)
- **VTref Sensing:** Usually sensed separately from the 20-pin connector
- **Signal Levels:** All signals match target I/O voltage
- **I/O Type:** CMOS/TTL compatible
- **Maximum Current per Pin:** 4-8mA (typical)

### Pull Resistor Requirements
| Signal       | Pull Direction | Resistance | Required?   | Notes                              |
|--------------|----------------|------------|-------------|------------------------------------|
| SWDIO/TMS    | Pull-up        | 10kΩ       | Yes         | Critical for proper operation      |
| TDI          | Pull-up        | 10kΩ       | Yes         | Prevents floating inputs           |
| nTRST        | Pull-up        | 10kΩ       | Yes         | Required by most TI devices        |
| nRESET       | Pull-up        | 10kΩ       | Yes         | Prevents spurious resets           |
| SWCLK/TCK    | None           | -          | Optional    | Can add pull-down if needed        |
| SWO/TDO      | None           | -          | No          | Driven by target                   |
| TDIS         | Varies         | 10kΩ       | Target-dep. | Check target requirements          |
| EMU0,2,3,4   | Pull-up        | 10kΩ       | Recommended | Target/processor dependent         |

### Series Resistors (Recommended)
- **Value:** 33Ω - 47Ω on all signal lines
- **Purpose:** Current limiting, signal integrity, ESD protection
- **Placement:** Near connector on adapter board

## Signal Descriptions

### Dual-Function Debug Signals (SWD/JTAG)
This connector supports both SWD (Serial Wire Debug) and JTAG modes:

- **SWDIO/TMS (Pin 1):**
  - SWD mode: Bidirectional data signal
  - JTAG mode: Test Mode Select (controls JTAG state machine)

- **SWCLK/TCK (Pin 11):**
  - SWD mode: Serial Wire Clock
  - JTAG mode: Test Clock

- **SWO/TDO (Pin 7):**
  - SWD mode: Serial Wire Output (trace data)
  - JTAG mode: Test Data Out (serial data from target)

### JTAG-Only Signals
- **TDI (Pin 3):** Test Data In - Serial data to target (JTAG mode only)
- **TDIS (Pin 4):** TDI State - Control signal for TDI
- **nTRST (Pin 2):** Test Reset (active low) - Resets JTAG TAP controller

### System Control Signals
- **nRESET (Pin 15):** System Reset (active low) - Resets target system
- **RTCK (Pin 9):** Return Test Clock - Adaptive clocking support

### TI-Specific EMU Signals
The EMU (emulation) pins provide additional debugging and control features. This connector provides EMU0, EMU2, EMU3, and EMU4 (note: no EMU1):

- **EMU0 (Pin 13):** Multi-purpose emulation signal
  - Real-time breakpoint signal
  - Can trigger external events
  - Cross-core triggering
  - Processor dependent functionality

- **EMU2 (Pin 17):** Emulation signal
  - Processor specific features
  - May function as TDO enable on some devices
  - Cross-triggering support

- **EMU3 (Pin 18):** Emulation signal
  - Advanced debugging features
  - Processor dependent functionality
  - May be NC on some targets

- **EMU4 (Pin 19):** Emulation signal
  - Extended debugging capabilities
  - Processor specific features
  - May be NC on some targets

### EMU Pin Usage by Processor Family
| Processor Family | EMU0        | EMU2        | EMU3        | EMU4    |
|------------------|-------------|-------------|-------------|---------|
| C2000           | RTDX        | TDO_EN      | Cross-trig  | NC      |
| C5000           | BIO         | CLKMD       | Cross-trig  | NC      |
| C6000           | RTDXCLK     | TDO_EN      | Cross-trig  | NC      |
| MSP430          | TEST/SBWTCK | NC          | NC          | NC      |
| ARM (Sitara)    | EMU0        | EMU2        | EMU3        | EMU4    |

## VTref and Power Considerations

**VTref (Pin 5):** Target reference voltage
- This pin senses the target board's I/O voltage level (typically 1.8V, 3.3V, or 5V)
- All debug signals operate at this voltage level
- Supplied BY the target board TO the debugger
- Used to ensure proper signal level translation
- Never drive voltage into this pin - it's an input to the debugger

**KEY (Pin 6):** Mechanical keying
- Used for connector polarization to prevent incorrect insertion
- No electrical connection
- May be implemented as a missing pin or keyed shroud

## Pin Mapping from ARM 20-pin JTAG

### Signal Correspondence
| Signal       | ARM 20-pin (2.54mm) | TI CTI-20 (1.27mm) | Notes                         |
|--------------|---------------------|--------------------|-------------------------------|
| TMS          | Pin 7               | Pin 1              | Dual-function SWDIO/TMS       |
| TDI          | Pin 5               | Pin 3              | Direct mapping                |
| TDO          | Pin 13              | Pin 7              | Dual-function SWO/TDO         |
| TCK          | Pin 9               | Pin 11             | Dual-function SWCLK/TCK       |
| nTRST        | Pin 3               | Pin 2              | Direct mapping                |
| nRESET       | Pin 15              | Pin 15             | Same pin number               |
| VTref        | Pin 1               | Pin 5              | Included in CTI-20            |
| RTCK         | Pin 11              | Pin 9              | Included in CTI-20            |
| TDIS         | N/A                 | Pin 4              | TI-specific TDI state control |
| KEY          | N/A                 | Pin 6              | Mechanical keying             |
| EMU0,2,3,4   | N/A                 | Pins 13,17,18,19   | TI-specific additions         |
| GND          | Even pins           | Pins 8,10,12,14,16,20 | Some even pins only        |

## Usage Notes

### As Adapter Output
When using this connector as an output on a JTAG adapter:

1. **Required Connections:**
   - All dual-function signals: SWDIO/TMS, SWCLK/TCK, SWO/TDO (supports both SWD and JTAG)
   - JTAG-only signals: TDI, TDIS, nTRST
   - System control: nRESET, RTCK
   - Power: VTref (pin 5), GND (pins 8,10,12,14,16,20)
   - KEY: Pin 6 should be mechanically keyed (no connection)
   - Pull-ups on SWDIO/TMS, TDI, nTRST, nRESET (10kΩ to VTref recommended)

2. **EMU Signals:**
   - EMU0, EMU2, EMU3, EMU4 on pins 13, 17, 18, 19
   - Can be left unconnected if only basic JTAG/SWD is needed
   - Should be connected through for full TI debugging features
   - Add pull-ups (10kΩ to VTref) if connecting EMU signals

3. **VTref Handling:**
   - VTref is on Pin 5 of this connector
   - Must be sourced from the target board (never drive from debugger)
   - Used for signal level translation
   - All pull-ups should connect to VTref, not a fixed voltage

4. **Series Resistors:**
   - 33Ω on all signal lines recommended
   - Protects against shorts and improves signal integrity
   - Place near the input connector on adapter board

### Cable Considerations
- Maximum cable length: 150mm recommended for speeds up to 10MHz
- Use ribbon cable with ground every other conductor
- Shield cable in high-EMI environments
- Twisted pair for critical signals (TCK/TMS) in long cables

### Target Board Requirements
TI target boards using CTI-20 must:
- Provide VTref on pin 5 (target voltage reference, typically 1.8V or 3.3V)
- Include pull-ups on SWDIO/TMS, TDI, nTRST, nRESET (if not on adapter/debugger)
- Connect appropriate EMU signals based on processor requirements
- Implement mechanical keying on pin 6 to prevent reverse insertion
- Provide solid ground connections on pins 8, 10, 12, 14, 16, 20
- Support either SWD or JTAG mode (or both) based on processor capabilities

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
