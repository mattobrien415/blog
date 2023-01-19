Title: Mike Tyson's Punchout! as a Neo4j graph
Date: 2016-03-16
Tags: visualization
Summary: a simple example of a graph database

![Mike Tyson's Punchout!!](http://underratedretro.com/press/wp-content/uploads/2014/08/Mike-Tysons-Punchout.jpg "Mike Tyson's Punchout!!")

This is a quick and fun little graph of the classic Nintendo game, Mike Tyson's Punch-Out!!.  

The information for the graph comes directly from the [Punchout Wiki](http://punchout.wikia.com/wiki/Punch-Out_Wiki). The graph is based off the NES console from 1987 as opposed to the earlier arcade games or the later release for the Wii. 

I took the liberty of having Little Mac win all his fights by knockout. But then he went up against Iron Mike...  

_Notice that the dataset is read in painlessly via Google Docs as outlined [here](http://blog.bruggen.com/2014/07/using-loadcsv-to-import-data-from.html)._


```
Query 1

LOAD CSV WITH HEADERS FROM
'https://docs.google.com/spreadsheets/u/0/d/1Jr5ABoLMrUPQ3Vm9GTOzVmNucfnWq1ELTxv2WxOYOx0/export?format=csv&id=1Jr5ABoLMrUPQ3Vm9GTOzVmNucfnWq1ELTxv2WxOYOx0&gid=0' AS line
MERGE (b1:boxer {
                    boxer_id: line.boxer_id,
                    name: line.name
                })
MERGE (b2:boxer {boxer_id: line.fought
                })
MERGE (f:fight  { fight_id: line.fight_id,
                  notes: line.notes,
                  outcome: line.outcome
                })
//CREATE (b1)-[:AGAINST]->(b2)
CREATE (b1)-[r:BOXER_STATUS {
                  total_fights: line.total_fights,
                  wins: line.wins,
                  wins_by_KO: line.wins_by_KO,
                  losses: line.losses,
                  weight: line.weight,
                  height: line.height,
                  nationality: line.nationality,
                  age: line.age,
                  rank: line.rank
                         } ]->(f);  

```

Here's what it looks like:

```
MATCH (n)
RETURN n
```
![mtpo](https://github.com/mobbSF/blog/blob/master/publicfolder/mtpo.png?raw=true)



Here's some simple queries to practice with:  


Query 1: What happened when Little Mac fought opponents ranked #1?  


```
MATCH (result) <-[r:BOXER_STATUS]- (boxer)
WHERE toInt(r.rank) = 1
RETURN result.outcome, result.notes
```


Query 2: Did Little Mac lose twice to anyone? Or win twice against anyone?
```
START n=node(*), m=node(*)
WHERE
  n.outcome=m.outcome AND
  ID(n) <ID(m)
RETURN n, m
```