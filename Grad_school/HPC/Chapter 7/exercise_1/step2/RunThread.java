package step2;

public class RunThread {
    public static void main(String[] args) {
        Threaded t = new Threaded();  // Create a new thread
        t.start();  // Start the thread

        try {
            Thread.sleep(5000);  // Let the thread run for 5 seconds
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        t.stopThreaded();  // Stop the thread by setting the flag to false
        System.out.println("Thread stopped.");
    }
}
