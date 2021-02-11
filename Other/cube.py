"""
Question:
You have 15 six-sided blocks. 
These are cubes with a letter (or a blank space) on each face.
Each block can have a different set of letters. 
For instance, one block may have A E I O U _ on its faces; 
another block may have A B C D E E.

Write a function that takes as input a 15 character message 
and the 15 blocks and returns a new ordering of the blocks 
that can spell out the message.

                           0                  1               2
Input - blocks = [['A', 'B', 'C', ''], ['X', 'Y', 'Z'], ['P', 'R', 'S']], message = 'SYB'
Output - (new ordering of block) = [2, 1, 0]

                          0                 1               2
Input - blocks = [['A', 'B', 'C'], ['C', 'Y', 'Z'], ['P', 'R', 'S']], message = 'CAR' 
Output - (new ordering of block) = [1, 0, 2]
"""