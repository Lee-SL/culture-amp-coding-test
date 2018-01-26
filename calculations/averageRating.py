import pandas as pd
class AverageRating(object):

    def __init__(self, survey, survey_res, comment):
        self.survey = survey
        self.survey_res = survey_res
        self.comment = comment

    def __rowIndexRQ(self, survey):
        # private
        # returns row index of rating question, takes in a dataframe of survey questions
        return list(survey.loc[survey.type == "ratingquestion", "type"].index.values)

    def __colRQ(self, rowIndex, survey_res):
        # private
        # this function returns columns from survey results that just has the ratings in it (incl. nulls) and the col-index
        # add 3 to index as responses start with column 3
        colIndex = [x + 3 for x in rowIndex]
        RQ = survey_res.iloc[:, colIndex]
        return RQ, colIndex

    def __avg(self, RQ):
        # private
        # Calculates the averages of individual columns in the RQ dataframe. Nulls will be ignored.
        avgRQ = []
        for col in list(RQ):
            # first drop all nans, we cannot calc average if we don't drop the NaNs
            ratings = RQ[col].dropna()
            avgRQ.append(float(sum(ratings)) / max(len(ratings), 1))
        return avgRQ

    def __dataQualityCheck(self, RQ, comment):
        # private
        # Checks for value range being 1-5 and if integer or not adds anomolies to a comment string
        for col in list(RQ):
            if len(RQ.loc[RQ[col] < 1, :]) != 0:
                comment += "\ncolumn {0} has a value less than 1.".format(col)
            if len(RQ.loc[RQ[col] > 5, :]) != 0:
                comment += "\ncolumn {0} has a value greater than 5.".format(
                    col)
            if RQ[col].dtype != "int64":
                comment += "\ncolumn {0} in survey response has a type other than integer.".format(
                    col)
        return comment

    def __createDict(self, survey, rowIndex, avgRQ):
        # private
        # returns key value pairs with the key being the question and the value being the average ratings
        # Notice that the length of avgRQ list is sufficient information to create our dictionary
        avgs = {}
        for (index, i) in enumerate(rowIndex):
            # i is the number in the rowIndex list where as index is the loops index
            qs = survey["text"][i]
            avgs[qs] = avgRQ[index]
        return avgs

    def avgRating(self):
        # public
        # average rating, takes in survey and survey_res outputs a dictionary with rating question and average rating
        rowIndex = self.__rowIndexRQ(self.survey)

        RQ, colIndex = self.__colRQ(rowIndex, self.survey_res)
        # remove all null rows with all condition only remove if all nans
        RQ = RQ.dropna(axis=0, how='all')

        # Data Quality Checks
        self.comment += self.__dataQualityCheck(RQ, self.comment)

        avgRQ = self.__avg(RQ)
        avgs = self.__createDict(self.survey, rowIndex, avgRQ)

        return avgs, self.comment
