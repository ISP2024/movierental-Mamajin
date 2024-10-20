## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.


## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.

## Questions

### 2.1 What refactoring signs (code smells) suggest this refactoring?

Ans. The key refactoring signs (code smells) that 
suggest moving the price_code attribute from the 
Movie class to the Rental class are Middle Man and Low Cohesion

### 2.2 What design principle suggests this refactoring? Why?

Ans. The design principle that suggests moving the price_code attribute 
to Rental is SRP. According to SRP, a class should have only one reason to 
change, meaning it should focus on a single responsibility.

For example from code:

- Movie class should be responsible for holding information relevant to a movie
such as title, year and genre. This makes the class focused and cohesive

- Rental class however should handled all the logic related to renting a movie, 
including determining the pricing strategy. By moving price code to Rental we 
ensure that Movie only manages it's own content while Rental handles the logic

