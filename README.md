# The Bridge and Torch Problem
A simple solution for "The Bridge and Torch" logic puzzle using Python (mathematical approach) and C++ (brute forcing).

# About the problem.
*"Four people come to a river in the night. There is a narrow bridge, and it can only hold two people at a time. They have one torch and, because it's night, the torch has to be used when crossing the bridge. When two people cross the bridge together, they must move at the slower person's pace. One person has to return with the torch."* [- Source](https://en.wikipedia.org/wiki/Bridge_and_torch_problem)

The crossing time for each individual **may vary**, but overall we are looking for the optimal crossing time for a determined set of people.

# About the Python program
This approach utilizes the following mathematical implementation to determine the optimal crossing time, as well as the combination of *"crossings"* or *"steps"* to follow in order to achieve the final time:

$When: A<B<C<D:$
<p align="center"> $min(2A + B + C + D, A + 3B + D)$ </p>

To keep it brief, ths equation represents the two (canonically) best ***"crossing strategies"***. Since there are several ways to send and bring back the lantern, the possible best routes are compared, and the one with the shortest time is chosen, thus avoiding checking all possible combinations and outcomes, since most, if not all of them, will yield higher times.

**TL;DR:** This program looks at all the known best strategies and sticks with the most efficient one.
