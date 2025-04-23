
import java.util.Scanner;

public class unitsConverter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the unit type (length, temperature, weight): ");
        String unitType = scanner.next().toLowerCase();

        System.out.print("Enter the unit to convert from (e.g., kilometers, celsius, kilograms): ");
        String fromUnit = scanner.next().toLowerCase();

        System.out.print("Enter the unit to convert to (e.g., miles, fahrenheit, pounds): ");
        String toUnit = scanner.next().toLowerCase();

        System.out.print("Enter the value: ");
        double value = scanner.nextDouble();


        double convertedValueResult;

        switch (unitType) {
            case "length" -> {
                if (fromUnit.equals("kilometers") && toUnit.equals("miles")) {
                    convertedValueResult = value * 0.621371;
                } else if (fromUnit.equals("miles") && toUnit.equals("kilometers")) {
                    convertedValueResult = value * 1.60934;
                } else {
                    System.out.println("Invalid length conversion.");
                    return;
                }
            }
            case "temperature" -> {
                if (fromUnit.equals("celsius") && toUnit.equals("fahrenheit")) {
                    convertedValueResult = (value * 9 / 5) + 32;
                } else if (fromUnit.equals("fahrenheit") && toUnit.equals("celsius")) {
                    convertedValueResult = (value - 32) * 5 / 9;
                } else {
                    System.out.println("Invalid temperature conversion.");
                    return;
                }
            }
            case "weight" -> {
                if (fromUnit.equals("kilograms") && toUnit.equals("pounds")) {
                    convertedValueResult = value * 2.20462;
                } else if (fromUnit.equals("pounds") && toUnit.equals("kilograms")) {
                    convertedValueResult = value * 0.453592;
                } else {
                    System.out.println("Invalid weight conversion.");
                    return;
                }
            }
            default -> {
                System.out.println("Invalid unit type.");
                return;
            }
        }
        System.out.println("Converted value: " + convertedValueResult + " " + toUnit);
    }
}

