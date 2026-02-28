# All Search queries Used

1. How do weights comparison and assigning work in a decision making system that ranks given options after comparing them?

# References that influenced my approach

1. The Weighted Decision Matrix (YouTube video by Arata Academy English)

2. An introduction to the weighted decision matrix (Blog by Lucid)

3. Weighted Scoring Model: Step-by-Step Implementation Guide (Blog by Product School)

4. A Short Story about Multiple Criteria Decision Analysis (MCDA) (YouTube Video by HealthOutcomesStrats)

# All AI Prompts Used

1. Design and build a “Decision Companion System” that helps a user make better decisions.

The system should assist a user in evaluating options for a real-world decision of their choice.

Your system must work without relying entirely on an AI model. If AI is used, clearly justify its role and limitations.

Examples (you are NOT limited to these):

Choosing a laptop under a budget

Selecting the best candidate for a job role

Deciding where to travel within constraints

Picking an investment strategy

Choosing a tech stack for a startup

Core Expectations:
Your system must:

Accept multiple options

Accept criteria (which may have different weights or importance)

Process and evaluate options against criteria

Provide a ranked recommendation

Explain why a particular recommendation was made

Beyond this, the design is up to you.

You may choose:

CLI / Web App / API / Desktop tool

Any programming language

Any framework

Simple or advanced logic

You define the depth. We are more interested in your thinking than feature count.

Constraints
The system should not be a static hard coded comparison.

The user should be able to change inputs and get different outcomes.

Your logic should be explainable (not a black box).

Deliverables
Please submit a Git repository containing:

    1. Source Code
    Clean, readable, and structured

    Meaningful commit history

    2. README.md
    Include:

    Your understanding of the problem

    Assumptions made

    Why you structured the solution the way you did

    Design decisions and trade-offs

    Edge cases considered

    How to run the project

    What you would improve with more time

    3. Design Diagram
    Provide at least one:

    Architecture diagram

    Data flow diagram

    Component diagram

    Or decision logic diagram

     I want to build a system according to the above details. The problem is selecting an online course from multiple options. I want the system to use weighted decision matrix or multiple criteria decision analysis method. The user should be able to enter the criterias, their weights (then normalise the weights), available inputs, rating of each option against each criteria ( on a scale of 1-10 for some and raw values for criteria like cost) and the weights should be normalised and then the effective weights calculated. Rank the options from best to worst and provide an explanation. The language i prefer is python and input entering mode cli for now. 

2. I want the system to allow mixed criterion types like cost and user reviews. Also normalisation of each rating and weight internally.

3. Give me mermaid code for the data flow diagram of the system which shows user entering criteria and options and then they are normalized, weighted scores are calculated then ranked and finally explanation is generated.

4. Provide a sample README.md and BUILD_PROCESS.md which shows the evolution of thinking and building stage of the system with these points included: 1.How you started 2.How your thinking evolved 3.Alternative approaches considered 4.Refactoring decisions 5.Mistakes and corrections.

# What I accepted, rejected, or modified from AI outputs.

1. Modified the suggestion it gave by deciding to use mixed criterion types.

2. Modified the data flow diagram by changing the notations of symbols to standard type.

3. Modified the README.md and BUILD_PROCESS.md by adding points AI missed and by removing unnecessary details.