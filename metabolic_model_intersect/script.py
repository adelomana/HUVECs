### 1. read 308 DEGs
DEGs = []
data_file = '/home/adrian/projects/vigur/results/transcriptomics/deseq2_filtered/strict_union_experiment_three.tsv'
with open(data_file, 'r') as f:
    next(f)
    for line in f:

        v = line.split('\t')
        DEGs.append(v[0])
#print(DEGs)

### 2. read Sarah's list
MGs = []
data_file = '/home/adrian/projects/HUVECs/data/met_candidates/Interesting redox and heparan sulphate proteins.csv'
with open(data_file, 'r') as f:
    next(f)
    for line in f:
        v = line.split(',')
        MGs.append(v[1])
#print(MGs)
#MGs.append('ENSG00000267436')


### 3. intersection
intersection = list(set(DEGs) & set(MGs))
print(intersection)
