## Crawler

A crawl - is a sequential visit (processing) of graph vertices in a certain order. One of the two commonly used crawl methods is wide crawl, or BFS (breadth-first search). It is also sometimes called wave, similar to a propagating wave.

The essence of BFS is quite simple. A detour begins with a visit to a certain peak. Further, the algorithm visits the neighbors of this vertex. Behind them are the neighbors of the neighbors, and so on.

### Program launch
```
python3 crawler.py <start_link> <destination_link>
```

### Example
```
python3 crawler.py https://kk.wikipedia.org/wiki/Басты_бет https://kk.wikipedia.org/wiki/Жапония
```
### Output of program:
```
level 1
https://kk.wikipedia.org/wiki/Жапония 
```
