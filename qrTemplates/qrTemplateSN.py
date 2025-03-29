#/usr/bin/

import subprocess

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("device", help="Nomad or Manta")
parser.add_argument("url", help="Target url")
parser.add_argument("-o", "--output", help="Output file name (pdf)")
parser.add_argument("-c", "--caption", help="Caption")

args = parser.parse_args()
print("Device:", args.device)
print("url:", args.url)
print("Output:", args.output)
print("Caption:", args.caption)

if args.device.lower() == 'nomad':
    w = 1404
    h = 1872
else:
    w = 1920
    h = 2560

# Position
x = 1100
y = 75
# text position
tx = x+32
ty = 340

# temporary files
qrFile = "qrFile.png"
tmpTemplate = "tmpTemplate.svg"
baseFileName = args.output.split(".")[0] 
outSVG = baseFileName + ".svg"
outPDF = baseFileName + ".pdf"

svg = f'''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
   width="{w}"
   height="{h}"
   version="1.1"
   id="svg65"
   xmlns:xlink="http://www.w3.org/1999/xlink"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:svg="http://www.w3.org/2000/svg">
  <defs
     id="defs69" />
   <a href="{args.url}">
      <image
         width="264"
         height="264"
         preserveAspectRatio="none"
         xlink:href="{qrFile}"
         id="image205"
         x="{x}"
         y="{y}" />
         <text
            xml:space="preserve"
            style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:32px;line-height:1.25;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Normal';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-variant-east-asian:normal;fill:#000000;fill-opacity:1;stroke:none"
            x="{tx}"
            y="{ty}"
            id="text3469"><tspan
            id="tspan3467"
            x="{tx}"
            y="{ty}"
            style="text-align:start;text-anchor:start">{args.caption}</tspan>
        </text>
   </a>
</svg>
'''

subprocess.run(f'qrencode -s 6 -o {qrFile} "{args.url}"', shell=True)

with open(outSVG, "w") as f:
    f.write(svg)

subprocess.run(f'inkscape --export-type="pdf" {outSVG}', shell=True)

