import csv


def main():
    file_name = 'players_1.csv'
    with open(file_name, 'rt') as file_in:
        csv_in = csv.DictReader(file_in)
        players = [row for row in csv_in]

        print(players)

        for player in players:
            for key, value in player.items():
                print(f'{key}: {value}')
            print()


if __name__ == '__main__':
    main()
