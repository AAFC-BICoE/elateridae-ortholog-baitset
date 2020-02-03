# *Elateridae* Ortholog Target Enrichment Baits

The Bait-100-85_Pass_Filtering_Renamed.fas bait set contains 40190 100nt baits designed from 8 *Elateroidea* species targetting 2260 orthologs. 

### Design Methodology
* Gathered 4296 Orthologs from OrthoDB for Coleoptera (Present in 80% of Species, Single Copy in All Species)

```
wget https://www.orthodb.org/tab?query=&level=7041&species=7041&universal=0.8&singlecopy=1&limit=5000 > OrthoDB_Coleoptera_80_Percent.tab
```

*  Prepare file for Orthograph
```
awk 'BEGIN {FS="\t"; OFS="\t"} {print $1, $6, $5}' OrthoDB_Coleoptera_80_Percent.tab > OrthoDB_Coleoptera_cut.tsv
```
 
2) Retrieve Official Gene Sets for the all Coleoptera species [odb10_arthropoda_fasta.tar.gz](https://v100.orthodb.org/download/odb10_arthropoda_fasta.tar.gz)

    | OrthoDB Species Identifier | Species Name              |
    |----------------------------|---------------------------|
    | 110193_0                   | Nicrophorus vespilloides  |
    | 116153_0                   | Aethina tumida            |
    | 1629725_0                  | Oryctes borbonicus        |
    | 166361_0                   | Onthophagus taurus        |
    | 217634_0                   | Anoplophora glabripennis  |
    | 224129_0                   | Agrilus planipennis       |
    | 7070_0                     | Tribolium castaneum       |
    | 7539_0                     | Leptinotarsa decemlineata |
    | 77166_0                    | Dendroctonus ponderosae   |

4. Orthograph was prepared follwing the instructions outlined in the [Orthograph README](https://github.com/mptrsen/Orthograph) by adding the 9 OGS and the OrthoDB_Coleoptera_cut.tsv
5. Orthograph was run on the following Elateridae transcriptomes assembled using rnaSPAdes v 1.13 after adaptor trimming with BBDuk

* I189 Melanotus villosus
* I246 Drilus concolor 
* [SRR4413771](https://www.ncbi.nlm.nih.gov/sra/SRR4413771) Phrixothrix hirtus
* [SRR7300147](https://www.ncbi.nlm.nih.gov/sra/SRR7300147) Pyrearinus fragilis 
* [SRR7300148](https://www.ncbi.nlm.nih.gov/sra/SRR7300148) Pyrearinus fragilis
* [SRR7300149](https://www.ncbi.nlm.nih.gov/sra/SRR7300149) Conoderus
* [SRR6286833](https://www.ncbi.nlm.nih.gov/sra/SRR6286833) Melanotus cribricollis
* [SRR6345452](https://www.ncbi.nlm.nih.gov/sra/SRR6345452) Photinus pyralis

6. Orthograph results were merged using Orthograph-reporter. 
7. Amino acid orthologs were aligned using T_Coffee 11.0.8 additionally outputting score_ascii files
8.) Protein alignments were converted to nucleotide alignments using Tranalign from EMBOSS 6.6.0 resulting in 4264 nucleotide alignments
9.) elateridae_baits.py performed the following steps:
    * Scanned each score_ascii file with sliding window starting a length of 200 AA. 
    Each alignment position has a TSC score from 1-9 so a max score of 200 AA is 1800. The window with a sum above 95% of the max TCS score was considered a conserved block.
    * 2764 Corresponding conserved blocks were excised from the nucleotide transalignments by multiplying the start and stop indices of protein alignments by 3. 
    * Any sequences with at least 20% gapped bases were removed from conserved blocks
    * 2260 Conserved blocks were found containing a minimum of 5 of the 8 Elateroidea species 
    * Curated blocks were created by selecting randomly 3 Elateroidea specimens 
    * Curated blocks were appended into a multi-fasta Elateridae_Submission.fasta and submitted to Arbor Biosciences for MyBaits manufacturing

### Arbor BioSciences Bait Design
The following procedures were performed by Brian Brunelle, Arbor Biosciences

1) 6780 loci provided for bait design (Ns were replaced with Ts if they occurred consecutively for
1-10 bases)
2) Using RepeatMasker, soft-masked the input sequences for simple repeats and repeats found in
the Elateridae database; 0.1% masked (all simple repeats)
3) 1.15X Tiling (100 nt bait from every 85 nt) interval based on GC, ΔG,
4) Each bait candidate was BLASTed against the 25 provided genomes;
| Species                   | TaxID   | Common Name              | Accession       |
|---------------------------|---------|--------------------------|-----------------|
| Oryzaephilus surinamensis | 41112   | saw-toothed grain beetle | GCA_004796505.1 |
| Popillia japonica         | 7064    | Japanese beetle          | GCA_004785975.1 |
| Asbolus verrucosus        | 1661398 | beetles                  | GCA_004193795.1 |
| Protaetia brevitarsis     | 348688  | beetles                  | GCA_004143645.1 |
| Diabrotica virgifera      | 50389   | western corn rootworm    | GCF_003013835.1 |
| Harmonia axyridis         | 115357  | beetles                  | GCA_003865315.1 |
| Harmonia axyridis         | 115357  | beetles                  | GCA_003865295.1 |
| Harmonia axyridis         | 115357  | beetles                  | GCA_003865275.1 |
| Coccinella septempunctata | 41139   | seven-spotted ladybird   | GCA_003568925.1 |
| Harmonia axyridis         | 115357  | beetles                  | GCA_003402655.1 |
| Aleochara bilineata       | 135921  | beetles                  | GCA_003054995.1 |
| Sitophilus oryzae         | 7048    | rice weevil              | GCA_002938485.1 |
| Agrilus planipennis       | 224129  | emerald ash borer        | GCF_000699045.2 |
| Anoplophora glabripennis  | 217634  | Asian longhorned beetle  | GCF_000390285.2 |
| Leptinotarsa decemlineata | 7539    | Colorado potato beetle   | GCF_000500325.1 |
| Onthophagus taurus        | 166361  | beetles                  | GCF_000648695.1 |
| Pogonus chalceus          | 235516  | beetles                  | GCA_002278615.1 |
| Aethina tumida            | 116153  | small hive beetle        | GCF_001937115.1 |
| Tribolium castaneum       | 7070    | red flour beetle         | GCF_000002335.3 |
| Oryctes borbonicus        | 1629725 | beetles                  | GCA_001443705.1 |
| Dendroctonus ponderosae   | 77166   | mountain pine beetle     | GCF_000355655.1 |
| Nicrophorus vespilloides  | 110193  | beetles                  | GCF_001412225.1 |
| Priacma serrata           | 50550   | beetles                  | GCA_000281835.1 |
| Hypothenemus hampei       | 57062   | coffee berry borer       | GCA_001012855.1 |
| Dendroctonus ponderosae   | 77166   | mountain pine beetle     | GCA_000346045.2 |
     
    A hybridization melting temperature (Tm, defined as temperature at which 50% of molecules are hybridized) was estimated for each hit assuming standard myBaits® buffers and conditions.

5) For each bait candidate, one BLAST hit with the highest Tm is first discarded from the results
(allowing for 1 hit in the genome), and only the top 500 hits (by bit score) are considered. Based
on the distribution of remaining calculated Tm's, we filtered out non-specific baits using the
following criteria:
    * Stringent (only specific baits pass). Bait candidates pass if they satisfy one of these conditions:
        - No hits with Tm above 60°C
        - At most 2 hits 62.5 – 65°C
        - At most 10 hits 62.5 – 65°C and at least 1 failing flanking bait
        - At most 10 hits 62.5 – 65°C, 2 hits 65 – 67.5°C, and fewer than 2 passing flanking baits
        - At most 2 hits 62.5 – 65°C, 1 hit 65 – 67.5°C, 1 hit 70°C or above, and < 2 passing flanking baits
    * Moderate (some non-specific baits pass)
        - Additional candidates pass if they have at most 10 hits 62.5 – 65°C and 2 hits above 65°C, and fewer than 2 passing baits on each flank.
    * Relaxed (more non-specific baits pass)
        - Additional candidates pass if they have at most 10 hits 62.5 – 65°C and 4 hits above 65°C, and fewer than 2
passing baits on each flank.

6) Optimal bait design, keep only baits that passed “Stringent” BLAST filtering for all 25 genomes and were ≤25% Repeat
Masked

