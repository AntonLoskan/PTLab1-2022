from Types import DataType

RatingType = dict[str, float]


class CountSubjects:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.rating: RatingType = {}

    def calc(self) -> RatingType:
        for key in self.data:
            self.rating[key] = 0
            for subject in self.data[key]:
                if subject[1] == 76:
                    self.rating[key] += 1
        return self.rating
