
"""
imageinputで、盤面情報は受け取っている
深さ優先探索により実装
"""
def solver(boards, x=0, y=0):
    "数独を解く"
    if y > 8: #行数が9を超えたら終了
        return True
    elif boards[y][x] != 0: #空欄ではない場合を考える
        if x == 8: #9列目までいったら次の行に移動
            if solver(boards, 0, y+1):
                return True
        else:#そうでなければ同行の次の列へ
            if solver(boards, x+1, y):
                return True
    else:#空欄の場合、深さ優先探索
        for i in range(1, 10):#1から9までの数字を全て試す
            if check(boards, x, y, i): #チェックする
                boards[y][x] = i #OKなら数字を入れる
                if x == 8: #8列までいったら次の行に移動
                    if solver(boards, 0, y+1):
                        return True
                else:
                    if solver(boards, x+1, y):
                        return True
        boards[y][x] = 0 #戻ってきたら0に戻す
        return False

def check(values, x, y, i):
    if row(values, y, i) and column(values, x, i) and block(values, x, y, i):
        return True
    return False

def row(values, y, i):
    "横をチェック"
    return all(True if i != values[y][_x] else False for _x in range(9))

def column(values, x, i):
    "縦をチェック"
    return all(True if i != values[_y][x] else False for _y in range(9))

def block(values, x, y, i):
    "3x3のブロックをチェック"
    xbase = (x // 3) * 3
    ybase = (y // 3) * 3
    return all(True if i != values[_y][_x] else False
            for _y in range(ybase, ybase + 3)
                for _x in range(xbase, xbase + 3))
            
