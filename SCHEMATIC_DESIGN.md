# Adapterama JTAG Converter Pack - Schematic Design

## Overview
This document describes the complete schematic design for the JTAG converter pack adapter board. The board takes J-Link JTAG signals via ribbon cable and provides three different output connectors.

## Design Philosophy
- **Passive adapter:** No active components, no power supply required
- **Simple and reliable:** Using only resistors for pull-ups and series protection
- **Ribbon cable inputs:** Each output has its own ribbon cable input from J-Link
- **Parallel outputs:** All three outputs can be populated simultaneously

## Bill of Materials

### Connectors

| Qty | Reference | Value | Description | Footprint | Notes |
|-----|-----------|-------|-------------|-----------|-------|
| 1 | J1 | CONN_02x10_P1.27mm | ARM 20-pin 1.27mm output | PinHeader_2x10_P1.27mm | Samtec FTSH-110-01-L-DV-K |
| 1 | J2 | CONN_02x10_P1.27mm | TI CTI-20 1.27mm output | PinHeader_2x10_P1.27mm | Samtec FTSH-110-01-L-DV-K |
| 1 | J3 | CONN_02x05_P1.27mm | Cortex 10-pin 1.27mm output | PinHeader_2x05_P1.27mm | Samtec FTSH-105-01-L-DV-K |
| 1 | J4 | CONN_02x10_P2.54mm | Input for ARM 20-pin | PinHeader_2x10_P2.54mm_IDC | IDC box header |
| 1 | J5 | CONN_02x10_P2.54mm | Input for TI CTI-20 | PinHeader_2x10_P2.54mm_IDC | IDC box header |
| 1 | J6 | CONN_02x10_P2.54mm | Input for Cortex 10-pin | PinHeader_2x10_P2.54mm_IDC | IDC box header |

### Resistors

#### Pull-up Resistors (10kΩ, 0603)
| Qty | Reference | Value | Description | Notes |
|-----|-----------|-------|-------------|-------|
| 3 | R1, R8, R15 | 10kΩ | Pull-up for TMS/SWDIO | One per output section |
| 3 | R2, R9, R16 | 10kΩ | Pull-up for TDI | One per output section |
| 3 | R3, R10, R17 | 10kΩ | Pull-up for nTRST | One per output section |
| 3 | R4, R11, R18 | 10kΩ | Pull-up for nRESET | One per output section |

#### Series Protection Resistors (33Ω, 0603)
| Qty | Reference | Value | Description | Notes |
|-----|-----------|-------|-------------|-------|
| 3 | R5, R12, R19 | 33Ω | Series on TMS/SWDIO | One per output section |
| 3 | R6, R13, R20 | 33Ω | Series on TCK/SWCLK | One per output section |
| 3 | R7, R14, R21 | 33Ω | Series on TDO/SWO | One per output section |

### Capacitors
| Qty | Reference | Value | Description | Notes |
|-----|-----------|-------|-------------|-------|
| 3 | C1, C2, C3 | 100nF | VTref decoupling | 0603, ceramic, X7R |

### Optional Components
| Qty | Reference | Value | Description | Notes |
|-----|-----------|-------|-------------|-------|
| 3 | D1, D2, D3 | LED | Power indicator | Optional, on VTref |
| 3 | R22, R23, R24 | 1kΩ | LED current limiting | If LEDs used |

## Schematic Sections

### Section 1: ARM 20-pin 1.27mm Output

#### Input Connector (J4 - IDC 2x10, 2.54mm)
```
Pin  Signal      Connection
1    VTref    -> To C1, R1-R4 pull-ups, LED circuit, J1 pin 1
2    NC       -> No connection
3    nTRST    -> Through R3 to VTref, to J1 pin 3
4    GND      -> Ground plane
5    TDI      -> Through R2 to VTref, to J1 pin 5
6    GND      -> Ground plane
7    TMS      -> Through R1 to VTref, through R5 (33Ω), to J1 pin 7
8    GND      -> Ground plane
9    TCK      -> Through R6 (33Ω), to J1 pin 9
10   GND      -> Ground plane
11   RTCK     -> Direct to J1 pin 11
12   GND      -> Ground plane
13   TDO      -> Through R7 (33Ω), to J1 pin 13
14   GND      -> Ground plane (keyed - may be removed)
15   nRESET   -> Through R4 to VTref, to J1 pin 15
16   GND      -> Ground plane
17   NC       -> No connection
18   GND      -> Ground plane
19   NC       -> No connection
20   GND      -> Ground plane
```

