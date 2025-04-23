import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class guessingNumber {
    public static void main (String[] args){
        //Guessing number game i used to play on my friends,easier to do calculations in head
        Scanner scanner = new Scanner(System.in);

        String[] acknowledgements = {"yes","y"};

        System.out.println("Guess a number, but do not reveal it");
        System.out.println("Type Yes/y once done");

        String firstAcknowledgement = scanner.next().toLowerCase();
        boolean contains = Arrays.stream(acknowledgements).anyMatch(a -> a.contains(firstAcknowledgement));
        if (!contains){
           System.out.println("Well.... would you still like to continue the game?, if Yes, ");

        }

        System.out.println("Now type in your answer");
        double value = scanner.nextDouble();

    }
}
