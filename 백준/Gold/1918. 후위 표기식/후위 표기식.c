// Infix -> Postfix

#include <stdio.h>
#include <stdlib.h>
#define MAX_SIZE 100

typedef char element;
typedef struct StackType{
    element data[MAX_SIZE];
    int top;
}StackType;

void init_stack(StackType* s){
    s->top=-1;
}

int is_full(StackType* s){
    return s->top==MAX_SIZE-1;
}

int is_empty(StackType* s){
    return s->top==-1;
}

void push(StackType* s, element item){
    if(is_full(s)){
        exit(1);
    }
    s->data[++(s->top)]=item;
}

element pop(StackType* s){
    if(is_empty(s)){
        exit(1);
    }
    return s->data[(s->top)--];
}

element peek(StackType* s){
    return s->data[s->top];
}

int prac(char c){
    switch(c){
        case '(': case ')':
            return 0;
        case '*': case '/':
            return 2;
        case '+': case '-':
            return 1;
    }
}

int main(){
    StackType stk;
    char s[MAX_SIZE],top_op;

    scanf("%s",s);
    init_stack(&stk);

    for(int i=0; s[i]!='\0'; i++){
        switch(s[i]){
            case '+': case '-': case '*': case '/':
                while(!is_empty(&stk) && prac(s[i])<=prac(peek(&stk))){
                    printf("%c",pop(&stk));
                }
                push(&stk,s[i]);
                break;
            case '(':
                push(&stk,s[i]);
                break;
            case ')':
                top_op=pop(&stk);
                while(top_op!='('){
                    printf("%c",top_op);
                    top_op=pop(&stk);
                }
                break;
            default: // alpha case
                printf("%c",s[i]);
                break;
        }
    }
    while(!is_empty(&stk)){
        printf("%c",pop(&stk));
    }
}
