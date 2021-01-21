package Basic_Questions_Set.javaFiles;

import java.util.Scanner;

public class One {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double sample_cm = sc.nextInt();
        int foot,inch;
        foot = (int) (sample_cm / 30.48);
        inch = (int) (((sample_cm / 30.48) - foot) * 12);
        System.out.println(foot+ " " + inch);
        sc.close();
    }
}