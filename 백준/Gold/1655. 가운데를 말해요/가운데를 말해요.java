/*
[알고리즘]
1. Min Heap을 통한 중간값 구하기. (1번 코드=주석코드)
2. Min Heap + Max Heap을 통한 중간값 구하기.(2번코드) (선택)

"왜 Heap인 것인가?"
=> 데이터의 전체를 다 봐야하는 경우는 비교적 힙은 덜 효율적이다.
=> 그러나, 전체 중 일부의 데이터만 확인하는 경우, 느슨한 정렬 상태를 유지하는 힙이 효율적.
=> k번째 수를 구하는 문제와 같은 유형이다.

[설계과정]
<1번 알고리즘>
1. 중간값을 구하기 위해서, 삭제연산을 몇번 진행하여야하는가?
=> 홀수인 경우, (현재 heapSize/2+1)번째 삭제연산 시 나오는 값이 중간값이다.
=> 짝수인 경우, (현재 heapSize/2+1)번째 삭제연산 시 중간값 2개 중 마지막값이다.(첫째는 heapSize/2)

2. 삭제연산은 heap을 재조정하므로, 삭제된값을 기억해야할 필요가 있다.
=> 삭제연산은 heap_size를 줄이고, root자리에 임시로 기존heap의 마지막 단말노드를 기준으로 재조정을 하게된다.
=> 그러므로, 리턴된값을 기억하여 재삽입을 해야 다음번 입력값의 올바른 중간값을 구할 수 있다.
=> 이를 위해, re_list[] 1차원 배열을 설정하여, 리턴된값들을 담아주고, 정답 출력 후 재삽입을 진행한다.

3. 논리설계는 정답이다. 그러나 선택하지 않은 이유는?
=> 시간초과 가능성이 높기 때문이다.
=> 소스코드를 보면 알겠지만, 시간복잡도는 대략 다음과 같다.
    - 입력값 : O(n)
    - 중간값까지 삭제연산 : k * O(log n)
    - 재삽입 : k * O(log n)
=> 즉 위의 3가지 연산의 총합이 시간복잡도이므로, 1초의 시간제한이라면 간당하게 넘어갈 수 있겠지만,
=> 0.1초에서는 불가능 가능성이 높다.

<2번 알고리즘>
1. 원리는?
=> 다음의 배열을 보자.
=> 1 2 3 4 5 6
=> 이 배열의 중간값은 이 문제의 기준을 바탕으로는 3 < 4 이므로, 3이다.
=> 1번 알고리즘의 경우, (pop 순서: 1,2,3,4)를 통해, 3과4를 비교하게 된다.
=> 그렇다면, 조금만 시야를 다르게 보자.
=> 1 2 3 | 4 5 6
=> 이런식으로, 중간값은 배열의 '가운데를 기준으로 결정되게 된다.'
=> group 1은 (1,2,3) 그리고 group 2는 (4,5,6)으로 묶어, 각각 최대힙 최소힙을 설정하게 되면?
    <Max>    <min>
    3        4
   1 2      5 6
=> '최상단 root 노드에는 항상 중간값이 달리게 된다.'
=> 즉, Max 힙의 root는 데이터의 전체 개수가 홀수인 경우, '항상 중앙값'이 된다.
=> 다시 말해, 정답 출력은 Max Heap의 root를 출력하면 되는 것이다.

2. 데이터를 어느 힙에다 넣어야 하는가?
=> Max Heap의 root는 가장 큰값, Min Heap의 root는 가장 작은 값이 되어야 중간값이 유지된다.
=> len(Max)==len(Min) -> insert to max heap
=> else -> insert to min heap
=> 이유는 1 | 2 3 배열과 1 2 | 3 배열을 비교해 보면된다.(홀수인 경우)
=> 짝수개가 될시 (heap 배열로 치환하면) 4 1 | 2 3, 2 1 | 3 4 후자가 정답임을 알 수 있다.

3. 주의점은?
=> Max Heap의 root값 < Min heap의 root값이 유지되어야 하기 때문에
=> 중복값 또는 순서가 뒤죽박죽인 수를 넣게 되었을 시 균형이 깨지는 경우가 발생할 수 있다.
=> 그러므로, 재조정이 필요하다.
=> else -> swap(max_root,min_root)

4. 시간복잡도
=> 삽입위치 결정 : O(log n)
=> 재조정 : O(log n)*2
=> 총합을 진행하게 되면, 1번알고리즘보다 훨씬 단축됨을 알 수 있다.
*/

