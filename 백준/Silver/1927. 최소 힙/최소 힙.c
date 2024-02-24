// Min Heap
// https://www.acmicpc.net/problem/1927
/*
* Python3(already AC) -> C
*/

#include <stdio.h>
#include <stdlib.h>
#define MAX_ELEMENT 100001

typedef struct {
    int key;
}element;

typedef struct {
    element heap[MAX_ELEMENT];
    int heap_size;
}HeapType;

HeapType* create() { return (HeapType*)malloc(sizeof(HeapType));}

void init(HeapType* h) {h->heap_size=0;}

void insert_min_heap(HeapType* h, element item){
    int i;
    i=++(h->heap_size);
    
    // 최상단 루트가 아니고, 삽입노드 < 삽입노드의 부모
    while((i!=1) && (item.key < h->heap[i/2].key)){
        h->heap[i]=h->heap[i/2]; // 삽입노드의 부모 끌어내리기
        i/=2; // 조상노드로 이동
    }

    h->heap[i]=item; // 발견한 삽입 위치에 삽입
}

element delete_min_heap(HeapType* h){
    int parent,child;
    element item,temp;

    parent=1; child=2;
    item=h->heap[1]; // root node
    temp=h->heap[(h->heap_size)--]; // last node

    while(child<=h->heap_size){
        // 오른쪽 자식 노드가 더 크면
        if((child<h->heap_size) && (h->heap[child].key > h->heap[child+1].key)){
            child++;
        }
        // 대상 노드의 위치가 결정되면(더 내려갈 필요가 없다면)
        if(temp.key<=h->heap[child].key){
            break;
        }
        h->heap[parent]=h->heap[child];
        parent=child;
        child*=2;
    }

    h->heap[parent]=temp; // 발견된 위치에 원래 마지막 노드 삽입
    return item;
}

int main() {
    HeapType* h=create();
    int n;

    init(h);
    scanf("%d",&n);
    
    for(int i=0; i<n; i++){
        int tmp;
        scanf("%d",&tmp);
        if(tmp==0){
            if(h->heap_size==0) printf("%d\n",0);
            else printf("%d\n",delete_min_heap(h));
        }
        else{
            insert_min_heap(h,(element){tmp});
        }
    }

    free(h);
    return 0;
}