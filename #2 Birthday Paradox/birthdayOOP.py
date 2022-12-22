"""Birthday Paradox Simulation"""

import datetime
import random


class BirthdayParadox:
    def __init__(self, numOfBDays):
        self.MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
        self.numOfBDays = numOfBDays
        self.birthdays = self.get_birthdays()
        self.birthdaysText = self.get_month_of_birthdays()
        self.match = self.get_match(self.birthdays)

    def get_birthdays(self):
        """Return a list of a number random date objects for birthdays."""
        birthdays = []

        for i in range(self.numOfBDays):
            startOfYear = datetime.date(2022, 1, 1)

            # Get a random day into the year
            randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
            birthday = startOfYear + randomNumberOfDays
            birthdays.append(birthday)

        return birthdays

    def get_month_of_birthdays(self):
        dateText = []
        for i, birthday in enumerate(self.birthdays):
            monthName = self.MONTHS[birthday.month - 1]
            dateText.append(f'{monthName} {birthday.day}')

        return dateText

    def get_match(self, birthdays):
        """Returns the date of a birthday that occurs more than once in the birthdays list."""
        # Compare each birthday to every other birthday
        for a, birthdayA in enumerate(birthdays):
            for b, birthdayB in enumerate(birthdays[a + 1:]):
                if birthdayA == birthdayB:
                    return f'{self.MONTHS[birthdayA.month - 1]} {birthdayA.day}'  # Return the matching birthday

    def get_sim_match(self):
        simMatch = 0  # How many simulations had matching birthdays in them
        for i in range(100_000):
            # Report on the progress every 10.000 simulations:
            if i % 10_000 == 0:
                ...
            birthdays = self.get_birthdays()
            if self.get_match(birthdays) is not None:
                simMatch += 1

        # Display simulations results:
        probabilty = round(simMatch / 100_000 * 100, 1)

        return {'siMatch': simMatch, 'probabilty': probabilty}
