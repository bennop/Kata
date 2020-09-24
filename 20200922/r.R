step <- 4
my.name <- "Benno"
# this may not work on all systems

print(commandArgs(TRUE))
cat('nframe: ', sys.nframe(),'\n')
for(i in sys.nframe():0){
  cat(i, '\n')
  print(ls(name = sys.frame(i)))
}

# Introspection - find lines of this script
this.file <- sys.frame(1)$ofile
#this.file <- 'main.r' # hard coded
# detect number of lines in this script
my.lines <- nrow(read.table(this.file, head=FALSE, sep = '@', blank.lines.skip = FALSE))

# helper function
next.file <- function(n=0){
  return(sprintf('file%d.csv', n+1))
}

# for initial file simply write string
initial.file <- function(){
  write(sprintf("'%s', %d, %d",  my.name, my.lines, my.lines), next.file())
}

# transition from previous file
relay.file <- function(n=3){
  infile <- next.file(n-1)
  if(file.exists(infile)){
    old <- read.table(infile, header = FALSE, sep=',')
    nl <- nrow(old)
    new <- rbind(old, as.data.frame(list(V1=my.name, V2=my.lines, V3=my.lines + old[nl,ncol(old)])))
    # print(new)
    write.table(new, file = next.file(n),            col.names = FALSE,
                row.names = FALSE,
                sep = ',')
  } else {
    warning("input file ", infile, " not found")
  }
}

# body of script
infile <- next.file(step-2)
if(file.exists(infile)){
  cat(step - 1, ' -> ', step, '\n')
  relay.file(step-1)
} else {
  cat('initial file\n')
  initial.file()
}
