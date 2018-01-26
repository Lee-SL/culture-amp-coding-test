Packages required to run app:
Pandas

Usage of pandas package justification
App will require mostly reading and exporting csv files and data analysis which 
is what pandas dataframes excel at.


Solution concepts
why we want to separate import and export as classes so it is decoupled to business logic
we may want to edit business logic or replace import and export functions so we can change each 
component without having to change the code overall.

create import class 
create export class

Design decisions
Functions should only contain one calculation/logic not multiple calculations for example a function
would calculate the participation percentage and another calculate the total participation count. Not achieving both in one function. 

Design Solutions
Calculating participation percentage and total participant counts
Check the third column of result table as this is the date submitted, if it is null, NaN assume user did not participate. Hence, participation percentage is (participants/total users) * 100. Total participant counts were assumed to be the number of users who participated.

Calcuting average of rating question
There is two major ways to solve average rating of a question. The first way could be to check whether or not the column (from the results) has integer data and between 1-5 if so consider this column a rated question. The second is to actually check for ratedquestion status from the survey table and record its index and apply it from the fourth column onwards on the results table. In my solution I have implemented a combination of both, using the second method for actual data processing and the first method for data quality checks. In production environments when the volume of data is high its extremely hard to check each value in a column to see if it is integer or not so I have opted to just check for column type and for the 1-5 check it is near impossible to loop through each element and see if that number is between 1-5 so I have counted the elements and summed the columns if the sum of the column is less than the count it will mean that one of the elements has a 0 input. Currently, I cannot think of a nice way and production ready method to check if any number is greater than 5 so I will leave it as a possible improvement in the future. 

Development Tools
github
vscode 
jupyter notebook (testing)

Extensibility
- Import multiple files using * notation (wildcard concats)

- Export not just display but an csv file

