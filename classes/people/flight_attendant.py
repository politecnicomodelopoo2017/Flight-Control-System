from .crew import *


class FlightAttendant(Crew):
    def __init__(self, name=None, last_name=None, dni=None, date_of_born=None,
                 languages_that_speak=None, models_allowed_to_fly=None):
        """Creates a FlightAttendant

        :param name: is the name. type<str>
        :param last_name: is the last name. type<str>
        :param dni: is the dni. type<str>
        :param date_of_born: is the day of born. type<date>
        :param languages_that_speak: type<list>
        :param models_allowed_to_fly: type<list>
        """
        Crew.__init__(self, name, last_name, dni, date_of_born, models_allowed_to_fly)

        self.languages_that_speak = languages_that_speak

    def charge_txt(self, l):
        # TODO: pasarle una lista de aviones en vez de l[5].split(',') ya que esto es una lista de string y no de aviones.
        Crew.charge_txt(self, l)
        self.models_allowed_to_fly = l[5].split(',')
        self.languages_that_speak = l[6].split(',')