#### Output Connector (J1 - 2x10, 1.27mm)
Direct mapping - same pinout as input, just smaller pitch

#### Supporting Components
- C1: 100nF between VTref (pin 1) and GND
- R1: 10kΩ pull-up on TMS (between J4-7 and J4-1)
- R2: 10kΩ pull-up on TDI (between J4-5 and J4-1)
- R3: 10kΩ pull-up on nTRST (between J4-3 and J4-1)
- R4: 10kΩ pull-up on nRESET (between J4-15 and J4-1)
- R5: 33Ω series on TMS (between pull-up and J1-7)
- R6: 33Ω series on TCK (between J4-9 and J1-9)
- R7: 33Ω series on TDO (between J4-13 and J1-13)
- D1 (optional): LED from VTref through R22 (1kΩ) to GND

### Section 2: TI CTI-20 1.27mm Output

#### Input Connector (J5 - IDC 2x10, 2.54mm)
```
Pin  Signal      ARM Pin  TI CTI-20 Mapping
1    VTref       1     -> To C2, R8-R11 pull-ups, LED circuit
2    GND         2     -> Ground plane (pin 2 on CTI-20)
3    TMS         7     -> Through R8, R12, to J2 pin 1
4    GND         4     -> Ground plane (pin 2 on CTI-20)
5    TDI         5     -> Through R9, to J2 pin 3
6    GND         6     -> Ground plane (pin 4 on CTI-20)
7    TDO         13    -> Through R14, to J2 pin 5
8    GND         8     -> Ground plane (pin 6 on CTI-20)
9    TCK         9     -> Through R13, to J2 pin 7
10   GND         10    -> Ground plane (pin 8 on CTI-20)
11   nTRST       3     -> Through R10, to J2 pin 9
12   GND         12    -> Ground plane (pin 10 on CTI-20)
13   nRESET      15    -> Through R11, to J2 pin 11
14   GND         14    -> Ground plane (pin 12 on CTI-20)
15   EMU0        -     -> J2 pin 13 (optional, can be NC)
16   GND         16    -> Ground plane (pin 14 on CTI-20)
17   EMU1        -     -> J2 pin 15 (optional, can be NC)
18   GND         18    -> Ground plane (pin 16 on CTI-20)
19   EMU2        -     -> J2 pin 17 (optional, can be NC)
20   GND         20    -> Ground plane (pin 18, 20 on CTI-20)
```

#### Output Connector (J2 - 2x10, 1.27mm)
TI CTI-20 pinout as documented in TI-CTI-20-1.27mm.md

#### Supporting Components
- C2: 100nF between VTref and GND
- R8: 10kΩ pull-up on TMS (VTref to TMS line)
- R9: 10kΩ pull-up on TDI
- R10: 10kΩ pull-up on nTRST
- R11: 10kΩ pull-up on nRESET
- R12: 33Ω series on TMS
- R13: 33Ω series on TCK
- R14: 33Ω series on TDO
- D2 (optional): LED on VTref
- R23 (optional): 1kΩ current limit for D2

**Note:** EMU pins (13, 15, 17, 19) can be wired through or left unconnected depending on target requirements.

### Section 3: Cortex 10-pin 1.27mm Output

#### Input Connector (J6 - IDC 2x10, 2.54mm)
```
Pin  Signal      ARM Pin  Cortex 10-pin Mapping
1    VTref       1     -> To C3, R15-R18 pull-ups, LED, J3 pin 1
2    GND         2     -> Ground plane
3    SWDIO/TMS   7     -> Through R15, R19, to J3 pin 2
4    GND         4     -> Ground plane (J3 pin 3)
5    SWCLK/TCK   9     -> Through R20, to J3 pin 4
6    GND         6     -> Ground plane (J3 pin 5)
7    SWO/TDO     13    -> Through R21, to J3 pin 6
8    GND         8     -> Ground plane (J3 pin 7 is KEY)
9    TDI         5     -> Through R16, to J3 pin 8
10   GND         10    -> Ground plane (J3 pin 9)
11   nRESET      15    -> Through R18, to J3 pin 10
12-20 GND        -     -> Ground plane
```

#### Output Connector (J3 - 2x5, 1.27mm)
Cortex Debug 10-pin pinout as documented in Cortex-10pin-1.27mm.md

