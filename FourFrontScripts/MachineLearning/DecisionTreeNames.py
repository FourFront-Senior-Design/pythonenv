from MachineLearning.DecisionTreeAll import DecisionTreeAll

class DecisionTreeNames(DecisionTreeAll):

    def __init__(self):
        super().__init__()

    def __selectData(self):
        name = ['FirstName', 'MiddleName', 'LastName', 'Suffix', 'FirstNameS_D', 'MiddleNameS_D', 'LastNameS_D',  'SuffixS_D',
                'FirstNameS_D_2', 'MiddleNameS_D_2', 'LastNameS_D_2', 'SuffixS_D_2', 'FirstNameS_D_3', 'MiddleNameS_D_3',
                'LastNameS_D_3', 'SuffixS_D_3', 'FirstNameS_D_4', 'MiddleNameS_D_4', 'LastNameS_D_4', 'SuffixS_D_4',
                'FirstNameS_D_5', 'MiddleNameS_D_5', 'LastNameS_D_5', 'SuffixS_D_5', 'FirstNameS_D_6', 'MiddleNameS_D_6',
                'LastNameS_D_6', 'SuffixS_D_6']
        self._dataframe = self._dataframe[self._dataframe['category'].isin(name)]


    def Predict(self, markerType, imageLoc, coordinates):
        self.__selectData()
        category = super().Predict(markerType, imageLoc, coordinates)
        return category
