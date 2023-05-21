import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {

    public static void main(String args[]) throws IOException {
        BufferedReader buffer = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String [] input = buffer.readLine().split(" "); //arrA
        Integer N = Integer.parseInt(input[0]);    //A 배열의 크기
        Integer M = Integer.parseInt(input[1]);    //B 배열의 크기

        int[] arrA = new int[N];
        int[] arrB = new int[M];
        int[] merge = new int[N+M];

        input = buffer.readLine().split(" "); //arrA
        for(int i=0; i<input.length; i++)
            arrA[i] = Integer.parseInt(input[i]);

        input = buffer.readLine().split(" "); //arrA
        for(int i=0; i<input.length; i++)
            arrB[i] = Integer.parseInt(input[i]);

        //합병
        int size = N+M;
        int indexA=0, indexB=0, i=0;
        int flag = 1;   //A = 1, B = 2
        int smaller=0;
        // 2 5 6 7 9
        // 1 3 4 8

        for(; i<size; i++) {
            if(indexB==M || indexA==N) {
                if(indexA==N) flag = 2; //A배열은 끝났고 B배열 나머지 merge 해야함
                break;
            }

            if(arrA[indexA] < arrB[indexB]){
                smaller = arrA[indexA];
                indexA+=1;
            }
            else{
                smaller = arrB[indexB];
                indexB+=1;
            }
            merge[i] = smaller;
        }


        while(flag==1 && indexA<N){
            merge[i++] = arrA[indexA++];
        }

        while(flag==2 && indexB<M){
            merge[i++] = arrB[indexB++];
        }

        for(int m:merge){
            bw.write(m+ " ");
        }
        bw.flush();
        bw.close();

    }
}
