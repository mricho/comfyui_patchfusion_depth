import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from .patchfusion import PatchFusionNode

NODE_CLASS_MAPPINGS = {
    "PatchFusion": PatchFusionNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PatchFusion": "PatchFusion"
}
