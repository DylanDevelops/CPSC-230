package Extra_Projects;
import java.util.Scanner;

public class HelloWorld {
    public static void main(String[] args) {
        int x;
        int y;
        int z;

        Scanner scanner = null;

        try {
            scanner = new Scanner(System.in);

            while (true) {
                try {
                    System.out.println("Enter the first number:");
                    x = Integer.parseInt(scanner.nextLine());
                    break;
                } catch (Exception e) {
                    System.out.println("Not a valid number, please try again!");
                }
            }

            while (true) {
                try {
                    System.out.println("Enter the second number:");
                    y = Integer.parseInt(scanner.nextLine());
                    break;
                } catch (Exception e) {
                    System.out.println("Not a valid number, please try again!");
                }
            }

            z = x + y;
            
            System.out.println(x + " + " + y + " = " + z);
        } finally {
            if(scanner != null) {
                scanner.close();
            }
        }
    }
}

