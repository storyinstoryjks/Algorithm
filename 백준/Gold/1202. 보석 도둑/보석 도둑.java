// LOPOV
// https://www.acmicpc.net/problem/1202

/* 
내 기준 평가
난이도 : 어려움
시간 : 1시간 30분

[설계]
<1. 어떤 자료구조를 사용해야 하는가?>
=> 각 가방에는 1개의 보석만 담을 수 있고, 못넣는 경우도 있을 수 있다.
=> 넣을 수 있다면, 최대 가격의 보석을 가방에 넣어야 한다.
=> 다시 말해, 넣을 수 있는 보석들의 후보 중, 가장 비싼 가격을 넣어야 한다.
=> 이를 통해, 전체 데이터에서 최대값을 갖는 1개의 데이터만 뽑으면 되기에, Heap이 효율적인 문제이다.
=> 만약, 전체 데이터 개수에 가깝게 정렬 데이터를 뽑아야 한다면, 다른 자료구조가 유용하다.

<2. 데이터의 우선순위 기준은 어떻게 설정해야 하는가?>
=> 이 부분이 어렵다. 처음에는 다음과 같이 선정하였다.

==> (1) 보석 Max heap 1개 + 가방 Max Heap 1개
==> 데이터 우선순위(보석,가방) : (가격,무게)
==> 가방에서 1개를 poll 진행하여, 현재 가방 무게에 해당되는 보석heap에서 꺼내 ans에 더하는 과정이다.
==> 이의 문제점은 다음 2가지가 존재한다. 예시를 들어보자
===> (n,k)=(4,4), 보석((1,100),(2,200),(13,300),(10,500))
===> 가방(10,10,10,14), 답:1100
===> 1번째 순회: 현재 가방(14), 1번째 가방 heap 삭제원소(10,500) 가능하기에 ans+=500
===> (13,300)이 들어와야하기에 잘못 선정된 것을 확인가능.
===> 반대로, 보석의 우선순위가 무게가 되어도, 예제입력2번에서 오답이 나오게 된다.
===> 즉, 1번째 문제점은 해당 가방에 삽입가능한 '후보 가방들 선정이 먼저 이루어지지 않는다.'이다.
===> 2번째 문제점은 poll은 heap에서 '해당 원소를 삭제하기에, 이를 기억해서 다시 삽입해야한다'이다.
===> 그러므로, 탈락

=> (1)의 문제점들을 해결하는 것은 결국, 정렬+heap이다.
=> 데이터의 우선순위는 '보석(min무게)+가방(min무게)'이며, ans는 maxHeap을 사용한다.
=> 보석과 가방의 자료구조는 '배열'이다.
=> Heap의 기본원리는 LPT 알고리즘이다.(ex Machine Scheduling)
=> 이 문제에서 데이터의 우선순위는 결국 '가장 적은 무게'가 되고,
=> 이는 LPT 알고리즘의 머신 스케쥴링에서 기계 작업 시간을 최소로 두는 것과 유사하다.
=> 이는 가장 큰것 또는 가장 작은 것을 탐욕적으로 선택하는 그리디 알고리즘이기도 하다.
=> 해당 가방의 후보 보석들을 찾기 위해, 오름차순으로 정렬된 보석/가방 배열들을 이용하고,
=> '후보 보석들 중에서, 가장 비싼 보석 1개를 찾는 것'을 위해 최대힙을 사용하는 것이 핵심이 된다.

<3. 알고리즘 과정과 어떤 정렬 기법을 사용해야 하는가?>
[알고리즘 과정]
1. 보석과 가방을 모두 무게 기준으로 오름차순 정렬.
2. 모든 가방을 순회하여 탐색한다.
3. 해당 가방의 무게 >= 1번째 보석 무게(보석 중 가장 낮은 무게)
    3.1 ans를 위한 max heap에 가격을 기준으로 삽입.
4. max heap에서 root 데이터를 삭제 및 리턴하여 ans에 더함.(비어있지 않다면)
    (비어있다? == 후보 보석들이 없다. == 모든 보석 무게 > 해당 가방 무게인 경우)

[정렬 기법]
=> 시간제한 1초이므로, O(n*n)은 피해야 한다.
=> (heap의 삽입과 삭제는 O(log n)이므로 상관없음)
=> 최소 O(nlog n)의 정렬 알고리즘 필요.
=> Java에서는 2가지 정렬 내장 함수 제공.
==> Arrays.sort(ArrayList) : DualPivotQuickSort(pivot 2개 활용한 퀵정렬) - 평균 nlog n / 최악 n*n
==> Collections.sort(List) : TimeSort(삽입정렬+합병정렬) - 평균/최악 모두 nlog n
=> 더 줄이고 싶다? O(n)을 자랑하는 기수정렬 사용하면 될 듯 싶다.
*/
import java.util.*;
import java.io.*;

class Gem {
    int weight;
    int price;

    public Gem(int w, int p){
        this.weight=w;
        this.price=p;
    }
}

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n=Integer.parseInt(st.nextToken());
        int k=Integer.parseInt(st.nextToken());
        
        Gem[] gems = new Gem[n]; // 정렬 안된 보석 배열
        int[] bags = new int[k]; // 정렬 안된 가방 배열
        PriorityQueue<Integer> bag = new PriorityQueue<>(Collections.reverseOrder()); // 후보 보석 중 결정을 위한 pq
        long ans=0; // 30만*100만이 최대이므로, long 타입 설정.

        for(int i=0; i<n; i++){
            st=new StringTokenizer(br.readLine());
            int weight=Integer.parseInt(st.nextToken());
            int price=Integer.parseInt(st.nextToken());
            gems[i]=new Gem(weight,price);
        }
        for(int i=0; i<k; i++){
            bags[i]=Integer.parseInt(br.readLine());
        }

        Arrays.sort(bags); // 가방 오름차순 정렬
        Arrays.sort(gems, new Comparator<Gem>() { // 보석 오름차순 정렬
            // o2-o1 : max heap
            // o1-o2 : min heap
            // 데이터의 우선순위 기준 정하는 오버라이딩 함수
            @Override
            public int compare(Gem o1, Gem o2){
                // 무게가 같은 보석들이라면,
                if(o1.weight==o2.weight){
                    // 무게가 같은 보석들 중에서, 가격 기준 내림차순
                    return o2.price-o1.price;
                }
                // 무게가 다르다면
                else{
                    // 무게가 작은 기준으로 오름차순
                    return o1.weight-o2.weight;
                }
            }
        });
        
        // 모든 가방 순회
        for(int i=0,idx=0; i<k; i++){
            // 1번째 보석부터 비교 시작. (가장 낮은 무게의 보석이기 때문)
            // 1번째 보석부터 모든 가방에 못들어간다? 나머지 보석들도 전부 못들어감.
            while(idx<n && gems[idx].weight<=bags[i]){
                // pq에 후보 보석 삽입.
                // 가격 기준 max heap
                bag.offer(gems[idx++].price);
            }
            // 해당 가방에 후보 보석들이 존재한다면
            if(!bag.isEmpty()){
                // 가장 비싼 보석 차출.
                ans+=bag.poll();
            }
        }
        System.out.println(ans);
    }
}