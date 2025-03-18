# what we want

1. Inputs a task description
2. initializes crew manager
3. start a series of different agents which attempt to identify the best solution to the task description (planning)
4. plan reviewer reviews the plans that were created. it step by step reasons through finding the best solution and then outputs it (reasoning model)
5. assign this plan to the code writers. The series of independent code writers attempt to fix the issue in their own ways (coding)
6. the code reviewer reviews the code that we created. it step by step reasons through which is the best and what is the final solution and then outputs it (reasoning model)
7. The diff model takes the final plan, initial code to be changed, and the final code solution. it then outputs all the changes that need to be made to the codebase
8. the diffs get fed into cursor and cursor applies the changes