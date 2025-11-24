"""
KiCad symbol generation for connectors and passive components

This module includes automatic overlap avoidance:
- Calculates optimal symbol width based on pin name lengths
- Adjusts left and right rectangle bounds independently
- Positions Value and Datasheet properties to prevent overlap
- Uses 10mil (0.254mm) grid alignment for cleaner symbols

The overlap detection ensures that long pin names like "SWDIO/TMS",
"SWCLK/TCK", and "GNDDetect" don't extend beyond the symbol rectangle.
"""


def create_pin(num, name, pin_type, side, y_pos):
    """
    Generate a single pin S-expression

    Args:
        num: Pin number (string)
        name: Pin name (string)
        pin_type: Electrical type (power_in, input, output, bidirectional, etc.)
        side: 'left' or 'right'
        y_pos: Y position in mm

    Returns:
        S-expression string for the pin
    """
    x_pos = -10.16 if side == 'left' else 10.16
    angle = 0 if side == 'left' else 180

    return f'''\t\t\t(pin {pin_type} line (at {x_pos} {y_pos} {angle}) (length 2.54)
\t\t\t\t(name "{name}" (effects (font (size 1.27 1.27))))
\t\t\t\t(number "{num}" (effects (font (size 1.27 1.27))))
\t\t\t)'''


def calculate_text_width(text, font_size=1.27):
    """
    Estimate the width of text in KiCad units (mm)

    Args:
        text: The text string
        font_size: Font size in mm (default 1.27)

    Returns:
        Estimated width in mm
    """
    # KiCad uses proportional fonts, approximate width per character
    # Average character width is roughly 0.6 * font_size
    char_width = 0.6 * font_size
    return len(text) * char_width


