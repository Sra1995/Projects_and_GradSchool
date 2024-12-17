class SummationThread extends Thread {
    private long start, end, sum;

    public SummationThread(long start, long end) {
        this.start = start;
        this.end = end;
    }

    public void run() {
        sum = 0;
        for (long i = start; i <= end; i++) {
            sum += i;
        }
    }

    public long getSum() {
        return sum;
    }
}

public class ThreadedSummation {
    public static void main(String[] args) {
        long[] ns = {1_000_000L, 100_000_000L, 1_000_000_000L};

        for (long n : ns) {
            long totalSum = 0;
            SummationThread[] threads = new SummationThread[8];
            long startTime = System.nanoTime();

            // Divide the summation range among 8 threads
            long range = n / 8;
            for (int i = 0; i < 8; i++) {
                long start = i * range + 1;
                long end = (i == 7) ? n : (i + 1) * range;
                threads[i] = new SummationThread(start, end);
                threads[i].start();
            }

            // Combine results from all threads
            for (int i = 0; i < 8; i++) {
                try {
                    threads[i].join();
                    totalSum += threads[i].getSum();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }

            long endTime = System.nanoTime();
            System.out.println("Total Sum: " + totalSum + ", Time: " + (endTime - startTime) / 1_000_000 + " ms for n = " + n);
        }
    }
}
