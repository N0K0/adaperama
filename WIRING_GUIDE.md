# KiCad Schematic Wiring Guide

## Overview
The schematic has been generated with all components placed and footprints assigned. You now need to wire the connections in KiCad's schematic editor.

## Opening the Schematic
```bash
eeschema adapterama.kicad_sch
```

## Schematic Layout
The schematic is organized in three vertical sections on an A3 page:
- **Left:** Section 1 - ARM 20-pin 1.27mm Output
- **Center:** Section 2 - TI CTI-20 1.27mm Output
- **Right:** Section 3 - Cortex 10-pin 1.27mm Output

Each section has:
- Input connector (top): J4, J5, or J6 (2.54mm IDC connector)
- Output connector (bottom): J1, J2, or J3 (1.27mm header)
- Pull-up resistors: R1-R4, R8-R11, or R15-R18 (10kΩ)
- Series resistors: R5-R7, R12-R14, or R19-R21 (33Ω)
- Decoupling capacitor: C1, C2, or C3 (100nF)

## Wiring Instructions

### General Wiring Tips in KiCad
1. **Place Wire (W key):** Press 'W' to start a wire
2. **Place Label (L key):** Press 'L' to create a net label
3. **Ground Symbol:** Press 'P' then search for "GND" power symbol
4. **Use Net Labels:** For cleaner schematics, use net labels instead of long wires

### Net Naming Convention
Use these net names for consistency:
- **Section 1:** `S1_VTref`, `S1_TMS`, `S1_TCK`, `S1_TDI`, `S1_TDO`, `S1_nTRST`, `S1_nRESET`, etc.
- **Section 2:** `S2_VTref`, `S2_TMS`, `S2_TCK`, `S2_TDI`, `S2_TDO`, `S2_nTRST`, `S2_nRESET`, etc.
- **Section 3:** `S3_VTref`, `S3_SWDIO`, `S3_SWCLK`, `S3_SWO`, `S3_TDI`, `S3_nRESET`, etc.

## Section 1: ARM 20-pin 1.27mm Wiring

### Ground Connections
Connect all even-numbered pins of J4 and J1 to GND:
- J4 pins: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20 → GND symbol
- J1 pins: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20 → GND symbol
- C1 pin 2 → GND

### VTref Distribution
- J4 pin 1 → Label `S1_VTref`
- `S1_VTref` → R1 pin 1, R2 pin 1, R3 pin 1, R4 pin 1 (pull-ups)
- `S1_VTref` → C1 pin 1 (decoupling)
- `S1_VTref` → J1 pin 1 (output)

### TMS Signal Path
- J4 pin 7 → R1 pin 2 → Label `S1_TMS_PU`
- `S1_TMS_PU` → R5 pin 1 → R5 pin 2 → J1 pin 7
- (Pull-up on TMS, then series resistor)

### TDI Signal Path
- J4 pin 5 → R2 pin 2 → Label `S1_TDI_PU`
- `S1_TDI_PU` → J1 pin 5
- (Pull-up on TDI, no series resistor needed)

### TCK Signal Path
- J4 pin 9 → R6 pin 1 → R6 pin 2 → J1 pin 9
- (Series resistor on TCK)

### TDO Signal Path
- J4 pin 13 → R7 pin 1 → R7 pin 2 → J1 pin 13
- (Series resistor on TDO)

### nTRST Signal Path
- J4 pin 3 → R3 pin 2 → Label `S1_nTRST_PU`
- `S1_nTRST_PU` → J1 pin 3
- (Pull-up on nTRST)

### nRESET Signal Path
- J4 pin 15 → R4 pin 2 → Label `S1_nRESET_PU`
- `S1_nRESET_PU` → J1 pin 15
- (Pull-up on nRESET)

### Other Signals (Direct Connection)
- J4 pin 11 (RTCK) → J1 pin 11
- J4 pin 17 (NC) → No connection
- J4 pin 19 (NC) → No connection

