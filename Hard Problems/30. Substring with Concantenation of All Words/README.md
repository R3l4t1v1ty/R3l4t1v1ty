## 30. Substring with Concatenation of All Words

link: https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/

### Problem:

You are given a string s and an array of strings words. All 
the strings of words are of the same length.

A concatenated substring in s is a substring that contains all 
the strings of any permutation of words concatenated.

- For example, if words = ["ab","cd","ef"], then "abcdef", 
"abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all 
concatenated strings. "acdbef" is not a concatenated substring 
because it is not the concatenation of any permutation of words.

Return the starting indices of all the concatenated substrings 
in s. You can return the answer in any order.

### Constraints:

- 1 <= s.length <= 104
- 1 <= words.length <= 5000
- 1 <= words[i].length <= 30
- ***s*** and ***words[i]*** consist of lowercase English letters.

### Discussing Solution:

First we make a hashmap (dictionary) of word frequencies in
***words***. 

Now we have to search for ***len(words)*** consecutive chunks 
of ***len(words[i])*** characters where each chunk is one unique 
word from dictionary we made earlier. If we find such substring
we can add index where it begins to our solution, we pop oldest
chunk, reduce counter by one and continue our search.

When we finish we have to put that algoritm into offset loop 
that will deal with situations where there are stray characters
here and there.

Example:

word: "abarfoofoobarthefoobarman"

words: ["bar","foo","the"]

First step:

>dictionary = {"bar":1,"foo":1,"the":1}

Second step:

>offset = 0

>is "aba" in dictionary? -> False

>is "rfo" in dictionary> -> False

...

>is "rma" in dictionary? -> False

Third step:

>offset = 1

>is "bar" in dictionary? -> True

>is "foo" in dictionary? -> True

>is "foo" in dictionary? -> True

We found 3 words but there is 2 "foo" and no "the"
so we have to remove "bar" from our current substring
and continue our search

>is "bar" in dicrionary? -> True

Same problem as before, 2 "foo" and no "the", but this
time we remove "foo"

> is "the" in dicrionary? -> True

Now we have a substring that is made of all 3 words!
We add its begining index (7), remove "foo" and continue
our search

In case that we find substring that isn't contained in 
***words*** we reset our counter to 0 and remove all current
substrings.

Fourth Step:

> offset = 2

We don't find anything with this offset.

And that's it. No more offsets because ***len(word[i]) == 3***.

### Complexities:

- Time: O(n*k)
- Space: O(m*k)
- n - length of ***s***
- k - length of ***word[i]***
- m - length of ***words***