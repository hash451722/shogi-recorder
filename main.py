import pathlib

import cv2

import preprocess_board
import classify_piece



def test():

    path_current_dir = pathlib.Path(__file__).parent
    path_img = path_current_dir.joinpath("sample.jpg")
    
    
    pb = preprocess_board.PreprocessBoard()
    cp = classify_piece.ClassifyPiece()




    img_src = cv2.imread(str(path_img))  # (H, W, C)
    board_corners = [(55, 36), (743, 26), (60, 762), (739, 766)]



    img_cells = pb.run(img_src, board_corners)

    print(img_cells.shape)

    list81 = cp.run(img_cells)

    print(list81)




if __name__ == "__main__":
    # path_current_dir = pathlib.Path(__file__).parent
    # path_sample_board = path_current_dir.joinpath("sample.jpg")

    test()
    