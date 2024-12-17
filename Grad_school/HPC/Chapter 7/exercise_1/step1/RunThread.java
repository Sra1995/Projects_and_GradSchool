package step1;

public class RunThread {
    public static void main(String[] args) {
        Threaded t = new Threaded();  // Create a new thread
        t.start();  // Start the thread
        System.out.println("Main Thread.");  // Print from the main thread
    }
}
