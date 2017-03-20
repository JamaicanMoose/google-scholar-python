** A more full featured googlescholar scraper is available at https://github.com/ckreibich/scholar.py nice work by Christain & fairly well maintained


Requirements
============
- Python 3.0+
- urllib3
- Beautiful Soup
- re

Usage
=====
import gscholarapi.main as gscholar

gscholar('phrase')

NOTICE
======
- Google Scholar limits automated scraping and has no public API (though you probably know this) so more often than not if making any volume of requests with this you WILL be shut out.

