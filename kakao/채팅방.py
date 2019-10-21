from sys  import stdin
input=stdin.readline

def preprocessing(record):
    li=[]
    l=''
    for s in record:
        if s.isalnum():
            l+=s
        else:
            if l.isalnum():
                li.append(l)
                l=''
    return li


def solution(record):
    answer = []
    events=[]
    dict={}
    for i,s in enumerate(record):
        if s=='Enter':
            id=record[i+1]
            name=record[i+2]
            dict[id]=name
            events.append([s,id])
        elif s=='Leave':
            id = record[i + 1]
            name = record[i + 2]
            events.append([s,id])
        elif s=='Change':
            id = record[i + 1]
            name = record[i + 2]
            dict[id]=name

    for event in events:
        if event[0]=='Enter':
            answer.append('{}님이 들어왔습니다.'.format(dict[event[1]]))
        elif event[0] =='Leave':
            answer.append('{}님이 나갔습니다.'.format(dict[event[1]]))

    return answer

if __name__ == '__main__':
    # record = input()
    record='[“Enter uid1234 Muzi”, “Enter uid4567 Prodo”,”Leave uid1234”,”Enter uid1234 Prodo”,”Change uid4567 Ryan”]'
    record = preprocessing(record)
    answer=solution(record)


