// Max Heap
// https://www.acmicpc.net/problem/11279

import java.io.*;
import java.util.StringTokenizer;

class HeapType {
    private int[] heap;
    private int heap_size;

    public HeapType() {
        heap=new int[100001];
        heap_size=0;
    }
    public int getSize() {
        return heap_size;
    }
    public void insert_max_heap(int item){
        int i=++(heap_size);
        
        while((i!=1) && (item > heap[i/2])){
            heap[i]=heap[i/2];
            i/=2;
        }

        heap[i]=item;
    }
    public int delete_max_heap(){
        int parent, child;
        int item,temp;

        parent=1; child=2;
        item=heap[1];
        temp=heap[heap_size--];

        while(child<=heap_size){
            if((child<heap_size) && (heap[child] < heap[child+1])){
                child++;
            }
            if(temp >= heap[child]){
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
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n=Integer.parseInt(st.nextToken());
        HeapType h = new HeapType();

        for(int i=0; i<n; i++){
            st=new StringTokenizer(br.readLine());
            int t=Integer.parseInt(st.nextToken());
            if(t==0){
                if(h.getSize()==0){
                    System.out.println(0);
                }
                else{
                    System.out.println(h.delete_max_heap());
                }
            }
            else{
                h.insert_max_heap(t);
            }
        }
    }
}