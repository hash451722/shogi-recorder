import pathlib

import cv2
import numpy as np
import onnxruntime as ort



class LocateBoard():
    def __init__(self) -> None:
        path_current_dir = pathlib.Path(__file__).parent
        self.path_board_onnx = path_current_dir.joinpath("models", "board.onnx")


    def run(self, img_src:np.ndarray) -> list:
        x0 = 0
        y0 = 0
        x1 = 0
        y1 = 0
        x2 = 0
        y2 = 0
        x3 = 0
        y3 = 0
        return [(x0, y0), (x1, y1), (x2, y2), (x3, y3)]




if __name__ == "__main__":
    path_current_dir = pathlib.Path(__file__).parent
    path_img_src = path_current_dir.joinpath("sample.jpg")
    print(path_current_dir)

