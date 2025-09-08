import java.util.Scanner;

public class crtsw2{
    public static void main(String[] args) {
        int m;
        Scanner sc = new Scanner(System.in);

        System.out.print("Month no. ");
        m = sc.nextInt();

        switch(m) {
            case 1: 
                System.out.println("31 days");
                break;
            case 2: 
                System.out.println("28/29 days");
                break;
            case 3: 
                System.out.println("31 days");
                break;
            case 4: 
                System.out.println("30 days");
                break;
            case 5: 
                System.out.println("31 days");
                break;
            case 6: 
                System.out.println("30 days");
                break;
            case 7: 
                System.out.println("31 days");
                break;
            case 8: 
                System.out.println("31 days");
                break;
            case 9: 
                System.out.println("30 days");
                break;
            case 10: 
                System.out.println("31 days");
                break;
            case 11: 
                System.out.println("30 days");
                break;
            case 12: 
                System.out.println("31 days");
                break;
            default: 
                System.out.println("Error");
        }
    }
}
