// Sorting Card
// https://www.acmicpc.net/problem/1715
/*
=> 허프만 코드
=> 원래는 허프만 트리를 그려나가면서 간선 가중치를 결정하여, 빈도수 체크를 진행.
=> 합을 구해야 하는 문제이므로, 최소힙에서 2개씩 빼서 정답에 더하고, 다시 최소힙에 삽입.

(추가)
n==1 일때는 비교를 하지 않아도 되므로, 0이다. (이것땜에 95프로에서 틀림)
*/
import java.io.*;
import java.util.*;

class HeapType{
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
public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException{
        HeapType h=new HeapType();
        int n=Integer.parseInt(new StringTokenizer(br.readLine()).nextToken());
        int sum=0;
        
        if(n==1){
            System.out.println(0);
        }
        else if(n==2){
            for(int i=0; i<n; i++){
                sum+=Integer.parseInt(new StringTokenizer(br.readLine()).nextToken());
            }
            System.out.println(sum);
        }
        else{
            for(int i=0; i<n; i++){
                h.insert_min_heap(Integer.parseInt(new StringTokenizer(br.readLine()).nextToken()));
            }

            while(h.getSize()>1){
                int t=h.delete_min_heap()+h.delete_min_heap();
                h.insert_min_heap(t);
                sum+=t;
            }

            System.out.println(sum);
        }
    }
}
