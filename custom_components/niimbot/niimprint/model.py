from enum import Enum
from typing import List, TypedDict, Union

class PrintDirection(Enum):
    TOP = "top"
    LEFT = "left"

class LabelType(Enum):
    WITH_GAPS = "WithGaps"
    BLACK = "Black"
    CONTINUOUS = "Continuous"
    TRANSPARENT = "Transparent"
    HEAT_SHRINK_TUBE = "HeatShrinkTube"
    BLACK_MARK_GAP = "BlackMarkGap"
    PVC_TAG = "PvcTag"
    PERFORATED = "Perforated"

class PrinterModel(Enum):
    UNKNOWN = "UNKNOWN"
    B3S_P = "B3S_P"
    T2S = "T2S"
    N1 = "N1"
    TP2M_H = "TP2M_H"
    B31 = "B31"
    B21_PRO = "B21_PRO"
    B18S = "B18S"
    D11_H = "D11_H"
    B21_H = "B21_H"
    HI_D110 = "HI_D110"
    D110_M = "D110_M"
    M2_H = "M2_H"
    A20 = "A20"
    MP3K_W = "MP3K_W"
    A203 = "A203"
    MP3K = "MP3K"
    K3_W = "K3_W"
    K3 = "K3"
    BETTY = "BETTY"
    T8S = "T8S"
    DXX = "DXX"
    B21S = "B21S"
    B21_L2B = "B21_L2B"
    D11S = "D11S"
    A63 = "A63"
    FUST = "FUST"
    P1 = "P1"
    P18 = "P18"
    S6 = "S6"
    B21S_C2B = "B21S_C2B"
    P1S = "P1S"
    B1 = "B1"
    A8 = "A8"
    B21_C2B = "B21_C2B"
    Z401 = "Z401"
    B16 = "B16"
    B32R = "B32R"
    B32 = "B32"
    D41 = "D41"
    S3 = "S3"
    JC_M90 = "JC_M90"
    JCB3S = "JCB3S"
    B203 = "B203"
    S1 = "S1"
    D61 = "D61"
    D110 = "D110"
    B21 = "B21"
    D101 = "D101"
    HI_NB_D11 = "HI_NB_D11"
    A8_P = "A8_P"
    S6_P = "S6_P"
    T6 = "T6"
    B50W = "B50W"
    T7 = "T7"
    T8 = "T8"
    B3S = "B3S"
    B3 = "B3"
    B18 = "B18"
    D11 = "D11"
    B11 = "B11"
    B50 = "B50"
    ET10 = "ET10"

class PrinterModelMeta(TypedDict):
    model: PrinterModel
    id: List[int]
    dpi: int
    printDirection: PrintDirection
    printheadPixels: int
    paperTypes: List[LabelType]

