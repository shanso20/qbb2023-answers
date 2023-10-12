#!/usr/bin/env python

import sys

#from model_peaks import load_bedgraph, bin_array
import numpy
import scipy.stats
import matplotlib.pyplot as plt


def main():
    # Load file names and fragment width
    forward_sample_fname, reverse_sample_fname, forward_control_fname, reverse_control_fname, out_wig_fname, out_bed_fname = sys.argv[1:]
    fragment_width = 198

    # Define what genomic region we want to analyze
    target = "chr2R"
    chromstart = 10000000
    chromend =  12000000
    chromlen = chromend - chromstart

    # Load the sample bedgraph data, reusing the function we already wrote
    forward = load_bedgraph(forward_sample_fname, target, chromstart, chromend)
    reverse = load_bedgraph(reverse_sample_fname, target, chromstart, chromend)

    # Combine tag densities, shifting by our previously found fragment width
    combined_array = numpy.zeros_like(forward)
    combined_array[99:] += forward[:-99]
    combined_array[:-99] += reverse[99:]

    # Load the control bedgraph data, reusing the function we already wrote
    forward = load_bedgraph(forward_control_fname, target, chromstart, chromend)
    reverse = load_bedgraph(reverse_control_fname, target, chromstart, chromend)
    
    # Combine tag densities
    combined_control = forward + reverse
    
    # Adjust the control to have the same coverage as our sample
    n = numpy.sum(combined_array)/numpy.sum(combined_control)
    combined_control = n * combined_control

    # Create a background mean using our previous binning function and a 1K window
    # Make sure to adjust to be the mean expected per base
    oneK_mean = bin_array(combined_control, 1000)/1000

    # Find the mean tags/bp and make each background position the higher of the
    # the binned score and global background score
    global_mean = numpy.mean(combined_control)
    final_mean = numpy.maximum(oneK_mean, global_mean)

    # Score the sample using a binsize that is twice our fragment size
    # We can reuse the binning function we already wrote
    sample_score = bin_array(combined_array, 396)

    # Find the p-value for each position (you can pass a whole array of values
    # and and array of means). Use scipy.stats.poisson for the distribution.
    # Remeber that we're looking for the probability of seeing a value this large
    # or larger
    # Also, don't forget that your background is per base, while your sample is
    # per 2 * width bases. You'll need to adjust your background
    p_val = 1 - scipy.stats.poisson.cdf(sample_score, final_mean * 396)
    print(numpy.mean(p_val))

    # Transform the p-values into -log10
    # You will also need to set a minimum pvalue so you doen't get a divide by
    # zero error. I suggest using 1e-250
    p_val = numpy.maximum(p_val, 1e-250)
    p_val = numpy.log10(p_val) * -1

    # Write p-values to a wiggle file
    # The file should start with the line
    # "fixedStep chrom=CHROM start=CHROMSTART step=1 span=1" where CHROM and
    # CHROMSTART are filled in from your target genomic region. Then you have
    # one value per line (in this case, representing a value for each basepair).
    # Note that wiggle files start coordinates at 1, not zero, so add 1 to your
    # chromstart. Also, the file should end in the suffix ".wig"
    write_wiggle(p_val, target, chromstart, out_wig_fname)

    # Write bed file with non-overlapping peaks defined by high-scoring regions
    write_bed(p_val, target, chromstart, chromend, 396, out_bed_fname)

    #___________________________________________________________________________________________________________________________

def load_bedgraph(fname, target, chromstart, chromend):
    # Create array to hold tag counts
    coverage = numpy.zeros(chromend - chromstart, int)

    #Read the file in line by line
    for line in open(fname):
        # Break the line into individual fields
        chrom, start, end, score = line.rstrip().split('\t')
        #print(chrom)
        # Check if the data fall in our target region
        if chrom != target:
            continue
        start = int(start)
        end = int(end)
        if start < chromstart or end >= chromend:
            continue
        # Add tags to our array
        coverage[start-chromstart:end-chromend] = int(score)
        #print(coverage)
        #print(chromstart)
        #print(score)
    return coverage

def bin_array(data, binsize):
    # Create array to hold scores
    binned = numpy.zeros(data.shape[0], data.dtype)
    #print(data.shape)

    # For each position in the window, add to the score array
    for i in range(binsize):
        binned[i:data.shape[0] - binsize + i] += data[binsize//2:-binsize//2]
    return binned

def write_wiggle(pvalues, chrom, chromstart, fname):
    output = open(fname, 'w')
    print(f"fixedStep chrom={chrom} start={chromstart + 1} step=1 span=1",
          file=output)
    for i in pvalues:
        print(i, file=output)
    output.close()

def write_bed(scores, chrom, chromstart, chromend, width, fname):
    chromlen = chromend - chromstart
    output = open(fname, 'w')
    while numpy.amax(scores) >= 10:
        pos = numpy.argmax(scores)
        start = pos
        while start > 0 and scores[start - 1] >= 10:
            start -= 1
        end = pos
        while end < chromlen - 1 and scores[end + 1] >= 10:
            end += 1
        end = min(chromlen, end + width - 1)
        print(f"{chrom}\t{start + chromstart}\t{end + chromstart}", file=output)
        scores[start:end] = 0
    output.close()


if __name__ == "__main__":
    main()