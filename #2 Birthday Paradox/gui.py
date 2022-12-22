from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from time import sleep

from birthdayOOP import BirthdayParadox


class MainApp:
    def __init__(self):
        self.root = Tk()

        # Import the tcl file
        self.root.tk.call('source', '../theme-to-tkinter/forest-light.tcl')

        # Set theme with the theme_use method
        ttk.Style().theme_use('forest-light')

        # Set Windows configuration
        self.root.title('Birthday Paradox')

        self.width = 780
        self.height = 350
        self.sys_width = int((self.root.winfo_screenwidth() / 2) - (self.width / 2))
        self.sys_height = int((self.root.winfo_screenheight() / 2) - (self.height / 2))
        self.root.geometry(f'{self.width}x{self.height}+{self.sys_width}+{self.sys_height}')
        self.root.resizable(False, False)

        # Building the UI
        # Frame where we will get input of user
        self.inputFrame = ttk.Frame(self.root, width=self.width / 2)

        self.labelNameAPP = ttk.Label(self.inputFrame, text='Paradoxo do Aniversário', font='Roboto 24',
                                      justify='center')

        self.labelBirthdays = ttk.Label(self.inputFrame, text='Quantos aniversários devo gerar? (MAX 100)')
        self.birthdayVar = StringVar(value='1')
        self.entryBirthdays = ttk.Spinbox(self.inputFrame, textvariable=self.birthdayVar, width=5,
                                          from_=1, to=100, wrap=True, justify='center')
        self.birthdayButton = ttk.Button(self.inputFrame, text='OK', style='Accent.TButton',
                                         command=self.show_the_results)

        self.verticalLine = ttk.Separator(self.root, orient=VERTICAL)

        # Frame where we will show the results
        self.paradoxFrame = ttk.Frame(self.root)
        self.labelMatchDate = ttk.Label(self.paradoxFrame, justify='center', font='lucida 11')
        self.labelGenerateMoreSimulation = ttk.Label(self.paradoxFrame, justify='center')
        self.labelShowSimMatch = ttk.Label(self.paradoxFrame, justify='center', font='lucida 11')
        self.buttonGenerateMoreSimulation = ttk.Button(self.paradoxFrame, text='Gerar', style='Accent.TButton',
                                                       command=self.generate_simulations)
        self.progressVar = IntVar()
        self.simulationProgress = ttk.Progressbar(self.paradoxFrame, orient=HORIZONTAL,
                                                  length=200, mode='determinate', maximum=100)

        # START THE PROGRAM
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        # Drawing the frame where we will get input of user
        self.inputFrame.place(x=1, y=1)

        self.labelNameAPP.grid(row=0, column=0, columnspan=2, pady=(90, 20), padx=(30, 30))

        self.labelBirthdays.grid(row=1, column=0, columnspan=2, pady=(0, 10), padx=(0, 0))
        self.entryBirthdays.grid(row=2, column=0, columnspan=1, pady=(0, 0), padx=(30, 0))
        self.birthdayButton.grid(row=2, column=0, columnspan=2, pady=(0, 0), padx=(120, 0))

        self.verticalLine.place(x=self.width/2, y=0, height=self.height)

        # Frame where we will show the results
        self.paradoxFrame.place(x=self.width / 2 + 20, y=1)

        # Give focus to main object
        self.entryBirthdays.icursor(END)
        self.entryBirthdays.focus()

    def show_the_results(self):
        # Reset progress bar
        self.simulationProgress['value'] = 0

        # Get number of birthdays
        numOfBirthdays = self.get_num_of_birthdays()
        if numOfBirthdays is not None:
            # Call draw results if it's possible to calculate
            self.birthdayParadox = BirthdayParadox(numOfBirthdays)
            self.forget_widgets_to_show_the_results()
            self.draw_the_results()

    def forget_widgets_to_show_the_results(self):
        # Forget widgets of results frame
        self.labelGenerateMoreSimulation.grid_forget()
        self.labelShowSimMatch.grid_forget()
        self.labelMatchDate.grid_forget()
        self.simulationProgress.grid_forget()
        self.buttonGenerateMoreSimulation.grid_forget()

    def get_num_of_birthdays(self):
        response = self.birthdayVar.get()
        if response.isdecimal() and (0 < int(response) <= 100):
            numBDays = int(response)
            return numBDays
        else:
            messagebox.showerror('Valor inválido', 'Por favor insira um valor entre 0 e 100')
            return None

    def get_dates_of_birthday(self):
        DatesOfBirthdays = []
        for i, dates in enumerate(self.birthdayParadox.birthdaysText):
            DatesOfBirthdays.append(f'{dates}; ')
            if i % 10 == 0 and i != 0:
                DatesOfBirthdays.append('\n')
        return DatesOfBirthdays

    def messagebox_about_the_dates(self, datesOfBirthdays):
        messagebox.showinfo('Aniversários gerados',
                            f'Aqui estão {self.birthdayParadox.numOfBDays} aniversários: \n\n' + ''.join(
                                datesOfBirthdays))

    def draw_widgets_after_results(self):
        self.labelMatchDate.grid(row=1, column=0, columnspan=2, padx=(10, 0), pady=(80, 5))
        self.labelGenerateMoreSimulation.grid(row=3, column=0, columnspan=2, padx=(0, 0), pady=(5, 5))
        self.simulationProgress.grid(row=4, column=0, columnspan=2, ipady=10)
        self.buttonGenerateMoreSimulation.grid(row=5, column=0, columnspan=2, padx=(10, 0), pady=(20, 2))

    def draw_the_results(self):
        DatesOfBirthdays = self.get_dates_of_birthday()

        self.messagebox_about_the_dates(DatesOfBirthdays)

        if self.birthdayParadox.match is not None:
            self.labelMatchDate[
                'text'] = f'Nesta simulação muitas pessoas \ntem o seu aniversário ' \
                          f'em {self.birthdayParadox.match}. '
        else:
            self.labelMatchDate[
                'text'] = 'Nesta simulação não foram encontradas \npessoas com a mesma data de aniversário.'

        self.labelGenerateMoreSimulation[
            'text'] = f'Deseja simular {self.birthdayParadox.numOfBDays} aniversários 100.000 vezes?'

        self.draw_widgets_after_results()

    def calculate_match_birthdays(self):
        simMatch = 0  # How many simulations had matching birthdays in them
        for i in range(100_000 + 1):
            # Report on the progress every 10.000 simulations:
            if i % 10_000 == 0:
                self.simulationProgress['value'] = int(i / 10_00)
                self.simulationProgress.update()
            birthdays = self.birthdayParadox.get_birthdays()
            if self.birthdayParadox.get_match(birthdays) is not None:
                simMatch += 1

        # Display simulations results:
        probabilty = round(simMatch / 100_000 * 100, 1)

        return {'siMatch': simMatch, 'probabilty': probabilty}

    def generate_simulations(self, *args):
        # Display simulations results:
        simMatch = self.calculate_match_birthdays()
        self.labelShowSimMatch.grid(row=2, column=0, columnspan=2)

        self.labelShowSimMatch['text'] = f'Em 100.000 simulações de {self.birthdayParadox.numOfBDays} pessoas,' \
                                         f'\nhouve um aniversário correspondete \nnesse grupo {simMatch["siMatch"]} vezes. ' \
                                         f'\nIsso significa que {self.birthdayParadox.numOfBDays} pessoas' \
                                         f' têm {simMatch["probabilty"]}%\n de chance de ter um aniversário \nigual em seu grupo.' \
                                         f'\n\nBIZZARO NEM!'

        # Sleep 2 seconds until forget the generates widgets
        sleep(0.5)
        self.labelGenerateMoreSimulation.grid_forget()
        self.buttonGenerateMoreSimulation.grid_forget()
        self.simulationProgress.grid_forget()


if __name__ == '__main__':
    MainApp()
