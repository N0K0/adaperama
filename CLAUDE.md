# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Adapterama** is a JTAG/SWD converter pack adapter board designed to work with Segger J-Link debuggers. The board converts between different JTAG connector formats commonly used in embedded development.

### Purpose
Convert J-Link's standard 20-pin JTAG interface (via ribbon cable) to three different target connector formats:
1. ARM 20-pin 1.27mm compact JTAG
2. TI CTI-20 1.27mm (Texas Instruments compact JTAG with EMU pins)
3. ARM Cortex 10-pin 1.27mm (modern ARM SWD/JTAG debug connector)

### Design Approach
- **Passive adapter:** No active components or external power required
- **Ribbon cable inputs:** Each output has its own 2.54mm IDC input for ribbon cable connection
- **Simple and reliable:** Uses only resistors for signal conditioning (pull-ups and series protection)
- **Modular:** Populate only the output connectors you need

This is a KiCad hardware design project using KiCad 9.0.

## File Structure

### KiCad Design Files
- `adapterama.kicad_pro` - KiCad project configuration (JSON format)
- `adapterama.kicad_sch` - Schematic design file (S-expression format)
- `adapterama.kicad_pcb` - PCB layout file (S-expression format)

### Documentation
- `CLAUDE.md` - This file, guidance for Claude Code
- `SCHEMATIC_DESIGN.md` - Complete schematic design specification with BOM and implementation guide
- `connector-specs/` - Detailed specifications for each JTAG connector type:
  - `ARM-20pin-1.27mm.md` - Compact ARM JTAG connector specification
  - `ARM-20pin-2.54mm.md` - Standard ARM JTAG connector (reference, used for J-Link input)
  - `TI-CTI-20-1.27mm.md` - Texas Instruments CTI-20 connector specification
  - `Cortex-10pin-1.27mm.md` - ARM Cortex Debug connector specification

## Working with KiCad Files

### File Formats
- KiCad project files (.kicad_pro) are JSON-based and can be edited directly
- Schematic (.kicad_sch) and PCB (.kicad_pcb) files use KiCad's S-expression format
- All files are text-based and version control friendly

### Editing Workflow
- KiCad files use specific version markers (e.g., `version 20241229` for PCB, `version 20250114` for schematics)
- The generator is always "pcbnew" for PCB files and "eeschema" for schematic files
- Generator version matches the KiCad version (currently 9.0)

### KiCad Coordinate System
**IMPORTANT:** When programmatically generating KiCad schematic files:
- Coordinates are stored internally in **mils** (thousandths of an inch), where 1 mil = 0.0254mm
- The `mm_to_mils()` conversion function divides mm by 0.0254, resulting in large numbers
- **Use coordinates 1/10th of your desired mm placement** in the script
- Example: To place a component at 50mm in KiCad, use `5` in the Python script
- Script values represent "conceptual mm" but are converted to mils internally
- A3 usable area in script units: approximately 3-38 (X), 2-24 (Y)
- See `generate_schematic.py` for implementation example

### KiCad Commands
To open the project in KiCad:
```bash
kicad adapterama.kicad_pro
```

To open specific editors:
```bash
# Open schematic editor
eeschema adapterama.kicad_sch

# Open PCB editor
pcbnew adapterama.kicad_pcb
```

## Circuit Design Details

### Schematic Structure
The schematic is divided into three independent sections, one for each output connector:

1. **Section 1: ARM 20-pin 1.27mm Output**
   - Input: J4 (2x10, 2.54mm IDC connector for ribbon cable)
   - Output: J1 (2x10, 1.27mm header)
   - Components: R1-R7 (pull-ups and series resistors), C1 (decoupling)

2. **Section 2: TI CTI-20 1.27mm Output**
   - Input: J5 (2x10, 2.54mm IDC connector, remapped for TI pinout)
   - Output: J2 (2x10, 1.27mm header)
   - Components: R8-R14 (pull-ups and series resistors), C2 (decoupling)
   - Note: EMU pins (13, 15, 17, 19) can be connected or left NC

3. **Section 3: Cortex 10-pin 1.27mm Output**
   - Input: J6 (2x10, 2.54mm IDC connector)
   - Output: J3 (2x5, 1.27mm header)
   - Components: R15-R21 (pull-ups and series resistors), C3 (decoupling)

### Key Component Values
- **Pull-up resistors:** 10kΩ on TMS/SWDIO, TDI, nTRST, nRESET (to VTref)
- **Series resistors:** 33Ω on TMS, TCK, TDO for signal integrity and protection
- **Decoupling capacitors:** 100nF ceramic (X7R) on VTref for each section
- **All resistors:** 0603 package for hand assembly
- **All capacitors:** 0603 ceramic

### Signal Mappings
Each connector type has different pinouts. Key mappings:
- **ARM 20-pin → TI CTI-20:** Signals reordered (see TI-CTI-20-1.27mm.md)
- **ARM 20-pin → Cortex 10-pin:** Subset of signals (see Cortex-10pin-1.27mm.md)
- Detailed pin mappings in `SCHEMATIC_DESIGN.md`

## Implementing the Schematic in KiCad

