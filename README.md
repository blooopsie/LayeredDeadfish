Layered Deadfish is an esolang created by me.

Commands and operation precedence
Command	Precedence	Definition
i	1	Increment the accumulator
d	2	Decrement the accumulator.
s	3	Square the accumulator.
o	4	Output the accumulator value.
h	5	Halt.
Example
acc = 0
iidisiddso
^^ ^ ^
acc += 4
  d s ddso
  ^   ^^
acc -= 3
    s   so
    ^   ^
acc **= 2
acc **= 2
         o
         ^
print(acc)
Value: 1
