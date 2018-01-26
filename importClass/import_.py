import pandas as pd

class Import(object):

    def __checkSurveyQs(self, survey):
        # private
        # check survey schema must contain columns type, theme, text
        # first check if there is a survey if not fail straight away
        if survey is None:
            raise Exception("Please import a survey")

        checkList = ['theme', 'type', 'text']
        for colName in list(survey.columns):
            if colName in checkList:
                # print(checkList)
                # remove this name from check list if present
                checkList.remove(colName)
        if len(checkList) != 0:
            raise Exception(
                "{0} columns is not in the imported file please load again".format(checkList))

    def __checkSurveyRes(self, survey, survey_res):
        # private
        # check survey result number of response columns must be the same as the number of questions on the survey
        # otherwise fail the import until they match.
        # first check if there is a survey_res if not fail straight away
        if survey_res is None:
            raise Exception("Please import a survey response")
        numberOfQs = len(survey)
        numberOfResp = len(list(survey_res.iloc[:, 3:].columns))
        #print(numberOfQs, numberOfResp)
        if numberOfQs != numberOfResp:
            raise Exception("{0} questions were asked in the survey but there are {1} responses please check".format(
                numberOfQs, numberOfResp))

    def importSurveys(self, file_path):
        # private
        # Check if file can be loaded into a dataframe
        try:
            # remember to no header for responses
            if 'response'in file_path:
                df = pd.read_csv(file_path.strip(), header=None)
            else:
                df = pd.read_csv(file_path.strip())
        except Exception as err:
            print("Import error encountered, please try again:", err)
        else:
            return df

    def checkSurveys(self, survey, survey_res):
        self.__checkSurveyQs(survey)
        self.__checkSurveyRes(survey, survey_res)
        
        #if import no errors print message import successful
        print("\nImport Successful!\n")