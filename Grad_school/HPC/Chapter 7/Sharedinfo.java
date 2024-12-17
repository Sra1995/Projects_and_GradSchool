public class SharedInfo
{
    int sharedCounter = 0;


    /*
     * I have ensured that two processes can't both be excuting increment code at the same time
     * However, I have no protected agaisnt one process executing incfeamnet and one executing decrment
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

    // I f I want multiple threads to be doing stuff here and each on finish 
    // what it is doing then I need to provide a a singular access point that they 
    // all use that restricts them to one at a time.

    public synchronized void doTheThing(int id)
    {
        system.out.println("Threaded thread"+id+": say hi once: "+ sharedCounter);
        if (id ==1)
            increment();
        if (id ==2)
            decrement();
    }
}
 