#### Supporting Components
- C3: 100nF between VTref (J3 pin 1) and GND
- R15: 10kΩ pull-up on SWDIO/TMS
- R16: 10kΩ pull-up on TDI (for JTAG mode)
- R17: 10kΩ pull-up (spare, or for nTRST if needed)
- R18: 10kΩ pull-up on nRESET
- R19: 33Ω series on SWDIO/TMS
- R20: 33Ω series on SWCLK/TCK
- R21: 33Ω series on SWO/TDO
- D3 (optional): LED on VTref
- R24 (optional): 1kΩ current limit for D3

## Schematic Notes and Annotations

### Title Block
- **Title:** Adapterama - JTAG Converter Pack
- **Description:** Multi-format JTAG/SWD adapter for Segger J-Link
- **Revision:** 1.0
- **Date:** 2025-11-23
- **Author:** [Your Name]
- **License:** Open Source Hardware

### General Notes (to add to schematic)
1. All GND pins on connectors connect to ground plane
2. VTref supplied by target board via ribbon cable
3. Pull-up resistors to VTref on critical signals
4. Series resistors provide basic ESD protection
5. Each output section is independent
6. Populate only the output connectors needed
7. Use keyed IDC connectors to prevent reverse connection

### Signal Integrity Notes
1. Keep traces short, especially for high-speed signals (TCK, SWCLK)
2. Route critical signals as differential pairs where practical
3. Use ground plane on bottom layer
4. Place decoupling capacitors close to connectors (<5mm)
5. Avoid routing under connectors

### Test Points (Recommended)
Add test points for debugging:
- TP1: VTref (Section 1)
- TP2: VTref (Section 2)
- TP3: VTref (Section 3)
- TP4: TMS/SWDIO (Section 1)
- TP5: TCK/SWCLK (Section 1)
- TP6: GND (common)

## Power Budget
- **VTref Source:** Target board via ribbon cable
- **Current Draw per Section:**
  - Pull-up resistors: ~0.4mA max (at 3.3V with 10kΩ)
  - LED (if used): ~2-3mA
  - **Total per section:** <5mA
- **Total adapter:** <15mA (all sections populated)

## Implementation in KiCad

### Step 1: Symbol Library Setup
Use KiCad standard libraries:
- **Connector_Generic:** For all connectors (2x10, 2x5 headers)
- **Device:** For resistors (R) and capacitors (C)
- **Device:** For LEDs (LED) if used

### Step 2: Place Components
1. Start with Section 1 (ARM 20-pin) on left side of schematic
2. Place Section 2 (TI CTI-20) in center
3. Place Section 3 (Cortex 10-pin) on right side
4. Arrange hierarchically: Input connector at top, components in middle, output at bottom
5. Leave space for labels and notes

### Step 3: Wire Connections
1. Use net labels for clarity (VTref, TMS, TCK, TDI, TDO, etc.)
2. Use power symbols for GND
3. Keep wiring clean and orthogonal
4. Group related signals

### Step 4: Annotations
1. Annotate components (Tools → Annotate Schematic)
2. Add text notes for each section
3. Add pin function labels on connectors
4. Fill in title block

### Step 5: Electrical Rules Check
1. Run ERC (Inspect → Electrical Rules Checker)
2. Resolve any errors or warnings
3. Verify all pins are connected

### Step 6: Generate Netlist
1. Generate netlist for PCB layout (File → Export → Netlist)
2. Ready for PCB design

## Common Design Patterns

### Pull-up Resistor Connection
```
VTref ----+----+---- (to other pull-ups)
          |
         [R1] 10kΩ
          |
          +----(Signal line, e.g., TMS)---[R5 33Ω]----> To output connector
          |
    (From input connector)
```

### Decoupling Capacitor Placement
```
VTref ----[C1 100nF]---- GND
  |                       |
  +-------> To J1 Pin 1   +----> To all GND pins
```

### Optional LED Circuit
```
VTref ----[R22 1kΩ]----[D1 LED]---- GND
```

## Future Expansion

### Additional Output Connectors (Future)
- TI 14-pin 2.54mm
- Tag-Connect TC2050 footprint (no connector populated)
- 6-pin SWD (compact)
- cJTAG 8-pin for TI

### Enhanced Features (Future)
- Level shifters for multi-voltage support
- ESD protection diodes (TPD2E001 or similar)
- Switchable pull-up resistors (solder jumpers)
- Buffered outputs for driving multiple targets

## Revision History
- **Rev 1.0 (2025-11-23):** Initial design with three output formats