def create_connector_symbol(name, datasheet, pins):
    """
    Generate a complete connector symbol from pin definitions with automatic
    overlap avoidance for pin names and properties.

    Args:
        name: Symbol name (e.g., "ARM_JTAG_20pin_1.27mm")
        datasheet: Path to datasheet file
        pins: List of tuples (pin_num, pin_name, pin_type, side)

    Returns:
        Complete symbol S-expression
    """
    # Calculate vertical spacing and bounds
    pin_count = len(pins)
    y_spacing = 5.08  # Standard 200mil spacing

    # Find maximum pin name length for each side
    max_left_name_len = 0
    max_right_name_len = 0

    for num, pin_name, pin_type, side in pins:
        name_width = calculate_text_width(pin_name)
        if side == 'left':
            max_left_name_len = max(max_left_name_len, name_width)
        else:
            max_right_name_len = max(max_right_name_len, name_width)

    # Calculate rectangle width with padding
    # Base width from pin connection point (2.54mm) + pin name offset (1.016mm) + text + margin (1mm)
    left_width = max(7.62, 2.54 + 1.016 + max_left_name_len + 1.0)
    right_width = max(7.62, 2.54 + 1.016 + max_right_name_len + 1.0)

    # Round to nearest 0.254mm (10mil) grid
    left_width = round(left_width / 0.254) * 0.254
    right_width = round(right_width / 0.254) * 0.254

    # Calculate positions for each pin (alternating left/right)
    pin_defs = []
    y_start = ((pin_count // 2) - 1) * y_spacing / 2

    for i, (num, pin_name, pin_type, side) in enumerate(pins):
        # Alternating pattern: odd pins on left, even on right
        row = i // 2
        y_pos = y_start - (row * y_spacing)
        pin_defs.append(create_pin(num, pin_name, pin_type, side, y_pos))

    # Calculate rectangle bounds
    rect_top = y_start + 2.54
    rect_bottom = -(y_start + 2.54)

    # Calculate property positions to avoid overlap
    # Reference goes above the symbol
    ref_y = rect_top + 1.27

    # Value goes below - check if symbol name is long
    value_width = calculate_text_width(name)
    value_y = rect_bottom - 1.27
    value_x = 0

    # If symbol name is very long, offset it or move it down further
    if value_width > (left_width + right_width - 2.0):
        value_y = rect_bottom - 2.54  # Move further down

    # Datasheet property position - offset to avoid overlap when visible
    # Place it above and slightly offset from Reference
    datasheet_x = 0.254
    datasheet_y = rect_top + 2.794

    # Build symbol S-expression
    symbol = f'''
\t(symbol "{name}"
\t\t(pin_names (offset 1.016))
\t\t(exclude_from_sim no) (in_bom yes) (on_board yes)
\t\t(property "Reference" "J"
\t\t\t(at 0 {ref_y:.2f} 0)
\t\t\t(effects (font (size 1.27 1.27)))
\t\t)
\t\t(property "Value" "{name}"
\t\t\t(at {value_x:.3f} {value_y:.2f} 0)
\t\t\t(effects (font (size 1.27 1.27)))
\t\t)
\t\t(property "Footprint" ""
\t\t\t(at 0 0 0)
\t\t\t(effects (font (size 1.27 1.27)) hide)
\t\t)
\t\t(property "Datasheet" "{datasheet}"
\t\t\t(at {datasheet_x:.3f} {datasheet_y:.3f} 0)
\t\t\t(effects (font (size 1.27 1.27)) hide)
\t\t)
\t\t(symbol "{name}_1_1"
\t\t\t(rectangle (start -{left_width:.2f} {rect_top:.2f}) (end {right_width:.2f} {rect_bottom:.2f})
\t\t\t\t(stroke (width 0.254) (type default))
\t\t\t\t(fill (type background))
\t\t\t)
{chr(10).join(pin_defs)}
\t\t)
\t)'''
    return symbol


def create_resistor_symbol():
    """
    Create basic resistor symbol

    Returns:
        Complete resistor symbol S-expression
    """
    return '''
\t(symbol "R"
\t\t(pin_numbers hide) (pin_names (offset 0))
\t\t(exclude_from_sim no) (in_bom yes) (on_board yes)
\t\t(property "Reference" "R" (at 2.032 0 90) (effects (font (size 1.27 1.27))))
\t\t(property "Value" "R" (at 0 0 90) (effects (font (size 1.27 1.27))))
\t\t(property "Footprint" "" (at -1.778 0 90) (effects (font (size 1.27 1.27)) hide))
\t\t(property "Datasheet" "~" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
\t\t(symbol "R_0_1"
\t\t\t(rectangle (start -1.016 -2.54) (end 1.016 2.54)
\t\t\t\t(stroke (width 0.254) (type default))
\t\t\t\t(fill (type none))
\t\t\t)
\t\t)
\t\t(symbol "R_1_1"
\t\t\t(pin passive line (at 0 3.81 270) (length 1.27)
\t\t\t\t(name "~" (effects (font (size 1.27 1.27))))
\t\t\t\t(number "1" (effects (font (size 1.27 1.27))))
\t\t\t)
\t\t\t(pin passive line (at 0 -3.81 90) (length 1.27)
\t\t\t\t(name "~" (effects (font (size 1.27 1.27))))
\t\t\t\t(number "2" (effects (font (size 1.27 1.27))))
\t\t\t)
\t\t)
\t)'''


def create_capacitor_symbol():
    """
    Create basic capacitor symbol

    Returns:
        Complete capacitor symbol S-expression
    """
    return '''
\t(symbol "C"
\t\t(pin_numbers hide) (pin_names (offset 0.254))
\t\t(exclude_from_sim no) (in_bom yes) (on_board yes)
\t\t(property "Reference" "C" (at 0.635 2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
\t\t(property "Value" "C" (at 0.635 -2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
\t\t(property "Footprint" "" (at 0.9652 -3.81 0) (effects (font (size 1.27 1.27)) hide))
\t\t(property "Datasheet" "~" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
\t\t(symbol "C_0_1"
\t\t\t(polyline (pts (xy -2.032 -0.762) (xy 2.032 -0.762))
\t\t\t\t(stroke (width 0.508) (type default)) (fill (type none))
\t\t\t)
\t\t\t(polyline (pts (xy -2.032 0.762) (xy 2.032 0.762))
\t\t\t\t(stroke (width 0.508) (type default)) (fill (type none))
\t\t\t)
\t\t)
\t\t(symbol "C_1_1"
\t\t\t(pin passive line (at 0 3.81 270) (length 2.794)
\t\t\t\t(name "~" (effects (font (size 1.27 1.27))))
\t\t\t\t(number "1" (effects (font (size 1.27 1.27))))
\t\t\t)
\t\t\t(pin passive line (at 0 -3.81 90) (length 2.794)
\t\t\t\t(name "~" (effects (font (size 1.27 1.27))))
\t\t\t\t(number "2" (effects (font (size 1.27 1.27))))
\t\t\t)
\t\t)
\t)'''
