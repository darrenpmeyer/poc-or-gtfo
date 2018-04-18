Mirror of the Journal of PoC||GTFO
==================================

This repository contains a copy of all PDFs and `spoiler*.html` files related to the [PoC||GTFO journal](https://www.alchemistowl.org/pocorgtfo/) as listed on https://www.alchemistowl.org/pocorgtfo/

It also contains a script, `update.py`, to make it easy for you to download and verify your own copies from that site. This script relies on Python 3.5 or newer, and a recent version of GNU wget.


## Script basics

    python3 update.py

This script removes any `*.tmp` file and `index.html`, then uses GNU wget in your PATH to download any PDF or HTML files linked from https://www.alchemistowl.org/pocorgtfo/ that are newer than what's already in the directory. It also obtains the published SHA256 hash digests from that site for comparison.

If it finds new PDF files (presumed to be issues of the journal), it downloads them and compares their SHA256 hash to the one advertised by the above site, reporting the results.

Output looks something like:

```
index.html          100%[===================>]   7.28K  42.8KB/s    in 0.2s
robots.txt.tmp      100%[===================>]     139  --.-KB/s    in 0s
pocorgtfo17.pdf     100%[===================>]  56.96M  7.26MB/s    in 11s
1 new issue, checking digest:
40b8985521e671b59c305d2f5512f31b95f1e8c59b9c05ad2ca6413a99d59c97  pocorgtfo17.pdf: OK
```

The digest lines are printed to STDOUT for your parsing pleasure. Look for `FAILED` to find digest mismatches and `!NOT FOUND` to find downloaded PDFs not listed in the digest table at https://www.alchemistowl.org/pocorgtfo/

## LICENSE

### The Journal PDFs are made available under the following grant of license:

> Permission to use all or part of this work for personal, classroom, or whatever other use is NOT
granted unless you make a copy and pass it to a neighbor without fee, excepting libations offered by the aforementioned
neighbor in order to facilitate neighborly hacking, and that said copy bears this notice and the full citation on the first
page. Because if burning a book is a sin—which it surely is!—then copying of a book is your sacred duty. For uses in
outer space where a neighbor to share with cannot be readily found, seek blessing from the Pastor and kindly provide
your orbital ephemerides and radio band so that updates could be beamed to you via the Southern Appalachian
Space Agency (SASA).

### The `update.py` script is made available under the [WTFPL]:

```
        DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
                    Version 2, December 2004 

 Copyright (C) 2004 Sam Hocevar <sam@hocevar.net> 

 Everyone is permitted to copy and distribute verbatim or modified 
 copies of this license document, and changing it is allowed as long 
 as the name is changed. 

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION 

  0. You just DO WHAT THE FUCK YOU WANT TO.
```

However, the authors and contributors also disclaim any and all warranties, because this is a fun hobby project and and so there are no express or implied warranties nor any warranty of fitness for purpose.

Credit to the original author of this code (darrenpmeyer) would be nice, but not required. Buying him a drink would be awesome also.