# plex-tools
Various scripts for Plex

## refresh_metadata.py
Run the script without any command line arguments to list sections of your Plex server.

Example output:
```
Listing Plex Library Sections:
  Section 'Home Movies' found with Key '7'
  Section 'Movies' found with Key '5'
  Section 'TV Shows' found with Key '2'
```

Then run the script with the section key numbers to go through the sections and refresh items older than 5 days.

Example command line:
` refresh_metadata.py 2 `
This will refresh the TV Shows section. When an item is added less than 5 days ago, metadata is refreshed.

With the -d parameter, you can tweak how recent the item is added to the library, in order for the metadata to be refreshed:
Example command line:
` refresh_metadata.py -d 10 2 `

This will refresh the TV shows section. When an item is added less than 10 days ago, metadata is refreshed.
