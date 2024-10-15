#Klass DVD som inehåller relevant information om DVD filmen.
class DVD:
    def __init__(self, Title, Directors, Genre, Year):
        self.Title = Title
        self.Directors = Directors
        self.Genre = Genre
        self.Year = Year

#Fukntion som visar information om DVD filmen.
    def Show_info(self):
        directors = ", ".join(self.Directors)
        return (f"{self.Title}, Directors: {directors}, Genre: {self.Genre}, Production year: {self.Year}")