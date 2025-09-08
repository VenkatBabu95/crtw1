import java.util.Scanner;

public class crtsw8{
    public static void main(String[] args) {
        float a, b, res;
        int op;
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter first number: ");
        a = sc.nextFloat();
        System.out.print("Enter second number: ");
        b = sc.nextFloat();

        System.out.println("Choose op.");
        op = sc.nextInt();

        switch(op) {
            case 1: res = a + b; break;
            case 2: res = a - b; break;
            case 3: res = a * b; break;
            case 4: res = a / b; break;
            default: res = 0; System.out.println("error"); break;
        }

        System.out.println("Result: " + res);
    }
}
