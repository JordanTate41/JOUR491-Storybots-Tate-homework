verbs = ['ate', 'ran', 'pooped', 'snorted', 'growled', 'mated', 'nursed', 'grunted', 'slept', 'snored']

nouns = ['penguins', 'elephants', 'lions', 'camels', 'bears', 'tigers', 'armadillos', 'monkeys', 'giraffes', 'zebras']

import random

for verb in verbs:
	print "when I went to the zoo, the", random.choice(nouns), random.choice(verbs), "while I passed their cage."
    