import java.util.Arrays;

public class _01_strings {
    public static void main(String[] args) {
        String name = "Jane Doe";
        System.out.println(name);

        // String concatenation
        String firstName = "Jane";
        String lastName = "Doe";
        String fullName = firstName + " " + lastName;
        System.out.println(fullName);

        // String methods
        System.out.println("Length of full name: " + fullName.length());
        System.out.println("Uppercase full name: " + fullName.toUpperCase());
        System.out.println("Lowercase full name: " + fullName.toLowerCase());

        System.out.println("a" + " is in fullName: " + fullName.contains("a")); // This will check if the string "a" is
                                                                                // contained in fullName

        System.out.println("Index of 'Doe': " + fullName.indexOf("Doe")); // This will return the index of the first
                                                                          // occurrence of "Doe" in fullName

        System.out.println("Last index of 'e': " + fullName.lastIndexOf("e")); // This will return the index of the last
                                                                               // occurrence of "e"
        // in fullName

        System.out.println("Substring of full name (0, 4): " + fullName.substring(0, 4)); // This will return the
                                                                                          // substring of fullName
        // starting from index 0 to index 4 (exclusive)

        /* === CHARS == */
        char firstChar = fullName.charAt(0);
        System.out.println("First character of full name: " + firstChar);

        char lastChar = fullName.charAt(fullName.length() - 1);
        System.out.println("Last character of full name: " + lastChar);

        // using Array Char
        char[] charArray = fullName.toCharArray();
        System.out.println("Characters in full name:");
        for (char c : charArray) {
            System.out.print(c + " ");
        }
        String wordToChar = "Listen".toLowerCase();
        String word2ToChar = "Silent".toLowerCase();
        char[] wordCharArray = wordToChar.toCharArray();
        char[] word2CharArray = word2ToChar.toCharArray();
        //sort
        Arrays.sort(wordCharArray);
        Arrays.sort(word2CharArray);
        if (Arrays.equals(wordCharArray, word2CharArray)) {
            System.out.println("\n" + wordToChar.substring(0,1).toUpperCase() + wordToChar.substring(1) + " and " + word2ToChar.substring(0,1).toUpperCase() + word2ToChar.substring(1) + " are anagrams.");
        } else {
            System.out.println("\n" + wordToChar.substring(0,1).toUpperCase() + wordToChar.substring(1) + " and " + word2ToChar.substring(0,1).toUpperCase() + word2ToChar.substring(1) + " are not anagrams.");
        }
        
        // ternaria
        String result = (wordToChar.equals(word2ToChar)) ? "The words are the same." : "The words are different.";
        System.out.println(result);
        
    }
}