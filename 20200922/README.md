# Data Relay
2020-09-22

Arianna, Benno, Danka, Sylvain

## Relay Task
Write scripts to either

- output 
    - a team member's name
    - lines of script
    - total lines of scripts (same as `lines of script` since first and only script)
```
    'Nick', 5, 5
```
- take output of preceding script and output that appended by the previously defined output
```
    'Nick', 5, 5
    'Benno', 10, 15
```

Each script should be in a **different programming language**. 

## Approach
### Considerations

#### Persistence

Passing data between scripts could be done via

- piping
- files
    - text (e.g., *.csv)
    - json
- database
    - new `repl.it` feature

Options `pipe` is not available on `repl.it`, option `database` did not work for `R` as advertised -> files; since **json** may not be easily accessible (bash) -> **csv** which can be handled easily across languages.

Since sharing of files across repls is apparently not supported on `repl.it` and was implemented via *manual copy* from one repl to the next.

#### Language selection
in alphabetical order
- [`bash`](https://www.gnu.org/software/bash)
    - see post on [useful shell tools](https://www.johndcook.com/blog/2019/08/30/cut-sort-awk/)
- [`Java`](https://www.java.com/)
- [`Julia`](https://julialang.org/) (after Google hit)
- [`Python`](https://www.python.org/)
- [`R`](https://www.r-project.org)

#### Relay processing

Two strategies for the subsequent relay steps 

1. *copy* (used for `bash` and `python` (1st version))
    - input file to output 
    - parse for `lines so far`
    - append self-related info to output
2. *load* (used for `R` and `python` (2nd version))
    - input file
    - augment with self-related info after parsing for `lines so far`
    - write combined info to output
    
#### Line Count
Initially hard-code the number of lines (see "*introspection*" in Outlook below for improvement)

### Realisation
1. Use least familiar language for simplest task (initial step, first file): `Java` and `Julia`.

2. `bash` was chosen for step 2 as it's initial version relied on its input having exactly one line. (generalized now)

3. `python` and `R` offer better high-level function support and, thus, were selected for the latter steps.

### Extension / Outlook
For fun: 

- add **flexibility**
    - handle any step (`bash`, `R`)
        - indicate via parameter (or automatically continue on highest output found?)
        - default to original sequence
    - fault tolerance (`R`)
        - start over when input file not accessible
- add **introspection** (detect line count for current script) where feasible
    - No(t yet)
        - `Java`, `Julia`
    - Partly
        - `R`
    - done
        - `bash`, `python`
- **Workflow** ideas for *Git setup* (all scripts in same directory - needs some kind of UNIX)
    - `makefile` (started)
        - [x] **clean**: remove all output files
        - [x] make scripts **directly executable** (except `java`), i.e., script can be called either, e.g. `python python1.py` or `./python1.py`
            - [x] `make` target `executable` to set `x`-flag
            - [x] add exec line at start of script (except `java`)
        
