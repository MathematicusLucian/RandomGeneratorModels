import static org.junit.Assert.*;
import org.junit.Test;

public class RandomGenTest {
    @Test
    public void testValidRandomNumber() {
        int[] randomNums = {-1, 0, 1, 2, 3};
        float[] probabilities = {0.01f, 0.3f, 0.58f, 0.1f, 0.01f};
        RandomGen randomGen = new RandomGen(randomNums, probabilities);

        int num = randomGen.nextNum();
        boolean isValid = false;
        
        for (int i : randomNums) {
            if (i == num) {
                isValid = true;
                break;
            }
        }

        assertTrue(isValid);
    }

    @Test
    public void testNonEmptyResponse() {
        int[] randomNums = {-1, 0, 1, 2, 3};
        float[] probabilities = {0.01f, 0.3f, 0.58f, 0.1f, 0.01f};

        RandomGen randomGen = new RandomGen(randomNums, probabilities);

        int num = randomGen.nextNum();

        assertTrue(num != 0);
    }

    @Test
    public void testEmptyInputArrays() {
        int[] randomNums = {};
        float[] probabilities = {};

        RandomGen randomGen = new RandomGen(randomNums, probabilities);

        int num = randomGen.nextNum();

        assertEquals(-1, num);
    }
}
