def solution(lines):
    answer=0
    timeline=[]
    checktime=[]
    for line in lines:
        line=line.lstrip()
        line=line.split(' ')
        dur=float(line[2].replace('s',''))*1000
        HH=int(line[1][0:2])*24*60*1000
        MM=int(line[1][3:5])*60*1000
        SS=float(line[1][6:])*1000
        time=HH+MM+SS
        start_t=time-dur+1

        timeline.append((int(start_t),int(time)))
        checktime.append(start_t)
        checktime.append(time-1)

    for check_t in checktime:
        count=0
        for log in timeline:
            if is_exist(log,check_t):
                count+=1

        if answer < count:
            answer=count

    return answer

def is_exist(log, checktime):
    state=False
    if log[0]<=checktime<log[1]:
        state=True
    if log[0]<=checktime+999<log[1]:
        state=True
    if checktime<=log[0]<log[1]<=checktime+999:
        state=True
    if log[0]<=checktime and checktime+999<=log[1]:
        state=True

    return state



if __name__=="__main__":
    # lines=['2016-09-15 01:00:04.001 2.0s', '2016-09-15 01:00:07.000 2s']
    lines='“2016-09-15 20:59:57.421 0.351s”, “2016-09-15 20:59:58.233 1.181s”, “2016-09-15 20:59:58.299 0.8s”, “2016-09-15 20:59:58.688 1.041s”, “2016-09-15 20:59:59.591 1.412s”, “2016-09-15 21:00:00.464 1.466s”, “2016-09-15 21:00:00.741 1.581s”, “2016-09-15 21:00:00.748 2.31s”, “2016-09-15 21:00:00.966 0.381s”, “2016-09-15 21:00:02.066 2.62s”'
    # lines='“2016-09-15 01:00:04.002 2.0s”, “2016-09-15 01:00:07.000 2s”'
    lines=lines.replace('“','').replace('”','').split(',')
    print(solution(lines))
