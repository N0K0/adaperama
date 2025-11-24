"""
Connector pin definitions for JTAG/SWD adapters

Each connector is defined as a list of tuples:
    (pin_number, pin_name, electrical_type, side)

Electrical types:
    - power_in: Power pins (VTref, GND)
    - input: Input signals (TMS, TDI, TCK, etc.)
    - output: Output signals (TDO, RTCK, SWO)
    - bidirectional: Bidirectional signals (SWDIO, EMU pins)
    - open_collector: Open collector outputs (nRESET, nSRST)
    - no_connect: Not connected pins (NC, KEY)

Side:
    - left: Pin appears on left side of symbol
    - right: Pin appears on right side of symbol
"""

# ============================================================================
# ARM JTAG 20-pin 1.27mm - Standard ARM JTAG connector
# ============================================================================

ARM_20PIN_PINS = [
    # (pin_num, name, type, side)
    ('1', 'VTref', 'power_in', 'left'),
    ('2', 'GND', 'power_in', 'right'),
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

# ============================================================================
# TI CTI-20 1.27mm - Texas Instruments Compact JTAG
# ============================================================================
# Note: Different pinout from ARM standard!
# - TMS on pin 1 instead of VTref
# - VTref is NOT on connector (separate connection)
# - Includes EMU0-3 pins for enhanced debugging

TI_CTI_20PIN_PINS = [
    ('1', 'TMS', 'input', 'left'),
    ('2', 'GND', 'power_in', 'right'),
    ('3', 'TDI', 'input', 'left'),
    ('4', 'GND', 'power_in', 'right'),
    ('5', 'TDO', 'output', 'left'),
    ('6', 'GND', 'power_in', 'right'),
    ('7', 'TCK', 'input', 'left'),
    ('8', 'GND', 'power_in', 'right'),
    ('9', 'nTRST', 'input', 'left'),
    ('10', 'GND', 'power_in', 'right'),
    ('11', 'nSRST', 'open_collector', 'left'),
    ('12', 'GND', 'power_in', 'right'),
    ('13', 'EMU0', 'bidirectional', 'left'),
    ('14', 'GND', 'power_in', 'right'),
    ('15', 'EMU1', 'bidirectional', 'left'),
    ('16', 'GND', 'power_in', 'right'),
    ('17', 'EMU2', 'bidirectional', 'left'),
    ('18', 'GND', 'power_in', 'right'),
    ('19', 'EMU3', 'bidirectional', 'left'),
    ('20', 'GND', 'power_in', 'right'),
]

# ============================================================================
# ARM Cortex Debug 10-pin 1.27mm - Modern ARM SWD/JTAG connector
# ============================================================================
# Note: Compact connector supporting both SWD and JTAG modes
# - Pin 7 is KEY (mechanical, not connected)
# - Dual-function pins: SWDIO/TMS, SWCLK/TCK, SWO/TDO

CORTEX_10PIN_PINS = [
    ('1', 'VTref', 'power_in', 'left'),
    ('2', 'SWDIO/TMS', 'bidirectional', 'right'),
    ('3', 'GND', 'power_in', 'left'),
    ('4', 'SWCLK/TCK', 'input', 'right'),
    ('5', 'GND', 'power_in', 'left'),
    ('6', 'SWO/TDO', 'output', 'right'),
    ('7', 'KEY', 'no_connect', 'left'),
    ('8', 'TDI', 'input', 'right'),
    ('9', 'GNDDetect', 'power_in', 'left'),
    ('10', 'nRESET', 'open_collector', 'right'),
]

# ============================================================================
# TI 14-pin JTAG 2.54mm - Texas Instruments Standard JTAG
# ============================================================================
# Note: Features EMU0/1 pins for cross-core triggering and advanced debug
# - Commonly used with C2000, C5000, C6000 DSPs
# - Pin 6 is KEY (mechanical keying)

TI_14PIN_PINS = [
    ('1', 'TMS', 'input', 'left'),
    ('2', 'nTRST', 'input', 'right'),
    ('3', 'TDI', 'input', 'left'),
    ('4', 'TDIS', 'input', 'right'),
    ('5', 'VTref', 'power_in', 'left'),
    ('6', 'KEY', 'no_connect', 'right'),
    ('7', 'TDO', 'output', 'left'),
    ('8', 'GND', 'power_in', 'right'),
    ('9', 'RTCK', 'output', 'left'),
    ('10', 'GND', 'power_in', 'right'),
    ('11', 'TCK', 'input', 'left'),
    ('12', 'GND', 'power_in', 'right'),
    ('13', 'EMU0', 'bidirectional', 'left'),
    ('14', 'EMU1', 'bidirectional', 'right'),
]

# ============================================================================
# Connector Metadata
# ============================================================================

CONNECTOR_INFO = {
    'ARM_JTAG_20pin_1.27mm': {
        'pins': ARM_20PIN_PINS,
        'datasheet': 'connector-specs/ARM-20pin-1.27mm.md',
        'description': 'Standard ARM 20-pin JTAG connector',
    },
    'TI_CTI_20pin_1.27mm': {
        'pins': TI_CTI_20PIN_PINS,
        'datasheet': 'connector-specs/TI-CTI-20-1.27mm.md',
        'description': 'TI Compact JTAG with EMU pins',
    },
    'Cortex_Debug_10pin_1.27mm': {
        'pins': CORTEX_10PIN_PINS,
        'datasheet': 'connector-specs/Cortex-10pin-1.27mm.md',
        'description': 'ARM Cortex SWD/JTAG Debug connector',
    },
    'TI_JTAG_14pin_2.54mm': {
        'pins': TI_14PIN_PINS,
        'datasheet': 'connector-specs/TI-14pin-2.54mm.md',
        'description': 'TI 14-pin JTAG with EMU0/1',
    },
}
