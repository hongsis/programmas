def solution(x):
    answer = 0
    answer = int(x[0]) + int(x[-1])
    return answer

def solution(L, x):
    answer = []
    for i, v in enumerate(L):
        if x == v :
            answer.append(i)

    if answer == []:
        answer.append(-1)
    return answer
