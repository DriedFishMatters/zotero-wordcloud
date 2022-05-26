# zotero-wordcloud

This is a small utility to download full-text data from a Zotero collection
and create a wordcloud, using `nltk` and `wordcloud` python libraries.

You will need to supply a Zotero API key and user/library ID, as well as the ID of a collection to work with. You can find the group and collection ID when navigating a collection in the web library, by looking at the URL in the browser location bar. For example:

https://www.zotero.org/groups/2183860/dried_fish_matters/collections/27MV6NK5

In the above URL, the group ID is `2183860` while the collection ID is `27MV6NK5`.

You will also need to supply an image file as a mask; this will provide an outline to shape the wordcloud. The file `fish_mask.png` is included as an example.

## Installation

```
    pip install -r requirements.txt
    python -m nltk.downloader popular
```

## Usage

```
    zotero-wordcloud.py [-h] --collection COLLECTION --library LIBRARY
                           [--library-type {user,group}] --key KEY --mask MASK
                           --output OUTPUT [--purge]

    optional arguments:
          -h, --help            show this help message and exit
          --collection COLLECTION
                                Zotero collection ID
          --library LIBRARY     Zotero library/user ID
          --library-type {user,group}
                                Zotero library type
          --key KEY             Zotero API key
          --mask MASK           Image mask file
          --output OUTPUT       Filename for output
          --purge               Purge fulltext cache
```

## Copying

Copyright 2022, Eric Thrift

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

## Credits

This script was originally written for the
[Dried Fish Matters](https://driedfishmatters.org) project, supported
by the [Social Sciences and Humanities Research Council of
Canada](http://sshrc-crsh.gc.ca).
