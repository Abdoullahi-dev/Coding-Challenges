# Coding Challenges

Small programs written as practice, from the CC site.

Done:
  - CCWC, a small word/line/character/byte counter. It was a good refresher on how to use argparse, and I learned how to take input from stdin. You can pipe the output of other commands as input for ccwc.
  - Usage example: ```cat your_text.txt | py ccwc.py -m -c -l -w```
	
		An odd quirk (forgive the redundancy) is that the "cat" command works fine, but "dir" and "ls"
		count extra lines. Instead of returning 1 line for "ls", it counts three. And "dir" returns one
		extra line, perhaps the empty line after the command's output?? In that case, "ls" still counts
		an extra line.
