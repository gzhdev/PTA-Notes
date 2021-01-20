package Basic_Questions_Set.javaFiles;

import java.util.Scanner;

public class One {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double sample_cm = sc.nextInt();
        double mid;
        mid = Math.floor((sample_cm / 100) / 0.3084);
        int foot,inch;
        foot = (int) mid;
        inch = (int) ((mid-foot)*12);
        System.out.println(foot+ " " + inch);
    }
}