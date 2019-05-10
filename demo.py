import spotlight

annotations = spotlight.annotate('http://model.dbpedia-spotlight.org/en/annotate',
                                'Germany India country bus',
                                confidence=0.4, support=20)

print(annotations)