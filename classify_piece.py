import pathlib
import pickle

import numpy as np
import onnxruntime as ort


class ClassifyPiece():
    def __init__(self) -> None:
        self.path_current_dir = pathlib.Path(__file__).parent
        self.path_piece_onnx = self.path_current_dir.joinpath("models", "piece.onnx")
        self.path_pickle = pathlib.Path(__file__).parent.joinpath("models", "classes.pickle")


    def run(self, img:np.ndarray) -> list:
        '''
        マス目で切り出された81個の画像の駒種を分類する. onnx使用.
        input  : (81, 1, 64, 64)
        return : 81マスの駒予測値(3文字で表現、頭文字は先手:b, 後手:w, 空きマスはemp (empty))
        '''
        ort_session = ort.InferenceSession(str(self.path_piece_onnx), providers=['CPUExecutionProvider'])
        outputs = ort_session.run(
            None,
            {"input": img.astype(np.float32)},
        )
        preds = np.array(outputs[0], dtype=float)  # (81, 29)　各駒の確率
        # print(np.exp(preds))
        # print(np.sum(np.exp(preds)))  # 81
        preds_idx = np.argmax(preds, axis=1)  # 最も高い確率の駒idxだけ取り出す
        list81 = self._convert_idx_to_class(preds_idx)  # 3文字のクラス名に変換
        return list81


    def _convert_idx_to_class(self, predicted_idx):
        classes, _ = self._idx_to_name()
        predicted_class = []
        for n, idx in enumerate(predicted_idx):
            predicted_class.append( classes[ str(predicted_idx[n]) ] )
        return predicted_class


    def _idx_to_name(self):
        with open(self.path_pickle, mode='rb') as f:
            classes = pickle.load(f)

        d = {}
        for k, v in classes.items():
            d[str(v)] = k
        return d, len(classes)




if __name__ == "__main__":
    img_cells_dummy = np.random.randn(81, 1, 64, 64)  # (N, C, H, W)

    cf = ClassifyPiece()
    list81 = cf.run(img_cells_dummy)
    print(len(list81))
    print(list81)
