##### Examples:

###### Example 1
input:
   village =  [0, -3, 2, 1, -7, 5, 3, -1, 6]
     # index   0   1   2  3  4   5  6  7  8
     #                          ************
>>> max_fund(village)
   (13, 6, 9)      # Since mayor is not an engineer, you will need to convert the index offset
▸␣␣␣               ▸from zero to one.  (eg. start + 1, end + 1)
   fund: 13;
   starting at 6;  index 5 + 1
   ending at 9;    indext 8 + 1 (from mayor's perspective - the first potion should be ONE)

###### Example 2
input:
   One  = [0, 1, -1, -5, 0, 4, -3, -2]

>>> max_fund(one)
  (4, 6, 6))

###### Example 3
input:
   penniless = [0, 0, 0, 0, 1, -5, -2, -1, -3]
>>> max_fund(penniless)
  (1, 5, 5))

###### Example 4
input:
   extremes  = [-1, -2, -3, -4, -5]
>>> max_fund(extremes)
   'Mission Impossible. No one can contribute!'
  (0, 0, 0)