7) Final bait set, Bait-100-85_Pass_Filtering_Renamed.fas: 100 nt baits after recommended filtration = 40160 baits
•	target_sequences.masked.fas = the 6,780 total target sequences soft masked these for simple repeats (0.1% masked)
•	Bait-100-100.fas = Designed 100 nt baits every 100 nt; 40,471 baits
•	filter-files = folder of all BLAST analysis from all 25 genomes
•	Filtered_Baits.fasta = design after keeping only baits that were <=25% soft masked, matched a region of the genome that was <= 25% masked, and passed our Stringent analysis; 34,497 baits

### Phyluce Prediction of Bait Effectiveness
In order to provide a rough idea effectiveness, the bait set was compared against 23 Coleoptera assemblies available as of April 2019.
Bait set fasta headers were converted to Phyluce "UCE" format and processed via Phyluce, outlined in [Tutorial IV: Identifying UCE Loci and Designing Baits To Target Them: In-silico test of the bait design](https://phyluce.readthedocs.io/en/latest/tutorial-four.html#in-silico-test-of-the-bait-design)

Table 1. Target Hits Among NCBI Coleoptera Assemblies

### Built With

* [Python](https://www.python.org/doc/) - Programming language
* [Conda](https://conda.io/docs/index.html) - Package, dependency and environment management
* [Phyluce](https://phyluce.readthedocs.io/en/latest/index.html) - Target enrichment data analysis
* [BioPython](https://biopython.org/) - Tools for biological computation
* [Orthograph](https://github.com/mptrsen/Orthograph) - Orthology prediction
* [OrthoDB](https://www.orthodb.org/)- Hierarchical catalog of orthologs 
* [T_Coffee](http://www.tcoffee.org/Projects/tcoffee/) Multiple sequence alignment
* [Tranalign](http://emboss.sourceforge.net/apps/release/6.6/emboss/apps/tranalign.html) Nucleotide alignments from protein alignments

### Acknowledgements
BioMob greatly thanks the contributions from 1kite for the Melanotus villosus and Drilus concolor Transcriptome assemblies

### Contact
Jackson Eyres, Bioinformatics Programmer, Agriculture & Agri-Food Canada  
jackson.eyres@canada.ca

### Copyright
Agriculture & Agri-Food Canada, Government of Canada

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details