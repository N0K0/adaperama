# ARM 20-pin JTAG Connector (2.54mm pitch)

## Overview
The ARM 20-pin JTAG connector (also known as ARM-JTAG-20) is the standard debugging interface for ARM processors and is used by professional debuggers like Segger J-Link, ARM ULINK, and many others. With its 2.54mm (0.1") pitch, it's compatible with standard IDC ribbon cables and widely available connectors.

## Physical Specifications
- **Connector Type:** 2x10 pin header (dual row)
- **Pitch:** 2.54mm (0.1")
- **Pin Count:** 20 pins
- **Orientation:** 2 rows of 10 pins
- **Keying:** Pin 14 typically removed for mechanical keying
- **Standard:** ARM-JTAG-20, IEC 60603-13

## Common Part Numbers

### Box Headers (Shrouded)
- Samtec: TSW-110-07-G-D (dual row, keyed)
- Samtec: SSW-110-02-G-D-RA (right angle, shrouded)
- Amphenol: 10129378-910002BLF (shrouded)
- 3M: 2540-6002UB (unshrouded)

### Standard Pin Headers
- Sullins: SBH11-PBPC-D10-ST-BK (standard 2x10)
- Harwin: M20-9770346 (dual row)
- Amphenol: 67997-210HLF (through-hole)

### IDC Connectors (for ribbon cables)
- 3M: 3420-6000 (20-pin female IDC socket)
- Amphenol: T812120A101CEU (strain relief)
- TE Connectivity: 1-102202-0 (ribbon cable connector)

### Cables
- Segger: 19-pin ribbon cable (1m)
- ARM: Standard 20-conductor ribbon cable
- Generic: 20-pin IDC flat ribbon cable

## Pinout

### Signal Table
| Pin | Signal       | Pin | Signal      | Description                          |
|-----|--------------|-----|-------------|--------------------------------------|
| 1   | VTref        | 2   | NC/VDD      | Target reference voltage / Power     |
| 3   | nTRST        | 4   | GND         | Test Reset (active low)              |
| 5   | TDI          | 6   | GND         | Test Data In                         |
| 7   | TMS          | 8   | GND         | Test Mode Select                     |
| 9   | TCK          | 10  | GND         | Test Clock                           |
| 11  | RTCK         | 12  | GND         | Return Test Clock                    |
| 13  | TDO          | 14  | GND         | Test Data Out (often keyed)          |
| 15  | nRESET/nSRST | 16  | GND         | System Reset (active low)            |
| 17  | NC           | 18  | GND         | Not Connected (or DBGACK)            |
| 19  | NC/DBGRQ     | 20  | GND         | Debug Request (5V tolerant)          |

### Pin Diagram (Top View)
```
 ╔═══════════════════════════════════════╗
 ║  1   3   5   7   9   11  13  15  17  19  ║ Odd pins
 ║  2   4   6   8  10   12  14  16  18  20  ║ Even pins
 ╚═══════════════════════════════════════╝
    ▲                        ▲
   Pin 1                   Pin 14
 (Square pad)             (removed/key)
```

### Keying
- **Pin 14** is commonly removed on the male connector for keying
- Prevents reverse insertion with shrouded connectors
- Some designs remove pin 2 instead or use plastic key

## Electrical Specifications

### Voltage Levels
- **VTref Range:** 1.2V to 5.0V (most common: 1.8V, 3.3V, 5V)
- **Signal Levels:** All I/O signals match VTref voltage
- **I/O Type:** CMOS/TTL compatible, 5V tolerant on most debuggers
- **Maximum Current per Pin:** 10-20mA typical
- **VTref Current Capability:** 5-10mA (for pull-up resistors)

### Pull Resistor Requirements
| Signal  | Pull Direction | Resistance  | Required?   | Notes                            |
|---------|----------------|-------------|-------------|----------------------------------|
| TMS     | Pull-up        | 10kΩ-47kΩ   | Yes         | MUST have for proper operation   |
| TDI     | Pull-up        | 10kΩ-47kΩ   | Yes         | MUST have to prevent floating    |
| nTRST   | Pull-up        | 4.7kΩ-10kΩ  | Recommended | Many devices require it          |
| nRESET  | Pull-up        | 4.7kΩ-10kΩ  | Recommended | Prevents spurious resets         |
| TCK     | Pull-down      | 10kΩ-47kΩ   | Optional    | Keeps clock low when idle        |
| TDO     | None           | -           | No          | Driven by target device          |
| RTCK    | Pull-up/down   | 10kΩ-47kΩ   | Optional    | Target dependent                 |

### Series Resistors (Protection)
- **Value:** 22Ω - 100Ω on all signal lines
- **Purpose:**
  - Current limiting for short circuit protection
  - Signal integrity (reduces reflections)
  - ESD protection
- **Placement:** Near debugger connector (source end)

## Signal Descriptions

### Core JTAG Signals

**TCK (Test Clock) - Pin 9**
- Clock signal for JTAG operations
- Driven by debugger (output only)
- Typical frequency: 1-10 MHz (up to 50MHz for some debuggers)
- Pull-down prevents noise when disconnected

**TMS (Test Mode Select) - Pin 7**
- Controls JTAG Test Access Port (TAP) state machine
- Driven by debugger
- Must have pull-up (10kΩ minimum) - CRITICAL
- Without pull-up, JTAG will not function

**TDI (Test Data In) - Pin 5**
- Serial data input to target device
- Driven by debugger
- Must have pull-up to prevent floating - CRITICAL
- Data shifted in on rising edge of TCK

**TDO (Test Data Out) - Pin 13**
- Serial data output from target device
- Driven by target (tri-state when not selected)
- No pull resistor needed (actively driven)
- Data valid on falling edge of TCK

**nTRST (Test Reset, Active Low) - Pin 3**
- Asynchronous reset for JTAG TAP controller
- Optional in IEEE 1149.1 but commonly used
- Pull-up required on most targets
- Some debuggers can drive this, others leave it floating

### System Control Signals

**nRESET/nSRST (System Reset, Active Low) - Pin 15**
- Resets the entire target system
- Open-drain output from debugger (can be driven by target too)
- Pull-up required (typically 4.7kΩ-10kΩ)
- Used for "connect under reset" scenarios
- May be labeled nSRST (System Reset) or nRST

**VTref (Target Reference Voltage) - Pin 1**
- Provided by target board (target powers this pin)
- Debugger uses this to set I/O voltage levels
- Should be decoupled with 100nF ceramic capacitor
- Current draw: typically 1-5mA for level shifters
- CRITICAL: Must be present for debugger to function

**RTCK (Return Test Clock) - Pin 11**
- Return clock for adaptive clocking mode
- Used with slow or variable-speed targets
- Target echoes TCK back to debugger
- Allows debugger to synchronize with target speed
- Not used by most modern targets (can be left unconnected)

### Optional/Extended Signals

**Pin 2: NC/VDD**
- Not Connected on standard ARM JTAG-20
- Some implementations provide power (VDD) to target
- Typically 3.3V or 5V if implemented
- Check debugger documentation before use

**Pin 19: NC/DBGRQ (Debug Request)**
- Not used in standard configurations
- Some ARM7/ARM9 systems use for debug request
- Can request processor to enter debug mode
- Often left unconnected on modern designs

**Pin 17: NC/DBGACK**
- Not Connected in standard implementation
- Some implementations use for Debug Acknowledge
- Indicates processor has entered debug mode
- Rarely used with modern debuggers

## Pin Mapping to Other Connectors

### To ARM 20-pin 1.27mm
Direct 1:1 mapping - same pin numbers, only physical pitch differs

### To Cortex 10-pin
| 20-pin Signal | 20-pin Pin | 10-pin Signal | 10-pin Pin |
|---------------|------------|---------------|------------|
| VTref         | 1          | VTref         | 1          |
| TMS           | 7          | SWDIO/TMS     | 2          |
| TCK           | 9          | SWCLK/TCK     | 4          |
| TDO           | 13         | SWO/TDO       | 6          |
| TDI           | 5          | TDI           | 8          |
| nRESET        | 15         | nRESET        | 10         |
| GND           | Even pins  | GND           | 3, 5, 9    |

**Not present on 10-pin:** nTRST, RTCK, DBGRQ

### To TI CTI-20
| 20-pin ARM Signal | 20-pin Pin | TI CTI-20 Signal | TI CTI-20 Pin |
|-------------------|------------|------------------|---------------|
| TMS               | 7          | TMS              | 1             |
| TDI               | 5          | TDI              | 3             |
| TDO               | 13         | TDO              | 5             |
| TCK               | 9          | TCK              | 7             |
| nTRST             | 3          | nTRST            | 9             |
| nRESET            | 15         | nSRST            | 11            |
| VTref             | 1          | (separate)       | -             |

**TI CTI-20 additional signals:** EMU0-3 (not present on ARM 20-pin)

## Usage Notes

### As Input from J-Link Debugger
When using this connector to receive signals from a J-Link or similar debugger via ribbon cable:

1. **Ribbon Cable Connection:**
   - Use standard 20-conductor IDC ribbon cable
   - Pin 1 marked with red stripe on ribbon cable
   - Verify orientation carefully (easy to reverse!)
   - Maximum length: 150mm recommended, 300mm maximum

2. **Signal Considerations:**
   - All signals driven by debugger (J-Link)
   - Pull resistors typically on target board, NOT on cable
   - For adapter board: terminate cable with IDC connector
   - No passive components needed on input side of adapter

3. **Protection (Optional):**
   - Series resistors (33Ω) can be added for protection
   - ESD protection diodes for production designs
   - Generally not critical for lab/development use

4. **Critical Connections:**
   - VTref MUST be connected (provides voltage reference)
   - All even-numbered GND pins should be connected
   - Core JTAG: TMS, TCK, TDI, TDO must be present
   - nRESET recommended for most use cases

### Cable Assembly
- **IDC Crimping:** Use IDC tool to crimp connectors onto ribbon cable
- **Pin 1 Alignment:** Red stripe indicates pin 1 conductor
- **Strain Relief:** Use connectors with strain relief for reliability
- **Cable Testing:** Verify continuity before connecting expensive equipment

### Common Configurations

**Minimal JTAG (4-wire + ground):**
- Pins 1 (VTref), 7 (TMS), 9 (TCK), 5 (TDI), 13 (TDO)
- All even pins (GND)
- Pull-ups on TMS, TDI (target side)

**Standard JTAG:**
- Above + Pin 3 (nTRST), Pin 15 (nRESET)
- Pull-ups on nTRST, nRESET (target side)

**Full Featured:**
- All signals including RTCK, DBGRQ
- Rarely needed for modern designs

## Compatibility

### Debugger Compatibility
This connector is the standard interface for:
- **Segger J-Link:** All models (BASE, PLUS, ULTRA+, PRO)
- **ARM ULINK:** ULINK2, ULINKplus, ULINKpro
- **Lauterbach:** TRACE32 debug probes
- **IAR I-jet:** I-jet and I-jet Trace
- **PEmicro:** Multilink debug probes
- **OpenOCD Compatible:** Many USB-JTAG adapters

### Target Compatibility
Used with:
- **ARM7/ARM9:** Classic ARM processors (ARM7TDMI, ARM920T, ARM926EJ-S)
- **ARM Cortex-A:** Application processors (via JTAG mode)
- **ARM Cortex-M:** Microcontrollers (via JTAG, though SWD more common now)
- **ARM Cortex-R:** Real-time processors
- **FPGA:** Many FPGAs support JTAG via this connector
- **Multi-device JTAG chains:** Daisy-chain multiple devices

## Design Recommendations

### For Adapter Input (from J-Link)

1. **Connector Selection:**
   - Use shrouded box header (prevents reverse insertion)
   - Key by removing pin 14
   - Through-hole for strength, or SMT with mounting pegs
   - Locking type (ejector latch) for secure connection

2. **PCB Layout:**
   - Pin 1 marked with square pad and silkscreen
   - All even pins connected to ground plane
   - Short traces from connector to next stage
   - No pull resistors needed on input side
   - Optional: Series resistors (33Ω) for protection

3. **Mechanical:**
   - Secure mounting (through-hole preferred)
   - Strain relief if using fixed cable
   - Adequate clearance around connector for cable bend radius

4. **Testing:**
   - Test points on critical signals (VTref, TMS, TCK)
   - LED indicator on VTref (optional, shows target power)
   - Ground test point

### Signal Integrity Considerations

**For Standard Speeds (<10MHz):**
- Standard FR-4 PCB is fine
- Basic ground plane sufficient
- Ribbon cable up to 300mm OK
- No special impedance control needed

**For High Speeds (>10MHz):**
- Controlled impedance (50Ω single-ended or 100Ω differential)
- Shorter cable (<150mm)
- Minimize stubs and discontinuities
- Use twisted-pair or shielded cable

## Common Issues and Troubleshooting

### Connection Problems

**Debugger doesn't detect target:**
- Check VTref is present (measure Pin 1)
- Verify ribbon cable orientation (Pin 1 alignment)
- Check all GND connections
- Ensure target board is powered

**JTAG communication fails:**
- Verify TMS has pull-up resistor (critical!)
- Check TDI has pull-up resistor
- Measure TCK signal with oscilloscope
- Reduce JTAG clock speed in debugger software

**Intermittent connection:**
- Check IDC connector crimps
- Inspect for bent pins
- Verify cable seating in connector
- Check for broken conductors in ribbon cable

### Electrical Issues

**High-speed communication errors:**
- Reduce JTAG clock frequency
- Shorten cable length
- Add series resistors (33Ω-47Ω)
- Check for ground loops

**Target resets unexpectedly:**
- Verify nRESET pull-up resistor
- Check for shorts on nRESET line
- Disable debugger "reset on connect" if not needed

**Signal reflections/ringing:**
- Add series resistors (47Ω-100Ω)
- Ensure proper grounding
- Check cable quality
- Reduce trace lengths

### Mechanical Issues

**Cable keeps disconnecting:**
- Use shrouded/keyed connector
- Add locking IDC connectors
- Ensure proper IDC crimp
- Use strain relief

**Reversed cable connection:**
- Always use keyed/shrouded connectors
- Mark Pin 1 clearly on both ends
- Use red stripe conductor for Pin 1
- Double-check before connecting

## Adapters and Accessories

### 20-pin to 10-pin Adapter
Converts ARM 20-pin (2.54mm) to Cortex 10-pin (1.27mm):
- Segger: 8.06.10 (official adapter)
- Generic: Many third-party available
- DIY: Simple PCB project

### Ribbon Cable Lengths
- **Standard:** 150mm (best signal integrity)
- **Long:** 300mm (acceptable for most uses)
- **Custom:** Can make any length, but signal quality degrades

### IDC Assembly
- **Tools:** IDC crimp tool (or bench vise for careful work)
- **Cable:** 20-conductor 1.27mm pitch ribbon cable
- **Connectors:** 2x20 IDC socket with strain relief

## References
- IEEE 1149.1 JTAG Standard (ANSI/IEEE Std 1149.1)
- ARM Debug Interface Architecture Specification (ADIv5)
- Segger J-Link / J-Trace User Guide
- ARM Application Note 205: JTAG Debugging
- IEC 60603-13 Connector Standard
