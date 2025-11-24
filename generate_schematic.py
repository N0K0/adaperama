#!/usr/bin/env python3
"""
Generate KiCad schematic for Adapterama JTAG Converter Pack

This script generates a complete KiCad schematic file with:
- Custom connector symbols (ARM JTAG, TI CTI-20, Cortex Debug)
- Passive component symbols (resistors, capacitors)
- Component placement on A3 sheet
- All symbols embedded (no external library dependencies)

Usage:
    python3 generate_schematic.py

Output:
    adapterama.kicad_sch - Complete KiCad schematic file
"""

from datetime import datetime

from connector_data import CONNECTOR_INFO
from symbol_gen import (
    create_connector_symbol,
    create_resistor_symbol,
    create_capacitor_symbol,
)
from component_gen import create_component, create_text_label


def generate_schematic_header():
    """Generate schematic file header with metadata"""
    return f"""(kicad_sch
\t(version 20250114)
\t(generator "python-script")
\t(generator_version "2.0")
\t(uuid c5f55ab1-dc13-4818-9acb-5ba26cd36488)
\t(paper "A3")
\t(title_block
\t\t(title "Adapterama - JTAG Converter Pack")
\t\t(date "{datetime.now().strftime('%Y-%m-%d')}")
\t\t(rev "1.0")
\t\t(comment 1 "Multi-format JTAG/SWD adapter - Female output connectors")
\t\t(comment 2 "ARM 20-pin, TI CTI-20, Cortex 10-pin outputs")
\t\t(comment 3 "Passive adapter - wire per WIRING_GUIDE.md")
\t)

\t(lib_symbols
"""


def generate_symbols():
    """Generate all embedded symbols"""
    symbols = []

    # Connector symbols from data
    for name, info in CONNECTOR_INFO.items():
        symbols.append(
            create_connector_symbol(name, info['datasheet'], info['pins'])
        )

    # Passive component symbols
    symbols.append(create_resistor_symbol())
    symbols.append(create_capacitor_symbol())

    return symbols


def generate_section(section_num, x_base, y_base, connector_name, resistors, capacitor):
    """
    Generate a complete section with connector, resistors, and capacitor

    Args:
        section_num: Section number (1, 2, or 3)
        x_base: Base X coordinate
        y_base: Base Y coordinate
        connector_name: Connector symbol name
        resistors: List of (ref, value, description) tuples
        capacitor: Tuple of (ref, value)

    Returns:
        List of component/text S-expressions
    """
    parts = []

    # Section label
    section_names = {
        1: "Section 1: ARM 20-pin",
        2: "Section 2: TI CTI-20",
        3: "Section 3: Cortex 10-pin",
    }
    parts.append(create_text_label(section_names[section_num], x_base - 0.2, 0.3, 2.5))

    # Connector
    j_ref = f"J{section_num}"
    parts.append(create_component(
        j_ref,
        f"{connector_name.split('_')[0]}_Output",
        connector_name,
        x_base,
        y_base,
        "Connector_PinHeader_1.27mm:PinHeader_2x10_P1.27mm_Vertical"
        if "10pin" not in connector_name
        else "Connector_PinHeader_1.27mm:PinHeader_2x05_P1.27mm_Vertical",
    ))

    # Resistors to the right of connector
    for i, (ref, val, desc) in enumerate(resistors):
        parts.append(create_component(
            ref,
            val,
            "R",
            x_base + 0.35,
            y_base - 0.2 + (i * 0.07),
            "Resistor_SMD:R_0603_1608Metric",
            {"Description": desc},
        ))

    # Capacitor
    c_ref, c_val = capacitor
    parts.append(create_component(
        c_ref,
        c_val,
        "C",
        x_base + 0.5,
        y_base + 0.35,
        "Capacitor_SMD:C_0603_1608Metric",
        {"Description": "VTref decoupling"},
    ))

    return parts


def generate_components():
    """Generate all component instances"""
    parts = []

    # NOTE: KiCad coordinate system - values are 1/100th of desired mm placement
    # See kicad_utils.py for explanation

    # Section 1: ARM 20-pin
    parts.extend(generate_section(
        section_num=1,
        x_base=0.5,
        y_base=0.7,
        connector_name="ARM_JTAG_20pin_1.27mm",
        resistors=[
            ("R1", "10k", "TMS pullup"),
            ("R2", "10k", "TDI pullup"),
            ("R3", "10k", "nTRST pullup"),
            ("R4", "10k", "nRESET pullup"),
            ("R5", "33", "TMS series"),
            ("R6", "33", "TCK series"),
            ("R7", "33", "TDO series"),
        ],
        capacitor=("C1", "100nF"),
    ))

    # Section 2: TI CTI-20
    parts.extend(generate_section(
        section_num=2,
        x_base=1.6,
        y_base=0.7,
        connector_name="TI_CTI_20pin_1.27mm",
        resistors=[
            ("R8", "10k", "TMS pullup"),
            ("R9", "10k", "TDI pullup"),
            ("R10", "10k", "nTRST pullup"),
            ("R11", "10k", "nSRST pullup"),
            ("R12", "33", "TMS series"),
            ("R13", "33", "TCK series"),
            ("R14", "33", "TDO series"),
        ],
        capacitor=("C2", "100nF"),
    ))

    # Section 3: Cortex 10-pin
    parts.extend(generate_section(
        section_num=3,
        x_base=2.7,
        y_base=0.7,
        connector_name="Cortex_Debug_10pin_1.27mm",
        resistors=[
            ("R15", "10k", "SWDIO pullup"),
            ("R16", "10k", "TDI pullup"),
            ("R17", "10k", "spare"),
            ("R18", "10k", "nRESET pullup"),
            ("R19", "33", "SWDIO series"),
            ("R20", "33", "SWCLK series"),
            ("R21", "33", "SWO series"),
        ],
        capacitor=("C3", "100nF"),
    ))

    # Footer note
    parts.append(
        create_text_label("Wire per WIRING_GUIDE.md | All female outputs", 0.3, 1.8, 2.0)
    )

    return parts


def generate_schematic_footer():
    """Generate schematic file footer"""
    return """\t(sheet_instances
\t\t(path "/" (page "1"))
\t)
\t(embedded_fonts no)
)
"""


def main():
    """Main schematic generation function"""
    print("Generating Adapterama JTAG Converter Pack schematic...")
    print("Using modular architecture...")

    parts = []

    # Header
    parts.append(generate_schematic_header())

    # Symbols
    parts.extend(generate_symbols())
    parts.append("\t)\n\n")

    # Components
    parts.extend(generate_components())

    # Footer
    parts.append(generate_schematic_footer())

    # Write file
    output_file = "adapterama.kicad_sch"
    with open(output_file, 'w') as f:
        f.write(''.join(parts))

    print(f"✓ Schematic generated: {output_file}")
    print(f"✓ Modular design: 5 Python modules")
    print(f"✓ Symbols: ARM 20-pin, TI CTI-20, Cortex 10-pin")
    print(f"✓ Components: 3 connectors, 21 resistors, 3 capacitors")
    print("\nModules:")
    print("  - kicad_utils.py       (utilities)")
    print("  - connector_data.py    (pin definitions)")
    print("  - symbol_gen.py        (symbol generation)")
    print("  - component_gen.py     (component instances)")
    print("  - generate_schematic.py (main orchestrator)")
    print("\nNext: Open in KiCad and wire connections")


if __name__ == "__main__":
    main()
