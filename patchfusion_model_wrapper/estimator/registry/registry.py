# Copyright (c) OpenMMLab. All rights reserved.
import torch.nn as nn
from mmengine import Registry
from mmengine.registry import MODELS as MMENGINE_MODELS
from mmengine.registry import DATASETS as MMENGINE_DATASETS

# Check if registries already exist in the parent registry
_scope_name = 'patchfusion_model_wrapper'

# Check if MODELS registry already exists
if _scope_name in MMENGINE_MODELS.children:
    MODELS = MMENGINE_MODELS.children[_scope_name]
else:
    MODELS = Registry('model', parent=MMENGINE_MODELS, locations=['patchfusion_model_wrapper.estimator.models'], scope=_scope_name)

# Check if DATASETS registry already exists  
if _scope_name in MMENGINE_DATASETS.children:
    DATASETS = MMENGINE_DATASETS.children[_scope_name]
else:
    DATASETS = Registry('dataset', parent=MMENGINE_DATASETS, locations=['patchfusion_model_wrapper.estimator.datasets'], scope=_scope_name)
