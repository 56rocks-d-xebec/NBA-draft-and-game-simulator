# NBA DRAFT and Game simulator
    #### Video Demo:https://youtu.be/v9N6kJzXA-4yes
    #### Description:
   Technical Implementation: The Draft & Simulation Engine
1. The Draft
The simulation begins with a draft (PG through C) where the player chooses a player among the top 75 players evenly distributed to 15 per position
the user is prompted until they enter a valid name for a given position and once the user team is set the players selected by the user are taken off the board now the system chooses the highest ovr players available at the given position to draft the counter team that can put up a fair fight.
2. The Data
Both the User and the System draw from a comprehensive dataset containing era-adjusted statistics then the program instantiates a Player Class that stores data like
Shot Frequency (SPF)which is the probability of a player taking a shot during a given possession. , 3-Point Bias (VBias) which is the likelihood of a player choosing a 3-pointer over a 2-pointer , and Accuracy Metrics: Era-adjusted 2PT and 3PT probabilities that normalize shooting efficiency across different eras of basketball history.

3. The Simulator
The game is simulated not by total score, but by individual possessions. Players are paired into tuples by position then the engine uses random.choice to select a matchup and random.random() to determine possession and shot outcomes based on the Player Class attributes.And to account for the chaos of a real game that has between high-speed fast break plays and slow and hard  defensive stands the total number of simulated plays is non-static, fluctuating within a statistically probable range.


