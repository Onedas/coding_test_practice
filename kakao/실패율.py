# 실패율
# 스테이지 도달했으나 아직 클리어하지 못한 플레이어의 수/ 스테이지에 도달한 플레이어 수
from sys import stdin
input=stdin.readline


def solution(N, stages):
    answer = []

    f={}
    histogram=[0 for _ in range(N+2)]
    for stage in stages:
        histogram[stage]+=1
    for i in range(1,N+1):
        fail=histogram[i]/sum(histogram[i:])
        try:
            f[fail].append(i)
        except:
            f[fail]=[i]
    while f:
        for i in f.pop(max(f)):
            answer.append(i)
    return answer

print(solution(4,[4,4,4,4,4]))