## 420. Strong Password Checker

link: https://leetcode.com/problems/strong-password-checker/description/

### Problem:

A password is considered strong if the below conditions are all met:

- It has at least 6 characters and at most 20 characters.
- It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
- It does not contain three repeating characters in a row (i.e., "Baaabb0" is weak, but "Baaba0" is strong).
- Given a string password, return the minimum number of steps required to make password strong. if password is already strong, return 0.

In one step, you can:

- Insert one character to password,
- Delete one character from password, or
- Replace one character of password with another character.

### Constraints:

- 1 <= password.length <= 50
- password consists of letters, digits, dot '.' or exclamation mark '!'.

### Discussing Solution:

We can split this problem in 2 parts.

First part is if our password is shorter than 21.

We count the number of letters, digits and signs in it, and then we count
how many of those counts are 0.

We also count lengths of all subsequences that consist of the same characters
divided by 3.

Our solution for this part is going to be maximum of those 2 counts.

If n is smaller than 6 we don't need to count the second count, our
result is max of 6-n and first count.

Now, that was an easy part. The hard part is if our password is longer
than 20.

It's too much for me to write detailed explanation here but the idea
is to find all subsequences that contain one character and are longer than 2.
And then we need to reduce them in an optimal way.


### Complexities:

- Time: O(n) 
- Space: O(n)