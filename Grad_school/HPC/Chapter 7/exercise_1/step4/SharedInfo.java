package step4;

class SharedInfo {
    private int sharedCounter = 0;

    public synchronized void increment() {
        sharedCounter++;
        System.out.println(Thread.currentThread().getName() + ": Incremented, Counter = " + sharedCounter);
    }

    public synchronized void decrement() {
        sharedCounter--;
        System.out.println(Thread.currentThread().getName() + ": Decremented, Counter = " + sharedCounter);
    }
}