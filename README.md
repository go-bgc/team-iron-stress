<!-- # Sample Project

This is an example of how teams can structure their project repositories and format their project README.md file.

When creating a project repository from this template choose "Public" so other participants can follow progress. Add a "topic" to your repository details (click on the gear icon next to the "About" section on the repository page) to help others find your work (e.g. `icesat2-hackweek-2024`).


## Files and folders in your project repository

This template provides the following suggested organizaiton structure for the project repository, but each project team is free to organize their repository as they see fit.

* **`contributors/`**
<br> Each team member can create their own folder under contributors, within which they can work on their own scripts, notebooks, and other files. Having a dedicated folder for each person helps to prevent conflicts when merging with the main branch. This is a good place for team members to start off exploring data and methods for the project.
* **`notebooks/`**
<br> Notebooks that are considered delivered results for the project should go in here.
* **`scripts/`**
<br> Code that is shared by the team should go in here (e.g. functions or subroutines). These will be files other than Jupyter Notebooks such as Python scripts (.py).
* `.gitignore`
<br> This file sets the files that will be globally ignored by `git` for the project. (e.g. you may want git to ignore temporary files or large data files, [read more about ignoring files here](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files))
* `environment.yml`
<br> `conda` environment description needed to run this project.
* `README.md`
<br> Description of the project (see suggested headings below)
* `model-card.md`
<br> Description (following a metadata standard) of any machine learning models used in the project

# Recommended content for your README.md file:

(you can remove the content here and above from your final project README.md file so that it begins with the Project or Team Name title below)
-->

# Team Iron Stress

## Project Title and Introduction

Provide a brief introduction describing the proposed work. Be sure to also decribe what skills team members will get to learn and practice as part of this project.

### Collaborators

List all participants on the project. Here is a good space to share your personal goals for the hackweek and things you can help with.

| Name | Personal goals | Can help with | Role |
| ------------- | ------------- | ------------- | ------------- |
| Katherine J. | I want to learn specific python libraries for working with these data  | I can help with understanding our dataset, programming in R  | Project Lead |
| Rosalind F. | Practice leading a software project | machine learning and python (scipy, scikit-learn) | Project Lead |
| Alan T. | learning about your dataset | GitHub, Jupyter, cloud computing | Project Helper |
| Rachel C. | learn to use github, resolve merge conflicts | I am familiar with our dataset | Team Member  |
| ... | ... | ... | ... |
| ... | ... | ... | ... |

### The problem

How does iron stress vary in different regions of the Pacific Ocean, specifically the Southern Ocean, the North Pacific, and the equatorial Pacific?  How does iron stress co-vary with oxygen, nitrate, and carbon?

## Data and Methods

### Data

BGC Argo profiles of fluorescence, irradiance, nitrate, oxygen.

### Existing methods

Methods to estimate iron stress are from [Ryan-Keogh and Thomalla, 2020](https://doi.org/10.3389/fmars.2020.00275).

### Proposed methods/tools

We will apply this method to BGC Argo profiles in new regions.

### Additional resources or background reading

Schallenberg, C., Strzepek, R. F., Bestley, S., Wojtasiewicz, B., & Trull, T. W. (2022). Iron limitation drives the globally extreme fluorescence/chlorophyll ratios of the Southern Ocean. Geophysical Research Letters, 49, e2021GL097616. (https://doi.org/10.1029/2021GL097616) 

Thomas J. Ryan-Keogh et al., Multidecadal trend of increasing iron stress in Southern Ocean phytoplankton.Science379,834-840(2023). (https://doi.org/10.1126/science.abl5237)

## Project goals and tasks

### Project goals

List the specific project goals or research questions you want to answer. Think about what outcomes or deliverables you'd like to create (e.g. a series of tutorial notebooks demonstrating how to work with a dataset, results of an anaysis to answer a science question, an example of applying a new analysis method, or a new python package).

* Goal 1
* Goal 2
* ...

### Tasks

What are the individual tasks or steps that need to be taken to achieve each of the project goals identified above? What are the skills that participants will need or will learn and practice to complete each of these tasks? Think about which tasks are dependent on prior tasks, or which tasks can be performed in parallel.

* Calculate alpha_NPQ
  * Write one function to calculate MLD (Hayden)
  * Write one function to calculate PAR_15, depth where PAR = 15 (Ally)
  * Write one function to load unadjusted Fl data and find non-quenched fluorescence (F_m; value at shallower of MLD and PAR_15) (Jannes)
  * Calculate NPQ from difference between non-quenched Fl and measured Fl / non-quenched Fl
* Regress NPQ with PAR to get alpha_NPQ
  * Write function to compute Equation 3
  <img width="253" height="46" alt="image" src="https://github.com/user-attachments/assets/f4de18bd-4f68-4844-a623-ce2ae67b63f0" />

* Compare alpha_NPQ to oxygen, nitrate, DIC, etc 
  

## Project Results

Use this section to briefly summarize your project results. This could take the form of describing the progress your team made to answering a research question, developing a tool or tutorial, interesting things found in exploring a new dataset, lessons learned for applying a new method, personal accomplishments of each team member, or anything else the team wants to share.

You could include figures or images here, links to notebooks or code elsewhere in the repository (such as in the [notebooks](notebooks/) folder), and information on how others can run your notebooks or code.
