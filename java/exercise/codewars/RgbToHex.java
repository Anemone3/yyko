/*
    by: s_ariku
    @codewars ref: https://www.codewars.com/kata/513e08acc600c94f01000001/train/java
*/

public class RgbToHex {

    public static void main(String[] args) {
        rgb(10, 10, 10);
    }

    public static String rgb(int r, int g, int b) {
        //System.out.println((char) ('A' + (14 - 10)));
        return toHex(r) + toHex(g) + toHex(b);
    }

    private static String toHex(int n) {

        if (n < 0)
            n = 0;
        if (n > 255)
            n = 255;

        int high = n / 16;
        int low = n % 16;

        return "" + hexChar(high) + hexChar(low);
    }

    private static char hexChar(int v) {
        return (char) (v < 10 ? ('0' + v) : ('A' + v - 10));
    }
}
// nivel noob
// public static String rgb(int r, int g, int b) {
// return toHex(r) + toHex(g) + toHex(b);
// }

// private static String toHex(int n) {

// if (n < 0)
// n = 0;
// if (n > 255)
// n = 255;
// if (n == 0)
// return "00";

// List<Character> list = new ArrayList<>();
// int r;
// char h;

// while (n > 0) {
// r = n % 16;

// if (r < 10) {
// h = (char) ('0' + r);
// } else {
// h = (char) ('A' + (r - 10));
// }

// list.add(h);
// n = n / 16;
// }

// Collections.reverse(list);

// StringBuilder sb = new StringBuilder();
// for (char c : list) {
// sb.append(c);
// }

// if (sb.length() == 1) {
// sb.insert(0, '0');
// }

// return sb.toString();
// }
