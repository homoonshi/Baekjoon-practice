import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N=Integer.parseInt(br.readLine()); // 수열의 개수

        int[] A=new int[N]; // A(i) 수열
        String[] num=new String[N]; // A (i) 수열을 bufferreader로 받을 스트링 배열
        num=br.readLine().split(" "); // 배열에 스페이스바를 기준으로 나눠서 넣어줌

        for (int i=0;i<N;i++) {
            A[i] = Integer.parseInt(num[i]); // int 배열에 수열 A를 넣어줌
        }

        int[] res=new int[N]; // NGE 수 담을 배열
        Stack<Integer> stack = new Stack<>(); // 비교할 수를 스택에 넣음
        int stackIndex=0; // 스택에 들어간 가장 최근 인덱스

        for (int i=0;i<N;i++){
            if(res[i]!=0){  // 만약 NGE를 이미 구했다면 넘어감
                continue;
            }

            for (int j=i+1;j<N;j++){ // NGE를 찾는 과정

                if(A[i]<A[j]){ // NGE를 구했다면
                    res[i]=A[j]; // 일단 i에 NGE 값을 넣는다.
                    while(!stack.empty()){ // 스택이 비어있지 않다면
                        if (stackIndex>-1&&res[stackIndex] != 0) { // Index 값을 구한 뒤
                            stackIndex--;
                            continue;
                        }
                        res[stackIndex]=A[j]; // NGE 값을 넣어준다. 왜냐면 i보다 큰 수는 스택에 있는 값보다 큰 값인 것이 확실하기 때문이다.
                        stack.pop();
                    }
                    break;
                }else{
                    if(stack.empty()){ // 스택에 아무런 값도 없다면
                        stack.add(A[j]); // 스택에 값을 넣어준다.
                        stackIndex=j;
                    }else {
                        if(stack.peek()>A[j]){ // 스택의 맨 위에 있는 값보다 작다면 그 안의 값들보다 무조건 작은 값이다.
                                                // 스택의 맨 밑 값이 젤 위에 쌓인 값보다 크기 때문이다.
                            stack.add(A[j]);
                            stackIndex=j;
                        }else {
                            while (!stack.empty()) { // A[j] 값이 스택의 맨 윗 값보다 크다면 A[j]보다 작은 값들이 있는지 확인하며 빼준다.
                                if (stack.peek() < A[j]) {
                                    if (res[stackIndex] != 0) { // Index 값을 구하고
                                        stackIndex--;
                                        continue;
                                    }
                                    res[stackIndex] = A[j]; // NGE 값을 구해주고
                                    stack.pop(); // 빼준다.
                                }else{ // 더이상 A[j] 값이 스택에 있는 값보다 크지 않다면
                                    stack.add(A[j]); // 스택에 넣어주고
                                    stackIndex=j;
                                    break; // 반복을 중단함
                                }
                            }
                            if(stack.empty()) {
                                stack.add(A[j]);
                                stackIndex = j;
                            }
                        }
                    }
                }

            }

            if (res[i]==0){ // 만약 -1값을 얻는다면 끝까지 돌았고 모든 값이 스택에 있는것인데 그때까지 NGE 값을 얻지 못했다면
                            // 그 값은 NGE가 없는 것이다. 스택에 있는 모든 값과 A[i] 값에 -1 을 넣어준다.
                res[i]=-1;
                while(!stack.empty()){
                    if (res[stackIndex] != 0) { // Index 값을 구하고
                        stackIndex--;
                        continue;
                    }
                    res[stackIndex]=-1;
                    stack.pop();
                }
            }
        }

        for(int n:res){
            bw.write(n+" ");
        }

        bw.flush();
        bw.close();

    }
}