// Teateromino

import java.io.*;
import java.util.*;

public class Main{
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int n,m;
    static int max=-1;
    static int[][] l;

    static void getData(String s) throws IOException{
        StringTokenizer st = new StringTokenizer(s);
        n=Integer.parseInt(st.nextToken());
        m=Integer.parseInt(st.nextToken());

        l=new int[n][m];

        for(int i=0; i<n; i++){
            int col=0;
            st = new StringTokenizer(br.readLine());
            while(st.hasMoreTokens()){
                l[i][col++]=Integer.parseInt(st.nextToken());
            }
        }
    }

    static int checkLine(){
        int cnt1=-1,cnt2=-1;
        // Width
        for(int i=0; i<n; i++){
            for(int j=0; j<=m-4; j++){
                int sum=0;
                for(int k=j; k<j+4; k++){
                    sum+=l[i][k];
                }
                cnt1=Math.max(cnt1,sum);
            }
        }
        // Height
        for(int i=0; i<m; i++){
            for(int j=0; j<=n-4; j++){
                int sum=0;
                for(int k=j; k<j+4; k++){
                    sum+=l[k][i];
                }
                cnt2=Math.max(cnt2,sum);
            }
        }
        return Math.max(cnt1,cnt2);
    }

    static int checkSquare(){
        int cnt=-1;

        for(int i=1; i<n; i++){
            for(int o=0; o<=m-2; o++){
                int sum=0;
                for(int j=i-1; j<=i; j++){
                    for(int k=o; k<o+2; k++){
                        sum+=l[j][k];
                    }
                }
                cnt=Math.max(cnt,sum);
            }
        }
        return cnt;
    }

    static int checkL(){
        // Case: 8 -- Original 4 + Symmetry 4 -- Include to Rotation
        // And KRn able to this Algorithm
        int cnt=-1;
        // Case 1: L, Rotation 180deg to Right by Symmetry L
        for(int i=0; i<m-1; i++){
            for(int j=0; j<=n-3; j++){
                int sum=0;
                for(int k=j; k<j+3; k++){
                    sum+=l[k][i];
                }
                // L,Symmetry L,R_180_KRn
                int tmp=Math.max(l[j+2][i+1],l[j][i+1]);
                sum+=Math.max(tmp,l[j+1][i+1]);
                cnt=Math.max(cnt,sum);
            }
        }
        // Case 2: Rotation 90deg to Right by L, Rotation 270deg to Right by Symmetry L
        for(int i=0; i<n-1; i++){
            for(int j=0; j<=m-3; j++){
                int sum=0;
                for(int k=j; k<j+3; k++){
                    sum+=l[i][k];
                }
                //L,Symmetry L,O_KRn
                int tmp=Math.max(l[i+1][j],l[i+1][j+2]);
                sum+=Math.max(tmp,l[i+1][j+1]);
                cnt=Math.max(cnt,sum);
            }
        }
        // Case 3: Rotation 180deg to Right by L, Symmetry L
        for(int i=1; i<m; i++){
            for(int j=0; j<=n-3; j++){
                int sum=0;
                for(int k=j; k<j+3; k++){
                    sum+=l[k][i];
                }
                //L, Symmetry L,R_90_KRn
                int tmp=Math.max(l[j][i-1],l[j+2][i-1]);
                sum+=Math.max(tmp,l[j+1][i-1]);
                cnt=Math.max(cnt,sum);
            }
        }
        // Case 4: Rotation 270deg to Right by L, Rotation 90deg to Right by Symmetry L
        for(int i=1; i<n; i++){
            for(int j=0; j<=m-3; j++){
                int sum=0;
                for(int k=j; k<j+3; k++){
                    sum+=l[i][k];
                }
                //L,Symmetry L,R_270_KRn
                int tmp=Math.max(l[i-1][j+2],l[i-1][j]);
                sum+=Math.max(tmp,l[i-1][j+1]);
                cnt=Math.max(cnt,sum);
            }
        }
        return cnt;
    }

    static int checkStairs(){
        int cnt=-1;
        for(int i=1; i<n-1; i++){
            for(int j=0; j<=m-2; j++){
                int sum=0;
                for(int k=j; k<j+2; k++){
                    sum+=l[i][k];
                }
                sum+=Math.max(l[i-1][j]+l[i+1][j+1],l[i-1][j+1]+l[i+1][j]);
                cnt=Math.max(cnt,sum);
            }
        }
        for(int i=1; i<m-1; i++){
            for(int j=0; j<=n-2; j++){
                int sum=0;
                for(int k=j; k<j+2; k++){
                    sum+=l[k][i];
                }
                sum+=Math.max(l[j+1][i-1]+l[j][i+1],l[j][i-1]+l[j+1][i+1]);
                cnt=Math.max(cnt,sum);
            }
        }
        return cnt;
    }

    public static void main(String[] args) throws IOException{
        getData(br.readLine());
        max=Math.max(max,checkLine());
        max=Math.max(max,checkSquare());
        max=Math.max(max,checkL());
        max=Math.max(max,checkStairs());
        System.out.print(max);
        br.close();
    }
}