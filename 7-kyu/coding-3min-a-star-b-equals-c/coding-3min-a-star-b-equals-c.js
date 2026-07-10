function findAB(numbers,c){
  for (var i = 0; i < numbers.length; i++)
  {
    for (var j = 0; j < numbers.length; j++)
    {
      if (i != j && numbers[i] * numbers[j] == c)
      {
        return [numbers[i], numbers[j]];
      }
    }
  }
  return null;
}