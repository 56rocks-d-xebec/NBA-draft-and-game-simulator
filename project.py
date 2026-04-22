import csv
import random as ran
from tabulate import tabulate
def main():
    print("""
   ________________________________________________________________________
  #                                                                        #
 |    🏀  W E L C O M E   T O   T H E   N B A   D R A F T   🏀              |
 |                                                                          |
 |  You will be playing against the SYSTEM in a draft of the century.       |
 |  (Technically 75 years, but well, that doesn't have quite the ring,      |
 |  does it? 🧐)                                                            |
 |                                                                          |
 |  Choose a player for every position from the Top 75 players of all time  |
 |  and see how your team fares against the great and legendary systems.    |
 |                                                                          |
 |  🥁 *DRUMROLLS*... AND LET THE DRAFT BEGIN!                              |
 |                                                                          |
 |  The first pick of every round has been graciously awarded to the USER.  |
 |                                                                          |
  #________________________________________________________________________#
    """)
    user_team,team_ovr,p_l,utp=get_team()
    s_team,steam_ovr,stp=system(p_l)
    final_box_score=winner(utp,stp)

    team_name = (input('enter team name : '))
    final_box_score=winner(utp,stp,team_name)
    avg_ovr=team_ovr/5
    print (f'''
Presenting to you the squad of {team_name}
*{user_team[0]}
*{user_team[1]}
*{user_team[2]}
*{user_team[3]}
and
*{user_team[4]}
team ovr : {team_ovr}
avg ovr :{avg_ovr:.2f}
''')
    print (f'''
Presenting to you the squad of the system
*{s_team[0]}
*{s_team[1]}
*{s_team[2]}
*{s_team[3]}
and
*{s_team[4]}
team ovr : {steam_ovr}
avg ovr :{(steam_ovr/5):.2f}
''')
    print(final_box_score)

def get_team():
    with open('dataset.csv') as ds:
        m_ds=csv.DictReader(ds)
        player_list=list(m_ds)
    user_team=[]
    team_ovr=0
    utp=[]

    for u_i in ['PG','SG','SF','PF','C']:
       player_pool =[]
       for u_pos in player_list :
           if u_pos['Pos']==u_i:
            player_pool.append(u_pos)
       while True :
               try:
                   player=name_getter((input(f'''
enter name of your {u_i}
(enter full names only no nick names)
{u_i} : ''')))
                   found = False
                   for p in player_pool:
                        if player == p['Name'] :
                            user_team.append(p['Name'])
                            team_ovr+= int(p['OVR'])
                            utp.append(p)
                            player_list.remove(p)
                            found=True
                            break
                        else :
                            continue

                   if found:
                       break
                   else :
                       print('player not found in dataset recheck position and spelling')


               except ValueError:
                    continue

    return user_team,team_ovr,player_list,utp
def name_getter(u_i):
    k=str(u_i).strip().title()
    return k
def system(k):
    ap=k
    mt=[]
    stp=[]
    team_ovr=0
    for u_i in ['PG','SG','SF','PF','C']:
       player_pool =[]
       for p in ap :
               if p['Pos']==u_i:
                   player_pool.append(p)

       if player_pool:
               sp=max(player_pool,key=lambda p:int(p['OVR']))
               mt.append(sp['Name'])
               team_ovr+=int(sp['OVR'])
               player_pool.remove(sp)
               stp.append(sp)

    return mt,int(team_ovr),stp

def winner(t1,t2,teamname='Player team'):
    class Player:
        def __init__ (self,name,ovr,pos,pt,tpt,spf,vbias):
            self.name= name
            self.ovr = ovr
            self.pos=pos
            self.pt=pt
            self.tpt=tpt
            self.spf=spf
            self.vbias=vbias
            self.score= 0
    team1=[]
    for p in t1:
        team1.append(Player(p['Name'],p['OVR'],p['Pos'],p['2pt'],p['3pt'],p['SPF'],p['VBias']))
    team2=[]
    for p in t2:
        team2.append(Player(p['Name'],p['OVR'],p['Pos'],p['2pt'],p['3pt'],p['SPF'],p['VBias']))
    up1,up2,up3,up4,up5=team1
    sp1,sp2,sp3,sp4,sp5=team2
    matchup=[(up1,sp1),(up2,sp2),(up3,sp3),(up4,sp4),(up5,sp5)]
    for _ in range(240+ran.randint(-25,25)):
        k=ran.choice(matchup)
        if int(_)%2==0 :
            p=k[0]
            seed=ran.random()
            if seed < float(p.spf):
                if ran.random()<float(p.vbias):
                    prob=float(p.tpt)
                    if ran.random()<prob:
                        p.score +=3
                else:
                    prob=float(p.pt)
                    if ran.random()<prob:
                        p.score+=2
        else:
            p=k[1]
            seed=ran.random()
            if seed < float(p.spf):
                if ran.random()<float(p.vbias):
                    prob=float(p.tpt)
                    if ran.random()<prob:
                        p.score +=3
                else:
                    prob=float(p.pt)
                    if ran.random()<prob:
                        p.score+=2
    teamscore2=int(sp1.score)+int(sp2.score)+int(sp3.score)+int(sp4.score)+int(sp5.score)

    teamscore1=int(up1.score)+int(up2.score)+int(up3.score)+int(up4.score)+int(up5.score)
    message=decide_winner(teamscore2,teamscore1)

    final_dict2=[[sp1.name,sp1.score],[sp2.name,sp2.score],[sp3.name,sp3.score],[sp4.name,sp4.score],[sp5.name,sp5.score],['Teamscore',teamscore1]]
    final_dict1=[[up1.name,up1.score],[up2.name,up2.score],[up3.name,up3.score],[up4.name,up4.score],[up5.name,up5.score],['Teamscore',teamscore2]]
    table_1= tabulate(final_dict1,headers=['Player','Score'],tablefmt='grid')
    table_2= tabulate(final_dict2,headers=['Player','Score'],tablefmt='grid')
    return f'''
{table_1}


{table_2}

{message}

'''
def decide_winner(t1,t2):
    diff=t1-t2

    if int(diff)>0:
        message=(f'congratulations player your team won by {diff} points')
    elif int(diff)==0:
        message=('the game is a tie')
    else:
        message= (f"better luck next time player the system's team won by {abs(diff)} points")

    return message

if __name__=="__main__":
    main()
