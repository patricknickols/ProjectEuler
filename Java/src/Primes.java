public interface Primes {

    static boolean isPrime(int k){
        double sqrt = Math.sqrt(k);
        for (int i = 2; i <= sqrt; i++){
            if (k % i == 0){
                return false;
            }
        }
        return true;
    }

    static long largestPrimeFactor(long n){
        long lastFactor;
        if (n % 2 == 0){
            n = n/2;
            lastFactor = 2;
            while (n % 2 == 0){
                n = n/2;
            }
        }
        else {
            lastFactor = 3;
        }
        int factor = 3;
        while (n > 1){
            if (n % factor == 0){
                n = n / factor;
                lastFactor = factor;
                while (n % factor == 0){
                    n = n/ factor;
                }
            }
            factor += 2;
        }
        return lastFactor;
    }

}
