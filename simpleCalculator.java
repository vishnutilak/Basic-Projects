import java.util.Scanner;


public class simpleCalculator {
    public static void main(String[] args) {
        // input
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the first number: ");
        double num1 = scanner.nextDouble();
        System.out.print("Enter the second number: ");
        double num2 = scanner.nextDouble();

        // Input the operation
        System.out.println("Enter an operator (+, -, *, /): ");
        char operator = scanner.next().charAt(0);

        //initialize result variable
        double result = 0;

        // main calculation here
        if (operator == '+') result = num1 + num2;
        else if (operator == '-') result = num1 - num2;
        else if (operator == '*') result = num1 * num2;
        else if (operator == '/') {
            if (num2 != 0) {
                result = num1 / num2;
            } else {
                System.out.println("Error! Division by zero.");
                return;
            }
        } else {
            // If an invalid operator is entered
            System.out.println("Invalid operator! Please enter +, -, *, or /.");
            return;
        }

        System.out.println("The result is: " + result);
    }
}

