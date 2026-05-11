import java.util.Stack;

public class BaseChecker {
    public static String[] baseChecker(int nFloors) {
        return new String[0];
    }

    // { -> pop } ->
    public boolean isValid(String braces) {
        String appers = "{([";
        String closed = "})]";
        Stack<Character> pila = new Stack<>();
        for (int i = 0; i < braces.length(); i++) {
            char letter = braces.charAt(i);
            if (appers.indexOf(letter) != -1) {
                pila.push(letter);

            }
            if (closed.indexOf(letter) != -1) {
                if (pila.isEmpty()) {
                    return false;
                }
                char top = pila.peek();
                if (appers.indexOf(top) != closed.indexOf(letter)) {
                    return false;
                }
                pila.pop();
            }
        }

        return pila.isEmpty();
    }
}