# Assignment of Classroom
# https://www.acmicpc.net/problem/11000

"""
난이도: 보통
시간: 30분

1. 어떤 자료구조를 사용해야 하는가?
=> 최소의 강의실을 사용하도록, 여러 강의를 '할당'하는 문제.
=> 다음과 같이 해석 가능.
=> 최소의 '기계'를 사용하도록, 여러 '작업'을 '할당'하는 문제.
=> '머신 스케쥴링' : 대표적인 우선순위 큐 활용문제.
=> LPT 알고리즘을 사용한다. (가장 긴 작업시간을 우선적으로 할당)
=> 그러므로, min heap 선택.


2. 데이터의 우선순위는 어떻게 되는가?
=> 머신 스케쥴링에서는 '기계의 종료시간'을 데이터의 우선순위로 정한다.
=> 이를 Min Heap을 통해, 가장 빨리 끝나느 기계에 새로운 작업을 할당하는 형식.
=> 이를 통해, '강의가 끝나는 시간'을 데이터의 우선순위로 정함.


3. heap의 삽입과 삭제의 조건?
=> 이 문제의 경우, 시작시간과 종료시간이 정해져있다.
=> 즉, 시작시간 오름차순으로 강의실에 배정된다는 의미.
=> 그러므로, 1번째는 강의들을 시작시간 기준으로 오름차순 정렬을 진행한다.
    (이때, Python Sorted 내장 함수 사용 : 병합정렬 - 최악도 O(nlog n) 보장)
=> 강의실을 몇개 사용해야하는지 구하는 문제이므로, 강의실 1번으로 초기 세팅. (room=1)
=> heap의 최상단은 '가장 빨리 끝나는 강의의 종료시간'이 저장되있다.
=> 그러므로, 'root의 종료시간 > 새로운 강의 시작시간' 이라면,
    heap에 새로운 강의를 삽입해주면 된다.
=> 반대로, 'root의 종료시간 <= 새로운 강의 시작시간' 이라면,
    => root에 해당되는 room을 새로운 강의실로 이용가능하기에,
    => root를 삭제한 원소를 바탕으로, 새로운 강의를 삽입하면 된다.

3번 정리 - 알고리즘 과정
(1). 입력 강의들 오름차순 정렬. (lecture 이중 리스트)
(2). Min Heap에 (lecture[0]의 종료시간, 초기room번호 1) 삽입.
(3). 나머지 강의들 for문으로 할당을 위한 탐색 시작.
(4-1). 가장 빨리 끝나는 강의 종료시간 > 현재 탐색 대상의 시작시간
    then, Min Heap에 (현재 탐색 대상의 종료시간, room+1)
(4-2). else then, 
    => root 제거 (나오는 값: root의 종료시간, root의 room번호)
    => Min Heap에 (현재 탐색 대상 종료시간, 삭제된 root의 room번호)
(5). room 출력.


4. 예시 (예제 입력 1번)
초기: heap=[(3,1)], room=1
1. (2,4)입력값 탐색
    => 3 > 2 이므로, heap=[(3,1),(4,2)], room=1+1=2
2. (3,5)입력값 탐색
    => 3 < 5 이므로,
    => root 삭제: (3,1), heap=[(4,2)]
    => Min heap 삽입: heap=[(4,2),(5,1)]
3. 종료 room=2 출력.
"""
import sys,heapq
input=sys.stdin.readline

n=int(input())
lecture=sorted([[*map(int,input().split())] for _ in range(n)], key=lambda x: x[0]) #1

heap,room=[],1
heapq.heappush(heap,(lecture[0][1],room)) #2: (종료시간,강의실번호)

for idx in range(1,n): #3
    s,t=lecture[idx][0],lecture[idx][1]
    if heap[0][0]>s: #4-1
        room+=1
        heapq.heappush(heap,(t,room))
    else: #4-2
        f_end,f_room=heapq.heappop(heap)
        heapq.heappush(heap,(t,f_room))

print(room)
