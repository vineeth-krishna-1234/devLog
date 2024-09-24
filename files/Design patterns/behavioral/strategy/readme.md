# Strategy Pattern

```
Definition : Strategy is a behavioral design pattern that lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable.
```


## where to use ?
-  Use the Strategy pattern when you want to use different variants of an algorithm within an object and be able to switch from one algorithm to another during runtime.
- Use the Strategy when you have a lot of similar classes that only differ in the way they execute some behavior.
- Use the pattern to isolate the business logic of a class from the implementation details of algorithms that may not be as important in the context of that logic
- Use the pattern when your class has a massive conditional statement that switches between different variants of the same algorithm.


## Eg
- A payment gateway that supports multiple payment methods (e.g., credit card, PayPal, bank transfer
- Games: We want player to either walk or run when he moves, but maybe in the future, he should also be able to swim, fly, teleport, burrow underground, etc
- Sorting: We want to sort these numbers, but we don't know if we are gonna use BrickSort, BubbleSort or some other sorting


[reference](https://refactoring.guru/design-patterns/strategy)
