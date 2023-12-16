# 입력 : 학생 수 N (1 이상 100 이하의 정수)
#        각 학생의 국어, 영어, 수학 점수 (0 이상 100 이하의 정수)
# 출력 : 각 학생의 평균 (소수점 둘째 자리까지 출력)

N = int(input())
aver = []
for i in range(N) :
    score = list(map(int, input().split()))
    SCaver = 0
    for j in range(3) :
        SCaver += score[j]
    aver.append(SCaver/float(3))
for i in range(N) :
    print("%.2f" % aver[i])