modelsLibrary: List[PrinterModelMeta] = [
    {
        "model": PrinterModel.B3S_P,
        "id": [272],
        "dpi": 203,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 576,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.BLACK, LabelType.CONTINUOUS, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.T2S,
        "id": [53250],
        "dpi": 203,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 832,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.BLACK],
    },
    {
        "model": PrinterModel.N1,
        "id": [3586],
        "dpi": 203,
        "printDirection": PrintDirection.LEFT,
        "printheadPixels": 120,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.HEAT_SHRINK_TUBE, LabelType.TRANSPARENT, LabelType.BLACK_MARK_GAP],
    },
    {
        "model": PrinterModel.TP2M_H,
        "id": [4609],
        "dpi": 300,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 591,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.BLACK, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.B31,
        "id": [5632],
        "dpi": 203,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 600,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.BLACK, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.B21_PRO,
        "id": [785],
        "dpi": 300,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 591,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.BLACK, LabelType.CONTINUOUS, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.B18S,
        "id": [3585],
        "dpi": 203,
        "printDirection": PrintDirection.LEFT,
        "printheadPixels": 120,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.TRANSPARENT, LabelType.BLACK_MARK_GAP, LabelType.HEAT_SHRINK_TUBE],
    },
    {
        "model": PrinterModel.D11_H,
        "id": [528],
        "dpi": 300,
        "printDirection": PrintDirection.LEFT,
        "printheadPixels": 178,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.B21_H,
        "id": [784],
        "dpi": 300,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 567,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.TRANSPARENT, LabelType.CONTINUOUS, LabelType.BLACK],
    },
    {
        "model": PrinterModel.HI_D110,
        "id": [2305],
        "dpi": 203,
        "printDirection": PrintDirection.LEFT,
        "printheadPixels": 120,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.D110_M,
        "id": [2320],
        "dpi": 203,
        "printDirection": PrintDirection.LEFT,
        "printheadPixels": 120,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.M2_H,
        "id": [4608],
        "dpi": 300,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 591,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.TRANSPARENT, LabelType.BLACK, LabelType.BLACK_MARK_GAP],
    },
    {
        "model": PrinterModel.A20,
        "id": [2817],
        "dpi": 203,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 400,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.BLACK, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.MP3K_W,
        "id": [4867],
        "dpi": 203,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 656,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.BLACK, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.A203,
        "id": [2818],
        "dpi": 203,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 400,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.BLACK, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.MP3K,
        "id": [4866],
        "dpi": 203,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 656,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.BLACK, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.K3_W,
        "id": [4865],
        "dpi": 203,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 656,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.BLACK, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.K3,
        "id": [4864],
        "dpi": 203,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 656,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.BLACK, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.BETTY,
        "id": [2561],
        "dpi": 203,
        "printDirection": PrintDirection.LEFT,
        "printheadPixels": 192,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.T8S,
        "id": [2053],
        "dpi": 300,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 851,
        "paperTypes": [LabelType.WITH_GAPS],
    },
    {
        "model": PrinterModel.B21S,
        "id": [777],
        "dpi": 203,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 384,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.BLACK, LabelType.CONTINUOUS, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.B21_L2B,
        "id": [769],
        "dpi": 203,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 384,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.BLACK, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.D11S,
        "id": [514],
        "dpi": 203,
        "printDirection": PrintDirection.LEFT,
        "printheadPixels": 96,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.A63,
        "id": [2054],
        "dpi": 300,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 851,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.TRANSPARENT, LabelType.BLACK],
    },
    {
        "model": PrinterModel.FUST,
        "id": [513],
        "dpi": 203,
        "printDirection": PrintDirection.LEFT,
        "printheadPixels": 96,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.P1,
        "id": [1024],
        "dpi": 300,
        "printDirection": PrintDirection.LEFT,
        "printheadPixels": 697,
        "paperTypes": [LabelType.PVC_TAG],
    },
    {
        "model": PrinterModel.P18,
        "id": [1026],
        "dpi": 300,
        "printDirection": PrintDirection.LEFT,
        "printheadPixels": 662,
        "paperTypes": [LabelType.PVC_TAG],
    },
    {
        "model": PrinterModel.S6,
        "id": [261],
        "dpi": 203,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 576,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.BLACK, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.B21S_C2B,
        "id": [776],
        "dpi": 203,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 384,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.BLACK, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.P1S,
        "id": [1025],
        "dpi": 300,
        "printDirection": PrintDirection.LEFT,
        "printheadPixels": 662,
        "paperTypes": [LabelType.PVC_TAG],
    },
    {
        "model": PrinterModel.B1,
        "id": [4096],
        "dpi": 203,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 384,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.BLACK, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.A8,
        "id": [256],
        "dpi": 203,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 600,
        "paperTypes": [LabelType.BLACK, LabelType.WITH_GAPS, LabelType.CONTINUOUS],
    },
    {
        "model": PrinterModel.B21_C2B,
        "id": [771, 775],
        "dpi": 203,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 384,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.CONTINUOUS, LabelType.TRANSPARENT, LabelType.BLACK],
    },
    {
        "model": PrinterModel.Z401,
        "id": [2051],
        "dpi": 300,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 851,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.B16,
        "id": [1792],
        "dpi": 203,
        "printDirection": PrintDirection.LEFT,
        "printheadPixels": 96,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.B32R,
        "id": [2050],
        "dpi": 300,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 851,
        "paperTypes": [LabelType.WITH_GAPS],
    },
    {
        "model": PrinterModel.B32,
        "id": [2049],
        "dpi": 300,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 851,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.S3,
        "id": [51460],
        "dpi": 203,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 384,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.BLACK, LabelType.CONTINUOUS, LabelType.PERFORATED],
    },
    {
        "model": PrinterModel.JC_M90,
        "id": [51461],
        "dpi": 203,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 384,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.BLACK, LabelType.CONTINUOUS, LabelType.PERFORATED],
    },
    {
        "model": PrinterModel.JCB3S,
        "id": [256],
        "dpi": 203,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 576,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.BLACK, LabelType.CONTINUOUS, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.B203,
        "id": [2816],
        "dpi": 203,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 400,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.BLACK, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.S1,
        "id": [51458],
        "dpi": 203,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 384,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.BLACK, LabelType.CONTINUOUS, LabelType.PERFORATED],
    },
    {
        "model": PrinterModel.D110,
        "id": [2304, 2305],
        "dpi": 203,
        "printDirection": PrintDirection.LEFT,
        "printheadPixels": 96,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.B21,
        "id": [768],
        "dpi": 203,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 384,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.BLACK, LabelType.CONTINUOUS, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.D101,
        "id": [2560],
        "dpi": 203,
        "printDirection": PrintDirection.LEFT,
        "printheadPixels": 192,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.HI_NB_D11,
        "id": [512],
        "dpi": 203,
        "printDirection": PrintDirection.LEFT,
        "printheadPixels": 120,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.A8_P,
        "id": [273],
        "dpi": 203,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 616,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.BLACK, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.S6_P,
        "id": [274],
        "dpi": 203,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 600,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.T6,
        "id": [51715],
        "dpi": 203,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 384,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.BLACK, LabelType.CONTINUOUS, LabelType.PERFORATED],
    },
    {
        "model": PrinterModel.B50W,
        "id": [51714],
        "dpi": 203,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 384,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.BLACK, LabelType.CONTINUOUS, LabelType.PERFORATED],
    },
    {
        "model": PrinterModel.T7,
        "id": [51717],
        "dpi": 203,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 384,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.BLACK, LabelType.CONTINUOUS, LabelType.PERFORATED],
    },
    {
        "model": PrinterModel.T8,
        "id": [51718],
        "dpi": 300,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 567,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.BLACK, LabelType.CONTINUOUS, LabelType.PERFORATED],
    },
    {
        "model": PrinterModel.B3S,
        "id": [256, 260, 262],
        "dpi": 203,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 576,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.BLACK, LabelType.CONTINUOUS, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.B3,
        "id": [52993],
        "dpi": 203,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 600,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.BLACK, LabelType.CONTINUOUS, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.B18,
        "id": [3584],
        "dpi": 203,
        "printDirection": PrintDirection.LEFT,
        "printheadPixels": 120,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.TRANSPARENT, LabelType.BLACK_MARK_GAP, LabelType.HEAT_SHRINK_TUBE],
    },
    {
        "model": PrinterModel.D11,
        "id": [512],
        "dpi": 203,
        "printDirection": PrintDirection.LEFT,
        "printheadPixels": 96,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.B11,
        "id": [51457],
        "dpi": 203,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 384,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.BLACK, LabelType.CONTINUOUS, LabelType.PERFORATED, LabelType.TRANSPARENT],
    },
    {
        "model": PrinterModel.B50,
        "id": [51713],
        "dpi": 203,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 400,
        "paperTypes": [LabelType.WITH_GAPS, LabelType.BLACK, LabelType.CONTINUOUS, LabelType.PERFORATED],
    },
    {
        "model": PrinterModel.ET10,
        "id": [5376],
        "dpi": 203,
        "printDirection": PrintDirection.TOP,
        "printheadPixels": 1600,
        "paperTypes": [LabelType.CONTINUOUS],
    }
]

def get_printer_meta_by_id(printer_id: int) -> Union[PrinterModelMeta, None]:
    for model in modelsLibrary:
        if printer_id in model["id"]:
            return model
    return None

def get_printer_meta_by_model(model: PrinterModel) -> Union[PrinterModelMeta, None]:
    for m in modelsLibrary:
        if m["model"] == model:
            return m
    return None
