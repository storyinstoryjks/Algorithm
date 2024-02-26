// Abs Heap
// https://www.acmicpc.net/problem/11286

import java.io.*;
import java.util.*;

class HeapType{
    private int heap[];
    private int heap_size;

    public HeapType() {
        heap=new int[100001];
        heap_size=0;
    }
    public int abs(int item) {
        return (item<0 ? -item:item);
    }
    public int getSize() {
        return heap_size;
    }
    public void insert_abs_heap(int item){
        int i=++(heap_size);

        while((i!=1) && ((abs(item)<abs(heap[i/2])) || (abs(item)==abs(heap[i/2]) && item<heap[i/2]))){
            heap[i]=heap[i/2];
            i/=2;
        }

        heap[i]=item;
    }
    public int delete_abs_heap(){
        int parent,child;
        int temp,item;

        parent=1; child=2;
        item=heap[1];
        temp=heap[heap_size--];

        while(child<=heap_size){
            if((child<heap_size) && ((abs(heap[child])>abs(heap[child+1])) || (abs(heap[child])==abs(heap[child+1]) && heap[child]>heap[child+1]))){
                child++;
            }
            if((abs(temp)<abs(heap[child])) || (abs(temp)==abs(heap[child]) && temp<=heap[child])){
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
        HeapType h = new HeapType();

        int n=Integer.parseInt(st.nextToken());

        for(int i=0; i<n; i++){
            st=new StringTokenizer(br.readLine());
            int t=Integer.parseInt(st.nextToken());
            if(t==0){
                if(h.getSize()==0){
                    System.out.println(0);
                }
                else{
                    System.out.println(h.delete_abs_heap());
                }
            }
            else{
                h.insert_abs_heap(t);
            }
        }
    }
}
