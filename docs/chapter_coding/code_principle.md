# Coding Principles

!!! abstract "Learning Objectives"

TBD

## Pivot your coding mindset

Here are the principles that you should pivot your coding mindset towards:

1. Don't repeat yourself: Learning how to automate and/or simplify repetitive tasks in your workflow because the time savings will be enormous.
2. Improve your coding style: Writing code that is more readable and maintainable before worrying about efficiency.
3. Write code for readability: Writing code that is self-documenting and readable by others.
   
## Advices for coders

- [Understand code before relying on it.](#understand-code-before-relying-on-it)
- [Don't repeat yourself](#dont-repeat-yourself)
- [Think and document before you code](#think-and-document-before-you-code)
- [Premature optimization is the root of all evil.](#premature-optimization-is-the-root-of-all-evil)


### **Understand code before relying on it.**

It's OK to __copy/paste code__ from Google or Stack Overflow. It's OK to ask AI to generate code for you. I myself am doing these all the time. However, make sure you __understand how it works__.  

Here are some ways to understand code:
* Run line by line and see what each does. 
* Change the code and see if it behaves as expected.
* Ask AI to explain the code.


If the code is implementing some statistical method, make sure you understand that method well enough to at least be able to accurately describe it in the methods section of a manuscript.

* E.g., do you really know what `confint` does to a `glm` in `R`? 

Here are some common pitfalls:
- **Beware of the context.** What works in one context may not work in another. Reading other's solution to problems is how we learn a language. Just like a spoken language -- seeing how native speakers construct phrases is important! But we need to understand those phrases before we incorporate them into our dialect, lest we be misunderstood (or worse).
- **AI hallucination.** AI is not always correct. In fact, it hallucinates a lot. So always try to verify the code.



### Don't repeat yourself

Don't repeat yourself (DRY) is a fundamental concept in programming. 


- **DRY in Workflow:** Learning how to automate and/or simplify repetitive tasks in your workflow because the time savings will be enormous. We will cover some tools to do this in this course, but you first need to be aware of the existence of these tools. 
  - Best practice: Optimize your workflow from time to time but not too often.
  - Shell Script: Process files in batches, customize your commands in the system.
  - GNU Make: Create a `Makefile` to customize the project-specific build process.
  - Transferable Workflows: Find the best practices making your workflow transferable across different platforms and machines.
  - Keyboard shortcuts: Use your keyboard more and your mouse less. This can be through keyboard shortcuts, changing interfaces, &c.
- **DRY in Programming:** What if you need to change 1 thing? Needs to be changed in multiple places. Risk getting a wrong answer because we forgot to change one small thing.
  - Functions: If you write the same code more than once, it should be a function.  For example, variables `score1=1`, `score2=2`, `score3=3` → `score=list(1,2,3)`. 
  - Write code __a bit more general__ than your data or specific task.
    * Don't assume particular dimensions.
    * Don't forget about missing values (even if *your* data have none).
    * But **don't try to handle every case.** Try to anticipate what you might be asked for, but don't prepare for every possibility.
  - Use __function arguments__ to handle different cases. 
    * Don't assume particular file names.
    * Don't assume particular tuning parameters. 
    * Don't assume particular regression formulas.

### Think and document before you code

 You should always document what you want the code to do before you start writing it. With the help of AI tools, this documentation can not only help your thinking process but also will help AI tools to understand your goals. You could keep updating this documentation as you develop the code.

Here is an example of before your develop a package. 
```r
# Averaging over drtmle option:
#   Instantiate empty lists 
#   Note: length = 1 if n_SL = 1 or "drtmle" not in avg_over):
#     nuisance_drtmle 
#     nuisance_aiptw_c
#     ic_drtmle 
#     QnMod, gnMod, QrnMod, grnMod
#     drtmle -- eventually avg over to get final point estimates
#     aiptw_c -- eventually avg over 
#     tmle -- eventually avg over
#     aiptw -- eventually avg over
#     gcomp -- eventually avg over
#     validRows -- should this be added to the output?
#   Wrap everything into a big for loop and add indexes to the
#   objects above
#   Add code below for loop to do aggregation

# For introducing cross-validated standard errors: 
#   if se_cv = "full", but cvFolds = 1
#   need to modify make_validRows recognize this situation?
#   Or could modify estimateQ/g directly and have the functions
#   call themselves if se_cv = "full" and cvFolds == 1
#   or probably better to add an if statement that would call the 
#   estimateQ again outside. Yes, that's probably the way to go
```
This is copied from a local branch of `drtmle` R package from [David Benkeser](https://github.com/benkeser).

Before you start coding, you can first "code" in natural language what you want to do.
You can write in the document on:
- The goal of the package
- How to decompose the goal into different functions
- The inputs and outputs of the functions you need.
- The potential approaches to implement the functions.

We call it "chain of thought" now in the context of using language models. We will talk about how to use AI tools to generate this meta-code but you need to be aware that you should think yourself. You should never be the slave of AI.





### **Premature optimization is the root of all evil.**



Get the code working and readable first, optimize and generalize later. 

Getting code **correct** AND **readable** is __most important__.
* Make your code more efficient later.
* After a paper is submitted for review?

Remember: you don't get bonus points for code that "looks impressive".

  In Donald Knuth's paper "Structured Programming With GoTo Statements", he wrote: "Programmers waste enormous amounts of time thinking about, or worrying about, the speed of noncritical parts of their programs, and these attempts at efficiency actually have a strong negative impact when debugging and maintenance are considered. We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil. Yet we should not pass up our opportunities in that critical 3%."




This course will teach you a lot about how to make your code more efficient. However, do not get too obsessed with efficiency. 

Let me share a common misconception - the idea that using vectorized operations is always better than `for` loops. When I first started coding, I would tie myself in knots trying to avoid loops at all costs, believing this would make me look like a more sophisticated programmer.
The reality is that premature optimization like this often leads to overly complex, hard-to-maintain code. I've learned that it's better to write straightforward code first, even if that means using loops, and then optimize later if profiling shows it's actually needed. Finding the right balance between readability and performance is a skill that develops with experience.