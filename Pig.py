import random

"""
Our first exercise is to simulate a single turn of Pig where a player rolls until a 1 (“pig”) is rolled, or the turn total is greater than or equal to 20. 
We will call this strategy Hold-at-20. The user doesn't need to make any choices, the computer will roll automagically, following the hold-at-20 strategy.

For each roll, print a line with “Roll:” and the random die roll value (1-6).

After a “pig” roll of 1, or a “hold,” print a line with “Turn total:”
followed by the turn total. In the case of a “pig,” this turn total is 0

Roll: 4
Roll: 5
Roll: 6
Roll: 5
Turn total: 20
...
Roll: 3
Roll: 1
Turn total: 0

"""

def rolld6():
    return random.randint(1,6)


def holdAt20Turn():
    turnTotal = 0
    while turnTotal < 20:
        points = rolld6()
        #print("Roll:",points)
        if points == 1:
            turnTotal = 0
            break
        else:
            turnTotal += points
    #print("Turn total:",turnTotal)
    return turnTotal

"""
Simulate a given number of hold-at-20 turns, and report the estimated probabilities of the possible scoring outcomes.

How many Hold-at-20 turn simulations?
1000000
Score Estimated Probability
0 0.624076
20 0.099659
21 0.095310
22 0.074086
23 0.054599
24 0.035313
25 0.016957
"""


def holdAt20Sim(trials):
    results  = {} 
    for _ in range(trials):
        turnTotal = holdAt20Turn()
        if turnTotal in results:
            results[turnTotal] += 1
        else: 
            results[turnTotal]  = 1 
    for score in results:
        results[score] = results[score]/trials
    return results


results =  holdAt20Sim(1000)
print("Score\tEstimated Probability")
for score in sorted(results):
    print(score,results[score],sep="\t")



def holdAt20(limit=20):
    turnTotal = 0
    while turnTotal < limit:
        roll = random.randint(1,6)
        #print("Roll:", roll)
        if roll == 1:
            turnTotal = 0
            #print("Turn Total:", turnTotal)
            return turnTotal
        else:
            turnTotal += roll
    #print("Turn Total:", turnTotal)
    return turnTotal

def holdAt20Outcomes(trials):
    outcomes = {0:0}
    for val in range(20,26):
        outcomes[val] = 0
    for _ in range(trials):
        score = holdAt20()
        outcomes[score] += 1
    for score in outcomes:
        print(score, outcomes[score]/trials)


# 20 21 22 23 24 25
# 42 43 44 45 46 47


def holdAtXOutcomes(limit,trials):
    outcomes = {0:0}
    for score in range(limit, limit+6):
        outcomes[score] = 0
    for _ in range(trials):
        score = holdAt20(limit) 
        outcomes[score] += 1
    for score in outcomes:
        print(score, outcomes[score]/trials)

#holdAtXOutcomes(100,100000)


def holdAt20OrGoal(player, score):
    turnTotal = 0
    while turnTotal < 20 and turnTotal + score < 100:
        roll = rolld6()
        print(f"Roll: {roll}")
        if roll == 1:
            print(f"Turn total: 0 \n New score: {score}")
            return 0, score
        else:
            turnTotal += roll
            if player == 1:
                print(f"Turn total: {turnTotal} \n Roll/Hold? ", end="")
                action = input()
                if action.lower() == 'h':
                    print(f"Turn total: {turnTotal}\nNew score: {score + turnTotal}")
                    return turnTotal, score + turnTotal
            else:
                print(f"Turn total: {turnTotal}")
    print(f"Turn total: {turnTotal} \n New score: {score + turnTotal}")
    return turnTotal, score + turnTotal


def pigGame():
    player = random.randint(1, 2)
    print(f"You will be player {player}.")
    print("Enter nothing to roll; enter anything to hold.")
   
    scores = {1: 0, 2: 0}
   
    while True:
        print(f"Player 1 score: {scores[1]} \n Player 2 score: {scores[2]}")
        print(f"It is player {player}'s turn.")

        if player == 1:
            turnTotal, newScore = holdAt20OrGoal(player,scores[player])
            scores[player] = newScore
            player = 3 - player 
        else:
            input()
            turnTotal, newScore = holdAt20OrGoal(player,scores[player])
            scores[player] = newScore
            player = 3 - player
        if newScore >= 100:
            print(f"player {player} wins!")
            break

if __name__ == "__main__":
    pigGame()



