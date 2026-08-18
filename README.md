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

## Variability of iron stress in HNLC regions

This project will calculate a proxy for iron stress using BGC Argo float data in three regions of the Pacific (Subpolar North Pacific, equatorial Pacific, and Southern Ocean).  Using these estimates, we will examine how iron stress relates to physical and biogeochemical properties, such as mixed layer depth, oxygen, nitrate, and carbon parameters.

### Collaborators

* Hayden 
* Jannes
* Ally
* Alison


### Questions

How does iron stress vary in different regions of the Pacific Ocean, specifically the Southern Ocean, the North Pacific, and the equatorial Pacific?  How does iron stress co-vary with oxygen, nitrate, and carbon?

## Data and Methods

### Data

BGC Argo profiles of fluorescence, PAR, nitrate, oxygen, pH and derived carbon parameters 

### Existing methods

Methods to estimate iron stress are from [Ryan-Keogh and Thomalla, 2020](https://doi.org/10.3389/fmars.2020.00275).

### Proposed methods/tools

We will apply this method to BGC Argo profiles in three previously unexamined regions.

### Additional resources or background reading

Schallenberg, C., Strzepek, R. F., Bestley, S., Wojtasiewicz, B., & Trull, T. W. 2022. Iron limitation drives the globally extreme fluorescence/chlorophyll ratios of the Southern Ocean. Geophysical Research Letters, 49, e2021GL097616. (https://doi.org/10.1029/2021GL097616) 

Ryan-Keogh, T. J. et al., 2023. Multidecadal trend of increasing iron stress in Southern Ocean phytoplankton. Science, 379, 834-840. (https://doi.org/10.1126/science.abl5237)

## Project goals and tasks

### Project goals

* Apply methods from Schallenberg et al. 2022 to float data from the Pacific 
* Assess the resulting estimates of iron stress in relation to physical and biogeochemical properties.

### Tasks

* Calculate alpha_NPQ
  * Write one function to calculate MLD (Hayden)
  * Write one function to calculate PAR_15, depth where PAR = 15 (Ally)
  * Write one function to load unadjusted Fl data and find non-quenched fluorescence (F_m; value at shallower of MLD and PAR_15) (Jannes)
  * Calculate NPQ from difference between non-quenched Fl and measured Fl / non-quenched Fl
* Regress NPQ with PAR to get alpha_NPQ
  * Write function to compute Equation 3
   <img width="253" height="46" alt="image" src="https://github.com/user-attachments/assets/f4de18bd-4f68-4844-a623-ce2ae67b63f0" /> (Alison)

* Compare alpha_NPQ to oxygen, nitrate, DIC, etc 
  

## Project Results

<!-- Use this section to briefly summarize your project results. This could take the form of describing the progress your team made to answering a research question, developing a tool or tutorial, interesting things found in exploring a new dataset, lessons learned for applying a new method, personal accomplishments of each team member, or anything else the team wants to share.

You could include figures or images here, links to notebooks or code elsewhere in the repository (such as in the [notebooks](notebooks/) folder), and information on how others can run your notebooks or code.
-->
