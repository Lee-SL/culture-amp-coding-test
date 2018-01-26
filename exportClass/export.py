class Export(object):
    def __init__(self, ppCount, ppPercent, avgs, comment):
        self.ppCount = ppCount
        self.ppPercent = ppPercent
        self.avgs = avgs
        self.comment = comment

    def displayRes(self):
        print("Survey Summary as Follows:\n")
        print("""
Participant Count: {0}
Participation Percentage {1:0.1f}%
        """.format(self.ppCount, self.ppPercent))

        # print all elements within the dictionary
        print("Questions and Ratings\n")
        for k, v in self.avgs.items():
            print("{0}: {1:0.2f}".format(k, v))

        # print comments
        print("""
Data Quality Comments:
    {0}""".format(self.comment))
