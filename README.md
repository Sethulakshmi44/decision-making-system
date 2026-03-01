# Decision Companion System

---

## 1. Understanding of the Problem

The problem involves building a structured decision-support system that allows users to evaluate multiple options against multiple criteria with varying importance levels.

Users should be able to:
- Define custom criteria
- Assign weights to each criterion
- Provide multiple options
- Rate each option against each criterion
- Receive a ranked result based on weighted scoring
- Understand why a particular option ranked highest

The core challenge is ensuring:
- Fair weight handling
- Consistent scoring logic
- Clear ranking output
- Explainability of results
- Protection against biased or invalid inputs

---

## 2. Assumptions Made

- Users define all criteria (no predefined criteria).
- Weights are positive numeric values.
- Weights do not need to sum to 100 (system normalizes internally).
- Ratings can be both on a scale of 1–10 or raw values(cost).
- Higher rating indicates better performance for criteria like benefit and lower rating indicates better performance for criteria like cost.
- All options are rated against all criteria.
- No external persistence is required (in-memory processing).

---

## 3. Why I Structured the Solution This Way

I decided to select the problem of deciding between various online courses one can take when in confusion.This problem was decided because it was relevant and relatable for me as a student.

The system is divided into independent modules to ensure:

- Separation of concerns
- Maintainability
- Scalability
- Easier testing
- Clear data flow

Logical flow:

1. Criteria Input
2. Weight Validation & Normalization
3. Option & Rating Input
4. Score Computation
5. Ranking
6. Explanation Generation

Each step is isolated so the system can later be:
- Converted into an API
- Integrated into a web application
- Extended with a GUI
- Wrapped inside a larger decision-support platform

This modular structure also makes debugging and testing simpler.

---

## 4. Design Decisions and Trade-offs

### Decision 1: Normalize Weights Internally
Instead of forcing users to enter percentage values, the system:
- Accepts any positive numbers
- Normalizes them automatically

Trade-off:
- Slightly more internal processing
- Much better usability and error prevention

---

### Decision 2: Dynamic Rating Scale
Using a dynamic rating scale provides flexibility by allowing both raw numerical values (e.g., cost) and subjective ratings.

Trade-off:
- More flexibility for mixed quantitative inputs
- Lesser clarity and uniformity

---

### Decision 3: Deterministic Weighted Scoring
Used the standard formula:

    total_score = Σ (normalized_weight × rating)

Trade-off:
- Linear weighting assumes additive contribution
- Does not model nonlinear preference interactions

However, it keeps the system simple, transparent, and explainable.

---

### Decision 4: Explanation Generation

The system analyzes weight contribution to explain:
- Why the top option ranked highest
- Which criteria influenced the outcome most

This improves trust and interpretability.

---

## 5. Edge Cases Considered

1. Input Validation Case
- Non-numeric input for number of criteria or courses
- Non-numeric weight or rating values
- Negative weight values
- Zero criteria entered
- Zero courses entered
- Extremely large weight values (e.g., 100000 vs 2)
- Garbage or unexpected user inputs

2. Mathematical Safety Cases
- Weights not summing to 100 (handled via internal normalization)
- Division-by-zero during normalization
- All options having identical values for a criterion
- Equal final scores (tie detection using tolerance threshold)

3. Logical Scenario Cases
- Single-criterion scenario
- Single-option scenario
- All options scoring equally
- Options filtered out entirely due to hard constraints
- Weights becoming proportionally equal after normalization

---

## 6. How to Run the Project

1. Clone the repository:

    git clone <repository-url>

2. Navigate to the project folder:

    cd decision-making-system

3. Run the program:

    python main.py

## Sample Input

Welcome to Course Decision Companion

Enter number of criteria: 3

Criterion 1:
Name: Cost
Weight: 5
Type: cost

Criterion 2:
Name: Rating
Weight: 4
Type: benefit

Criterion 3:
Name: Duration
Weight: 2
Type: cost

Enter number of courses: 2

Course 1:
Name: Data Science Bootcamp
Cost: 5000
Rating: 9
Duration: 12

Course 2:
Name: AI Foundations
Cost: 4000
Rating: 8
Duration: 10

Do you want to add hard constraints? no

---

## Sample output

=== Final Ranking ===
1. Data Science Bootcamp - Score: 0.8421
2. AI Foundations - Score: 0.7984

=== Explanation ===
Top recommendation: Data Science Bootcamp
Reasons:
- High rating impact
- Competitive cost
- Balanced duration


## 7. What I Would Improve With More Time

- Add unit tests for all modules
- Add input validation layer with structured error messages
- Implement a REST API wrapper
- Add persistent storage (JSON/Database)
- Add visualization of score breakdown
- Implement sensitivity analysis
- Add CI/CD pipeline
- Improve documentation coverage
- Add performance benchmarking for large option sets

---

## Conclusion

This implementation provides a structured, modular, and explainable weighted decision matrix system.

The focus was on correctness, clarity, scalability, and safe handling of user inputs, making it suitable for integration into larger systems.