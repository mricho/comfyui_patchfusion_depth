import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from .patchfusion import PatchFusion

NODE_CLASS_MAPPINGS = {
    "PatchFusion": PatchFusion
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PatchFusion": "PatchFusion"
}