The complete circuit design is documented in `SCHEMATIC_DESIGN.md`. To implement:

1. **Open the schematic editor:**
   ```bash
   eeschema adapterama.kicad_sch
   ```

2. **Add symbols from KiCad standard libraries:**
   - `Connector_Generic` - All pin headers (2x10, 2x5)
   - `Device` - Resistors (R), Capacitors (C), optional LEDs

3. **Follow the design in SCHEMATIC_DESIGN.md:**
   - Place components for each section
   - Wire according to the connection tables
   - Use net labels for clarity
   - Add annotations and notes

4. **Run Electrical Rules Check:**
   - Inspect → Electrical Rules Checker
   - Resolve all errors before proceeding to PCB

5. **Generate netlist for PCB layout:**
   - File → Export → Netlist

## PCB Layout Considerations

### Connector Placement
- All three output connectors (J1, J2, J3) on one edge for easy access
- Input IDC connectors (J4, J5, J6) on opposite edge
- Each section can be independently populated

### Routing Guidelines
- **Layer stack:** 2-layer board sufficient
  - Top: Components and signal routing
  - Bottom: Ground plane with minimal routing
- **Trace widths:** 0.25mm (10 mil) for signals, 0.5mm (20 mil) for power/ground
- **Clearance:** 0.2mm (8 mil) minimum
- **Keep traces short:** Especially for TCK/SWCLK (clock signals)
- **Route as differential pairs** where practical: TMS/TCK, SWDIO/SWCLK

### Component Placement
- Place decoupling caps (C1, C2, C3) within 5mm of respective connectors
- Pull-up resistors near VTref connection point
- Series resistors close to input connectors
- Leave space for test points on critical signals

### Manufacturing
- **Board size:** Depends on connector spacing, typically 50-80mm x 30-50mm
- **Finish:** ENIG (gold) for connector pads, HASL acceptable for others
- **Silkscreen:** Label all connectors clearly, mark Pin 1, add project name and version
- **Solder mask:** Standard (green, black, or blue)

## Design Validation

### Pre-Layout Checks
1. Verify all pull-ups present on required signals (TMS, TDI, nTRST, nRESET)
2. Check VTref connections to all pull-up resistors
3. Verify ground connections on all even-numbered connector pins
4. Confirm pinout mappings against connector spec documents

### Post-Layout Checks
1. DRC (Design Rule Check) must pass with no errors
2. Verify Pin 1 marking on all connectors
3. Check component reference designators are visible
4. Ensure mounting holes present (if needed)
5. Generate Gerber files and review in viewer

### Testing Procedure
1. Visual inspection after assembly
2. Continuity test: VTref to pull-up resistors
3. Continuity test: All GND pins connected
4. Resistance check: TMS to VTref should read ~10kΩ (pull-up)
5. Connectivity test: Input pins to output pins through series resistors
6. Functional test with J-Link and target board

## Common Tasks

### Viewing Connector Specifications
```bash
# Read detailed connector specs
cat connector-specs/ARM-20pin-1.27mm.md
cat connector-specs/TI-CTI-20-1.27mm.md
cat connector-specs/Cortex-10pin-1.27mm.md
```

### Reviewing Circuit Design
```bash
# View complete schematic design specification
cat SCHEMATIC_DESIGN.md
```

### Generating Manufacturing Files
In KiCad PCB editor:
1. File → Plot → Generate Gerber files
2. File → Fabrication Outputs → Drill Files (.drl)
3. File → Fabrication Outputs → Component Placement (.pos)
4. File → Fabrication Outputs → BOM (Bill of Materials)

## Important Considerations

### KiCad File Handling
- KiCad S-expression files have strict formatting requirements - maintain proper indentation and structure
- UUIDs in schematic files must be unique and valid
- **Changes to schematic and PCB files should be made through KiCad GUI** to ensure file integrity
- When editing .kicad_pro files directly, ensure JSON remains valid
- The project currently uses KiCad 9.0 file format - be aware of version compatibility

### Electrical Design
- VTref is supplied by the target board through the ribbon cable
- Maximum current draw per section: <5mA (from VTref)
- All signals are 5V tolerant but operate at target voltage (VTref)
- Series resistors (33Ω) provide basic ESD protection but are not a substitute for proper ESD diodes in production

### Mechanical Design
- Use shrouded/keyed connectors to prevent reverse insertion
- 1.27mm pitch connectors are delicate - consider mechanical support
- Add mounting holes for strain relief if adapter will be permanently mounted
- Leave clearance for ribbon cable bend radius

## Future Expansion Ideas

Additional connector formats that could be added:
- TI 14-pin 2.54mm JTAG
- Tag-Connect TC2050 footprint (pogo-pin connector)
- 6-pin SWD connector (minimal ARM debugging)
- cJTAG 8-pin connector (TI compact JTAG)
- SWD + UART combined connector (6-pin with serial console)

Enhanced features:
- ESD protection diodes (e.g., TPD2E001)
- Level shifters for multi-voltage support (1.8V, 3.3V, 5V)
- Switchable pull-up resistors (solder jumpers)
- LED activity indicators on clock lines
- Buffered outputs for driving multiple targets simultaneously
