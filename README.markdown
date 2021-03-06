The setting
====

In the ocean, there are islands where islanders live. There is one islander on each island.

The problem
====

Let's say that that each of the islands are located on a Cartesian plane defined by a pair of signed numeric coordinates. Let's also assume that each islander has a unique name. For example, an island for islander "Bobo"  would be located at the coordinates 2,10.

You need to write a program in Python that takes a single argument on the command line. The argument is the file name that contains input data. Your program needs to write an output that contains 5 closest islanders for each islander in the list. Note that we will have a lot of islands in the game, in a matter of millions, so the program needs efficient. Also, your program needs to be stable.

The input file
====

The file has multiple lines. Each line has three values listed as the islander name plus coordinates X, and Y. Name for each islander is written in ASCII characters. There will be no empty lines.

Input
====

    Bobo 1 2
    Freddy 10 100
    Loner 111 18

Output
====

For each islander on a single line, write the names of the next 5 closest islander names, sorted by the closest to farthest.  For example, it could be like this:

    Ben Bobo, Freddy, Loner, Matt, Mary
    Mary Bobo, Freddy, Loner, Ben, Matt
