import mysql.connector as mysql
import matplotlib.pyplot as plt
import numpy as np

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="capstone2021",
    database="NFLStatKing"
)
cursor = db.cursor()


#generateSite()      Brandon
    #generateIndexPage()  Brandon
    #for each team                      Hunter
        #generateTeamPage(team)  AJ
        #generateCharts(team)     AJ

nflTeams = ['ARI', 'ATL', 'BAL', 'BUF', 'CAR', 'CHI', 'CIN', 'CLE', 'DAL', 'DEN', 'DET', 'GB', 'HOU', 'IND', 'JAX',
           'KC', 'LV', 'LAC', 'LA', 'MIA', 'MIN', 'NE', 'NO', 'NYG', 'NYJ', 'PHI', 'PIT', 'SF', 'SEA', 'TB', 'TEN',          'WAS']

#nflTeams = ['PIT']


#Offensive Functions

def formationTendencies(offensiveTeam):
    formationQuery = """SELECT DISTINCT
        (SELECT COUNT(*) FROM PlayByPlay2020 WHERE OffenseTeam=%s && Formation='SHOTGUN') as shotgunCount,   
        (SELECT COUNT(*) FROM PlayByPlay2020 WHERE OffenseTeam=%s && Formation='UNDER CENTER') as underCenterCount,
        (SELECT COUNT(*) FROM PlayByPlay2020 WHERE OffenseTeam=%s && Formation='NO HUDDLE SHOTGUN') 
            as noHuddleShotgunCount,
        (SELECT COUNT(*) FROM PlayByPlay2020 WHERE OffenseTeam=%s && Formation='PUNT') as puntCount,
        (SELECT COUNT(*) FROM PlayByPlay2020 WHERE OffenseTeam=%s && Formation='NO HUDDLE') as noHuddleCount
        FROM PlayByPlay2020"""
    tuple1 = (offensiveTeam,) * 5
    cursor.execute(formationQuery, tuple1)
    records = list(cursor.fetchall())
    fig = plt.figure()
    formations = ['Shotgun', 'Under Center', 'No Huddle Shotgun', 'Punt', 'No Huddle']
    plt.bar(formations, records[0])
    plt.title( f"{offensiveTeam} Offensive Formations")
    plt.xticks(size=7)
    plt.yticks(size=7)
    return fig


def rushDirection(offensiveTeam):
    rushDirectionQuery = """SELECT DISTINCT
        (SELECT COUNT(*) FROM PlayByPlay2020 WHERE OffenseTeam=%s && RushDirection='LEFT TACKLE') as leftTackleCount,   
        (SELECT COUNT(*) FROM PlayByPlay2020 WHERE OffenseTeam=%s && RushDirection='LEFT GUARD') as leftGuardCount,
        (SELECT COUNT(*) FROM PlayByPlay2020 WHERE OffenseTeam=%s && RushDirection='LEFT END') as leftEndCount,   
        (SELECT COUNT(*) FROM PlayByPlay2020 WHERE OffenseTeam=%s && RushDirection='CENTER') as centerCount,
        (SELECT COUNT(*) FROM PlayByPlay2020 WHERE OffenseTeam=%s && RushDirection='RIGHT GUARD') as rightGuardCount,   
        (SELECT COUNT(*) FROM PlayByPlay2020 WHERE OffenseTeam=%s && RushDirection='RIGHT TACKLE') as rightTackleCount,
        (SELECT COUNT(*) FROM PlayByPlay2020 WHERE OffenseTeam=%s && RushDirection='RIGHT END') as rightEndCount   
        FROM PlayByPlay2020"""
    tuple1 = (offensiveTeam,) * 7
    cursor.execute(rushDirectionQuery, tuple1)
    records = list(cursor.fetchall())
    fig = plt.figure()
    rushDirections = ['LEFT END', 'LEFT TACKLE', 'LEFT GUARD', 'CENTER', 'RIGHT GUARD', 'RIGHT TACKLE', 'RIGHT END']
    plt.bar(rushDirections, records[0])
    plt.title(f"{offensiveTeam} Rushing Directions")
    plt.xticks(size=6)
    plt.yticks(size=6)
    return fig


