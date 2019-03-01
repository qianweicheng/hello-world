# Map
Map(I)
^
|
SortedMap(I)
^
|--------------------|
NavigableMap    AbstractMap
|                    |  |  
----------------------  |----------------------
         |                    |                |
      TreeMap               HashMap         IdentityHashMap
                              |
                            LinkedHashMap


# Set
HashSet 内部聚合一个HashMap
TreeSet
# List
Iterable<-Collection
            |
    ---------------------------------
    |                 |             |
 List(I)           Queue(I)       AbstractCollection(C)
                      |             |
                   Deqeue(I)      AbstractList
                      |             |
                      |           AbstractSequentialList
                      |             |
                      ---------------
                             |
                          LikedList