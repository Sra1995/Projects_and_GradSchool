public class RunThread
{
    // Parallels C's void main(int argc, char *argv[])
    public static void main(String[] args)
    {
        int len = args.length; // saves having to add an int parameter to every method you pass in an array.
        SharedInfo si = new SharedInfo();
        Threaded t = new Threaded(si,1);
        t.start(); // Starts up the thread.
        Threaded t2 = new Threaded(si,2);
        t2.start(); // Starts up the thread.
        for (int i=0;i<5000;i++)
            System.out.print("Main Thread.");
        t.stopThread();
        t2.stopThread();
        // t.stop(); deprecated - no longer supported and for threads very bad to just stop it without warning.
    }

}
