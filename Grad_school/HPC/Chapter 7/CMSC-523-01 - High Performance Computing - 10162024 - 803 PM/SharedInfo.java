public class SharedInfo
{
    int sharedCounter = 0;

    /**
     * I've ensured that two processes can't both be executing increment code at the same time.
     * However, I have not protected against one process executing increment and one executing decrement
     * at the same time.
     */
    public synchronized void increment()
    {
        sharedCounter++;
    }

    public synchronized void decrement()
    {
        sharedCounter--;
    }

    // If I want multiple threads to be doing stuff here and each one finish
    // what it is doing then I need to provide a singular access point that they
    // all use that restricts them to one at a time.
    public synchronized void doTheThing(int id)
    {
        //System.out.println("\nThreaded Thread" + id + ": Say hi once: " + sharedCounter);
        if (id == 1)
            decrement();
        if (id == 2)
            increment();
    }

}
