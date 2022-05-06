# 과제: 1 부터 10까지 반복하는 과정에서 3의 배수일 경우, year를 출력하시오
# 추가 과제 : 5의 배수일 때, dream 출력
# 추가 과제2: 15의 배수일 때, yeardream
# 나머지 모든 경우는 숫자 그대로 출력

# $ vi hello.py
# $ git status
# $ git add hello.py
# $ git commit

for x in range(20):
    if x % 3 == 0 and x % 5 == 0 :
        print('yeardream')
    elif x % 3 == 0:
        print('year')
    elif x % 5 == 0:
        print('dream')
