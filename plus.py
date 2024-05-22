import random
import time 

times = 10 ;
input("準備好未")
while True:
    input("新一輪開始")
    start = time.time()
    record = [] ;
    for i in range(times) :
        first_value = random.randint(1,10)
        second_value = random.randint(1,10)
        questions = f"{first_value} + {second_value} = "
        ans =int(first_value) + int(second_value)

        while True:
            try:
                ans_user_string =input(questions)
                if ans_user_string == 'x':
                    print("用戶輸入了0000")
                    exit()
                if len(ans_user_string) > 2 :
                   continue
                ans_user =int(ans_user_string)
            except Exception:
                continue
            else:
                break

        consolelog = True if ans_user == ans else False
        record.append([questions ,ans ,ans_user,consolelog])
        print(consolelog)

    end =time.time()
    wrong_ans = []
    for i in record :
        print(i)
        if i[3] == False :
            wrong_ans.append(i)

    wrong_ans_total =len(wrong_ans)

    total_time = end - start
    avg_total_time = total_time / times 
    print("執行時間：", end - start, "秒")
    print("平均每題花費的時間：", avg_total_time, "秒")
    print(f"回答了{times}題，錯了{wrong_ans_total} , 錯題顯示{wrong_ans}")