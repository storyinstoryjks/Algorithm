// Hanoi

#include <stdio.h>
#include <math.h>

void Hanoi(int n, int s, int t, int v){
    if(n == 1) printf("%d %d\n", s, t);
    else{
        Hanoi(n-1, s, v, t);
        printf("%d %d\n", s, t);
        Hanoi(n-1, v, t, s);
    }
}

int main(){
    int n;
    scanf("%d", &n);
    printf("%d\n", (int)(pow(2.,n))-1);
    Hanoi(n, 1, 3, 2);
    return 0;
}