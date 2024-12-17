public class Threaded extends Thread
{
    SharedInfo info;

    public Threaded(SharedInfo si, int i)
    {
        info = si;
        id = i;
    }

    public void run()
    {
        boolean flag = true;
        while(flag)
        {
            // we would like to make sure this all happens in a black so that
            // we don't get confused by who has done what.
            // Each thread has no idea what the other threads are doing, they are each their
            // own entity.
            System.out.println(“\n Threaded thread"+id+": say hi once: “+ info.sharedCounter);
            if (id ==1)
                info.increment();
            if (id ==2)
                info.decrement();

        }
    }
}

public synchronized void doTheThing()
{

    public void stopThread()
    {
        flag = false;
    }

}