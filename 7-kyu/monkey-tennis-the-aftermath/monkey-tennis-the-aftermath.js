function ballCollector(detritus) 
{
  var totalWeight = 0;
  for (var i = 0; i < detritus.length; i++)
  {
    if (detritus[i] == 58)
    {
      totalWeight += detritus[i];
    }
  }
  return {weight: totalWeight};
}