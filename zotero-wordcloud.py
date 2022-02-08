#!/usr/bin/env python
"""zotero-wordcloud

This is a small utility to download full-text data from a Zotero collection
and create a wordcloud, using `nltk` and `wordcloud` python libraries.

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
"""

import argparse

from wordcloud import WordCloud
from PIL import Image
import numpy as np

from pyzotero import zotero, zotero_errors
from cachier import cachier
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

@cachier()
def get_fulltext(library, library_type, key, collection):
    """Retrieve fulltext content for items in a Zotero collection."""
    text = []
    zot = zotero.Zotero(library, library_type, key)
    c = zot.everything(zot.collection_items(collection)) #, format='keys'))
    keys = [i['data']['key'] for i in c if i['data']['itemType']=='attachment']
    for k in keys:
        try:
            r = zot.fulltext_item(k)
            text.append(r['content'])
        except zotero_errors.ResourceNotFound: # 404 / no fulltext available
            continue
    return ' '.join(text)

def process_fulltext(text):
    """Filter the fulltext to exclude stop words ("the", "and", etc.)
    and require a minimum word length of 4 letters."""

    tokens = word_tokenize(text)
    stop_words = stopwords.words('english')
    return ' '.join([word for word in tokens if not word in stop_words and
        len(word) > 3])

def run(args):
    if args.purge:
        get_fulltext.clear_cache()
    text = get_fulltext(args.library, args.library_type, args.key,
            args.collection)
    text = process_fulltext(text)
    mask = np.array(Image.open(args.mask))
    wc = WordCloud( max_words=10000, mask=mask,
                    contour_width=4, contour_color='white', background_color='white')
    wc.generate(text)
    image = wc.to_file(args.output)

    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Generate a wordcloud from a Zotero collection.')
    parser.add_argument('--collection',  help='Zotero collection ID',
        required=True)
    parser.add_argument('--library',  help='Zotero library/user ID',
        required=True)
    parser.add_argument('--library-type',  help='library type', default='group',
        choices=['user', 'group'])
    parser.add_argument('--key',  help='Zotero API key', required=True)
    parser.add_argument('--mask', required=True, help='Image mask file')
    parser.add_argument('--output', help='filename for output', required=True)
    parser.add_argument('--purge', help='Purge fulltext cache',
        action='store_true')
    args = parser.parse_args()

    run(args)
