import java.util.HashSet;
import java.util.Set;

public class ValidSudoku {

    public static void main(String[] args) {
        char[][] inputBoard = {
                { '1', '2', '.', '.', '3', '.', '.', '.', '.' },
                { '4', '.', '.', '5', '.', '.', '.', '.', '.' },
                { '.', '9', '8', '.', '.', '.', '.', '.', '3' },
                { '5', '.', '.', '.', '6', '.', '.', '.', '4' },
                { '.', '.', '.', '8', '.', '3', '.', '.', '5' },
                { '7', '.', '.', '.', '2', '.', '.', '.', '6' },
                { '.', '.', '.', '.', '.', '.', '2', '.', '.' },
                { '.', '.', '.', '4', '1', '9', '.', '.', '8' },
                { '.', '.', '.', '.', '8', '.', '.', '7', '9' }

        };
        boolean expectOutput = true;

        if (ValidSudoku.isValidSudoku(inputBoard) == expectOutput) {
            System.out.println("Success");
        } else {
            System.out.println("Failed");
        }
    }

    // https://neetcode.io/problems/valid-sudoku/question?list=neetcode150

    // public static boolean isValidSudoku(char[][] board) {

    // Map<Integer, Set<Character>> rows = new HashMap<>();
    // Map<Integer, Set<Character>> cols = new HashMap<>();
    // Map<String, Set<Character>> squares = new HashMap<>();

    // for (int r = 0; r < 9; r++) {
    // for (int c = 0; c < 9; c++) {

    // char value = board[r][c];
    // if (value == '.')
    // continue;

    // rows.putIfAbsent(r, new HashSet<>());
    // cols.putIfAbsent(c, new HashSet<>());
    // String key = (r / 3) + "," + (c / 3);
    // squares.putIfAbsent(key, new HashSet<>());

    // if (rows.get(r).contains(value) ||
    // cols.get(c).contains(value) ||
    // squares.get(key).contains(value)) {
    // return false;
    // }

    // rows.get(r).add(value);
    // cols.get(c).add(value);
    // squares.get(key).add(value);
    // }
    // }

    // return true;
    // }

    public static boolean isValidSudoku(char[][] board) {

        for (int i = 0; i < 9; i++) {
            Set<Character> set = new HashSet<>();
            for (int j = 0; j < 9; j++) {
                char c = board[i][j];
                if (c == '.')
                    continue;

                if (!set.add(c))
                    return false;
            }
        }

        for (int j = 0; j < 9; j++) {
            Set<Character> set = new HashSet<>();
            for (int i = 0; i < 9; i++) {
                char c = board[i][j];
                if (c == '.')
                    continue;

                if (!set.add(c))
                    return false;
            }
        }

        for (int boxRow = 0; boxRow < 3; boxRow++) {
            for (int boxCol = 0; boxCol < 3; boxCol++) {

                Set<Character> set = new HashSet<>();

                for (int i = 0; i < 3; i++) {
                    for (int j = 0; j < 3; j++) {

                        char c = board[boxRow * 3 + i][boxCol * 3 + j];
                        if (c == '.')
                            continue;

                        if (!set.add(c))
                            return false;
                    }
                }
            }
        }

        return true;
    }

    // public static boolean isValidSudoku(char[][] board) {

    // for (int b = 0; b < board.length; b++) {
    // Set<Character> set = new HashSet<>();

    // for (int i = 0; i < board[b].length; i++) {
    // if (!set.add(board[b][i])) {
    // return false;
    // }
    // }
    // }

    // int i = 0, max = board.length;
    // int x = 0;
    // int y = 0;
    // while (i < max) {

    // char[] row_a = board[x];
    // char[] row_b = board[x + 1];
    // char[] row_c = board[x + 2];

    // Set<Character> row = new HashSet<>();

    // while (true) {
    // int a = 0, b = 1, c = 2;

    // if (a >= 6 || b >= 7 || c >= 8) {
    // break;
    // }

    // // pasarlo a lista, hacer un set.size() == list.length() -> continue sino
    // return
    // // false
    // if (!row.add(row_a[a]) || !row.add(row_a[b]) || !row.add(row_a[c])) {
    // return false;
    // }

    // if (!row.add(row_b[a]) || !row.add(row_b[b]) || !row.add(row_b[c])) {
    // return false;
    // }
    // if (!row.add(row_c[a]) || !row.add(row_c[b]) || !row.add(row_c[c])) {
    // return false;
    // }

    // a += 3;
    // b += 3;
    // c += 3;
    // }

    // char[] column_a = board[y];
    // char[] column_b = board[y + 3];
    // char[] column_c = board[y + 6];
    // Set<Character> column = new HashSet<>();

    // while (true) {
    // int a = 0, b = 3, c = 6;

    // if (a >= 2 || b >= 5 || c >= 8) {
    // break;
    // }

    // if (!column.add(column_a[a]) || !column.add(column_a[b]) ||
    // !column.add(column_a[c])) {
    // return false;
    // }

    // if (!column.add(column_b[a]) || !column.add(column_b[b]) ||
    // !column.add(column_b[c])) {
    // return false;
    // }
    // if (!column.add(column_c[a]) || !column.add(column_c[b]) ||
    // !column.add(column_c[c])) {
    // return false;
    // }

    // a++;
    // b++;
    // c++;
    // }
    // x += 3;
    // y += 1;
    // i++;
    // }

    // return true;
    // }
}
