Sarthak has a set S
 of N
 distinct prime numbers. He grew very fond of that set, and now he only likes a positive integer X
 if all of its prime factors belong to S
. Given the set and a positive integer M
, can you find out how many integers he likes which are not more than M
?

Note: Sarthak always like the number 1
.

Input Format
The first line of each input contains T
 - the number of test cases. The test cases then follow.
The first line of each test case contains two space-separated integers N
 and M
 - the size of S
 and the limit defined in the statement.
The second line of each test case contains N
 space-separated integers S1,S2,…,SN
 - the elements of S
.
Output Format
For each test case, output on a single line the number of positive integers Sarthak likes that is not more than M
.

Constraints
1≤T≤2
1≤N≤20
1≤M≤1016
2≤Si<1000
S
 has N
 distinct prime numbers
Sample Input 1 
 1
2 10
3 5
Sample Output 1 
 4
Explanation
Test case 1
: Sarthak likes the numbers 1
, 3
, 5
 and 9
.
