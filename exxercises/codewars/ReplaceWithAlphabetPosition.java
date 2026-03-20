
public class ReplaceWithAlphabetPosition {
    public static void main(String[] args) {
        String input = "The sunset sets at twelve o' clock.";
        String output = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11";
        if (output.equals(alphabetPosition(input))) {
            System.out.println("Success");
        } else {
            System.out.println("Failed");
        }
    }

    static String alphabetPosition(String text) {
        String format = text.trim();
        StringBuilder result = new StringBuilder();
        for (char c : format.toCharArray()) {
            if (Character.isLetter(c)) {
                int pos = Character.toLowerCase(c) - 'a' + 1;
                if (result.length() > 0) {
                    result.append(" ");
                }

                result.append(pos);
            }
        }
        return result.toString();
    }
}