public class Kata 
{
  private static boolean isEven(int num)
  {
    return num % 2 == 0;
  }
  public static Integer center(int[][] matrix) 
  {
    // Even = no true center
    if (isEven(matrix.length) || isEven(matrix[0].length))
    {
      return null;
    }
    
    int centerRow = (int)Math.floor((int)(matrix.length / 2));
    int centerColumn = (int)Math.floor((int)(matrix[0].length / 2));
    
    return matrix[centerRow][centerColumn];
  }
}