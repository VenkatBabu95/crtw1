import java.util.Scanner;

public class crtsw4 {
    public static void main(String[] args) {
        int n1, n2;
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter two numbers to find maximum: ");
        n1 = sc.nextInt();
        n2 = sc.nextInt();

        switch (n1 > n2 ? 1 : 2) {
            case 2: 
                System.out.println(n2 + " is maximum");
                break;
            case 1: 
                System.out.println(n1 + " is maximum");
                break;
        }
    }
}
