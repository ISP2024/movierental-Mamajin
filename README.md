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

### 5.2 Rationale

The price_code_for_movie method is implemented as a class method within the 
Movie class. This decision is justified based on several design principles:

1. High Cohesion

The Movie class is responsible for representing the properties and behaviors 
of movies, including attributes like title, year, and genres. Since the pricing rules depend on these attributes, placing the method within the Movie class ensures that all related functionality is grouped together. This makes the class more cohesive and easier to understand.

2. Single Responsibility Principle

The Movie class maintains a single responsibility: to encapsulate movie 
details and behaviors. Determining the price code based on the movie's attributes falls within this responsibility. This design keeps the class focused on its role without introducing unnecessary dependencies on other classes.