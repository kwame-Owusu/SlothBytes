import  java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        String res1 = String.join(" ", pigLatinSentence("hello world"));
        String res2 = String.join(" ", pigLatinSentence("this is pig latin"));
        String res3 = String.join(" ", pigLatinSentence("wall street journal"));


        System.out.println(res1);
        System.out.println(res2);
        System.out.println(res3);
    }

    public static String[] pigLatinSentence(String sentence) {
        String vowels = "aeiou";
        String[] words = sentence.split(" ");
        String[] pigLatinWords = new String[words.length];

        // Iterate through each word and convert it to Pig Latin
        for (int i = 0; i < words.length; i++) {
            String word = words[i];

            // If the first character is a vowel
            if (vowels.indexOf(Character.toLowerCase(word.charAt(0))) != -1) {
                pigLatinWords[i] = word + "way";  // Add "way" if it starts with a vowel
            } else {
                // Move the first letter to the end and add "ay"
                pigLatinWords[i] = word.substring(1) + word.charAt(0) + "ay";
            }
        }

        return pigLatinWords;
    }
}
