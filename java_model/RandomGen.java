import java.util.Random;
import java.util.HashMap;
import java.util.Map;

public class RandomGen {
    private int[] randomNums;
    private float[] probabilities;

    public RandomGen(int[] randomNums, float[] probabilities) {
        this.randomNums = randomNums;
        this.probabilities = probabilities;
    }

    /**
     * Returns one of the randomNums. When this method is called
     * multiple times over a long period, it should return the
     * numbers roughly with the initialized probabilities.
     */
    public Map<Integer, Integer> nextNum() {
        float randVal = new Random().nextFloat();
        float cumulativeProb = 0;
        Map<Integer, Integer> results = new HashMap<>();
        for (int i = 0; i < probabilities.length; i++) {
            cumulativeProb += probabilities[i];
            if (randVal <= cumulativeProb) {
                int num = randomNums[i];
                results.put(num, results.getOrDefault(num, 0) + 1);
                break;
            }
        }
        return results;
    }
}
