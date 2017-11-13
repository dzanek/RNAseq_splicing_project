''' This is a prototype of pipeline - olneliner set'''
import matplotlib.pylab as pl

pl.rcParams['figure.figsize'] = 16,9
import os

pl.style.use('ggplot')
pl.style.use('seaborn-paper')
def translate(seq):
    codontable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    seq = seq.upper()
    seq = seq[:len(seq) - len(seq)%3]
    prot_seq = [codontable[seq[i:i+3]] for i in range(len(seq))[::3]]
    return ''.join(prot_seq)



inputs = os.listdir('E-MTAB-4052/')
inputs = ['./E-MTAB-4052/{}'.format(i) for i in inputs if '.sam' in i]
allbeds = {}
for i in inputs:
    print i
    print 'samtools view {} -b > {}'.format(i, i.replace('.sam','.bam'))
    os.system('samtools view {} -b > {}'.format(i, i.replace('.sam','.bam')))
    print 'bedtools bamtobed -i {} -split  > {}'.format(i.replace('.sam','.bam'), i.replace('.sam','.bed'))
    os.system('bedtools bamtobed -i {} -split  > {}'.format(i.replace('.sam','.bam'), i.replace('.sam','.bed')))
    print i
    bed = open(i.replace('.sam','.bed')).readlines()

    allbeds[i] = bed
    print 'added {}'.format(i)
    bed = [i.strip().split('\t') for i in bed]
    print len(bed)
    splits = bed

    stops = set([int(i[2]) for i in splits])




    splitdict = {}
    for i in splits:
        try:
            splitdict[i[3]].append([i[1],i[2]])
        except:
            splitdict[i[3]] = [[i[1],i[2]]]

    ranges = {}

    pos_intron = {i:0 for i in range(max(stops)+1000)}
    for i in splitdict.iteritems():
        if len(i[1]) != 2:
            continue
        if int(i[1][1][0]) - int(i[1][0][1]) > 500:
            pass #continue
        for k in range(int(i[1][0][1]),int(i[1][1][0])):
	    try:
		ranges[(i[1][0][1], i[1][1][0])] += 1
	    except:
		ranges[(i[1][0][1], i[1][1][0])] = 1
            pos_intron[k] += 1

    genomic = open('rarr2_mouse.fa').readlines()[1:]
    genomic = ''.join([i.strip() for i in genomic])

    intron_starts = set([i[0] for i in ranges.iterkeys()])
    intron_variants = []
    for i in intron_starts:
        for k in ranges.iteritems():
            if i == k[0][0]:
                print k
                intron_variants.append(k[0])
        print '\n'
    print intron_variants
    pl.plot([i[0] for i in pos_intron.iteritems()],[i[1] for i in pos_intron.iteritems()], label=i)
    pl.ylim(0,400)
    pl.xlim(3400,4000)
    pl.legend()
    pl.savefig('introns_4052.png')
pl.cla()

print [i for i in allbeds.iterkeys()]
for i in allbeds.iteritems():
    bed = i[1]
    e_id = i[0]
    bed = [i.strip().split('\t') for i in bed]
    splits = bed
    stops = set([int(i[2]) for i in splits])

    ex_pos= {i:0 for i in range(max(stops)+1000)}
    for i in bed:
        if int(i[2]) - int(i[1]) < 3:
            continue
        for k in range(int(i[1]), int(i[2])):
            ex_pos[k] += 1

    pl.plot([i[0] for i in ex_pos.iteritems()],[i[1] for i in ex_pos.iteritems()],'-',label=e_id)
    #pl.xlim(3400,4000)
pl.yscale('log')
pl.legend()
pl.xlabel('Position in gene [bp]')
pl.ylabel('Number of mapped nucleotides')
pl.title('Mapping of {} to gene'.format(e_id))
pl.savefig('Mapped_{}.png'.format('4052'))
pl.cla()
