"""
KiCad component instance and text label generation
"""

from kicad_utils import mm_to_mils, generate_uuid


def create_component(ref, value, lib_id, x_mm, y_mm, footprint="", properties=None):
    """
    Create a component instance

    Args:
        ref: Reference designator (e.g., "R1", "J2")
        value: Component value (e.g., "10k", "100nF")
        lib_id: Symbol library ID (e.g., "R", "ARM_JTAG_20pin_1.27mm")
        x_mm: X position in mm (conceptual units - see kicad_utils.mm_to_mils)
        y_mm: Y position in mm (conceptual units - see kicad_utils.mm_to_mils)
        footprint: Footprint library path (optional)
        properties: Dictionary of additional properties (optional)

    Returns:
        Component instance S-expression
    """
    uuid_str = generate_uuid()
    x = mm_to_mils(x_mm)
    y = mm_to_mils(y_mm)
    props = properties or {}

    comp = f'\t(symbol (lib_id "{lib_id}") (at {x:.4f} {y:.4f} 0) (unit 1)\n'
    comp += f'\t\t(exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)\n'
    comp += f'\t\t(uuid {uuid_str})\n'
    comp += f'\t\t(property "Reference" "{ref}" (at {x:.4f} {y - mm_to_mils(3):.4f} 0)\n'
    comp += f'\t\t\t(effects (font (size 1.27 1.27)))\n'
    comp += f'\t\t)\n'
    comp += f'\t\t(property "Value" "{value}" (at {x:.4f} {y + mm_to_mils(3):.4f} 0)\n'
    comp += f'\t\t\t(effects (font (size 1.27 1.27)))\n'
    comp += f'\t\t)\n'
    if footprint:
        comp += f'\t\t(property "Footprint" "{footprint}" (at {x:.4f} {y:.4f} 0)\n'
        comp += f'\t\t\t(effects (font (size 1.27 1.27)) hide)\n'
        comp += f'\t\t)\n'
    comp += f'\t\t(property "Datasheet" "~" (at {x:.4f} {y:.4f} 0)\n'
    comp += f'\t\t\t(effects (font (size 1.27 1.27)) hide)\n'
    comp += f'\t\t)\n'
    for prop_name, prop_value in props.items():
        comp += f'\t\t(property "{prop_name}" "{prop_value}" (at {x:.4f} {y:.4f} 0)\n'
        comp += f'\t\t\t(effects (font (size 1.27 1.27)) hide)\n'
        comp += f'\t\t)\n'
    comp += f'\t\t(instances\n'
    comp += f'\t\t\t(project "adapterama"\n'
    comp += f'\t\t\t\t(path "/" (reference "{ref}") (unit 1))\n'
    comp += f'\t\t\t)\n'
    comp += f'\t\t)\n'
    comp += f'\t)\n'
    return comp


def create_text_label(text, x_mm, y_mm, size=2.54):
    """
    Create text label

    Args:
        text: Label text
        x_mm: X position in mm (conceptual units)
        y_mm: Y position in mm (conceptual units)
        size: Font size (default 2.54)

    Returns:
        Text label S-expression
    """
    x = mm_to_mils(x_mm)
    y = mm_to_mils(y_mm)
    uuid_str = generate_uuid()
    label = f'\t(text "{text}" (exclude_from_sim no)\n'
    label += f'\t\t(at {x:.4f} {y:.4f} 0)\n'
    label += f'\t\t(effects (font (size {size} {size}) bold) (justify left))\n'
    label += f'\t\t(uuid {uuid_str})\n'
    label += f'\t)\n'
    return label
