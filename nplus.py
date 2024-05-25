import random
import time 
import csv

###setting area 
n = 6
n_random = [True,10,13] 
pi_length = 20
times = 5 
pi ='3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
###

while True:
    input("準備好未")
    a = random.randint(0,len(pi) - pi_length)
    new_pi = pi[a:a+pi_length]
    start_pi = time.time()
    while True:
        start_value = input(f"新一輪開始, 準備好請輸入({new_pi}) : ")
        if start_value == new_pi :
            break
    end_pi = time.time()

    start = time.time()
    record = [] ;

    for i in range(times) :
        questions = ''
        ans = 0 
        if n_random[0] == True:
            n = random.randint(n_random[1],n_random[2])
        for j in range(n):
            ran = random.randint(1,10)
            if j+1 != n :
                questions += f"{ran} + "
            else :
                questions += f"{ran} = "
            ans += ran 

        while True:
            try:
                ans_user_string =input(questions)
                if ans_user_string == 'x':
                    print("用戶輸入了0000")
                    exit()
                if len(ans_user_string) > len(str(ans))  :
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
    wrong_ans = [i for i in record if not i[3]]
    wrong_ans_total =len(wrong_ans)

    total_time = end - start
    avg_total_time = total_time / times 
    pi_time = end_pi - start_pi
    print("執行時間：", end - start, "秒")
    print("平均每題花費的時間：", avg_total_time, "秒")
    print(f"回答了{times}題，錯了{wrong_ans_total}題 , 錯題顯示{wrong_ans}")
    
    data = [pi_time,times,total_time,avg_total_time,wrong_ans_total]

    for i in wrong_ans :
        data.append(i)

    with open('ndata.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data) 