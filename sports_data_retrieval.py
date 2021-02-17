import json

def lambda_handler(event, log): # TODO implement
    sport = event['Sport']
    user_team = event['Team']

    if(sport == 'Ncaaf'):
        response1 = ncaaf_action(user_team)
        return{'response1': response1}
    elif(sport == "Nhl"):
        response2 = nhl_action(user_team)
        return{'response2': response2}
    elif(sport == 'Mlb'):
        response3 = mlb_action(user_team)
        return{'response3': response3}
    else:
        response4 = "SPORT NOT FOUND\nPlease choose from one of the following sports:\nNCAAF\nNHL\nMLB"

        return {'response 4': response4}


#######    
def ncaaf_action(user_team):
    with open('ncaaf.json') as data_file:
        data = json.load(data_file)
        if (user_team == 'Penn State'):
            game_one = data['Penn State']['Game One']
            game_two = data['Penn State']['Game 2']
            game_three = data['Penn State']['Game 3']
            game_four = data['Penn State']['Game 4']
            game_five = data['Penn State']['Game 5']
            return {
                'statusCode': 200,
                'body': json.dumps('Here is your data'),
                "Game FIVE ago: ": game_five,
                "Game FOUR ago; ": game_four,
                "Game THREE ago: ": game_three,
                "Game TWO ago: ": game_two,
                "Last Game: ": game_one
            }
        elif (user_team == 'Morehead State'):
            game_one = data['Morehead State']['Game One']
            game_two = data['Morehead State']['Game 2']
            game_three = data['Morehead State']['Game 3']
            game_four = data['Morehead State']['Game 4']
            game_five = data['Morehead State']['Game 5']
            return {
                'statusCode': 200,
                'body': json.dumps('Here is your data'),
                "Game FIVE ago: ": game_five,
                "Game FOUR ago; ": game_four,
                "Game THREE ago: ": game_three,
                "Game TWO ago: ": game_two,
                "Last Game: ": game_one
            }
        elif (user_team == 'Marshall University'):
            game_one = data['Marshall University']['Game One']
            game_two = data['Marshall University']['Game 2']
            game_three = data['Marshall University']['Game 3']
            game_four = data['Marshall University']['Game 4']
            game_five = data['Marshall University']['Game 5']
            return{
                'statusCode': 200,
                'body': json.dumps('Here is your data:'),
                "\nGame FIVE ago: ": game_five,
                "\nGame FOUR ago; ": game_four,
                "\nGame THREE ago: ": game_three,
                "\nGame TWO ago: ": game_two,
                "\nLast Game: ": game_one
            }
        else: 
            response4 = "TEAM NOT FOUND\nPlease choose from one of the following teams:\nPenn State\nMorehead State\nMarshall University"
    
            return {'response 4': response4}


#####
def nhl_action(user_team):
    with open('nhl.json') as data_file:
        data = json.load(data_file)
        if (user_team == 'Boston Bruins'):
            game_one = data['Boston Bruins']["Game One"]
            game_two = data['Boston Bruins']["Game 2"]
            game_three = data['Boston Bruins']["Game 3"]
            game_four = data['Boston Bruins']["Game 4"]
            game_five = data['Boston Bruins']["Game 5"]
            return{
                'statusCode': 200,
                'body': json.dumps('Here is your data'),
                "Game FIVE ago: ": game_five,
                "Game FOUR ago; ": game_four,
                "Game THREE ago: ": game_three,
                "Game TWO ago: ": game_two,
                "Last Game: ": game_one
            }
        elif (user_team == 'Carolina Hurricanes'):
            game_one = data['Carolina Hurricanes']["Game One"]
            game_two = data['Carolina Hurricanes']["Game 2"]
            game_three = data['Carolina Hurricanes']["Game 3"]
            game_four = data['Carolina Hurricanes']["Game 4"]
            game_five = data['Carolina Hurricanes']["Game 5"]
            return{
                'statusCode': 200,
                'body': json.dumps('Here is your data'),
                "Game FIVE ago: ": game_five,
                "Game FOUR ago; ": game_four,
                "Game THREE ago: ": game_three,
                "Game TWO ago: ": game_two,
                "Last Game: ": game_one
            }
        elif (user_team == 'Edmonton Oilers'):
            game_one = data['Edmonton Oilers']["Game One"]
            game_two = data['Edmonton Oilers']["Game 2"]
            game_three = data['Edmonton Oilers']["Game 3"]
            game_four = data['Edmonton Oilers']["Game 4"]
            game_five = data['Edmonton Oilers']["Game 5"]
            return{
                'statusCode': 200,
                'body': json.dumps('Here is your data'),
                "Game FIVE ago: ": game_five,
                "Game FOUR ago; ": game_four,
                "Game THREE ago: ": game_three,
                "Game TWO ago: ": game_two,
                "Last Game: ": game_one
            }
        else: 
            response4 = "TEAM NOT FOUND\nPlease choose from one of the following teams:\nBoston Bruins\nCarolina Hurricanes\nEdmonton Oilers"
    
            return {'response 4': response4}



#####
def mlb_action(user_team):
    with open('mlb.json') as data_file:
        data = json.load(data_file)
        if (user_team == 'Boston Red Sox'):
            game_one = data['Boston Red Sox']["Game One"]
            game_two = data['Boston Red Sox']["Game 2"]
            game_three = data['Boston Red Sox']["Game 3"]
            game_four = data['Boston Red Sox']["Game 4"]
            game_five = data['Boston Red Sox']["Game 5"]
            return{
                'statusCode': 200,
                'body': json.dumps('Here is your data'),
                "Game FIVE ago: ": game_five,
                "Game FOUR ago; ": game_four,
                "Game THREE ago: ": game_three,
                "Game TWO ago: ": game_two,
                "Last Game: ": game_one
            }
        elif (user_team == 'La Dodgers'):
            game_one = data['La Dodgers']["Game One"]
            game_two = data['La Dodgers']["Game 2"]
            game_three = data['La Dodgers']["Game 3"]
            game_four = data['La Dodgers']["Game 4"]
            game_five = data['La Dodgers']["Game 5"]
            return{
                'statusCode': 200,
                'body': json.dumps('Here is your data'),
                "Game FIVE ago: ": game_five,
                "Game FOUR ago; ": game_four,
                "Game THREE ago: ": game_three,
                "Game TWO ago: ": game_two,
                "Last Game: ": game_one
            }
        elif (user_team == 'Pittsburg Pirates'):
            game_one = data['Pittsburg Pirates']["Game One"]
            game_two = data['Pittsburg Pirates']["Game 2"]
            game_three = data['Pittsburg Pirates']["Game 3"]
            game_four = data['Pittsburg Pirates']["Game 4"]
            game_five = data['Pittsburg Pirates']["Game 5"]
            return{
                'statusCode': 200,
                'body': json.dumps('Here is your data'),
                "Game FIVE ago: ": game_five,
                "Game FOUR ago; ": game_four,
                "Game THREE ago: ": game_three,
                "Game TWO ago: ": game_two,
                "Last Game: ": game_one
            }
        else: 
            response4 = "TEAM NOT FOUND\nPlease choose from one of the following teams:\nBoston Red Sox\nLA Dodgers\nPittsburg Pirates"
    
            return {'response 4': response4}


