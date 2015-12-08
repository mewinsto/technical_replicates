#Technical Replicates
##This is a basic python script to compare genotype accuracy of pyRAD for a pair of technical replicates. The 'technical_replicates' directory has numerous examples.

##INSTRUCTIONS FOR OPERATING TECHNICAL REPLICATE SCRIPTS
###First, use the 'grep' command to isolate the two samples you want to compare from the larger unlinked_snps file, both from the same one. Give this two-lined new file the .unlinkedsnps extension

###Next, apply rep_compare.py, the first argument being this new file, and then the second argument being the output of snp_location, and finally the third argument being the output of matching 
