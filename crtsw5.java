import java.util.Scanner;

public class crtsw5 {
    public static void main(String[] args) {
        int n;
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter any number to check even or odd: ");
        n = sc.nextInt();

        switch (n % 2) {
            case 0: 
                System.out.println("Even");
                break;
            case 1: 
                System.out.println("Odd");
                break;
        }
    }
}
