import pandas as pd
class PPCalcs(object):
    def __init__(self, survey_res, comment):
        self.survey_res = survey_res
        self.comment = comment

    def __ppCount(self, survey_res):
        # private
        return len(survey_res[2].dropna())

    def __ppPercent(self, survey_res, ppCount):
        # private
        countTotal = len(survey_res[2])
        ppPercent = ppCount / max(countTotal, 1) * 100
        # nice formatting to 1 decimal places
        return ppPercent

    def ppCalc(self):
        ppCount = self.__ppCount(self.survey_res)
        ppPercent = self.__ppPercent(self.survey_res, ppCount)
        return ppCount, ppPercent
