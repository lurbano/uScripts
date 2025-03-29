
title = "Tyger"
author = "William Blake"
stYear = "1794"
endYear = ""

stanzaSize = 0



poem = '''Tyger Tyger, burning bright,
In the forests of the night;
What immortal hand or eye,
Could frame thy fearful symmetry?

In what distant deeps or skies.
Burnt the fire of thine eyes?
On what wings dare he aspire?
What the hand, dare seize the fire?

And what shoulder, & what art,
Could twist the sinews of thy heart?
And when thy heart began to beat.
What dread hand? & what dread feet?

What the hammer? what the chain,
In what furnace was thy brain?
What the anvil? what dread grasp.
Dare its deadly terrors clasp?

When the stars threw down their spears
And water'd heaven with their tears:
Did he smile his work to see?
Did he who made the Lamb make thee?

Tyger Tyger burning bright,
In the forests of the night:
What immortal hand or eye,
Dare frame thy fearful symmetry?
'''


head = f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head>
  <title>{title}</title>

	<link
          rel="stylesheet"
          href="../Styles/poemStyle.css"
          type="text/css" />
</head>
<body>
    <h1>{title}</h1>
    <div class="poem">
'''


if len(endYear) > 0:
    tail = f'''{author} ({stYear} — {endYear})}}'''
else:
    tail = f'''{author} ({stYear})}}'''
tail = f'        <p class="credit">{tail}</p>\n'
tail += f'''\n      </div>
    </div>
</body>
</html>'''



#print(head, "\n\n", poem, "\n\n", tail)


p = '      <div class="stanza">\n'
lines = poem.split("\n")

for (i, line) in enumerate(lines):
    line = line.replace("&", "&amp;")
    line = line.strip()
    if len(line) > 0:
        if i%2 == 0:
            pLine = "poem1"
        else:
            pLine = "poem2"
        p += f'        <p class="{pLine}">{line}</p>'
    else:
        p += '      </div>\n      <div class="stanza">'

    #if i < len(lines)-1:
        #if len(lines[i+1]) == 0:
            #p += "!"
    #elif i == len(lines)-1:
        #p += "!"
    p += "\n"
    #print (i, line)

    i += 1
    if stanzaSize > 0 and i%stanzaSize == 0:
        p += '      </div>\n    <div class="stanza">'


print(head, "\n")
print(p)
print( tail)

fname = title.replace(" ", "_") + ".xhtml"
with open(fname, "w") as f:
    f.write(head)
    f.write(p)
    f.write(tail)
