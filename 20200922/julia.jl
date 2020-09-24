#!env julia

# simply copied from
#
# https://docs.julialang.org/en/v1/base/io-network/
#
# with adaptation to problem
#
open("file1.csv", "w") do io
           write(io, "'Danka', 9, 9\n")
       end;
       
