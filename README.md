# ffuf-mass v1.0

## Usage:
You can use this two way
### 1.Default Way:
`cd ffuf-mass`

`python ffuf-mass-v1.py`

Give Your Site List.List Urls Should Be Contain Urls Like This Format https://site.com/
Then Give Wordlist Full Path
like: /your/wordlist.txt
You Will See It Runs Successfully..
Output Will Save Randomely Like For First Website Output Will Be 1.html

### 2. Permanant Way:

For This You Have To Create A File Which Is `command.txt`

This `command.txt` Should Contains Your Own Command

Like: `ffuf -u %s -w /yourwordlist/path/word.txt -of html -o %s.html`

Just Don't Change The `-u %s` And `-of html -o %s.html` [By The Way You Can Change The Html Format to Any Which Support In FFUF]

For Ex: `ffuf -u %s -w /yourwordlist/path/word.txt -of json -o %s.json`

You Can Add Also Your Own Command/Attribute Which You Use In FFUF But Don't Change The `-u %s` And `-of html -o %s.html` Format

First `%s` Takes The Lines From The Site List File And Second One Is Save The Output Randomely

# Happy Hacking!
