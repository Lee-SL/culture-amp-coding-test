# Development
## Installation packages required to run app:
* Python 3.5 and above
* Pandas 

## Running the code
Run the code by using the command as follows, in the main directory
```
python3 main.py
```

## Development process
Under resources folder I have used a Jupyter Notebook called scratchpad to test all my python code before imputting into the modules

## Data Quality
# Import
* Check if survey contains columns theme, type & text. If not fail the import.
* Cross check between number of survey questions and survey responses they should match if not fail the import.
# AverageRating
* Check if ratings column have a value outside of 1-5, if there is add this to the comment string.
* Check if ratings column have a type other than integer, if there is add this to the comment string.

#Concepts
## Architecture concepts
We want to separate import and export as classes so it is decoupled to calculations. we may want to edit calculations or replace import and export functions so we can change each component without having to change the code overall.

## Design Thinking
### Calculating participation percentage and total participant counts
Check the third column of result table as this is the date submitted, if it is null, NaN assume user did not participate. Hence, participation percentage is (participants/total users) * 100. Total participant counts were assumed to be the number of users who participated.

### Calcuting average of rating question
There is two major ways to solve average rating of a question. The first way could be to check whether or not the column (from the results) has integer data and between 1-5 if so consider this column a rated question. The second is to actually check for ratedquestion status from the survey table and record its index and apply it from the fourth column onwards on the results table. In my solution I have implemented a combination of both, using the second method for actual data processing and the first method for data quality checks. 


