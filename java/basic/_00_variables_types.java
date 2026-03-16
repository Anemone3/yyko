public class _00_variables_types {
    public static void main(String[] args) {
        // Enteros
        System.out.println("byte   : " + Byte.MIN_VALUE + " a " + Byte.MAX_VALUE);
        System.out.println("short  : " + Short.MIN_VALUE + " a " + Short.MAX_VALUE);
        System.out.println("int    : " + Integer.MIN_VALUE + " a " + Integer.MAX_VALUE);
        System.out.println("long   : " + Long.MIN_VALUE + " a " + Long.MAX_VALUE);

        // Decimales
        System.out.println("float  : " + Float.MIN_VALUE + " a " + Float.MAX_VALUE);
        System.out.println("double : " + Double.MIN_VALUE + " a " + Double.MAX_VALUE);

        // Carácter
        System.out.println("char   : " + (int) Character.MIN_VALUE + " a " + (int) Character.MAX_VALUE);

        // Boolean (no tiene rango numérico)
        System.out.println("boolean: " + Boolean.FALSE + " o " + Boolean.TRUE);

        // Ejemplo de valores
        byte b = 120;
        int i = 50000;
        long l = 10000000000L;
        float f = 3.14f;
        double d = 3.14159265359;
        char c = 'J';
        boolean activo = true;

        System.out.println("\n--- Ejemplos de uso ---");
        System.out.println("byte b       = " + b);
        System.out.println("int i        = " + i);
        System.out.println("long l       = " + l);
        System.out.println("float f      = " + f);
        System.out.println("double d     = " + d);
        System.out.println("char c       = " + c);
        System.out.println("boolean activo = " + activo);
    }
}