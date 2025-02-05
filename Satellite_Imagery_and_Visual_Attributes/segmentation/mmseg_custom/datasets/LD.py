# Copyright (c) OpenMMLab. All rights reserved.
from mmseg.datasets.builder import DATASETS
from mmseg.datasets.custom import CustomDataset

@DATASETS.register_module(force=True)
class LD(CustomDataset):
    """ISPRS Potsdam dataset.

    In segmentation map annotation for Potsdam dataset, 0 is the ignore index.
    ``reduce_zero_label`` should be set to True. The ``img_suffix`` and
    ``seg_map_suffix`` are both fixed to '.png'.
    """
    CLASSES = ('background', 'road')

    PALETTE = [[255, 255, 255], [0, 255, 255]]

    def __init__(self, **kwargs):
        super(LD, self).__init__(
            img_suffix='.png',
            seg_map_suffix='.png',
            #reduce_zero_label=True,
            reduce_zero_label=False,
            **kwargs)
