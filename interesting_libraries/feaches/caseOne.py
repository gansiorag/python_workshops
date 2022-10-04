from typing import Dict

class htype:
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
    htype.DEFAULT: {"dtype": None},
    htype.IMAGE: {
        "dtype": "uint8",
    },
    htype.IMAGE_RGB: {
        "dtype": "uint8",
    },
    htype.IMAGE_GRAY: {
        "dtype": "uint8",
    },
    htype.CLASS_LABEL: {
        "dtype": "uint32",
        "class_names": [],
        "_info": ["class_names"],  # class_names should be stored in info, not meta
        "_disable_temp_transform": False,
    },
    htype.BBOX: {"dtype": "float32", "coords": {}, "_info": ["coords"]},
    htype.BBOX_3D: {"dtype": "float32", "coords": {}, "_info": ["coords"]},
    htype.AUDIO: {"dtype": "float64"},
    htype.VIDEO: {"dtype": "uint8"},
    htype.BINARY_MASK: {
        "dtype": "bool"
    },  # TODO: pack numpy arrays to store bools as 1 bit instead of 1 byte
    htype.INSTANCE_LABEL: {"dtype": "uint32"},
    htype.SEGMENT_MASK: {
        "dtype": "uint32",
        "class_names": [],
        "_info": ["class_names"],
    },
    htype.KEYPOINTS_COCO: {"dtype": "int32"},
    htype.POINT: {"dtype": "int32"},
    htype.JSON: {
        "dtype": "Any",
    },
    htype.LIST: {"dtype": "List"},
    htype.TEXT: {"dtype": "str"},
    htype.DICOM: {"sample_compression": "dcm"},
    htype.POINT_CLOUD: {"sample_compression": "las"},
    htype.POINT_CLOUD_CALIBRATION_MATRIX: {"dtype": "float32"},
    htype.POLYGON: {"dtype": "float32"},
}
for config in HTYPE_CONFIGURATIONS.values():
    print(config)
print('<=================================>')    
for config in HTYPE_CONFIGURATIONS:
    print(config)
    
print('<=================================>')    
for config in HTYPE_CONFIGURATIONS:
    print(config, HTYPE_CONFIGURATIONS[config])