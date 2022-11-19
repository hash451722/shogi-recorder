import cv2
import numpy as np



class PreprocessBoard():
    def __init__(self, cell_size:int=64, mean:float=0.5, sd:float=0.5) -> None:
        self.cell_size = cell_size
        self.mean = mean
        self.sd = sd


    def run(self, img_src:np.ndarray, board_corners:list) -> np.ndarray:
        img_extract = self._extract_board(img_src, board_corners)  # (576, 576, 3)
        img_preprocessed = self._preprocess(img_extract)  # (576, 576)
        img_cells = self._parcellate_board(img_preprocessed)  # (81, 1, 64, 64)
        return img_cells


    def _extract_board(self, img, board_corners) -> np.ndarray:
        '''
        盤面の抽出(切り抜き)
        input: OpenCV image, [(x0, y0), (x1, y1), (x2, y2), (x3, y3)]
        return: OpenCV image (H, W, C)
        '''
        dstSize = 9*self.cell_size

        pts1 = np.float32(board_corners)
        pts2 = np.float32([[0,0],[dstSize,0],[0,dstSize],[dstSize,dstSize]])

        mat = cv2.getPerspectiveTransform(pts1,pts2)
        img_dst = cv2.warpPerspective(img, mat, (dstSize, dstSize))
        return img_dst


    def _preprocess(self, img_bgr) -> np.ndarray:
        '''
        抽出した盤面画像の前処理
        入力画像はBGR(channels=3)
        正規化(0-1) -> 標準化(平均, 標準偏差)
        標準化のパラメータ(mean, sd)は学習時の値を設定する
        '''
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        img_rgb01 = img_rgb/255.0  # 0-255 -> 0.0-1.0
        img_std = (img_rgb01 - self.mean) / self.sd
        img_dst = np.transpose(img_std, (2, 0, 1))  # (H, W, C) -> (C, H, W)
        return img_dst


    def _parcellate_board(self, img) -> np.ndarray:
        '''
        81マスに画像を切り分け
        input: openCV image
        return: ndarray (81, channel, height, width)
        '''
        rows = 9  # 行数　段
        cols = 9  # 列数　筋

        squares = []
        for row_img in np.array_split(img, rows, axis=1):
            for chunk in np.array_split(row_img, cols, axis=2):
                squares.append(chunk)

        squares = np.array(squares)
        # squares = squares[:, np.newaxis, :, :] # 次元追加　(81, 64, 64) => (81, 1, 64, 64)
        return squares




if __name__ == "__main__":
    import pathlib
    path_current_dir = pathlib.Path(__file__).parent
    path_img = path_current_dir.joinpath("sample.jpg")
    
    img_src = cv2.imread(str(path_img))  # (H, W, C)
    board_corners = [(55, 36), (743, 26), (60, 762), (739, 766)]

    pb = PreprocessBoard(mean=0, sd=1)

    # img_b = pb._extract_board(img_src, board_corners)
    # cv2.imshow("Push Q key", img_b)
    # cv2.waitKey()  # push q key
    # exit()

    img_cells = pb.run(img_src, board_corners)
    print(img_cells)
    print(type(img_cells))
    print(img_cells.shape)
    print(type(img_cells[0]))
        
    # cv2.imshow("Push Q key", img_cells[10])
    # cv2.waitKey()  # push q key


    # # check
    # import torch
    # import torchvision
    # x = torch.from_numpy(img_cells[79].astype(np.float32)).clone()  # numpy to tensor
    # torchvision.utils.save_image(x, "temp.png")
