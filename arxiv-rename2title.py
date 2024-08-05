#!/usr/bin/env python
from glob import glob

import pymupdf as pf
import argparse
import textwrap
import sys
import re
import os


def to_rich_text_list(blocks: dict):
    rtexts = []

    for block in blocks:
        if 'lines' in block:
            for lines in block['lines']:
                for text in lines['spans']:
                    rtexts.append(text)

    return rtexts


def is_pdf(file: str):
    with open(file, mode='rb') as f:
        header = f.read(4)
        return header == '%PDF'.encode('ascii')


def pdf2title(file: str):
    doc = pf.open(filename=file)
    page0 = doc.get_page_text(pno=0, option='dict')
    page_width = page0['width']
    page_height = page0['height']
    blocks = page0['blocks']

    rtexts = to_rich_text_list(blocks)

    # 
    # Sort by text size, I assume that the title is the text 
    # with maximux font size at the top of the page
    # 
    rtexts.sort(key=lambda x:x['size'], reverse=True)

    for i, rtext in enumerate(rtexts):
        #
        # Assume that title is at the top quarter of the page
        #
        if rtext['bbox'][1] > page_width / 4:
            continue

        #
        # Assume that title text should longer that 5 character
        #
        if len(rtext['text']) < 5:
            continue

        size = rtext['size']
        break

    titles = []

    #
    # get a continuously rich text with same font size because of newline
    #
    while rtext['size'] == size:
        titles.append(rtext['text'])
        i += 1
        rtext = rtexts[i]

    title = "-".join(titles)

    #
    # Remove special characters
    #
    chars = re.findall(r'(:| )', title)

    for char in chars:
        title = title.replace(char, '-', 1)

    doc.close()
    return title


def pdf_rename(file, dry_run=False):
    if not is_pdf(file):
        print(f"Warning: '{file}' is not pdf, skip", file=sys.stderr)
        return

    title = pdf2title(file) + '.pdf'
    target = os.path.join(os.path.dirname(file), title)

    if os.path.isfile(target):
        print(f"Warning: '{target}' exist, skip", file=sys.stderr)
        return

    if dry_run:
        print(f'Rename {file} ==> {target}')
    else:
        os.rename(file, target)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rename arxiv pdf file to its title name", epilog=textwrap.dedent(f'''
        Example: 
                                                                                                                    
            {sys.argv[0]} <path/to/pdf>             rename target pdf
            {sys.argv[0]} <path/to/directory>       rename all pdf in target directory
            {sys.argv[0]} .                         rename all pdf in current directory
            {sys.argv[0]} -n <path/to/directory>    do nothing, just show what would happen

        Feel free to submit bug and suggestion to <https://github.com/suzakuwcx/arxiv-rename2title>
    '''), formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('path', metavar='path', type=str, nargs='+',
                        help='File name or directory to operate, support multiple target')
    parser.add_argument('-n', '--dry-run', action='store_true',
                        help="Don't actually do anything, just show what would be done")

    args = parser.parse_args()

    uris = args.path

    for uri in uris:
        if os.path.isfile(uri):
            pdf_rename(uri, args.dry_run)
        elif os.path.isdir(uri):
            for file in glob(os.path.join(uri, "*.pdf")):
                pdf_rename(file, args.dry_run)

        else:
            print(f"Unknown file: '{uri}', skip", file=sys.stderr)
