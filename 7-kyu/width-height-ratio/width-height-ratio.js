// Function should take width and height of an image and return a ratio string (ex."16:9").
//If any of width or height entry is 0 function should raise an error.
function gcd(a, b)
{
  if (b === 0)
  {
    return a;
  }
  else
  {
    return gcd(b, a % b);
  }
}
function calculateRatio(w, h)
{
  if (w == 0 || h == 0)
  {
    throw new Error("not now kitten, daddy's solving codewars problems");
  }
  var the_gcd = gcd(w, h);
  w /= the_gcd;
  h /= the_gcd;
  
  var toReturn = (w + ":" + h);
  return toReturn;
  
}