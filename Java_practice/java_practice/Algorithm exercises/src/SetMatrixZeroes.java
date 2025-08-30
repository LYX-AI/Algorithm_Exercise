import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class SetMatrixZeroes {
    public void setZero(int[][] matrix){
        int m = matrix.length;
        int n = matrix[0].length;

        Set<Integer> markCol = new HashSet<>();
        boolean[] markRow = new boolean[m];

        for(int i = 0;i < m;i++){
            for(int j =0; j<n;j++){
                if(matrix[i][j] == 0){
                    markRow[i] = true;
                    markCol.add(j);
                }
            }
        }
        for (int i =0;i<m;i++){
            if(markRow[i]){
                Arrays.fill(matrix[i],0);
            }
        }
        for(int j:markCol){
            for(int i = 0;i<m;i++){
                matrix[i][j] = 0;
            }
        }
    }

    public static void main(String[] args){
        SetMatrixZeroes solution = new SetMatrixZeroes();
        int[][] matrix2 = {{0,1,2,0}, {3,4,5,2}, {1,3,1,5}};
        solution.setZero(matrix2);
        System.out.println(Arrays.deepToString(matrix2));
    }
}
