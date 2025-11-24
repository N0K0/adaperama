"""
KiCad utility functions for coordinate conversion and ID generation
"""

import uuid


def mm_to_mils(mm):
    """
    Convert millimeters to mils (thousandths of an inch)

    Note: KiCad internally uses mils. 1 mil = 0.0254mm
    In this project, we use coordinates 1/100th of desired mm placement
    due to the conversion factor creating positions 100x larger.

    Args:
        mm: Value in millimeters (conceptual units in this project)

    Returns:
        Value in mils
    """
    return mm / 0.0254


def generate_uuid():
    """
    Generate a UUID for KiCad components

    Returns:
        UUID string
    """
    return str(uuid.uuid4())
