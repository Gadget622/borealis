# Borealis
This will be a note-taking app that extends the philosophy behind Obsidian to hypergraphs and utilizes AI to create a highly robust framework for constructing my second brain.

What I have thus far is quite simple, but it's been quite insightful thus far.

I'm utilizing [pygame](https://github.com/pygame/pygame) to get started on this project. My current goal to use this app to open text files that appear in virtual windows, and add basic functionality to the windows such as the ability to close them and change their size. The next step will be to edit the contents of the text files within the application itself. 

The aspects of hypergraphs that I hope to incorporate are yet to come, but here's a brief description of what I'm exploring:
- An edge contains a set of vertices, and can have any defined internal structure.
- An internal structure is a way to provide more information as to how vertices in an edge connect with one another. This is useful when the relationship between vertices changes depending on the context.
- Multigraphs in this context occur when any edges contain the same set of vertices. Loops are simply an edge containing only a single vertex.