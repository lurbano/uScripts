# My Scripts

## qrTemplateSN
* Creates pdf templates for SuperNotes with QR Code with link to url. 
* Requires command line programs:
    * qrencode
    * inkscape
* Parameters:
    * $1 (required): device: "Nomad" or "Manta"
    * $2 (required): url: string
    * -c --caption (optional): string
    * -o --output (required): output filename (pdf)
* Usage e.g.:
    > python3 qrTemplateSN.py Nomad https://soriki.com/uSciCalc -c uSci -o uSciCalc.pdf
