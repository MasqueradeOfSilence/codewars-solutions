function removeEveryOther(arr)
{
  var secondArr = [];
  var keep = true;
  for (var el in arr)
  {
    if (keep)
    {
      secondArr.push(arr[el]);
      keep = false;
    }
    else
    {
      keep = true;
    }
  }
  return secondArr;
}