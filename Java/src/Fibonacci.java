public class Fibonacci {
    private int firstTerm;
    private int secondTerm;

    public Fibonacci(int f1, int f2){
        firstTerm = f1;
        secondTerm = f2;
    }

    public int getNthTerm(int n){
        int fNMinusOne = firstTerm;
        int fN = secondTerm;
        for (int i = 0; i <= n; i++){
            int fnCopy = fN;
            fN += fNMinusOne;
            fNMinusOne = fnCopy;
        }
        return fNMinusOne;
    }


}
