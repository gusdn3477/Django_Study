num = input('주민등록번호를 입력하세요 : ').split('-')
lotto = []
repeat = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
ct = 0
total = 0

for i in range(len(num)):
    for j in range(6):
        total += int(num[i][j]) * repeat[ct]
        ct += 1

remainder = total % 11
code = 11 - remainder

if int(num[1][-1]) == code:
    print('성공')

else:
    print('실패')