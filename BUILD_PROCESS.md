# Build Process Documentation

This document outlines how the Decision Companion System was developed, including thought process, design evolution, refactoring decisions, and lessons learned.

---

## 1. How I Started

I began by breaking down the core problem:

> Given multiple options and multiple criteria with different importance levels, how do we compute a fair and explainable ranking?

I researched the problem on internet and came upon the classic solution - Weighted Decision Matrix System or also known as Multiple Criteria Decision Analysis. After finding the solution, the next step was to decide the specificity of the problem. I considered building a general decision making system that can deal with any type of real world problem by entering the criterias and options but later decided to focus on a specific problem so that i can focus on building the solution more clearly. I decided on the problem of deciding between various available courses online because it was a relatable problem.

The initial focus was on identifying:
- Required inputs
- Output expectations
- The scoring formula
- Data flow between components

I first implemented a minimal working version:
- Accept criteria
- Accept weights
- Accept options
- Accept ratings
- Multiply weights × ratings
- Rank by total score

This ensured I had a functional baseline before improving structure.

---

## 2. How My Thinking Evolved

Initially, I considered asking users to enter weights as percentages that sum to 100.

However, I realized:
- Users may not always enter weights correctly
- Enforcing exact sum constraints increases friction
- Validation logic would become unnecessarily strict

This led to a shift in approach:

Instead of forcing correct weight totals, I allowed any positive numeric weights and normalized them internally.

This improved:
- Usability
- Robustness
- Error tolerance

I also initially thought of using a fixed scale of 1-10 for ratings but then realised that it was not practical expectation.So I changed it to a dynamic system where the user can input both raw values or on a scale of 1-10 which is then normalised.

---

## 3. Alternative Approaches Considered

### Approach 1: Percentage-Based Weight Input
Pros:
- Conceptually clear
- Direct interpretation

Cons:
- User errors likely
- Frustrating validation logic
- Hard constraint enforcement

Decision:
Rejected in favor of internal normalization.

---

### Approach 2: Static ratings value

Pros:
- More simpler
- Direct representation

Cons:
- Not flexible
- Not user-friendly

Decision:
Used a dynamic system where both raw values and values on a 1-10 scale can be given.

---

### Approach 3: Non-Linear Scoring Models

Considered:
- Weighted geometric mean
- Multi-objective optimization
- Pairwise comparison models

Rejected because:
- Overkill for scope
- Reduced explainability
- Increased complexity without requirement justification

Chose linear weighted sum model for:
- Simplicity
- Transparency
- Deterministic behavior

---

## 4. Refactoring Decisions

### Refactoring 1: Separation of Modules

The first version was written in a single file.

This made:
- Debugging harder
- Testing more difficult
- Logic tightly coupled

Refactored into:
- Criteria handling module
- Weight normalization module
- Scoring module
- Ranking module
- Explanation module

Result:
- Better separation of concerns
- Easier testing
- More scalable structure

---

### Refactoring 2: Input Validation Isolation

Originally, validation logic was mixed inside calculation functions.

Refactored to:
- Validate inputs before processing
- Prevent invalid states from entering core logic

This reduced:
- Hidden bugs
- Defensive coding inside computation layer

---

### Refactoring 3: Explanation Layer Addition

The initial system only output ranked scores.

I later added an explanation layer that:
- Identifies highest contributing criteria
- Explains why top option ranked highest

This improved interpretability and trust in the output.

---

## 5. Mistakes and Corrections

### Mistake 1: Assuming Weights Would Be Reasonable

I initially assumed users would enter balanced weights.

Testing revealed cases like:
- 100000 for one criterion
- 2 for another

This exposed potential bias.

Correction:
Implemented automatic weight normalization.

---

### Mistake 2: Using a fixed scale

At one point, I allowed only fixed scale ratings.

This caused:
- Reduced flexibilty
- Unfair expectation from user

Correction:
Introduced dynamic rating system.

---

### Mistake 3: Tight Coupling of Input and Logic

Originally, input gathering was embedded in logic functions.

Correction:
Separated input layer from processing layer.

---

## 6. What Changed During Development and Why

### Change 1: Weight Handling Strategy
Changed from:
- Fixed percentage sum requirement

To:
- Flexible weight input with internal normalization

Reason:
Improved robustness and user experience.

---

### Change 2: Architecture Structure
Changed from:
- Single-file procedural script

To:
- Modular layered design

Reason:
Scalability, maintainability, and readability.

---

### Change 3: Added Explanation Engine
Originally:
- Only ranked output

Later:
- Added reasoning generation

Reason:
Improved transparency and decision explainability.

---

## Final Reflection

The development process evolved from a simple scoring script to a modular, explainable decision-support engine.

The biggest improvements came from:
- Challenging initial assumptions
- Handling edge cases
- Refactoring for clarity
- Improving input robustness
- Prioritizing explainability

The final result is a structured, scalable implementation suitable for extension into larger systems.