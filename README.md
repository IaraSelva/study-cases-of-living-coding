# CodeWars
Some challenges and descriptions about how to solve them

<h2>#Challenge1:</h2>
<ul>
  <li>Level: Beginner</li>
  <li>Topics: #FUNDAMENTALS #ARRAYSLISTS #DATASTRUCTURES #ARITHMETICMATHEMATICS #ALGORITHMS #NUMBERS</li>
</ul>

<b>Count of positives / sum of negatives</b><br>
https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/java<hr>

Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

If the input is an empty array or is null, return an empty array.<hr>

So, let's see. First of all we need to declare some array to store the results      
The rules are:
<dl>
  <dd>The first element must be the count of positive numbers given into input</dd> 
  <dd>The second element must be the sum of negative numbers given into input</dd>
</dl>

You can see how declare and manipulate arrays in Java on this article: https://www.geeksforgeeks.org/arrays-in-java/ <hr>

<ul>
  So, next steps :
    <li>Initialize a count variable for increment the quantity of positive numbers</li>
    <li>Initialize a variable for sum the quantity of negative numbers</li>
    <li>Make a loop to go through the input array</li>
      <p>At the same article above (about arrays) you can see how to manipulate them using <i>for</i> loop.</p>
    <li>Then, into the loop we can go through all the given elements and verify if its a positive or negative number.</li>
      <p>Here https://www.w3schools.com/java/java_conditions.asp you can read about conditions in Java and examples using if statments</p>
      <ul>
        <li>If it would be a positive number, we increment our previously declared count variable.</li>
        <li>If it would be a negative number, we sum into our previously declared sum variable.</li>
      </ul>
    <li>Finally, add count into the 0 position and sum into the 1 position in your previously initialized array at the begin</li>
    <li>At the end, return the array with count of positives and sum of negatives</li>

  
</ul>
