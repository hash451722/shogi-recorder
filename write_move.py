import pathlib



class WriteMove():
    def __init__(self) -> None:
        pass



    def run(self, move:str, sfen:str) -> bool:
        return True




if __name__ == "__main__":
    path_current_dir = pathlib.Path(__file__).parent
    print(path_current_dir)
