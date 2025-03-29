
title = "Daffodils"
author = "William Wordsworth"
stYear = "1770"
endYear = "1850"

stanzaSize = 0

head = f'''	\poemtitle{{ {title} }}
    \\begin{{verse}}
    \\begin{{altverse}}'''

poem = '''I wandered lonely as a cloud
That floats on high o'er vales and hills,
When all at once I saw a crowd,
A host, of golden daffodils;
Beside the lake, beneath the trees,
Fluttering and dancing in the breeze.

Continuous as the stars that shine
And twinkle on the milky way,
They stretched in never-ending line
Along the margin of a bay:
Ten thousand saw I at a glance,
Tossing their heads in sprightly dance.

The waves beside them danced; but they
Out-did the sparkling waves in glee:
A poet could not but be gay,
In such a jocund company:
I gazed—and gazed—but little thought
What wealth the show to me had brought:

For oft, when on my couch I lie
In vacant or in pensive mood,
They flash upon that inward eye
Which is the bliss of solitude;
And then my heart with pleasure fills,
And dances with the daffodils.
'''


tail = f'''	\\end{{altverse}}
\\end{{verse}}
\\attrib{{ {author} '''

if len(endYear) > 0:
    tail += f'''({stYear} \\textendash {endYear})}}'''
else:
    tail += f'''({stYear})}}'''

#print(head, "\n\n", poem, "\n\n", tail)

print(head, "\n")
p = ""
lines = poem.split("\n")

for (i, line) in enumerate(lines):
    line = line.replace("&", "\&")
    if len(line) > 0:
        p += line + '\\\\'

    #print (i,len(lines), line)
    if i < len(lines)-1:
        if len(lines[i+1]) == 0:
            p += "!"
    elif i == len(lines)-1:
        p += "!"
    p += "\n"
    #print (i, line)

    i += 1
    if stanzaSize > 0 and i%stanzaSize == 0:
        p += '!\n'



print(p)

print( tail)
