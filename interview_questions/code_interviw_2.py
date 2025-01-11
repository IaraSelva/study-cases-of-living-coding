'''
A groupped string is AAABBCCC
All the equal strings appears side by side
Thats not a groupped string: AABBACC. Because there's an 'A' apart

Given a 'k' number, that represents the amount of strings into a container,
return how much groupped strings are if the groupped string are sliced inyto the containers

For example, k = 3
The containers must have 3 strings each

So, that would be something like that:

AAA BBC CC

In this case, the return is 2 because there is 2 strings groupped: A and B.
All 'A' and all 'B' are at the same container
But C was tear apart
'''