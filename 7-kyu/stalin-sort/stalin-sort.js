function stalinSort(array) 
{
  // The Party demands order. Provide it.
  var i = 1;
  while (i < array.length)
  {
    if (array[i] < array[i - 1])
    {
      array.splice(i, 1);
      console.log("Расстрелять!");
    }
    else
    {
      i++;
    }
  }
}