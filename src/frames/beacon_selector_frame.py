"""
Filename: beacon_selector_frame.py
Date Created: 10/1/2022
"""

from mods import MODS

if MODS == 'vanilla':
    from frames.beacon_selector_frame_vanilla import BeaconSelectorFrame as BEACON_FRAME

BeaconSelectorFrame = BEACON_FRAME