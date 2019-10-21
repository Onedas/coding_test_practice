def solution(cachesize,cities):
    answer=0
    cache=[]
    for city in cities:
        city=city.upper()
        if city in cache:
            answer+=1
            cache.remove(city)
            cache.append(city)
        else:
            answer+=5
            if len(cache)<cachesize:
                cache.append(city)
            else:
                cache.pop(0)
                cache.append(city)
    return answer


if __name__=='__main__':
    cachesize=2
    # cities=['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']
    cities=['Jeju','Pangyo','NewYork','newyork']
    print(solution(cachesize,cities))