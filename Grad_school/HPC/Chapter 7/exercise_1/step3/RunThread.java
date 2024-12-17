package step3;

public class RunThread {
    public static void main(String[] args) {
        Threaded[] threads = new Threaded[5];  // Create an array for 5 threads

        // Create and start 5 threads
        for (int i = 0; i < 5; i++) {
            threads[i] = new Threaded();  // Create a new thread
            threads[i].start();  // Start the thread
        }

        try {
            Thread.sleep(5000);  // Let the threads run for 5 seconds
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        // Stop all 5 threads
        for (int i = 0; i < 5; i++) {
            threads[i].stopThreaded();  // Stop each thread
        }

        System.out.println("All threads stopped.");
    }
}

