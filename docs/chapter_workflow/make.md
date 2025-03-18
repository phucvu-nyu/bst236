# GNU Make 
!!! abstract "Learning Objectives"
    - Understand how Make can automate and document workflows
    - Learn Make syntax and basic concepts
    - Create Makefiles for common scientific computing tasks
    - Integrate Make with version control and data analysis pipelines

## Why Make?

Make is a powerful tool for:

1. **Automation**: Automate complex workflows with a single command
2. **Documentation**: Self-documenting build process; Makefiles are your cheat sheet
3. **Dependency Management**: Only rebuild what's necessary
4. **Reproducibility**: Ensure consistent builds across different environments

## Make Basics

### Makefile Structure

A basic Makefile consists of rules with targets, prerequisites, and recipes:

```makefile
target: prerequisites
    recipe
```

Example:
```makefile
paper.pdf: paper.tex references.bib
    pdflatex paper.tex
    bibtex paper
    pdflatex paper.tex
    pdflatex paper.tex
```

### Key Concepts

1. **Targets**: Files to be created
2. **Prerequisites**: Files needed to create the target
3. **Recipes**: Commands to create the target
4. **Phony Targets**: Targets that don't create files

## Common Workflows

### Version Control Workflow

```makefile
.PHONY: commit push pull clean

# Git commands with automatic messages
commit:
    git add .
    @read -p "Enter commit message: " msg; \
    git commit -m "$$msg"

push: commit
    git pull origin main
    git push origin main

pull:
    git pull origin main

# Clean generated files
clean:
    rm -f *.aux *.log *.bbl *.blg *.out
```

### LaTeX Document Workflow

```makefile
# Variables for file names
PAPER = paper
FIGS = $(wildcard figures/*.pdf)

# Main targets
.PHONY: all clean

all: $(PAPER).pdf

# Build PDF with automatic bibliography
$(PAPER).pdf: $(PAPER).tex bibliography.bib $(FIGS)
    pdflatex $(PAPER)
    bibtex $(PAPER)
    pdflatex $(PAPER)
    pdflatex $(PAPER)

# Clean LaTeX auxiliary files
clean:
    rm -f *.aux *.log *.bbl *.blg *.out $(PAPER).pdf

# Watch for changes and rebuild
watch:
    while true; do \
        make all; \
        inotifywait -e modify $(PAPER).tex bibliography.bib; \
    done
```

### Data Analysis Workflow

```makefile
# Directories
DATA_DIR = data
RESULTS_DIR = results
FIGS_DIR = figures

# Data files
RAW_DATA = $(DATA_DIR)/raw_data.csv
CLEAN_DATA = $(DATA_DIR)/clean_data.csv
ANALYSIS_RESULTS = $(RESULTS_DIR)/analysis_results.csv
FIGURES = $(FIGS_DIR)/figure1.pdf $(FIGS_DIR)/figure2.pdf

# Main targets
.PHONY: all clean

all: report.pdf

# Data processing pipeline
$(CLEAN_DATA): $(RAW_DATA) scripts/clean_data.R
    Rscript scripts/clean_data.R

$(ANALYSIS_RESULTS): $(CLEAN_DATA) scripts/analyze_data.R
    Rscript scripts/analyze_data.R

$(FIGS_DIR)/%.pdf: $(ANALYSIS_RESULTS) scripts/make_figures.R
    Rscript scripts/make_figures.R

# Generate report
report.pdf: report.Rmd $(ANALYSIS_RESULTS) $(FIGURES)
    R -e "rmarkdown::render('report.Rmd')"

# Clean generated files
clean:
    rm -f $(CLEAN_DATA) $(ANALYSIS_RESULTS) $(FIGURES) report.pdf
```

## Advanced Make Features

### Pattern Rules

Use pattern rules to handle multiple similar files:

```makefile
# Convert all .tex files to .pdf
%.pdf: %.tex
    pdflatex $<
```

### Variables and Functions

```makefile
# Variables
CC = gcc
CFLAGS = -Wall -O2

# Functions
SOURCES = $(wildcard src/*.c)
OBJECTS = $(SOURCES:.c=.o)
```

### Automatic Variables

- `$@`: Target name
- `$<`: First prerequisite
- `$^`: All prerequisites
- `$*`: Stem in pattern rule

Example:
```makefile
%.o: %.c
    $(CC) -c $(CFLAGS) $< -o $@
```

## Best Practices

### 1. Directory Structure

Organize your project with clear directory structure:
```makefile
# Directory structure
DIRS = data src results figures docs
$(shell mkdir -p $(DIRS))
```

### 2. Documentation

Include comments and help target:
```makefile
.PHONY: help
help:
    @echo "Available targets:"
    @echo "  all      - Build everything"
    @echo "  clean    - Remove generated files"
    @echo "  data     - Process raw data"
    @echo "  figures  - Generate figures"
```

### 3. Error Handling

Use error checking in recipes:
```makefile
data/processed.csv: data/raw.csv scripts/process.R
    Rscript scripts/process.R || (rm -f $@; exit 1)
```

### 4. Dependency Tracking

Track both code and data dependencies:
```makefile
results/model.rds: src/train_model.R data/training.csv
    Rscript $< data/training.csv $@
```

## Example: Complete Research Project