// 1번 코드
/*
import java.io.*;
import java.util.*;

class HeapType {
    private int heap[];
    private int heap_size;

    public HeapType(){
        heap=new int[100001];
        heap_size=0;
    }
    public int getSize() {
        return heap_size;
    }
    public void insert_min_heap(int item){
        int i=++(heap_size);

        while((i!=1) && (item<heap[i/2])){
            heap[i]=heap[i/2];
            i/=2;
        }

        heap[i]=item;
    }
    public int delete_min_heap(){
        int parent,child;
        int item,temp;

        parent=1; child=2;
        item=heap[1];
        temp=heap[(heap_size)--];

        while(child<=heap_size){
            if((child<heap_size) && (heap[child]>heap[child+1])){
                child++;
            }
            if(temp<=heap[child]){
                break;
            }
            heap[parent]=heap[child];
            parent=child;
            child*=2;
        }

        heap[parent]=temp;
        return item;
    }
}
public class Solution1655 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        HeapType h = new HeapType();
        int N=Integer.parseInt(new StringTokenizer(br.readLine()).nextToken());

        for(int i=1; i<=N; i++){
            int[] re_insert_list=new int[50001]; // 정답 출력 이후, 재삽입을 위한 그릇
            int re_idx=0;
            int t=Integer.parseInt(new StringTokenizer(br.readLine()).nextToken()); // 입력값

            h.insert_min_heap(t);

            int delete_cnt=(int)(i/2)+1; // 삭제연산을 몇번까지 진행할것인가(중간값까지 삭제하기 위함)
            // 홀수
            if(i%2>0){
                for(int j=1; j<=delete_cnt; j++){
                    int e=h.delete_min_heap();
                    re_insert_list[re_idx++]=e;
                }
                // 중간값 출력
                System.out.println(re_insert_list[re_idx-1]);
            }
            // 짝수
            else{
                for(int j=1; j<=delete_cnt; j++){
                    int e=h.delete_min_heap();
                    re_insert_list[re_idx++]=e;
                }
                int e1=re_insert_list[re_idx-1];
                int e2=re_insert_list[re_idx-2];
                // 중간값 출력
                System.out.println(e1>e2 ? e2:e1);
            }
            
            // 재삽입
            for(int k=0; k<re_idx; k++){
                h.insert_min_heap(re_insert_list[k]);
            }
        }
    }
}
*/

// 2번 코드
// Speak to middle number
// https://www.acmicpc.net/problem/1655

import java.io.*;
import java.util.*;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        PriorityQueue<Integer> minHeap = new PriorityQueue<>((o1, o2) -> o1 - o2);
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((o1, o2) -> o2 - o1);

        for(int i = 0 ; i < n; i++){
            int num = Integer.parseInt(br.readLine());

            if(minHeap.size() == maxHeap.size()) maxHeap.offer(num);
            else minHeap.offer(num);

            if(!minHeap.isEmpty() && !maxHeap.isEmpty())
                if(minHeap.peek() < maxHeap.peek()){
                    int tmp = minHeap.poll();
                    minHeap.offer(maxHeap.poll());
                    maxHeap.offer(tmp);
                }

            sb.append(maxHeap.peek() + "\n");
        }
        System.out.println(sb);
    }
}