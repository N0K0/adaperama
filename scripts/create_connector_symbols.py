#!/usr/bin/env python3
"""
Generate specific connector symbols for the Adapterama project.
This script creates properly named symbols for each connector type.
"""

import sys
import os

# Add scripts directory to path so we can import our modules
sys.path.insert(0, os.path.dirname(__file__))

from connector_data import CONNECTOR_INFO
from symbol_gen import create_connector_symbol


def generate_all_connector_symbols():
    """Generate all connector symbols from CONNECTOR_INFO"""
    symbols = []

    for symbol_name, info in CONNECTOR_INFO.items():
        print(f"Generating symbol: {symbol_name}")
        symbol = create_connector_symbol(
            name=symbol_name,
            datasheet=info['datasheet'],
            pins=info['pins']
        )
        symbols.append(symbol)

    return symbols


def add_20pin_2_54mm_connector():
    """Add the ARM 20-pin 2.54mm connector (IDC input connector)"""
    # This is the input connector from J-Link (standard 2.54mm pitch)
    ARM_20PIN_2_54MM_PINS = [
        ('1', 'VTref', 'power_in', 'left'),
        ('2', 'NC/VDD', 'power_in', 'right'),
        ('3', 'nTRST', 'input', 'left'),
        ('4', 'GND', 'power_in', 'right'),
        ('5', 'TDI', 'input', 'left'),
        ('6', 'GND', 'power_in', 'right'),
        ('7', 'TMS', 'input', 'left'),
        ('8', 'GND', 'power_in', 'right'),
        ('9', 'TCK', 'input', 'left'),
        ('10', 'GND', 'power_in', 'right'),
        ('11', 'RTCK', 'output', 'left'),
        ('12', 'GND', 'power_in', 'right'),
        ('13', 'TDO', 'output', 'left'),
        ('14', 'GND', 'power_in', 'right'),
        ('15', 'nRESET', 'open_collector', 'left'),
        ('16', 'GND', 'power_in', 'right'),
        ('17', 'NC', 'no_connect', 'left'),
        ('18', 'GND', 'power_in', 'right'),
        ('19', 'NC', 'no_connect', 'left'),
        ('20', 'GND', 'power_in', 'right'),
    ]

    print("Generating symbol: ARM_JTAG_20pin_2.54mm")
    return create_connector_symbol(
        name='ARM_JTAG_20pin_2.54mm',
        datasheet='connector-specs/ARM-20pin-2.54mm.md',
        pins=ARM_20PIN_2_54MM_PINS
    )


def create_symbol_library():
    """Create the complete symbol library file"""

    # Generate all symbols
    connector_symbols = generate_all_connector_symbols()

    # Add the 2.54mm input connector
    input_connector = add_20pin_2_54mm_connector()
    connector_symbols.append(input_connector)

    # Read existing library to preserve R, C, GND symbols
    library_path = '/home/user/adaperama/adapterama-symbols.kicad_sym'

    # Build the library header
    library_header = '''(kicad_symbol_lib
\t(version 20231120)
\t(generator "python-script")
\t(generator_version "2.0")
'''

    # Read existing symbols we want to keep (R, C, GND)
    with open(library_path, 'r') as f:
        content = f.read()

    # Extract R, C, GND symbols
    existing_symbols = []
    for symbol_name in ['R', 'C', 'GND']:
        start = content.find(f'\t(symbol "{symbol_name}"')
        if start != -1:
            # Find the matching closing parenthesis
            depth = 0
            pos = start
            symbol_start = start

            while pos < len(content):
                if content[pos] == '(':
                    depth += 1
                elif content[pos] == ')':
                    depth -= 1
                    if depth == 0:
                        existing_symbols.append(content[symbol_start:pos+1])
                        break
                pos += 1

    # Combine everything
    full_library = library_header

    # Add all connector symbols
    for symbol in connector_symbols:
        full_library += symbol + '\n'

    # Add existing symbols
    for symbol in existing_symbols:
        full_library += '\n' + symbol + '\n'

    # Close the library
    full_library += ')\n'

    return full_library


def main():
    """Main entry point"""
    print("Creating Adapterama connector symbols...")
    print("=" * 60)

    library_content = create_symbol_library()

    # Write to file
    output_path = '/home/user/adaperama/adapterama-symbols.kicad_sym'
    with open(output_path, 'w') as f:
        f.write(library_content)

    print("=" * 60)
    print(f"Symbol library created: {output_path}")
    print("\nSymbols included:")
    print("  - ARM_JTAG_20pin_2.54mm (input from J-Link)")
    print("  - ARM_JTAG_20pin_1.27mm (compact output)")
    print("  - TI_CTI_20pin_1.27mm (TI compact with EMU)")
    print("  - TI_JTAG_14pin_2.54mm (TI standard with EMU0/1)")
    print("  - Cortex_Debug_10pin_1.27mm (modern ARM SWD)")
    print("  - R (resistor)")
    print("  - C (capacitor)")
    print("  - GND (ground symbol)")


if __name__ == '__main__':
    main()
