import csv
from guizero import *


def main():
    def get_csv_data():

        file_name = tbx_csv_file.value

        with open(file_name, 'rt') as file_in:
            csv_in = csv.DictReader(file_in)
            players_ = [row for row in csv_in]
            show_data(players_)

    def show_data(players):
        for player in players:
            for key, value in player.items():
                lbx_data.append(value)

    # Build the form
    app = App()
    app.text_size = 14

    Text(app, text='Enter data file name')
    tbx_csv_file = TextBox(app, width=20)
    PushButton(app, text='load data file', command=get_csv_data)
    lbx_data = ListBox(app, width=350, height=200)

    app.display()


if __name__ == '__main__':
    main()
