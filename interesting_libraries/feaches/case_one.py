"""AI is creating summary for
"""

from typing import Dict


class Htype:
    """AI is creating summary for
    """
    DEFAULT = "generic"
    IMAGE = "image"
    IMAGE_RGB = "image.rgb"
    IMAGE_GRAY = "image.gray"
    CLASS_LABEL = "class_label"
    BBOX = "bbox"
    BBOX_3D = "bbox.3d"
    VIDEO = "video"
    BINARY_MASK = "binary_mask"
    INSTANCE_LABEL = "instance_label"
    SEGMENT_MASK = "segment_mask"
    KEYPOINTS_COCO = "keypoints_coco"
    POINT = "point"
    AUDIO = "audio"
    TEXT = "text"
    JSON = "json"
    LIST = "list"
    DICOM = "dicom"
    POINT_CLOUD = "point_cloud"
    POINT_CLOUD_CALIBRATION_MATRIX = "point_cloud.calibration_matrix"
    POLYGON = "polygon"


HTYPE_CONFIGURATIONS: Dict[str, Dict] = {
    Htype.DEFAULT: {"dtype": None},
    Htype.IMAGE: {
        "dtype": "uint8",
    },
    Htype.IMAGE_RGB: {
        "dtype": "uint8",
    },
    Htype.IMAGE_GRAY: {
        "dtype": "uint8",
    },
    Htype.CLASS_LABEL: {
        "dtype": "uint32",
        "class_names": [],
        # class_names should be stored in info, not meta
        "_info": ["class_names"],
        "_disable_temp_transform": False,
    },
    Htype.BBOX: {"dtype": "float32", "coords": {}, "_info": ["coords"]},
    Htype.BBOX_3D: {"dtype": "float32", "coords": {}, "_info": ["coords"]},
    Htype.AUDIO: {"dtype": "float64"},
    Htype.VIDEO: {"dtype": "uint8"},
    Htype.BINARY_MASK: {
        "dtype": "bool"
    },
    Htype.INSTANCE_LABEL: {"dtype": "uint32"},
    Htype.SEGMENT_MASK: {
        "dtype": "uint32",
        "class_names": [],
        "_info": ["class_names"],
    },
    Htype.KEYPOINTS_COCO: {"dtype": "int32"},
    Htype.POINT: {"dtype": "int32"},
    Htype.JSON: {
        "dtype": "Any",
    },
    Htype.LIST: {"dtype": "List"},
    Htype.TEXT: {"dtype": "str"},
    Htype.DICOM: {"sample_compression": "dcm"},
    Htype.POINT_CLOUD: {"sample_compression": "las"},
    Htype.POINT_CLOUD_CALIBRATION_MATRIX: {"dtype": "float32"},
    Htype.POLYGON: {"dtype": "float32"}
    }

for config in HTYPE_CONFIGURATIONS.values():
    print(config)

print('<=================================>')

for config in HTYPE_CONFIGURATIONS:
    print(config)

print('<=================================>')

for config in HTYPE_CONFIGURATIONS:
    print(config, HTYPE_CONFIGURATIONS[config])
