IN=1
NAME=Arianna
#------------------
INFILE=file${IN}.csv
OUTFILE=file$((${IN}+1)).csv
n2=`wc -l $0 | awk '{print $1}'`

if [ -f ${INFILE} ] ; then
  cat ${INFILE} | tee ${OUTFILE}
  n1=`awk '{print $NF}' < $INFILE`
else
  echo file ${INFILE} not found
  n1=0
  OUTFILE=file1.csv
  if [ -f ${OUTFILE} ] ; then
    echo output file exists - aborting
    exit 1
  fi
fi

n=$((n1+n2))
echo "'$NAME', $n2, $n" | tee -a ${OUTFILE}