## Section 2: TI CTI-20 1.27mm Wiring

**Important:** TI CTI-20 has different pinout than ARM 20-pin!

### Ground Connections
Connect all even-numbered pins of J5 and J2 to GND:
- J5 pins: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20 → GND
- J2 pins: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20 → GND
- C2 pin 2 → GND

### VTref Distribution
- J5 pin 1 → Label `S2_VTref`
- `S2_VTref` → R8 pin 1, R9 pin 1, R10 pin 1, R11 pin 1
- `S2_VTref` → C2 pin 1
- Note: VTref is NOT on J2 for TI CTI-20 (separate connection on target)

### Signal Mappings (ARM pins to TI CTI-20 pins)

#### TMS Signal
- J5 pin 3 (ARM pin 7) → R8 pin 2 → `S2_TMS_PU`
- `S2_TMS_PU` → R12 pin 1 → R12 pin 2 → J2 pin 1 (CTI-20 TMS)

#### TDI Signal
- J5 pin 5 (ARM pin 5) → R9 pin 2 → `S2_TDI_PU`
- `S2_TDI_PU` → J2 pin 3 (CTI-20 TDI)

#### TDO Signal
- J5 pin 7 (ARM pin 13) → R14 pin 1 → R14 pin 2 → J2 pin 5 (CTI-20 TDO)

#### TCK Signal
- J5 pin 9 (ARM pin 9) → R13 pin 1 → R13 pin 2 → J2 pin 7 (CTI-20 TCK)

#### nTRST Signal
- J5 pin 11 (ARM pin 3) → R10 pin 2 → `S2_nTRST_PU`
- `S2_nTRST_PU` → J2 pin 9 (CTI-20 nTRST)

#### nRESET Signal
- J5 pin 13 (ARM pin 15) → R11 pin 2 → `S2_nRESET_PU`
- `S2_nRESET_PU` → J2 pin 11 (CTI-20 nSRST)

#### EMU Signals (Optional)
- J5 pin 15 → J2 pin 13 (EMU0) - optional
- J5 pin 17 → J2 pin 15 (EMU1) - optional
- J5 pin 19 → J2 pin 17 (EMU2) - optional
- Remaining J5 odd pins can be left unconnected

## Section 3: Cortex 10-pin 1.27mm Wiring

### Ground Connections
- J6 pins: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20 → GND
- J3 pins: 3, 5, 7 (NC), 9 → GND
- C3 pin 2 → GND
- Note: J3 pin 7 is KEY (not connected)

### VTref Distribution
- J6 pin 1 → Label `S3_VTref`
- `S3_VTref` → R15 pin 1, R16 pin 1, R17 pin 1, R18 pin 1
- `S3_VTref` → C3 pin 1
- `S3_VTref` → J3 pin 1 (Cortex VTref)

### Signal Mappings (ARM pins to Cortex 10-pin)

#### SWDIO/TMS Signal
- J6 pin 3 (ARM pin 7 = TMS) → R15 pin 2 → `S3_SWDIO_PU`
- `S3_SWDIO_PU` → R19 pin 1 → R19 pin 2 → J3 pin 2 (SWDIO/TMS)

#### SWCLK/TCK Signal
- J6 pin 5 (ARM pin 9 = TCK) → R20 pin 1 → R20 pin 2 → J3 pin 4 (SWCLK/TCK)

#### SWO/TDO Signal
- J6 pin 7 (ARM pin 13 = TDO) → R21 pin 1 → R21 pin 2 → J3 pin 6 (SWO/TDO)

#### TDI Signal (for JTAG mode)
- J6 pin 9 (ARM pin 5 = TDI) → R16 pin 2 → `S3_TDI_PU`
- `S3_TDI_PU` → J3 pin 8 (TDI)

#### nRESET Signal
- J6 pin 11 (ARM pin 15 = nRESET) → R18 pin 2 → `S3_nRESET_PU`
- `S3_nRESET_PU` → J3 pin 10 (nRESET)

