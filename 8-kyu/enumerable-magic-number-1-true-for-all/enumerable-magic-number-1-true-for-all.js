function all(arr, fun) 
{
    for (const el of arr)
    {
      if (!fun(el))
      {
        return false;
      }
    }
  return true;
}