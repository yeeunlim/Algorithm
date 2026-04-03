import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] p = new int[N];

        for (int i = 0; i < N; i++) {
            p[i] = sc.nextInt();
        }

        Arrays.sort(p);

        int totalSum = 0;  // 전체 합계
        int currentSum = 0; // 이전 사람까지 대기한 시간의 합

        // 누적합 계산
        for (int i = 0; i < N; i++) {
            currentSum += p[i]; // 현재 사람이 끝나는 시점
            totalSum += currentSum; // 모든 사람이 기다린 총 시간 합산
        }

        System.out.println(totalSum);
    }
}