#### Unused pins
- J6 pins 13, 15, 17, 19 → No connection (or leave open)

## Quick Wiring Checklist

### Before You Start
- [ ] Open schematic: `eeschema adapterama.kicad_sch`
- [ ] Familiarize yourself with hotkeys: W (wire), L (label), P (power/GND)
- [ ] Review pin mappings in connector-specs/*.md files

### Section 1 Checklist
- [ ] Connect all even pins of J4 and J1 to GND
- [ ] Wire VTref from J4 pin 1 to pull-up resistors and C1
- [ ] Connect TMS path: J4-7 → R1 → R5 → J1-7
- [ ] Connect TDI path: J4-5 → R2 → J1-5
- [ ] Connect TCK path: J4-9 → R6 → J1-9
- [ ] Connect TDO path: J4-13 → R7 → J1-13
- [ ] Connect nTRST path: J4-3 → R3 → J1-3
- [ ] Connect nRESET path: J4-15 → R4 → J1-15
- [ ] Connect RTCK: J4-11 → J1-11

### Section 2 Checklist
- [ ] Connect all even pins of J5 and J2 to GND
- [ ] Wire VTref from J5 pin 1 to pull-up resistors and C2
- [ ] Map TMS: J5-3 → R8 → R12 → J2-1
- [ ] Map TDI: J5-5 → R9 → J2-3
- [ ] Map TDO: J5-7 → R14 → J2-5
- [ ] Map TCK: J5-9 → R13 → J2-7
- [ ] Map nTRST: J5-11 → R10 → J2-9
- [ ] Map nRESET: J5-13 → R11 → J2-11
- [ ] (Optional) Connect EMU pins: J5-15/17/19 → J2-13/15/17

### Section 3 Checklist
- [ ] Connect J6 even pins (2-20) and J3 pins (3,5,9) to GND
- [ ] Wire VTref from J6 pin 1 to pull-up resistors and C3
- [ ] Connect SWDIO: J6-3 → R15 → R19 → J3-2
- [ ] Connect SWCLK: J6-5 → R20 → J3-4
- [ ] Connect SWO: J6-7 → R21 → J3-6
- [ ] Connect TDI: J6-9 → R16 → J3-8
- [ ] Connect nRESET: J6-11 → R18 → J3-10
- [ ] Leave J3 pin 7 unconnected (KEY)

## After Wiring

### Run Electrical Rules Check
1. Click **Inspect → Electrical Rules Checker**
2. Click **Run ERC**
3. Resolve any errors (warnings about unconnected pins on unused J5/J6 pins are OK)

### Annotate Schematic
1. Click **Tools → Annotate Schematic**
2. Click **Annotate** to assign final reference designators

### Generate Netlist
1. Click **File → Export → Netlist**
2. Click **Generate Netlist**
3. This creates the file needed for PCB layout

## Tips for Clean Schematic
- Use net labels liberally to avoid crossing wires
- Keep wires orthogonal (90° angles)
- Group related signals together
- Add text notes to clarify pin mappings
- Use different colors for power nets (optional)

## Common Issues

### Symbol Missing from Library
If components don't show up:
- Go to **Preferences → Manage Symbol Libraries**
- Ensure `Connector_Generic` and `Device` are in the list
- If missing, add from `/usr/share/kicad/symbols/`

### Can't Place Wire
- Make sure you're in wire mode (W key)
- Click on a pin to start, click again to end
- Press ESC to cancel wire placement

### GND Symbols Not Connecting
- Use the GND power symbol from library (P key, search "GND")
- All GND symbols auto-connect (same net)
- No need to wire between separate GND symbols

## Next Steps
After completing wiring:
1. Save the schematic
2. Generate the BOM (Bill of Materials)
3. Create the PCB layout from the netlist
4. Route traces on the PCB
5. Generate Gerber files for manufacturing

See SCHEMATIC_DESIGN.md for detailed pin mapping tables and electrical specifications.
