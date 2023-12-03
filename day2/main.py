file1 = open('input.txt', 'r')
lines = file1.readlines()

sum = 0
for line in lines:
    red_count = -1
    green_count = -1
    blue_count = -1
    splitted_line = line.strip().split(":")
    game_number = int(splitted_line[0].split(" ")[1])
    current_game = splitted_line[1]
    sub_games = current_game.split(";")
    for x in range(len(sub_games)):
        curr_sub_game = sub_games[x].strip()
        ball_count = curr_sub_game.split(",")
        for j in range(len(ball_count)):
            ball_number = int(ball_count[j].strip().split(" ")[0])
            ball_color = ball_count[j].strip().split(" ")[1]
            # print(ball_color, ball_number)
            if ball_color == "red":
                red_count = max(red_count, ball_number)
            elif ball_color == "green":
                green_count = max(green_count, ball_number)
            else:
                blue_count = max(blue_count, ball_number)
    if (red_count <= 12 and green_count<=13 and blue_count <=14):
        print("game:", game_number)
        sum = sum + game_number



print(sum)

