out = 0
# 計算結果
typ = 0
# 計算用の入力数値
mode = 0
# mode選択用
flag = 0
# y or n フラグ用
checkflag = -1
# inの入力の是非(-1: 初回時のみ)
his_operand = 0
# 履歴を1回分保存
his_num = 0
# 履歴を1回分保存

print("Starting calculator...")
while True:
    print("Please select the calc mode. (\"+\" or \"-\" or \"*\" or \"/\" or \"0\" or \"c\" or \"h\" or \"q\")\nMode? : ")
    mode = input()
    if mode == "q":
        break
    if mode == "0":
        print("Do you want to reset calculation result? (y or N)\n")
        flag = input()
        if flag == "y":
            print("Reset calculation result.\n\n")
            out = 0
        else:
            print("Operation Cancelled.\n\n")

        continue

    if mode == "c":
        print("Result : " + str(out) + "\n\n")
        continue

    if mode == "h":
        if checkflag == -1:
            print("Cannot use history func before calculating once.\n\n")
            continue

        print("Do you want to calc " + his_operand +
              str(his_num) + " again? (y or N)\n")
        flag = input()
        if flag == "y":
            print("Calculated " + his_operand + str(his_num) + " again.\n")
            mode = his_operand
            typ = his_num
            checkflag = 1
        else:
            print("Operation cancelled.")
            continue

    if mode != "+" and "-" and "*" and "/":
        print("Please select the correct mode.\n\n")
        continue

    if checkflag <= 0:
        print("Please input the number.(int type ONLY)\nNumber? : ")
        typ = input()

    his_operand = mode
    his_num = typ

    if mode == "+":
        out = out + int(typ)
    if mode == "-":
        out = out - int(typ)
    if mode == "*":
        out = out * int(typ)
    if mode == "/":
        if typ != 0:
            out = out / int(typ)
        else:
            print("Cannot divide by zero.\nOperarion denied.\n")

    print("Result : " + str(out) + "\n\n")
    checkflag = 0

print("FINAL RESULT : " + str(out) + "\nQUit\n")
