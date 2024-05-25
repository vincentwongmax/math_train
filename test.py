import random
n = 3
questions = '' 
ans = 0 

for j in range(n):
    print(n,j,"nj")
    ran = random.randint(1,10)
    #value.append(random.randint(1,10))
    if j+1 != n :
        questions += f"{ran} + "
    else :
        questions += f"{ran}"
    
    ans += ran 

print(questions)
print(ans)