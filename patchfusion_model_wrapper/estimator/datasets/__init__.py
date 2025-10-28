import sys

if 'patchfusion_model_wrapper.estimator.datasets.u4k_dataset' not in sys.modules:
    from .u4k_dataset import UnrealStereo4kDataset
    from .general_dataset import ImageDataset

from .builder import build_dataset

__all__ = [
    'build_dataset',
]

# Dynamically add to __all__ if the modules were imported successfully
if 'patchfusion_model_wrapper.estimator.datasets.u4k_dataset' in sys.modules:
    __all__.append('UnrealStereo4kDataset')
if 'patchfusion_model_wrapper.estimator.datasets.general_dataset' in sys.modules:
    __all__.append('ImageDataset')
