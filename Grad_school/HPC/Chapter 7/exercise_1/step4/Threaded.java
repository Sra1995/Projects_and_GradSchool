package step4;

import java.util.Random;

public class Threaded extends Thread {
    private boolean flag = true;
    private SharedInfo sharedInfo;
    private Random rand = new Random();

    public Threaded(SharedInfo sharedInfo) {
        this.sharedInfo = sharedInfo;
    }

    public void run() {
        while (flag) {
            if (rand.nextBoolean()) {
                sharedInfo.increment();
            } else {
                sharedInfo.decrement();
            }

            try {
                Thread.sleep(500);  // Slow down the operations
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    public void stopThreaded() {
        flag = false;
    }
}