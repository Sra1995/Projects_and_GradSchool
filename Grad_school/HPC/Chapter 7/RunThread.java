Public class Run Thread
{
    // Parallels C's void main (int argc, char * argv[])

    public static void main(String[] args)
    {
        int len = args.length; // saves having to add an int parameter to every method you pass in an array
        SharedInfo si = new SharedInfo();
        Threaded t = new Threaded(si,1);
        t.start(); // Starts up the thread.
        Threaded t2 = new Threaded(si, 2);
        t2.start(); // Starts up the thread.
        for ( int i=0;i<1000;i++)
            System.out.println("Main Thread: " + i);
        t.stopThread(); // Stops the thread.
        t2.stopThread(); // Stops the thread.
        // t.stop(); // Deprecated method. no longer supported and for threads very bad to have a thread stop suddenly without warning.
    }
}