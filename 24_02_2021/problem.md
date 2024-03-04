**Weekly Challenge - #1**

Hmm, your factory's sorting machine seems to have been misprogrammed, and has shot out packages based on a set of rules (the input file).
You've been tasked with untangling the mess, and you need to figure out how many items came out of the factory!
The machine appears to have put containers inside of containers, with the product inside those containers!
You've been given 6 `light-greenish-blue` containers, and need to find how many items in `cloudy-blue` containers were put inside the light-greenish-blue containers

Each rule will have colour name, and one of the following
```
- The amount of items in that container.
- A list of container colours that go inside the container, and how many of them.
```

For the second option, the colours will look something like `4.red`, where `4` is how many red containers go in,
and `red` is the colour. Multiple of these can be chained together to look something like `4.red|2.blue`, which would be
`4` containers of the colour `red`, and `2` containers of the colour `blue`.

Let's imagine we have this set of rules:
```
green:5
teal:1.green
blue:2.teal|1.green
red:1.blue|2.teal|1.green
```
What's the total amount of `green` here, if we start with 2 `red`.
Well, each red has 1 blue, 2 teal, and 1 green. which means we have:
```
red
- 1 blue
    - 2 teal
        - 1 green
        - 1 green
    - 1 green
- 2 teal
    - 1 green
    - 1 green
- 1 green
```
Adding those up, we have 6 total green, so each red is equal to 6 * 5, because each green is equal to 5.
So the answer here is 60, because we start with 2 reds.

TL;DR: find how many items inside `cloudy-blue` containers you would end up with, with 6 `light-greenish-blue` containers.

Input: https://mystb.in/SittingRapidsLegacy