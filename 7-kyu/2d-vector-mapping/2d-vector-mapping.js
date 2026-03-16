function mapVector(vector, circle1, circle2) 
{
  // P' = C₂ + (P - C₁) × (r₂ / r₁)
  var term2 = [vector[0] - circle1[0], vector[1] - circle1[1]];
  var term3 = circle2[2] / circle1[2];
  var term1 = circle2;
  var toReturn = [term1[0] + term2[0] * term3, term1[1] + term2[1] * term3];
  return toReturn;
}
​
/*
  Test cases:
  vector = 5, 5
  circle1 = 10, 20, 42
  circle2 = -100, -42, 69
​
  term2 = [5 - 10, 5 - 20] = [-5, -15]
  term3 = 1.64
  term1 = -100, -42, 69
  toReturn = [-100 + -5 * 1.64, -42 + -15 * 1.64]
    = [-100 - 8.2, -42 - 24.6] = [-108.2, -66.6]
    Validated.
*/