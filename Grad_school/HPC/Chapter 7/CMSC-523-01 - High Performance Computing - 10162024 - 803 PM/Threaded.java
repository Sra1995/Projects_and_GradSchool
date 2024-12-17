public class Threaded extends Thread
{
    SharedInfo info;
    int id;

    public Threaded(SharedInfo si,int i)
    {
        info = si;
        id = i;
    }
    boolean flag = true;
    public void run()
    {
        while(flag)
        {
            // We would like to make sure this all happens in a block so that
            // we don't get confused by who has done what when.
            // Each thread has no idea what the other threads are doing, they are each their
            // own entity.
            System.out.println("\nThreaded Thread" + id + ": Say hi once: " + info.sharedCounter);
            info.doTheThing(id);
        }
    }

    public synchronized void doTheThing()
    {
        System.out.println("\nThreaded Thread" + id + ": Say hi once: " + info.sharedCounter);
        if (id == 1)
            info.decrement();
        if (id == 2)
            info.increment();
    }

    public void stopThread()
    {
        flag = false;
    }
}
