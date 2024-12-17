public class SerialSummation {
    public static void main(String[] args) {
        long[] ns = {1_000_000L, 100_000_000L, 1_000_000_000L};

        for (long n : ns) {
            long sum = 0;
            long startTime = System.nanoTime();

            for (long i = 1; i <= n; i++) {
                sum += i;
            }

            long endTime = System.nanoTime();
            System.out.println("Sum: " + sum + ", Time: " + (endTime - startTime) / 1_000_000 + " ms for n = " + n);
        }
    }
}
