// The Balance of the World

import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException{
        while(true){
            String a=br.readLine();
            if(a.equals(".")) break;

            boolean flag=true;
            Stack<Character> s = new Stack<Character>();
            for(char c:a.toCharArray()){
                if(c=='(' || c=='['){
                    s.add(c);
                }
                else if(c==')'){
                    if(!s.isEmpty() && s.peek()=='(') s.pop();
                    else {
                        flag=false;
                        break;
                    }
                }
                else if(c==']'){
                    if(!s.isEmpty() && s.peek()=='[') s.pop();
                    else {
                        flag=false;
                        break;
                    }
                }
            }
            if(flag && s.isEmpty()) sb.append("yes\n");
            else sb.append("no\n");
        }
        System.out.print(sb);
        br.close();
    }    
}
