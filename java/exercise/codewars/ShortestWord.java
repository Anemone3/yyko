
public class ShortestWord {

    public static void main(String[] args) {
        String test_input = "bitcoin take over the world maybe who knows perhaps";
        int result = findShort(test_input);
        if (result == 3) {
            System.out.println("Pass");
        } else {
            System.out.println("Failed pass");
        }

        System.out.println("result: " + result);

    }

    public static int findShort(String s) {
        String[] words = s.split(" ");
        int result = words[0].length();
        for(String c:words){
            result = Math.min(result, c.length());
        }
        return result;
    }
}