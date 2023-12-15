# 입력 : 한 마디(문장) 문자열 (공백 없이)
#        찾을 단어 문자열 (공백 없이)
# 출력 : 단어의 등장 횟수

sen = list(map(str,input()))
Fsen = list(map(str,input()))
Quantity = []
for i in range(len(Fsen)) :
    count = 0
    for j in range(len(sen)) :
        if Fsen[i] in sen[j] :
            count += 1
    Quantity.append(count)
print(min(Quantity))