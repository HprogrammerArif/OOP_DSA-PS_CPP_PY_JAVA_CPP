package SoOn;
//https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/

public class EvenDigits {
    public static void main(String[] args) {
        int[] nums = { 12, 345, 2, 6, 7896 };
        System.out.println("The Events digits are: "+ findNumbers(nums));
        ;
    }

    static int findNumbers(int[] nums) {
        int count = 0;
        for (int num : nums) {
            if (even(num)) {
                count++;
            }
        }
        return count;
    }

    static boolean even(int num) {
        int noOfDigits = digits(num);

        if (noOfDigits % 2 == 0) {
            return true;
        }
        return false;
    };

    // count number of digits in a number
    static int digits(int num) {

        if(num<0) {
            num = num *-1;
        }
        if(num==0) {
           return 1;
        }

        int count = 0;

        while (num > 0) {
            count++;
            num = num / 10;
        }

        return count;
    }
}