```makefile
# Configuration
R_SCRIPTS = $(wildcard scripts/*.R)
TEX_FILES = $(wildcard paper/*.tex)
BIB_FILES = $(wildcard paper/*.bib)

# Main targets
.PHONY: all paper data clean

all: paper data

# Paper compilation
paper: paper/manuscript.pdf

paper/manuscript.pdf: $(TEX_FILES) $(BIB_FILES) results/analysis.rds figures/*.pdf
    cd paper && pdflatex manuscript
    cd paper && bibtex manuscript
    cd paper && pdflatex manuscript
    cd paper && pdflatex manuscript

# Data analysis pipeline
data: results/analysis.rds figures/plot1.pdf figures/plot2.pdf

results/analysis.rds: scripts/analyze.R data/clean_data.csv
    Rscript $<

figures/%.pdf: scripts/plot.R results/analysis.rds
    Rscript $<

# Data cleaning
data/clean_data.csv: scripts/clean.R data/raw_data.csv
    Rscript $<

# Utility targets
clean:
    rm -f paper/*.{aux,log,bbl,blg}
    rm -f results/* figures/*

.PHONY: sync
sync: all
    git add .
    git commit -m "Update analysis and paper"
    git push origin main
```

## Resources

- [GNU Make Documentation](https://www.gnu.org/software/make/manual/)
- [Make for Data Science](https://blog.mindlessness.life/makefile/2019/11/17/the-language-agnostic-all-purpose-incredible-makefile.html)
- [Minimal Make](https://kbroman.org/minimal_make/)


### Project Organization Guidelines

Here is an example of a project structure:
```
project/
├── refs/
├── README.md
├── Makefile
├── data/
│   └── birds_count_table.csv
├── doc/
│   ├── notebook.md
│   ├── manuscript.md
│   └── changelog.txt
├── results/
│   └── summarized_results.csv
└── src/
    ├── sightings_analysis.py
    └── runall.py
```

1. **Create a Project Directory**:
      - Put each project in its own directory, named after the project.

2. **Organize Text Documents**:
      - Place all text documents related to the project in a `doc` directory. This includes manuscripts, documentation, and electronic lab notebooks.

3. **Manage Data**:
      - Store raw data and metadata in a `data` directory.
      - Place files generated during cleanup and analysis in a `results` directory.

4. **Source Code Management**:
      - Keep all project source code in a `src` directory. This includes scripts and programs written for the project.

5. **Executable Programs**:
      - If applicable, store compiled programs in a `bin` directory.

6. **File Naming**:
      - Name all files to reflect their content or function. Avoid using sequential numbers or manuscript location references.

7. **Documentation and Metadata**:
      - Include a `README` file in the project's root directory to provide an overview of the project.
      - Add a `Makefile` to define the project's build pipeline.

8. **Version Control**:
      - Use a version control system to track changes and manage project versions.

9. **Backup and Synchronization**:
      - Ensure that the project directory is mirrored off the working machine using a system like Dropbox or a remote version control repository.

Here is another example of project template for a paper project:

```
paper/
├── analysis/
│   ├── README.md
│   ├── 00_clean_data.R
│   ├── 01_fit_models.R
│   ├── 02_make_figures.R
│   └── sandbox/
├── sim/
│   ├── README.md
│   ├── helper_functions.R
│   ├── sim_script.R
│   ├── run_sim_script.sh
│   └── sandbox/
├── figs/
├── notes/
├── ref_papers/
├── submitted/
├── revision/
├── final/
├── README.md
├── Makefile
├── my_paper.tex
└── my_refs.bib
```

## Data Management

Example of data analysis project:
```
analysis/
├── raw_data/
├── data/
├── R/
│   ├── 00_clean_data.R
│   ├── 01_fit_models.R
│   ├── 02_make_figures.R
│   ├── 03_summarize_results.R
│   └── 04_report.Rmd
├── figs/
├── sandbox/
│   └── exploratory.R
├── ref_papers/
├── Makefile
├── README.md
└── renv
```
Here is the guideline for data management:

1. **Save the Raw Data**:
      - Raw data are sacred... but may be a mess. Always keep the original data as it was first generated. 
     - Tempting to edit raw data by hand. <u>Don't!</u> Avoid overwriting raw data files with cleaned versions. Consider setting file permissions to read-only to prevent accidental changes.

2. **Backup Raw Data (3-2-1 Rule)**:
      - Keep at least 3 copies of your data
     - Store the copies on 2 different types of storage media
     - Keep 1 backup copy off-site (e.g., cloud storage, external drive at another location)

3. **Create Analysis-Friendly Data**:
      - Convert data into open, non-proprietary formats (e.g., CSV for tabular data). Use meaningful variable names and ensure filenames reflect their content.

4. **Everything scripted**:
      - Document Data Processing Steps. Record all steps used to process data. Write scripts for each stage of data processing to ensure reproducibility and ease of re-running analyses.
5. **Document Data**:
      - Use meta-data files to describe raw and cleaned data (e.g., `.csv` so easy to read)

## Collaboration

1. **Talk to your collaborators**:
      - Not everyone is comfortable with LaTeX or git or what we have learned in this course. So build an automated pipleline to generate other types of files, e.g., use `pandoc` to generate `docx` from `tex`.
      - Address organization from the outset.
      - Only have single master version online. Every collaborator's edit should be easily synchronized. Ideally, bring people on board to your (version controlled, reproducible) system. But try to design your project template robust for different systems. For example, if the master version is on overleaf, then design workflow compatible for all overleaf, dropbox, and git synchronization.
      - Make explicit decisions about how project members will communicate.
2. **Create an Overview of Your Project**
      - Have a `README` file in the project's home directory that explains the purpose of the project.
      - Include the project's title, a brief description, up-to-date contact information, and examples of how to run various tasks.
      - Include a `CONTRIBUTING` file that describes how to get the project running, use it, or contribute to it, including dependencies and tests.
3. **Create a Shared Document to Track Progress**
      - Maintain a plain text file like `log.md` or use project management platforms like [Trello](https://trello.com/) to create issues for each task.
      - Clearly describe tasks to make them understandable for newcomers.
      - Write the document, so we can backtrack of the progress of the project and how the project evolved.
