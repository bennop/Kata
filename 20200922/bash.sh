#!/bin/bash

IN=${1:-1}
NAME=Arianna
#------------------
INFILE=file${IN}.csv
OUTFILE=file$((${IN}+1)).csv

# Introspection: own lines
# $0 refers to the command, i.e., the script
n2=`wc -l $0 | awk '{print $1}'`

if [ -f ${INFILE} ] ; then
  # using `tee` outputs also to `stdout`
  # could otherwise be simply copied (via `cp`)
  cat ${INFILE} | tee ${OUTFILE}
  # parse for lines so far: last field of line, 
  # added `tail` to keep only last line
  n1=`awk '{print $NF}' < $INFILE | tail -1`
else
  echo file ${INFILE} not found
  n1=0                            # no lines so far
  OUTFILE=file1.csv
  if [ -f ${OUTFILE} ] ; then
    echo output file exists - aborting
    exit 1
  fi
fi

# calculate updated line total
n=$((n1+n2))

# final line of output
echo "'$NAME', $n2, $n" | tee -a ${OUTFILE}
