# ARM Cortex Debug Connector (10-pin, 1.27mm pitch)

## Overview
The ARM Cortex Debug 10-pin connector (also called Cortex Debug+ETM connector or simply "ARM 10-pin") is the modern standard for ARM Cortex-M and Cortex-A debugging. It combines JTAG and Serial Wire Debug (SWD) functionality in a compact 10-pin, 1.27mm pitch connector. This is now the most common debug connector on modern ARM development boards.

## Physical Specifications
- **Connector Type:** 2x5 pin header
- **Pitch:** 1.27mm (0.05")
- **Pin Count:** 10 pins
- **Orientation:** 2 rows of 5 pins
- **Keying:** Pin 7 typically removed or plastic key tab

## Common Part Numbers

### Vertical (Through-Hole)
- Samtec: FTSH-105-01-L-DV-K (keyed)
- Samtec: FTSH-105-01-L-DV-007-K (keyed, pin 7 removed)
- Harwin: M50-3600542 (keyed)
- CNC Tech: 3220-10-0200-00

### Surface Mount
- Samtec: FTSH-105-01-L-DV-K-P (with PCB retention posts)
- Tag-Connect: TC2050-IDC (cable with spring-loaded pins)
- Tag-Connect: TC2050-IDC-NL (cable, no retention legs)

### Cables and Accessories
- Segger: 6.02.10 (10-pin Cortex cable)
- Segger: 8.06.10 (adapter 20-pin to 10-pin)
- Tag-Connect: TC2050 series (no-connector pogo-pin solution)

## Pinout

### Signal Table
| Pin | Signal       | Pin | Signal       | Description                          |
|-----|--------------|-----|--------------|--------------------------------------|
| 1   | VTref        | 2   | SWDIO/TMS    | Target voltage ref / SWD Data IO     |
| 3   | GND          | 4   | SWCLK/TCK    | Ground / SWD Clock                   |
| 5   | GND          | 6   | SWO/TDO      | Ground / Serial Wire Output          |
| 7   | KEY (NC)     | 8   | TDI/NC       | Keying pin / Test Data In            |
| 9   | GNDDetect    | 10  | nRESET       | Ground Detect / System Reset         |

### Pin Diagram (Top View)
```
 ╔═══════════════╗
 ║  1  3  5  7  9  ║
 ║  2  4  6  8 10  ║
 ╚═══════════════╝
    ▲
   Pin 1
   (Square pad)
```

### Alternative Pin Labeling (Signal-Centric)
Some documentation uses signal names directly:

| Pin | Primary Name | JTAG Mode | SWD Mode    |
|-----|--------------|-----------|-------------|
| 1   | VTref        | VTref     | VTref       |
| 2   | SWDIO/TMS    | TMS       | SWDIO       |
| 3   | GND          | GND       | GND         |
| 4   | SWCLK/TCK    | TCK       | SWCLK       |
| 5   | GND          | GND       | GND         |
| 6   | SWO/TDO      | TDO       | SWO (UART)  |
| 7   | KEY          | NC        | NC          |
| 8   | TDI          | TDI       | NC          |
| 9   | GNDDetect    | GND       | GND         |
| 10  | nRESET       | nRESET    | nRESET      |

## Electrical Specifications

### Voltage Levels
- **VTref Range:** 1.2V to 5.0V (typically 1.8V or 3.3V)
- **Signal Levels:** All I/O matches VTref
- **I/O Type:** CMOS compatible
- **Maximum Current per Pin:** 10mA typical

### Pull Resistor Requirements

#### JTAG Mode
| Signal  | Pull Direction | Resistance | Required?   | Notes                          |
|---------|----------------|------------|-------------|--------------------------------|
| TMS     | Pull-up        | 10kΩ-100kΩ | Yes         | Essential for JTAG operation   |
| TDI     | Pull-up        | 10kΩ-100kΩ | Recommended | Prevents floating              |
| TDO     | None           | -          | No          | Driven by target               |
| TCK     | Pull-down      | 10kΩ-100kΩ | Optional    | Keeps clock idle               |
| nRESET  | Pull-up        | 10kΩ       | Yes         | Prevents spurious resets       |

#### SWD Mode (Most Common)
| Signal  | Pull Direction | Resistance | Required?   | Notes                          |
|---------|----------------|------------|-------------|--------------------------------|
| SWDIO   | Pull-up        | 10kΩ-100kΩ | Yes         | Bidirectional, needs pull-up   |
| SWCLK   | Pull-down      | 10kΩ-100kΩ | Optional    | Keeps clock idle               |
| SWO     | None           | -          | No          | UART output from target        |
| nRESET  | Pull-up        | 10kΩ       | Yes         | Prevents spurious resets       |

**Note:** ARM recommends 100kΩ pull resistors, but 10kΩ-47kΩ commonly used for more robust signaling.

### Series Resistors (Optional Protection)
- **Value:** 22Ω - 47Ω on signal lines
- **Purpose:** Short circuit protection, signal integrity
- **Typical placement:** On adapter board or debugger

## Signal Descriptions

### Dual-Protocol Signals

**Pin 2: SWDIO/TMS**
- **JTAG Mode (TMS):** Test Mode Select, controls TAP state machine
- **SWD Mode (SWDIO):** Bidirectional data line for SWD protocol
- Always requires pull-up resistor

**Pin 4: SWCLK/TCK**
- **JTAG Mode (TCK):** Test clock for JTAG
- **SWD Mode (SWCLK):** Clock for SWD protocol
- Driven by debugger in both modes

**Pin 6: SWO/TDO**
- **JTAG Mode (TDO):** Test Data Out from target
- **SWD Mode (SWO):** Serial Wire Output - UART trace data from target
- SWO typically runs at SWCLK/2 to SWCLK/32 for trace data

**Pin 8: TDI/NC**
- **JTAG Mode (TDI):** Test Data In to target
- **SWD Mode:** Not connected (SWD only uses 2 data pins)
- May be left unconnected on adapter for SWD-only use

### Common Signals

**Pin 1: VTref (Target Voltage Reference)**
- Provided by target board
- Debugger uses this to set I/O levels
- Should be decoupled with 100nF capacitor
- Typical values: 1.8V, 2.5V, 3.3V, 5V

**Pin 10: nRESET (System Reset, Active Low)**
- Can be driven by debugger to reset target
- Should have pull-up on target board
- Open-drain output from debugger
- Used for "connect under reset" scenarios

**Pin 9: GNDDetect**
- Allows debugger to detect cable connection
- Tied to ground on target
- Some debuggers use this to sense target presence

**Pin 7: KEY (Keying Pin)**
- Mechanical keying only
- Not connected electrically
- May be pin removed or plastic key

**Pins 3, 5, 9: GND**
- Multiple ground pins reduce ground bounce
- Provide solid return path for high-speed signals
- Connect all to ground plane

## Operating Modes

### SWD Mode (Serial Wire Debug)
Most common mode for ARM Cortex-M devices:
- **Active Signals:** VTref, SWDIO, SWCLK, nRESET, GND
- **Optional:** SWO for serial trace output
- **Unused:** TDI (pin 8)
- **Advantages:** 2-wire protocol, faster than JTAG, supports CoreSight features
- **Typical Speed:** 1-4 MHz (up to 10MHz+ on some debuggers)

### JTAG Mode
Used for ARM Cortex-A, multi-device JTAG chains, or legacy compatibility:
- **Active Signals:** VTref, TMS, TCK, TDO, TDI, nRESET, GND
- **Unused:** SWO trace (TDO used instead)
- **Advantages:** Industry standard, chain multiple devices, better tool support
- **Typical Speed:** 1-10 MHz

### SWD with SWO Trace
Enhanced debugging with instruction trace:
- **Active Signals:** All SWD signals + SWO
- **SWO Usage:** UART output of trace data (printf, events, PC sampling)
- **Common Baud Rates:** 115200, 2000000, 4000000 bps
- **Note:** SWO often requires separate configuration in debugger

## Pin Mapping from ARM 20-pin JTAG

### 10-pin to 20-pin Correspondence
| 10-pin Signal | 10-pin Pin | 20-pin Signal | 20-pin Pin |
|---------------|------------|---------------|------------|
| VTref         | 1          | VTref         | 1          |
| SWDIO/TMS     | 2          | TMS           | 7          |
| GND           | 3, 5, 9    | GND           | Even pins  |
| SWCLK/TCK     | 4          | TCK           | 9          |
| SWO/TDO       | 6          | TDO           | 13         |
| TDI           | 8          | TDI           | 5          |
| nRESET        | 10         | nRESET        | 15         |

**Signals NOT on 10-pin connector:**
- nTRST (20-pin pin 3) - not needed for modern ARM
- RTCK (20-pin pin 11) - adaptive clocking not used with SWD
- DBGRQ (20-pin pin 19) - rarely used

## Usage Notes

### As Adapter Output
When using this connector as an output on a JTAG adapter:

1. **Minimal SWD Configuration:**
   - Connect: VTref, SWDIO, SWCLK, nRESET, GND
   - Pull-ups: SWDIO (10kΩ), nRESET (10kΩ)
   - Optional: SWO for trace
   - Leave TDI (pin 8) unconnected

2. **Full JTAG Configuration:**
   - Connect all signals including TDI
   - Pull-ups: TMS (10kΩ), TDI (10kΩ), nRESET (10kΩ)
   - Pull-down: TCK (10kΩ) optional

3. **Protection:**
   - Series resistors (33Ω) on all signals recommended
   - ESD protection diodes optional but good practice

4. **VTref:**
   - Must be provided by target
   - Add 100nF bypass capacitor on adapter
   - Max current draw: 5mA typical

### Cable Considerations
- **Maximum Length:**
  - Standard cable: 150mm for reliable operation
  - High-quality shielded: up to 300mm
  - Tag-Connect (direct): no cable, best signal integrity
- **Cable Type:**
  - 1.27mm ribbon cable (ground every other conductor)
  - Shielded twisted pair for long cables
- **Strain Relief:** Important due to small connector size

### Common Target Board Designs

**Minimum SWD Target (Most Common):**
```
Target Board:
- VTref from target VDD (with 100nF cap)
- 10kΩ pull-up on SWDIO
- 10kΩ pull-up on nRESET
- Connect SWCLK directly
- Optional: SWO from MCU
- Pin 7 removed or keyed
```

**Full JTAG Target:**
```
Target Board:
- All above, plus:
- 10kΩ pull-up on TDI
- Connect TDO from MCU
```

## Compatibility

### Debugger Compatibility
- **Segger J-Link:** All models (with 10-pin cable or adapter)
- **ARM ULINK:** ULINK2, ULINKplus, ULINKpro
- **ST-Link:** ST-Link/V2, ST-Link/V3 (native connector)
- **CMSIS-DAP:** Many open-source debuggers
- **Tag-Connect:** TC2050 cables work with most debuggers
- **OpenOCD Compatible:** Most USB debug adapters

### Target Compatibility
Widely used on:
- **ARM Cortex-M:** STM32, Nordic nRF, NXP LPC/Kinetis, TI MSP432, Atmel SAM
- **ARM Cortex-A:** Some development boards (less common, often use 20-pin)
- **RISC-V:** Some boards using ARM-compatible debuggers
- **Any JTAG Device:** Via JTAG mode (TMS, TCK, TDO, TDI)

## Design Recommendations

### For Passive Adapter Board

1. **Component Selection:**
   - 2x10kΩ resistor for pull-ups (SWDIO, nRESET)
   - 4x33Ω resistor for series protection (optional)
   - 100nF ceramic capacitor for VTref decoupling

2. **PCB Layout:**
   - Keep all signal traces short (<50mm ideal)
   - Use ground plane on bottom layer
   - Route SWDIO and SWCLK as differential pair if possible
   - Place decoupling cap close to connector (within 5mm)
   - Add test points for VTref, SWDIO, SWCLK, nRESET

3. **Connector Orientation:**
   - Mount connector on top side
   - Pin 1 indicator (square pad)
   - Shrouded connector prevents reverse insertion
   - Silkscreen label: "ARM 10-pin" or "Cortex Debug"

4. **Mounting:**
   - Add mounting holes for mechanical stability
   - Use connector with PCB retention posts if available
   - Consider strain relief for cable

### Labeling and Documentation
- Mark "10-pin ARM Cortex" to avoid confusion with other 10-pin connectors
- Label Pin 1 clearly
- Note SWD/JTAG mode selection if switchable
- Include pinout diagram on silkscreen (if space permits)

## Common Issues and Troubleshooting

### Connection Problems
- **Debugger can't connect:**
  - Verify VTref is present (measure pin 1)
  - Check SWDIO pull-up resistor
  - Ensure target is powered

- **Intermittent connection:**
  - Check cable seating
  - Verify all GND pins connected
  - Inspect for bent pins

- **SWO trace not working:**
  - SWO requires separate configuration in debugger
  - Check SWO baud rate matches debugger setting
  - Verify SWO pin connection on target MCU

### Electrical Issues
- **Communication errors at high speed:**
  - Reduce SWD clock speed
  - Add series resistors (33Ω)
  - Shorten cable length
  - Check for ground loops

- **Target resets unexpectedly:**
  - Check nRESET pull-up resistor
  - Verify nRESET not shorted
  - Check for debugger "reset on connect" setting

- **Wrong pin configuration:**
  - Verify pin 1 orientation (square pad)
  - Check against target board schematic
  - Measure signals with multimeter/oscilloscope

### Mode Selection Issues
- **JTAG mode not working:**
  - Verify TDI (pin 8) is connected
  - Check debugger software set to JTAG mode
  - Ensure target supports JTAG (not all Cortex-M do)

- **SWD mode not working:**
  - Common on adapters - check SWDIO pull-up present
  - Verify debugger set to SWD mode
  - Check SWDIO not damaged (it's bidirectional)

## Tag-Connect Alternative

The Tag-Connect TC2050 is a popular pogo-pin alternative that eliminates the physical connector:

**Advantages:**
- No connector cost or PCB space
- Reliable spring-loaded connection
- Same pinout as Cortex 10-pin
- Available with retention legs or retainer clip

**Considerations:**
- Requires precise footprint on target PCB
- Not suitable for permanent connection
- Excellent for production programming
- Popular for cost-sensitive designs

## References
- ARM Debug Interface Architecture Specification (ADIv5)
- ARM CoreSight Components Technical Reference Manual
- Segger J-Link User Guide
- CMSIS-DAP Specification
- ARM Application Note 290: Implementing SWD