def passType(offensiveTeam):
    shortPassQuery = """SELECT DISTINCT
        (SELECT COUNT(*) FROM PlayByPlay2020 WHERE OffenseTeam=%s && PassType='SHORT LEFT') as shortLeftCount,   
        (SELECT COUNT(*) FROM PlayByPlay2020 WHERE OffenseTeam=%s && PassType='SHORT MIDDLE') as shortMiddleCount,   
        (SELECT COUNT(*) FROM PlayByPlay2020 WHERE OffenseTeam=%s && PassType='SHORT RIGHT') as shortRightCount   
        FROM PlayByPlay2020"""
    deepPassQuery = """SELECT DISTINCT
        (SELECT COUNT(*) FROM PlayByPlay2020 WHERE OffenseTeam=%s && PassType='DEEP LEFT') as deepLeftCount,
        (SELECT COUNT(*) FROM PlayByPlay2020 WHERE OffenseTeam=%s && PassType='DEEP MIDDLE') as deepMiddleCount,
        (SELECT COUNT(*) FROM PlayByPlay2020 WHERE OffenseTeam=%s && PassType='DEEP RIGHT') as deepRightCount
        From PlayByPlay2020"""
    tuple1 = (offensiveTeam,) * 3
    cursor.execute(shortPassQuery, tuple1)
    records1 = list(cursor.fetchall())
    cursor.execute(deepPassQuery, tuple1)
    records2 = list(cursor.fetchall())
    fig = plt.figure()
    w = 0.4
    passDirections = ['LEFT', 'MIDDLE', 'RIGHT']
    shortBar = np.arange(len(passDirections))
    deepBar = [i+w for i in shortBar]
    plt.bar(shortBar, records1[0], w, label="SHORT")
    plt.bar(deepBar, records2[0], w, label="DEEP")
    plt.title(f"{offensiveTeam} Pass Type Tendencies")
    plt.xticks(shortBar+w/2, passDirections, size=6)
    plt.yticks(size=6)
    plt.legend()
    return fig


