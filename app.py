from Bio import SeqIO
import yaml, random, sys

## CONFIG ##
with file("config.yml", "r") as f:
    config = yaml.load(f.read())
try:
    dialect = config[sys.argv[1]]
except Exception as e:
    print e.message # hilariously, BioBroBot will speak this error message. Intended behavior.
    dialect = config['bro']

## Reads the first ten characters from a random genetic sequence
bio_data = [seq_record.seq.tostring() for seq_record in SeqIO.parse("bio/lady_slippers_orchid.fasta", "fasta")]
to_speak = list(bio_data[random.choice(range(len(bio_data)))])

for letter, word in dialect.iteritems():
    to_speak = [char if char.lower() != letter else word for char in to_speak]

to_speak = " ".join(to_speak[:10])
print to_speak