# NeighborFlow
Music player that implements a customizable vector databse to naturally flow between songs on a graph

## How to use
The pygame should be installed for this program to function. Once installed, users can configure settings in the *settings.cfg* file. Once set up users can download songs and add them to their tracklist file.

## Adding a track
In order to add a song to the graph, it must be moved into a reachable location and metadata must be logged in the tracklist file. Tracklist file can be configured but is tracklist.txt by default. It is recomended that users put all of their tracks in a common folder for orginizational purposes. All audio files that are supported by pygame are supported by this program (wav, ogg, and mp3). Metadata that needs to be added is the name of the track, the path from this directory to that file, and the integer values for each dimension. An example of metadata for a 2 dimension graph is seen below:

boing \
music/boing.mp3 \
5 \
5

## Settings.cfg lines
### Line 1: dimensionality
Determines the number of dimensions for each music track. Ex: if this is set to 2, each song can be placed on an xy graph like (5, 8) and (-40, 0).

### Line 2: tracklist file path
Path to the tracklist file. This file contains information on song name, filepath, and location in the vector database.

### Line 3: minimum neighbors
Number of neighbors each song creates. This is the minimum amount of songs that can be played after the current song finishes. Since edges are undirected, nodes can have more than this amount of edges.

### Line 4: repeat queue size
The maximum size the repeat queue can be. Ex: if this line is 2, the next song will never be the previously 2 played songs. It is best practice to have this value be lower than the minimum neighbor value.

### Remaining lines: dimension Labels
The remaining lines determine the label each dimension has in the vector. This has zero effect on how the graph/database opperate and is purely for display/tracking purposes.

An example of what is found in a settings.cfg file is seen below

2\
tracklist.txt\
1\
0\
value 1\
value 2