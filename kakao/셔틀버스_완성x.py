def solution(n,t,m,timetable):
    answer=''
    StartTime='09:00'
    busTime=[]
    for i in range(n):
        busTime.append(i*m)


    return answer


if __name__=='__main__':
    n=1
    t=1
    m=5
    timetable=['08:00','08:02','08:03']
    print(solution(n,t,m,timetable))
