import pathlib


def convert_sfen(list81:list) -> str:
    '''
    sfen形式に変換
    input: list81
    return : str  ( [次の手番] [持ち駒] [次は何手目] は除く)
    '''

    # Conversion dictionary for SFEN notation
    cnv = { "ou":"k", "hi":"r", "ka":"b",
            "ki":"g", "gi":"s", "ke":"n", "ky":"l", "fu":"p",
            "ry": "+r", "um":"+b", "ng":"+s", "nk":"+n", "ny":"+l", "to":"+p"}

    sfen = ""
    empty_count = 0
    for i, s in enumerate(list81):
        # delimiter / (slash)
        if i > 0 and (i % 9) == 0:
            sfen += str(empty_count)
            empty_count = 0
            sfen += "/"

        if s[0] == "b":  # black piece
            sfen += str(empty_count)
            empty_count = 0
            sfen += cnv[s[1:]].upper()

        elif s[0] == "w":  # white piece
            sfen += str(empty_count)
            empty_count = 0
            sfen += cnv[s[1:]].lower()

        else:  # empty cell
            empty_count += 1
    
    sfen += str(empty_count)
    return sfen.replace("0", "")




def cas(csa:str) -> str:
    
    turn = csa[0]









if __name__ == "__main__":
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

    sfen = convert_sfen(list81)
    print(sfen)
