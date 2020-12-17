public class ProblemOne {

    public static void main(String[] args) {
        ArithmeticProgression threes = new ArithmeticProgression(3.0, 333);
        ArithmeticProgression fives = new ArithmeticProgression(5.0,199);
        ArithmeticProgression fifteens = new ArithmeticProgression(15.0, 66);
        System.out.println();
        double sumThrees = threes.sumProgression();
        double sumFives = fives.sumProgression();
        double sumFifteens = fifteens.sumProgression();
        double answer = sumThrees + sumFives - sumFifteens;
        System.out.println(answer);
    }
}
