

class IsMove():
    '''
    指し手を判定する
    '''
    def __init__(self) -> None:
        self.phase_previous = self.phase_init()[:]


    def run(self, phase0:list, phase1:list) -> str:
        '''
        return csa
        ex. "+7776FU"
        '''
        move = self.move_csa(phase0, phase1)
        return move


    def move_csa(self, phase0:list, phase1:list) -> str:
        # 局面に変化が無い場合
        if phase0 == phase1:
            print("局面に変化なし")
            return None

        changed_cell_idx = []
        for i, (p0, p1) in enumerate(zip(phase0, phase1)):
            if p0 != p1:
                changed_cell_idx.append(i)

        piece = None  # 動かした駒
        if len(changed_cell_idx) == 1:  # 駒台から打った
            pos0 = "00"
            pos1 = self.idx_table(changed_cell_idx[0])
            piece = phase1[changed_cell_idx[0]]

        elif len(changed_cell_idx) == 2:  # 盤上の駒を動かした
            if phase1[changed_cell_idx[0]] == "emp":
                pos0 = self.idx_table(changed_cell_idx[0])
                pos1 = self.idx_table(changed_cell_idx[1])
                piece = phase1[changed_cell_idx[1]]
            else:
                pos0 = self.idx_table(changed_cell_idx[1])
                pos1 = self.idx_table(changed_cell_idx[0])
                piece = phase1[changed_cell_idx[0]]
        else:  # 誤認識
            move = None
            print("Misrecognition")
        
        if piece is not None:
            turn = "+" if piece[0] == "b" else "-"
            move = turn + pos0 + pos1 + piece[1:].upper()

        # print(changed_cell_idx)
        # print(move)
        return move



    def phase_init(self) -> list:
        '''
        平手初期配置
        '''
        list81 = [
            "wky", "wke", "wgi", "wki", "wou", "wki", "wgi", "wke", "wky",
            "emp", "whi", "emp", "emp", "emp", "emp", "emp", "wka", "emp",
            "wfu", "wfu", "wfu", "wfu", "wfu", "wfu", "wfu", "wfu", "wfu",
            "emp", "emp", "emp", "emp", "emp", "emp", "emp", "emp", "emp",
            "emp", "emp", "emp", "emp", "emp", "emp", "emp", "emp", "emp",
            "emp", "emp", "emp", "emp", "emp", "emp", "emp", "emp", "emp",
            "bfu", "bfu", "bfu", "bfu", "bfu", "bfu", "bfu", "bfu", "bfu",
            "emp", "bka", "emp", "emp", "emp", "emp", "emp", "bhi", "emp",
            "bky", "bke", "bgi", "bki", "bou", "bki", "bgi", "bke", "bky"
        ]
        return list81[:]


    def phase_empty(self) -> list:
        list81 = ["emp"]*81
        return list81[:]



    def idx_table(self, idx:int) -> str:
        suji = 9 - idx % 9
        dan = 1 + idx // 9
        num2kanji = {
            "1":"一", "2":"二", "3":"三", "4":"四", "5":"五", "6":"六", "7":"七", "8":"八", "9":"九"
        }
        num2alphabet = {
            "1":"a", "2":"b", "3":"c", "4":"d", "5":"e", "6":"f", "7":"g", "8":"h", "9":"i"
        }
        # return str(suji*10 + dan), str(suji)+num2kanji[str(dan)], str(suji)+num2alphabet[str(dan)]
        return str(suji*10 + dan)




if __name__ == "__main__":
    im = IsMove()
    # print(im.idx_table(56))

    # 平手初期配置
    phase0 = [
        "wky", "wke", "wgi", "wki", "wou", "wki", "wgi", "wke", "wky",
        "emp", "whi", "emp", "emp", "emp", "emp", "emp", "wka", "emp",
        "wfu", "wfu", "wfu", "wfu", "wfu", "wfu", "wfu", "wfu", "wfu",
        "emp", "emp", "emp", "emp", "emp", "emp", "emp", "emp", "emp",
        "emp", "emp", "emp", "emp", "emp", "emp", "emp", "emp", "emp",
        "emp", "emp", "emp", "emp", "emp", "emp", "emp", "emp", "emp",
        "bfu", "bfu", "bfu", "bfu", "bfu", "bfu", "bfu", "bfu", "bfu",
        "emp", "bka", "emp", "emp", "emp", "emp", "emp", "bhi", "emp",
        "bky", "bke", "bgi", "bki", "bou", "bki", "bgi", "bke", "bky"
    ]
    # ▲７六歩
    phase1 = [
        "wky", "wke", "wgi", "wki", "wou", "wki", "wgi", "wke", "wky",
        "emp", "whi", "emp", "emp", "emp", "emp", "emp", "wka", "emp",
        "wfu", "wfu", "wfu", "wfu", "wfu", "wfu", "wfu", "wfu", "wfu",
        "emp", "emp", "emp", "emp", "emp", "emp", "emp", "emp", "emp",
        "emp", "emp", "emp", "emp", "emp", "emp", "emp", "emp", "emp",
        "emp", "emp", "bfu", "emp", "emp", "emp", "emp", "emp", "emp",
        "bfu", "bfu", "emp", "bfu", "bfu", "bfu", "bfu", "bfu", "bfu",
        "emp", "bka", "emp", "emp", "emp", "emp", "emp", "bhi", "emp",
        "bky", "bke", "bgi", "bki", "bou", "bki", "bgi", "bke", "bky"
    ]

    csa_move = im.run(phase0, phase1)
    print(csa_move)
