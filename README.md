# Bicluster results from Massive Associative K-biclustering

[Massive Associative K-biclustering (MAK)](https://www.osti.gov/biblio/1347092-massive-associative-biclustering-mak-v1) is a biclustering method to identify patterns in layers of two dimensional (2D) data.

MAK leverages a pseudo-random walk, a data-dependent null distribution, a combination of robust bicluster coherence criteria, and a high performance computing (HPC) strategy to divide the NP-hard problem into many smaller tasks.
Starting points are generated using hierarchical clustering and tree cutting, and each starting point is used to compute a MAK trajectory. A trajectory ends when no additional moves can improve the score. Trajectory endpoints are harvested, a score threshold is applied, and the results are pruned for a desired level of bicluster overlap.


In multiple algorithm evaluations, MAK outperformed other methods on simulated and real world datasets, particularly in terms of resulting biological enrichments, coverage of the input data with significant biclusters, and biologically meaningful cases of bicluster overlap. We will update here with a publication link.


