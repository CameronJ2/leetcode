public class App {
    public static void main(String[] args) throws Exception {
        // String s = "Hello World";
        // String s = " fly me to the moon ";
        String s = "luffy is still joyboy";
        System.out.println(lengthOfLastWord(s));
    }

    public static int lengthOfLastWord(String s) {
        String[] words = s.split(" ");
        int length = words[words.length - 1].length();
        return length;
    }
}
