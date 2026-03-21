function betterThanAverage(classPoints, yourPoints) 
{
  var classmateCount = classPoints.length + 1;
  var sum = 0;
  for (var score of classPoints)
  {
    sum += score;
  }
  sum += yourPoints;
  var average = sum / classmateCount;
  return yourPoints > average;
}
​