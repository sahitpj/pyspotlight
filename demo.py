import spotlight

l = spotlight.Config()

annotations = spotlight.annotate(l.spotlight_address,
                                'Germany India country bus',
                                confidence=0.4, support=20)

print(annotations)