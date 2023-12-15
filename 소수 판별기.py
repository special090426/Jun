#정수 N (2 <=N <= 10000)
#2부터 N까지의 모든 소수를 공백으로 구분하여 출력

N = int(input())
count = 0 #나중에 count가 2라면 소수

for i in range(2,N+1) :
    for j in range(1,i+1) :
        if i%j==0 :
            count += 1
    if count==2 :
        print("%d " % i,end="")
    count = 0