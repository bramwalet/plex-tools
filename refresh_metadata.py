#!/usr/bin/python

from plexapi.server import PlexServer
from plexapi.library import MovieSection,ShowSection
from datetime import datetime
from plexapi.myplex import MyPlexUser
import argparse

def main(args):
    plex = PlexServer()   # Defaults to localhost:32400

    if not options.sections:
        print('Listing Plex Library Sections:')
        for section in plex.library.sections():
            print('  Section \'%s\' found with Key \'%s\'' % (section.title,section.key))

    for section in plex.library.sections():
        if int(section.key) in options.sections:
            print('Found section %s to process' % section.title)
            recentItems = section.recentlyAdded()
            for item in recentItems:
                if not item.is_watched:
                    print('Unwatched: %s, added at %s' % (item.title, item.addedAt))
                    timedelta = datetime.now() - item.addedAt
                    if timedelta.days < int(options.days):
                        print('+ Item should be refreshed')
                        item.refresh()

class Options(object):
    pass

if __name__ == "__main__":
    options = Options()
    parser = argparse.ArgumentParser(description='Plex Metadata refresher.')
    parser.add_argument('-days', default='5',
                   help='number of days to keep refreshing')
    parser.add_argument('sections', metavar='s', type=int, nargs='*',
                   help='Plex section keys to process')
    args = parser.parse_args(namespace=Options)
    main(options)
