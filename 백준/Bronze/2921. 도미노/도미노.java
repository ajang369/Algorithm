import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int N;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        int sum = 0;
        for (int i = 1; i <= N; i++) {
            for (int j = 0; j <=i; j++) {
                sum += i;
                sum += j;
            }
        }
        System.out.println(sum);
    }
}