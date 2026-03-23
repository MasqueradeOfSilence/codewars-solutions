import java.util.*;
​
public class DescendingOrder 
{
  public static int sortDesc(final int num) 
  {
    String numAsStr = String.valueOf(num);
    ArrayList<Integer> theNums = new ArrayList<>();
​
    for (int i = 0; i < numAsStr.length(); i++) 
    {
      char current = numAsStr.charAt(i);
      theNums.add(Character.getNumericValue(current));
    }
​
    theNums.sort(Collections.reverseOrder());
​
    StringBuilder sorted = new StringBuilder();
    for (int i = 0; i < theNums.size(); i++) 
    {
      sorted.append(theNums.get(i));
    }
​
    return Integer.parseInt(sorted.toString());
  }
}