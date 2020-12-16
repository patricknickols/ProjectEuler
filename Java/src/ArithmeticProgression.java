public class ArithmeticProgression {
    private double firstTerm;
    private double commonDifference;
    private double numTerms;

    public ArithmeticProgression(double firstTerm, double commonDifference, double numTerms){
        this.firstTerm = firstTerm;
        this.commonDifference = commonDifference;
        this.numTerms = numTerms;
    }
    public ArithmeticProgression(double firstTermAndDifference, double numTerms){
        this.firstTerm = firstTermAndDifference;
        this.commonDifference = firstTermAndDifference;
        this.numTerms = numTerms;
    }

    public double sumProgression(){
        return (numTerms / 2) * (2 * firstTerm + ((numTerms - 1) * commonDifference));
    }

}
