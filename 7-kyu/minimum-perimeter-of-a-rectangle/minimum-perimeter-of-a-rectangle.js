​
function minimumPerimeter(area) 
{
  var best = null;
  for (var a = 1; a < Math.sqrt(area) + 1; a++)
  {
    if (area % a == 0)
    {
      var b = area / a;
      var perimeter = 2 * (a + b);
      if (best == null || perimeter < best)
      {
        best = perimeter;
      }
    }
  }
  return best;
}
/*
  This is a factoring type problem
*/
​