function countLonelyLetters(text) 
{
  const lower = text.toLowerCase();
  let numLonelyLetters = 0;
​
  for (const letter of lower) 
  {
    if (!/^[a-z]$/.test(letter)) continue; // skip non-letters
​
    const isUnique = lower.indexOf(letter) === lower.lastIndexOf(letter);
    const prevChar = String.fromCharCode(letter.charCodeAt(0) - 1);
    const nextChar = String.fromCharCode(letter.charCodeAt(0) + 1);
​
    const prevAbsent = letter === 'a' || !lower.includes(prevChar);
    const nextAbsent = letter === 'z' || !lower.includes(nextChar);
​
    if (isUnique && prevAbsent && nextAbsent) 
    {
      numLonelyLetters++;
    }
  }
​
  return numLonelyLetters;
}