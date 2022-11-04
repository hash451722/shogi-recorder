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


    def _preprocess(self, img) -> np.ndarray:
        '''
        抽出した盤面画像の前処理
        入力画像は白黒(channel=1)
        正規化(0-1) -> 標準化(平均, 標準偏差)
        標準化のパラメータ(mean, sd)は学習時の値を設定する
        '''
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_gray01 = img_gray/255.0  # 0-255 -> 0.0-1.0
        img_dst = (img_gray01 - self.mean) / self.sd
        return img_dst


    def _extract_board(self, img, board_corners) -> np.ndarray:
        '''
        盤面の抽出(切り抜き)
        input: OpenCV image, [(x0, y0), (x1, y1), (x2, y2), (x3, y3)]
        return: OpenCV image
        '''
        dstSize = 9*self.cell_size

        pts1 = np.float32(board_corners)
        pts2 = np.float32([[0,0],[dstSize,0],[0,dstSize],[dstSize,dstSize]])

        mat = cv2.getPerspectiveTransform(pts1,pts2)
        img_dst = cv2.warpPerspective(img, mat, (dstSize, dstSize))
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
        for row_img in np.array_split(img, rows, axis=0):
            for chunk in np.array_split(row_img, cols, axis=1):
                squares.append(chunk)

        squares = np.array(squares)
        squares = squares[:, np.newaxis, :, :] # 次元追加　(81, 64, 64) => (81, 1, 64, 64)
        return squares




if __name__ == "__main__":
    import pathlib
    path_current_dir = pathlib.Path(__file__).parent
    path_img = path_current_dir.joinpath("sample.jpg")
    
    img_src = cv2.imread(str(path_img))  # (H, W, C)
    board_corners = [(318, 301), (1254, 300), (320, 1312), (1254, 1314)]

    pb = PreprocessBoard(mean=0.5, sd=0.5)
    img_cells = pb.run(img_src, board_corners)
    print(img_cells.shape)
    print(img_cells)
        
    cv2.imshow("Push Q key", img_cells[15][0])
    cv2.waitKey()  # push q key
