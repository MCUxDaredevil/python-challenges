**Weekly Challenge - #3**

You are tasked with identifying the different mineral formations in a cave.
The 4 formations you will need to identify are:

```diff
+ Stalactites
+ Stalagmite
+ Pillars
+ Both (Stalactite and Stalagmite, but not a Pillar)
```

Stalactites are formations which grow from the top down,
Stalagmites are formations which grow from the bottom up,
Pillars are both joined together,
and both are when a Stalactite and Stalagmite are separated by air (in the same column).

Your input data will consist of a 2-Dimensional List (a list containing lists), containing 4 lists, each representing a row, with each inner list (row) containing numbers of either 0 or 1.
Each column will be either a Stalactite, Stalagmite, Pillar or Both[Stalactite & Stalagmite] and can never be neither of those, (meaning there will always be a 1 on either or both sides of the column, and never not forming a valid formation).
There will always only be 4 rows, but assume an infinite amount of columns.

1 represents formed mineral, and 0 represents air.

Your output should be a list containing the formation represented by the following letters:
C = Stalactites
G = Stalagmite
P = Pillar
B = Both (Stalactites and Stalagmite, but not a pillar)

For example, given the following input:

```py
[[0, 1, 1, 0, 1],
 [1, 1, 1, 0, 1],
 [1, 1, 0, 0, 0],
 [1, 1, 0, 1, 1]]
```

Your answer would be:

```py
['G', 'P', 'C', 'G', 'B']
```

Good Luck! And Happy Coding :)
