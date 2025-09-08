import java.util.Scanner;

public class crtsw6 {
    public static void main(String[] args) {
        int n;
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter any number: ");
        n = sc.nextInt();

        switch (n > 0 ? 1 : 0) {
            case 1:
                System.out.println(n + " is positive.");
                break;
            case 0:
                switch (n < 0 ? 1 : 0) {
                    case 1:
                        System.out.println(n + " is negative.");
                        break;
                    case 0:
                        System.out.println(n + " is zero.");
                        break;
                }
                break;
        }
    }
}