def passVsRun(offensiveTeam):
    passVsRunQuery = """SELECT DISTINCT
        (SELECT COUNT(*) FROM PlayByPlay2020 WHERE OffenseTeam=%s && PlayType='PASS') as passCount,   
        (SELECT COUNT(*) FROM PlayByPlay2020 WHERE OffenseTeam=%s && PlayType='RUSH') as rushCount   
        FROM PlayByPlay2020"""
    tuple1 = (offensiveTeam,) * 2
    cursor.execute(passVsRunQuery, tuple1)
    records = list(cursor.fetchall())
    rushDirections = ['PASS', 'RUSH']
    fig, ax1 = plt.subplots()
    ax1.pie(records[0], labels=rushDirections, autopct='%.2f', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title(f"{offensiveTeam} Pass vs Rush")
    return fig

'''
def qbCompletions():
    qbCompletionsQuery = """SELECT DISTINCT
        (SELECT SUBSTRING(DESCRIPTION, 3, 6) FROM PlayByPlay2020 WHERE OffenseTeam='PIT' && PlayType='PASS') as passer,   
        (SELECT SUBSTRING(DESCRIPTION, 3, 6) FROM PlayByPlay2020 WHERE OffenseTeam='PIT' && PlayType='RUSH') as rusher   
        FROM PlayByPlay2020"""
    cursor.execute(qbCompletionsQuery)
    records = list(cursor.fetchall())
    for record in records[0]:
        print(record)
'''
'''
    tuple1 = (offensiveTeam,) * 2
    rushDirections = ['PASS', 'RUSH']
    fig, ax1 = plt.subplots()
    ax1.pie(records[0], labels=rushDirections, autopct='%.2f', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title(f"{offensiveTeam} Pass vs Rush")
    return fig
    '''

#Defensive Functions

def defPassType(defensiveTeam):
    defPassTypeQuery = """SELECT DISTINCT
        (SELECT COUNT(*) FROM PlayByPlay2020 WHERE OffenseTeam=%s && PassType='SHORT LEFT') as shortLeftCount,  
        (SELECT COUNT(*) FROM PlayByPlay2020 WHERE OffenseTeam=%s && PassType='DEEP LEFT') as deepLeftCount, 
        (SELECT COUNT(*) FROM PlayByPlay2020 WHERE OffenseTeam=%s && PassType='SHORT MIDDLE') as shortMiddleCount,
        (SELECT COUNT(*) FROM PlayByPlay2020 WHERE OffenseTeam=%s && PassType='DEEP MIDDLE') as deepMiddleCount,   
        (SELECT COUNT(*) FROM PlayByPlay2020 WHERE OffenseTeam=%s && PassType='SHORT RIGHT') as shortRightCount,   
        (SELECT COUNT(*) FROM PlayByPlay2020 WHERE OffenseTeam=%s && PassType='DEEP RIGHT') as deepRightCount 
        FROM PlayByPlay2020"""
    tuple1 = (defensiveTeam,) * 6
    cursor.execute(defPassTypeQuery, tuple1)
    records = list(cursor.fetchall())
    fig = plt.figure()
    passDirections = ['SHORT LEFT', 'DEEP LEFT', 'SHORT MIDDLE', 'DEEP MIDDLE', 'SHORT RIGHT', 'DEEP RIGHT']
    plt.bar(passDirections, records[0])
    plt.title(f"Pass Directions vs {defensiveTeam} Defense")
    plt.xticks(size=6)
    plt.yticks(size=6)
    return fig

def defRushDirection(defensiveTeam):
    rushDirectionQuery = """SELECT DISTINCT
        (SELECT COUNT(*) FROM PlayByPlay2020 WHERE DefenseTeam=%s && RushDirection='LEFT TACKLE') as leftTackleCount,   
        (SELECT COUNT(*) FROM PlayByPlay2020 WHERE DefenseTeam=%s && RushDirection='LEFT GUARD') as leftGuardCount,
        (SELECT COUNT(*) FROM PlayByPlay2020 WHERE DefenseTeam=%s && RushDirection='LEFT END') as leftEndCount,   
        (SELECT COUNT(*) FROM PlayByPlay2020 WHERE DefenseTeam=%s && RushDirection='CENTER') as centerCount,
        (SELECT COUNT(*) FROM PlayByPlay2020 WHERE DefenseTeam=%s && RushDirection='RIGHT GUARD') as rightGuardCount,   
        (SELECT COUNT(*) FROM PlayByPlay2020 WHERE DefenseTeam=%s && RushDirection='RIGHT TACKLE') as rightTackleCount,
        (SELECT COUNT(*) FROM PlayByPlay2020 WHERE DefenseTeam=%s && RushDirection='RIGHT END') as rightEndCount   
        FROM PlayByPlay2020"""
    tuple1 = (defensiveTeam,) * 7
    cursor.execute(rushDirectionQuery, tuple1)
    records = list(cursor.fetchall())
    fig = plt.figure()
    rushDirections = ['LEFT END', 'LEFT TACKLE', 'LEFT GUARD', 'CENTER', 'RIGHT GUARD', 'RIGHT TACKLE', 'RIGHT END']
    plt.bar(rushDirections, records[0])
    plt.title(f"Rush Directions vs {defensiveTeam} Defense")
    plt.xticks(size=6)
    plt.yticks(size=6)
    return fig






def genTeamPage(fileName, nflTeam):
    htmlFile = open(fileName, "w")
    htmlFile.write(
        f"""

<html>
    <title>NFL StatKing Team Page</title>
    <link rel="stylesheet" type="text/css" href="{{{{ url_for('static', filename='teamCSS.css') }}}}" />
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
	<script type="text/javascript" src="{{{{ url_for('static', filename='jquery.js') }}}}"></script>
</head>
  <body>
    <div id="container">
      <div id="header">
        <img src="https://media.discordapp.net/attachments/801569540478599168/819424695803838534/b8e73c30-b638-4ded-a6c8-4b83f6b29104_200x200.png" alt="Stat King Logo" width="150" height="100" class="w3-display-topleft">
        <h1>NFL Stat King</h1>
      </div>
      <div id="content">
        <div id="nav">
          <h3>Account Information</h3>
          <ul class="w3-ul w3-hoverable w3-large">
            <li class="w3-center"><img src="http://s3.amazonaws.com/37assets/svn/765-default-avatar.png" style="height:90px;  border-radius: 50%;"></li>
            <li><a href="{{{{ url_for('index') }}}}">Home</a></li>
			<li><a href="{{{{ url_for('teamPage') }}}}">Teams</a></li>
            <li><a href="{{{{ url_for('teamComparison') }}}}">Team Comparisons</a></li>
			<li><a href="">Players</a></li>
			<li><a href="{{{{ url_for('home') }}}}">Log Out</a></li>
			<li><a href="">About</a></li>
          </ul>
        </div>
                          
                          
                          
                          <div class="button_grp">
			<ul>
		 <li data-li="all" class="btn active">All</li>
                                         <li data-li="Offense" class="btn">Offense</li>
        <li data-li="Defense" class="btn">Defense</li>
			</ul>
		</div>
                          <div class="item_grp">
 
    <div class="item Offense">
    <div class="name"> {nflTeam} Offensive Formations
        </div>
	                 <p><img src="{{{{url_for('static',filename='{nflTeam}_Formation.svg')}}}}"></img></p>
			</div>
 
    <div class="item Offense">
    <div class="name"> {nflTeam} Rushing Directions
        </div>
      <p><img src="{{{{url_for('static',filename='{nflTeam}_Rush.svg')}}}}"></img></p>
			</div>

 
    <div class="item Offense">
    <div class="name"> {nflTeam} Pass vs Run
        </div>
      <p><img src="{{{{url_for('static',filename='{nflTeam}_PassVsRun.svg')}}}}"></img></p>
			</div>                                                      

    <div class="item Offense">
    <div class="name"> {nflTeam} Pass Type Tendencies
        </div>
      <p><img src="{{{{url_for('static',filename='{nflTeam}_PassType.svg')}}}}"></img></p>
			</div>
    
    <div class="item Defense">
    <div class="name"> Pass Directions vs {nflTeam}s Defense
        </div>
      <p><img src="{{{{url_for('static',filename='{nflTeam}_DefPassType.svg')}}}}"></img></p>
			</div>

    <div class="item Defense">
    <div class="name"> Rush Directions vs {nflTeam}s Defense
        </div>
      <p><img src="{{{{url_for('static',filename='{nflTeam}_DefRushDirection.svg')}}}}"></img></p>
			</div>
                       <script>
              $(".btn").click(function(){{
	var attr = $(this).attr("data-li");

	$(".btn").removeClass("active");
	$(this).addClass("active");

	$(".item").hide();
	
	if(attr == "Offense"){{
		$("." + attr).show();
}}
else if(attr == "Defense"){{
		$("." + attr).show();
}}
	else{{
			$(".item").show();
		}}
	}});
            </script>                                    
            </body>
        </html>""")
    htmlFile.close() 


def main():
    for nflTeam in nflTeams:
        print(nflTeam)
        genTeamPage(f"{nflTeam}.html", nflTeam)
        formationTendencies(nflTeam).savefig(f"{nflTeam}_Formation.svg", format='svg')
        rushDirection(nflTeam).savefig(f"{nflTeam}_Rush.svg", format='svg')
        passVsRun(nflTeam).savefig(f"{nflTeam}_PassVsRun.svg", format='svg')
        passType(nflTeam).savefig(f"{nflTeam}_PassType.svg", format='svg')
        defPassType(nflTeam).savefig(f"{nflTeam}_DefPassType.svg", format='svg')
        defRushDirection(nflTeam).savefig(f"{nflTeam}_DefRushDirection.svg", format='svg')

main()