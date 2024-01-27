// Print to Star-10
/*
* 파이썬의 기본 스택 깊이는 1000이지만, 자바는 10000이다.
* 자바는 재귀보다는 반복문과 루프가 잘 맞는 언어지만, 재귀 연습을 하자.
* 자바에서의 스택 오버플로우 방지를 위한 깊이 제한 수동 설정은
* JVM 옵션 -XX를 통해서 실행옵션으로 수동 설정하는 방법이 있다.
*/
import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    static ArrayList<String> Recursion_Star(int n){
        if(n==1){
            ArrayList<String> tmp = new ArrayList<String>(){{add("*");}};
            return tmp;
        }
        ArrayList<String> s = Recursion_Star((int)(n/3));
        ArrayList<String> l = new ArrayList<String>();

        for(String a : s){
            l.add(a+a+a);
        }
        for(String a : s){
            String t = a;
            for(int i = 0; i < (int)(n/3); i++){
                t += " ";
            }
            t += a;
            l.add(t);
        }
        for(String a : s){
            l.add(a+a+a);
        }
        return l;
    }

    public static void main(String[] args) throws IOException{
        int n = Integer.parseInt(br.readLine());
        ArrayList<String> a = Recursion_Star(n);
        for(int i=0; i< a.size(); i++)
            System.out.println(a.get(i));
        br.close();
    }
}
