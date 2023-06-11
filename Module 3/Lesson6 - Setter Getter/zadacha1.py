class Year:
    def __init__(self, days, season):
        self.__days = days
        self.__season = season

    @property
    def days(self):
        return self.__days

    @days.setter
    def days(self, days):
        self.__days = days

    @property
    def season(self):
        return self.__season

    @season.setter
    def season(self, season):
        self.__season = season

    def get_days(self):
        return self.__days

    def set_days(self, days):
        if days == 365 or days == 366:
            self.__days = days
        else:
            raise Exception(f"Вы передали некорректное значение,  в году не может быть {days}")

    def get_season(self):
        return self.__season
    def set_season(self, season):
        if season == "Зима" or season == "Лето" or season == "Осень" or season == "Весна":
            self.__season = season
        else:
            raise Exception(f"Вы передали некорректное значение,  в году не может быть сезона с названием: {season}")




year = Year(365, "Зима")
year2 = Year(366, "Осень")



print(year.get_days(), year.get_season())
print(year2.get_days(), year2.get_season())


#обработка исключений - кол-во дней вы году
# year.set_days(280)
# print(year.get_days())

#обработка исключений - название сезона
# year.set_season("ваЛето")
# print(year.get_days(), year.get_season())