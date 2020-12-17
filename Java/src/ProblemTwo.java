public class ProblemTwo {


    public static void main(String[] args) {
        Fibonacci stdFib = new Fibonacci(1,0);
        int n = 3;
        int sum = 0;
        while (stdFib.getNthTerm(n) <= 4000000){
            sum += stdFib.getNthTerm(n);
            n += 3;
        }
        System.out.println(sum);
    }
}
