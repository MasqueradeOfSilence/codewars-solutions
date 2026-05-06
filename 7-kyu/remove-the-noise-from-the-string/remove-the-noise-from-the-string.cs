using System.Text.RegularExpressions;
​
public class Kata
{
  public static string RemoveNoise(string message)
  {
    return Regex.Replace(message, @"[%$&/#·@|º\\ª]", "");
  }
}