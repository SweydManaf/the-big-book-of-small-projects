from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from bagels_functions import Bagels


class MainApp:
    def __init__(self):
        self.root = Tk()

        # Import the tcl file
        self.root.tk.call('source', '../theme-to-tkinter/forest-light.tcl')

        # Set the theme with the theme_use method
        ttk.Style().theme_use('forest-light')

        # Set Windows configuration
        self.root.title('Bagels')

        self.width = 480
        self.height = 150
        self.sys_widht = int((self.root.winfo_screenwidth() / 2) - (self.width / 2))
        self.sys_height = int((self.root.winfo_screenheight() / 2) - (self.height / 2))

        self.root.geometry(f'{self.width}x{self.height}+{self.width}+{self.sys_height}')
        self.root.resizable(False, False)

        # Start program
        self.bagels = Bagels()
        self.info_game()
        self.widgets(self.root)
        self.draw_widgets()
        self.root.mainloop()

    def widgets(self, root):
        self.mainFrame = ttk.Frame(root)

        self.labelApp = ttk.Label(self.mainFrame, text='Bagels', font='Roboto 20')

        # self.restarButton = ttk.Button(self.mainFrame, text='R', style='Accent.TButton', width=10)
        # self.infoButton = ttk.Button(self.mainFrame, text='i', style='Accent.TButton', width=10)

        self.labelGuess = ttk.Label(self.mainFrame, text=f'Guess #{self.bagels.numGuesses}', font='14')
        self.validateGuess = self.mainFrame.register(self.validate_entry_guess)
        self.entryVar = StringVar()
        self.entryGuess = ttk.Entry(self.mainFrame, justify='center', textvariable=self.entryVar,
                                    validate='focusout', validatecommand=self.validate_entry_guess)
        self.entryGuess.bind('<Return>', lambda e: self.bind_enter())
        self.buttonGuess = ttk.Button(self.mainFrame, text='OK', style='Accent.TButton', command=self.input_guess)

        self.labelClues = ttk.Label(self.mainFrame, text='')

    def draw_widgets(self):
        self.mainFrame.grid(row=0, column=0)

        self.labelApp.grid(row=1, column=0, columnspan=3, padx=(30, 0), pady=10)
        # self.restarButton.grid(row=1, column=1)
        # self.infoButton.grid(row=1, column=2)

        self.labelGuess.grid(row=2, column=0, padx=(50, 10))
        self.entryGuess.grid(row=2, column=1)
        self.buttonGuess.grid(row=2, column=2, padx=(10, 0))

        self.labelClues.grid(row=3, column=0, columnspan=3, pady=(20, 0))

        self.entryGuess.focus()

    def info_game(self):
        messagebox.showinfo('About Game', 'In Bagels, a deductive logic game, you must guess a secret '
                                          'three-digit number based on clues. \n\nThe game offers one of '
                                          'the following hints in response to your guess: “Pico” when '
                                          'your guess has a correct digit in the wrong place, “Fermi” '
                                          'when your guess has a correct digit in the correct place, '
                                          'and “Bagels” if your guess has no correct digits. \nYou have '
                                          '10 tries to guess the secret number.')

    def input_guess(self, *args):
        self.bagels.guess = self.entryVar.get()
        self.labelClues['text'] = self.bagels.main_game()
        self.labelGuess['text'] = f'Guess #{self.bagels.numGuesses}'

        if self.validate_entry_guess():
            if self.bagels.win:
                messagebox.showinfo('Winner', 'You got it!')
                self.play_again()
            elif self.bagels.win == 0:
                messagebox.showinfo('Looser', f'You ran out of guesses.\nThe answer was {self.bagels.secretNum}.')
                self.play_again()
        else:
            messagebox.showerror('Invalid digit', 'You must insert a number or only 3 digits')
            self.entryVar.set('')
            self.entryGuess.focus()

    def bind_enter(self, *args):
        self.input_guess()

    def validate_entry_guess(self):
        if len(self.entryVar.get()) != self.bagels.NUM_DIGITS or not self.entryVar.get().isdecimal():
            return False
        else:
            return True

    def play_again(self):
        if messagebox.askyesno('Bagels', f'\nDo you want to try again?'):
            self.bagels.reset()
            self.entryVar.set('')
            self.labelClues['text'] = ''
            self.labelGuess['text'] = f'Guess #{self.bagels.numGuesses}'
            self.entryGuess.focus()

        else:
            self.root.destroy()

if __name__ == '__main__':
    MainApp()
