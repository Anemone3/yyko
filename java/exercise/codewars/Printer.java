
public class Printer {

    public static String printerError(String s) {
        int longitud = s.length();
        int errors = 0;
        for (int i = 0; i < longitud; i++) {
            char c = s.charAt(i);
            if (c >= 'n') {
                errors += 1;
            }
        }
        return errors + "/" + longitud;
    }
}