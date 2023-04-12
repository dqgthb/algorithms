public class Solution {
    String[] candidates = { "aya", "ye", "woo", "ma" };

    public int solution(String[] babbling) {
        int answer = 0;

        for (var word : babbling) {
            if (canMake(word, -1)) {
                System.out.println(word);
                answer++;
            }
        }

        return answer;
    }

    public boolean canMake(String word, int prevIdx) {
        if (word == "") {
            return true;
        }

        boolean is_possible = false;
        int idx = 0;

        for (var candidate : candidates) {
            if (idx != prevIdx &&
                    word.length() >= candidate.length() &&
                    word.startsWith(candidate)) {
                is_possible = is_possible || canMake(word.substring(candidate.length()), idx);
            }
            idx++;
        }

        return is_possible;
    }

    public void test() {
        System.out.println("testing...");
        test_canMake();
    }

    public void test_canMake() {
        assert true == canMake("ayaye", -1);
        assert false == canMake("ayayea", -1);
    }

}
