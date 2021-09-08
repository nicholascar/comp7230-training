from rdflib import Graph

g = Graph().parse("lecture_02_person.ttl")
print(f"The number of triples in the graph is {len(g)}")

for r in g.query(
    """
    PREFIX ex: <http://example.com/>
    
    SELECT *
    WHERE {
        ?p a ex:Person ;
            ex:name "Nick" ;
        .
    }
    """
):
    print(f"The ID of the node of type ex:Person with ex:name \"Nick\" is {r[0]}")
