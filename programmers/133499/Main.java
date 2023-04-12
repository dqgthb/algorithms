public class Main {
    public static void main(String args[]) {
        var solution = new Solution();

        String[] babbling = { "ayaaya", "yemawoo", "u", "maa" };
        int answer = solution.solution(babbling);
        System.out.println(answer);

        String[] input2 = { "ayaye", "uuu", "yeye", "yemawoo", "ayaayaa" };
        int answer2 = solution.solution(input2);
        System.out.println(answer2);

    }

}