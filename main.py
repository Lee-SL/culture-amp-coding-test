# import all methods here
from importClass.import_ import Import
from exportClass.export import Export
from calculations.ppCalcs import *
from calculations.averageRating import *


def Main():
    # initialise comments
    comment = ""
    # import
    importOb = Import()
    print("""
To summarise survey results please enter the file path for both the survey and the survey responses
Please enter the survey file path for example: ./example-data/survey-1.csv 
    """)
    survey = importOb.importSurveys(input())

    print("""
Please enter the survey response file path for example: ./example-data/survey-1-responses.csv
    """)
    survey_res = importOb.importSurveys(input())
    importOb.checkSurveys(survey, survey_res)

    # Calculations
    # participation calculations
    # initialise object
    ppCalc = PPCalcs(survey_res, comment)
    ppCount, ppPercent = ppCalc.ppCalc()

    # average rating calculations
    # initialise object
    avgRQ = AverageRating(survey, survey_res, comment)
    avgs, comment = avgRQ.avgRating()

    # export class
    export = Export(ppCount, ppPercent, avgs, comment)
    export.displayRes()

if __name__ == "__main__":
    Main()
