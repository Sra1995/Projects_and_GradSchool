package step3;

public class Threaded extends Thread {
    private boolean flag = true;  // Control flag for stopping the thread

    public void run() {
        while (flag) {
            System.out.println(Thread.currentThread().getName() + ": Just keep swimming.");
            try {
                Thread.sleep(1000);  // Pause for 1 second
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    public void stopThreaded() {
        flag = false;  // Method to stop the thread by setting the flag to false
    }
}

