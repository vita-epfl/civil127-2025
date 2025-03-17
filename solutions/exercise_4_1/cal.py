import datetime


class Cal:
    """ Prints a calendar's month view for a given year and month. """

    def __init__(self):
        self._year = datetime.datetime.today().year
        self._month = datetime.datetime.today().month
        self.week_start("mon")

    def year(self, year):
        """ Sets the year. Defaults to the current year. """
        self._year = year

    def month(self, month):
        """ Sets the month. Defaults to the current month."""

        # define the month names instead of using datetime.strptime which
        # will depend on the user's locale.
        month_to_number = {
            "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
            "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12
        }
        self._month = month_to_number[month.lower()]

    def week_start(self, start_day):
        """ Sets the start day of the week. Possible values are mon for Mondays
        and sun for Sundays. Defaults to mon. """
        if start_day.lower() == "mon":
            self._week_days = [0, 1, 2, 3, 4, 5, 6]
        elif start_day.lower() == "sun":
            self._week_days = [6, 0, 1, 2, 3, 4, 5]
        else:
            raise ValueError(
                "Only 'sun' or 'mon' are allowed as week start days")

    def build(self):
        """ Builds the month view. """
        r = []

        # month name + year, centered. The available width is 20.
        # Again, we don't use datetime.strftime to avoid tying our behavior
        # to the user's locale.
        month_names = ["January", "February", "March", "April", "May", "June",
                       "July", "August", "September", "October", "November", "December"]
        s = month_names[self._month-1] + " " + str(self._year)
        r.append(s.center(20))

        # Print the abbreviated day of the week names
        day_names = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
        line = [day_names[d] for d in self._week_days]
        r.append(" ".join(line))

        # Store the 1st of the month in day. The code will increment day by
        # one day until the month changes, at which point we'll be done.
        day = datetime.date(self._year, self._month, 1)

        line = []
        while self._week_days[len(line)] != day.weekday():
            # Add empty cells until we are on the correct day.
            line.append("  ")

        # Loop as long as the month doesn't change.
        while day.month == self._month:
            line.append(str(day.day).rjust(2))
            day = day + datetime.timedelta(days=1)
            if len(line) == 7:
                # We have recorded 7 entries
                r.append(" ".join(line))
                line = []

        # The last line is only included when it's not empty to avoid a trailing
        # empty line
        if line != []:
            r.append(" ".join(line))

        return "\n".join(r)

    def print(self):
        """ Prints the month view to stdout. """
        print(self.build())
