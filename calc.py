out = 0  # 計算結果
typ = 0  # 計算用の入力数値
mode = 0  # mode選択用

print("Starting calculator...\n", end='')
while True:
    print("Please select the calc mode. (\"+\" or \"-\" or \"*\" or \"/\" or \"q\")\nMode? : ", end='')
    mode = input()              # モード選択
    if mode == "q":             # 'q'を入力したら終了．30行目にジャンプ
        break

    if mode != "+" and mode != "-" and mode != "*" and mode != "/":  # 存在しない演算モードの場合
        print("Please select the correct mode.\n\n", end='')
        continue                # これより下の処理を無視して，ループ先頭に戻る

    print("Please input the number.(int type ONLY)\nNumber? : ", end='')
    typ = input()               # 数値入力

    if mode == "+":             # 足し算
        out = out + int(typ)
    if mode == "-":             # 引き算
        out = out - int(typ)
    if mode == "*":             # 掛け算
        out = out * int(typ)
    if mode == "/":             # 割り算
        out = out / int(typ)

    print("Result : " + str(out) + "\n\n", end='')
# end while
print("FINAL RESULT : " + str(out) + "\nQuit\n", end='')
