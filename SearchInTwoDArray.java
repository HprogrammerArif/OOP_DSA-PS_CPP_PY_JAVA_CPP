import java.util.Arrays;

public class SearchInTwoDArray {
    public static void main(String[] args) {
        int[][] arr = {
                { 23, 4, 1 },
                { 63, 42, 17, 56 },
                { 28, 92, 11, 58, 44 }
        };

        int target = 17;
        int[] ans = search(arr, target);
        System.out.println(Arrays.toString(ans));

    }

    static int[] search(int[][] arr, int target) {
        for (int row = 0; row < arr.length; row++) {
            for (int col = 0; col < arr[row].length; col++) {
                // System.out.print(arr[row][col]+ " ");
                if (arr[row][col] == target) {
                    // return arr[row][col];
                    return new int[] { row, col };
                }
            }
            System.out.println();

        }
        return new int[] { -1, -1 };

    }
}
