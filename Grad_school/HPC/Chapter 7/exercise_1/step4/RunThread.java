package step4;

public class RunThread {
    public static void main(String[] args) {
        SharedInfo sharedInfo = new SharedInfo();
        Threaded[] threads = new Threaded[5];

        // Create and start 5 threads
        for (int i = 0; i < 5; i++) {
            threads[i] = new Threaded(sharedInfo);
            threads[i].start();
        }

        try {
            Thread.sleep(5000);  // Let the threads run for 5 seconds
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        // Stop all 5 threads
        for (int i = 0; i < 5; i++) {
            threads[i].stopThreaded();
        }
    }
}
