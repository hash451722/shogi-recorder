

class IsMove():
    '''
    一手指されたか判定する
    '''
    def __init__(self) -> None:
        self.phase_previous = self.phase_init()[:]


    def run(self, pahse:list) -> bool:
        '''
        return
        ex. "1二歩", "9/9/9/9/9/9/9/9/9"
        '''

        return True


    def compare_phase(self, phase:list) -> bool:
        if phase == self.phase_previous:
            return False

        list81 = []
        for p0, p1 in zip(self.phase_previous, phase):
            if p0 == p1:
                list81.append(False)
            else:
                list81.append(True)

        print(sum(list81))
        if sum(list81) == 1:
            print("駒台から打った")
        elif sum(list81) == 2:
            print("一手指した")
        if sum(list81) > 2:
            print("誤検出")


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
            "wky", "wke", "wgi", "wki", "wou", "wki", "wgi", "wke", "wky"
        ]
        return list81[:]


    def phase_empty(self) -> list:
        list81 = ["emp"]*81
        return list81[:]



if __name__ == "__main__":
    im = IsMove()

    p = im.phase_init()[:]
    p[0] = "emp"

    list81 = im.compare_phase(p)
    print(list81)
