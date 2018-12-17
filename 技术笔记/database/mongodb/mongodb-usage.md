## Operators
#### Query:db.collection.find()
操作符：
- Comparison：$gt,$lt等
- Logical: $and, $not, $nor, $or
- Element: $exists, $type
- Evaluation: $expr,$jsonSchema,$mod,$regex,$text,$where
- Array: $all, $elemMatch,$size
- Projection: $,$elemMatch,$meta,$slice
db.foo.find( { $where: function() {
   return (hex_md5(this.name) == "9b53e667f30cd329dca1ec9e6a83e994")
} } );
\#$:类似limit的作用
db.foo.find(
   { "grades.mean": { $gt: 70 } },
   { "grades.$": 1 }
)
#### Update:db.collection.update()
操作符:
- Field Update: $currentDate, $inc, $min, $max, $mul, $rename, $set, $setOnInsert, $unset
db.products.update(
   { sku: "abc123" },
   { $inc: { quantity: -2, "metrics.orders": 1 } }
)
db.products.update(
   { sku: "unknown" },
   { $unset: { quantity: "", instock: "" } }
)
- Array Update:
- Bitwise Update
#### db.collection.findAndModify()

#### db.collection.aggregate()

## Database Commands
所有的命令标准格式为db.runCommand(xxx)/db.adminCommand(xxx), db.collection.xxx只是包括shell或者类似pymongo等动态语言的helper方法
db.runCommand( { addShard: "xxx"} ) 等同 sh.addShard() 等同于
db.runCommand( { dropIndexes: "collection", index: "age_1" } 等同 db.collection.dropIndex("age_1");
#### Aggregation Commands
    aggregate, count, distinct, group, mapReduce
#### Geospatial Commands    
geoNear, geoSearch
#### Query and Write Operation Commands
delete	Deletes one or more documents.
eval	Deprecated. Runs a JavaScript function on the database server.
find	Selects documents in a collection or a view.
findAndModify	Returns and modifies a single document.
getLastError	Returns the success status of the last operation.
getMore	Returns batches of documents currently pointed to by the cursor.
getPrevError	Returns status document containing all errors since the last resetError command.
insert	Inserts one or more documents.
parallelCollectionScan	Lets applications use multiple parallel cursors when reading documents from a collection.
resetError	Resets the last error status.
update  Updates one or more documents.
#### Replication Commands¶
db.runCommand( { isMaster: 1 } )
#### Sharding Commands¶
db.runCommand( { addShard: "repl0/mongodb3.example.net:27327"} )
#### Administration Commands
db.collection.dropIndex("age_1");
#### Diagnostic Commands¶
db.collection.explain()
#### Sheel Method
所有sh开头的命令
sh.addShard() 等同于： db.runCommand( { addShard: "xxx"} )