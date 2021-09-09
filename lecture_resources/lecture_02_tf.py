from rdflib import Graph
from timefuncs import TFUN

g = Graph().parse("lecture_02_tf.ttl")
print(f"The number of triples in the graph is {len(g)}")

for r in g.query(
        """
        PREFIX tfun: <https://w3id.org/timefuncs/>
        
        SELECT ?x ?y
        WHERE {
            ?x a ?c1 .
            ?y a ?c2 .
        
            FILTER tfun:isBefore(?x, ?y)
        }
        """
):
    print(f"{r[0]} is before {r[1]}")
