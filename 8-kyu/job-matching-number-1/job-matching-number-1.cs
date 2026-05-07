using StriveObjects;
using System;
​
public class Strive
{
  public static bool Match(Candidate c, Job j)
  {
    if (c.MinSalary == null || j.MaxSalary == null)
    {
      throw new ArgumentNullException();
    }
    else
    {
      double minSalaryReq = c.MinSalary.Value - (.1 * c.MinSalary.Value);
      double maxSalaryOffered = j.MaxSalary.Value;
      if (maxSalaryOffered < minSalaryReq)
      {
        return false;
      }
      return true;
    }
  }
}