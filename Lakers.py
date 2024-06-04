#docstring- Jayden Zheng -Lakers_2023_24 database application
#imports
import sqlite3

#contants and varibles
DATABASE="/Users/jaydenzheng/Desktop/Database.db"



#1.functions
def print_all_Lakers():
    '''print all the Lakers nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
   
    #Lakers_Player
    sql= "SELECT * FROM Lakers_Player_2023_24;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results first
    print(f"Name                 Position     Jersey_number    Age     Salary_million")
    for Player in results:
        print(f"{Player[1]:<20} {Player[2]:<12} {Player[3]:<16} {Player[4]:<7} {Player[5]:<4}")
    print()
     
    #Lakers_Player_attendance
    sql= "SELECT * FROM Lakers_Player_Attendance_2023_24;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results first
    print(f"Player_id       Present_count   Absent_count    Injured_count")
    for Attendance in results:
        print(f"{Attendance[1]:<15} {Attendance[2]:<15} {Attendance[3]:<15} {Attendance[4]:<4}")
    print()
    
    #Lakers_Player_average_stats
    sql= "SELECT * FROM Lakers_Player_Average_Stats_2023_24;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results first
    print(f"Player_id    Minutes_per_game  Points_per_game  Rebounds_per_game  Assists_per_game  Steals_per_game  Blocks_per_game     Turnovers_per_game")
    for Average in results:
        print(f"{Average[1]:<12} {Average[2]:<17} {Average[3]:<16} {Average[4]:<18} {Average[5]:<17} {Average[6]:<16} {Average[7]:<19} {Average[8]:<4}")
    print()
    #loop finished here
    db.close()

#2.Lakers Player Details
def print_Lakers_Player():
   '''print 2023-24_Lakers_Player's table'''
   db = sqlite3.connect(DATABASE)
   cursor = db.cursor()
   #Lakers_Player
   sql= "SELECT * FROM Lakers_Player_2023_24;"
   cursor.execute(sql)
   results = cursor.fetchall()
   #loop through all the results first
   print(f"Name                 Position     Jersey_number    Age     Salary_million")
   for Player in results:
        print(f"{Player[1]:<20} {Player[2]:<12} {Player[3]:<16} {Player[4]:<7} {Player[5]:<4}")
   print()
   #loop finished here
   db.close()

#3.Lakers_Attendance
def print_Laker_Attendance():
    '''print 2023-24_Lakers_Attendance's table'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
   #Lakers_Player_attendance
    sql= "SELECT * FROM Lakers_Player_Attendance_2023_24;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results first
    print(f"Player_id       Present_count   Absent_count    Injured_count")
    for Attendance in results:
        print(f"{Attendance[1]:<15} {Attendance[2]:<15} {Attendance[3]:<15} {Attendance[4]:<4}")
    print()
    #loop finished here
    db.close()


#4.Lakers_Average_Stats
def print_Lakers_Average_Stats():
    '''print Lakers_Average_Stats' table'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
  #Lakers_Player_average_stats
    sql= "SELECT * FROM Lakers_Player_Average_Stats_2023_24;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results first
    print(f"Player_id    Minutes_per_game  Points_per_game  Rebounds_per_game  Assists_per_game  Steals_per_game  Blocks_per_game     Turnovers_per_game")
    for Average in results:
        print(f"{Average[1]:<12} {Average[2]:<17} {Average[3]:<16} {Average[4]:<18} {Average[5]:<17} {Average[6]:<16} {Average[7]:<19} {Average[8]:<4}")
    print()
    #loop finished here
    db.close()


#5.Lakers Player Salary_million from highest to lowest
def print_Lakers_Player_Salary_million():
    '''print Lakers_Player_Salary_million from highest to lowest '''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #Lakers_Player
    sql= "SELECT * FROM Lakers_Player_2023_24 ORDER BY Salary_million DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results first
    print(f"Name                 Position     Jersey_number    Age     Salary_million")
    for Player in results:
        print(f"{Player[1]:<20} {Player[2]:<12} {Player[3]:<16} {Player[4]:<7} {Player[5]:<4}")
    print()
    #loop finished here
    db.close()    


#6.Lakers Player Average Stats Points per game from highest to lowest
def print_Lakers_Average_Stats_Points_per_game():
    '''print Lakers Player Average Stats Points per game from highest to lowest'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
  #Lakers_Player_average_stats
    sql= "SELECT * FROM Lakers_Player_Average_Stats_2023_24 order by Points_per_game DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results first
    print(f"Player_id    Minutes_per_game  Points_per_game  Rebounds_per_game  Assists_per_game  Steals_per_game  Blocks_per_game     Turnovers_per_game")
    for Average in results:
        print(f"{Average[1]:<12} {Average[2]:<17} {Average[3]:<16} {Average[4]:<18} {Average[5]:<17} {Average[6]:<16} {Average[7]:<19} {Average[8]:<4}")
    print()
    #loop finished here
    db.close()


#7.Lakers Player Average Stats Rebounds per game from highest to lowest
def print_Lakers_Average_Stats_Rebounds_per_game():
    '''print Lakers Player Average Stats Rebounds per game from highest to lowest'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
  #Lakers_Player_average_stats
    sql= "SELECT * FROM Lakers_Player_Average_Stats_2023_24 order by Rebounds_per_game DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results first
    print(f"Player_id    Minutes_per_game  Points_per_game  Rebounds_per_game  Assists_per_game  Steals_per_game  Blocks_per_game     Turnovers_per_game")
    for Average in results:
        print(f"{Average[1]:<12} {Average[2]:<17} {Average[3]:<16} {Average[4]:<18} {Average[5]:<17} {Average[6]:<16} {Average[7]:<19} {Average[8]:<4}")
    print()
    #loop finished here
    db.close()


#8.Lakers Player Average Stats Assists per game from highest to lowest
def print_Lakers_Average_Stats_Assists_per_game():
    '''print Lakers Player Average Stats Assists per game from highest to lowest'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
  #Lakers_Player_average_stats
    sql= "SELECT * FROM Lakers_Player_Average_Stats_2023_24 order by Assists_per_game DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results first
    print(f"Player_id    Minutes_per_game  Points_per_game  Rebounds_per_game  Assists_per_game  Steals_per_game  Blocks_per_game     Turnovers_per_game")
    for Average in results:
        print(f"{Average[1]:<12} {Average[2]:<17} {Average[3]:<16} {Average[4]:<18} {Average[5]:<17} {Average[6]:<16} {Average[7]:<19} {Average[8]:<4}")
    print()
    #loop finished here
    db.close()


#9.Search and Print Player all Details
def search_and_print_player():
    '''search and print Player by Player ID'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
  #Print Player_ID and Name
    sql="SELECT Player_id, Name FROM Lakers_Player_2023_24;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results first
    print(f"Player_id    Name")
    for Name in results:
        print(f"{Name[0]:<12} {Name[1]:<12}")
    print()
  #Input Player_id
    player_id = int(input("Enter Player_id to view Player_information:"))

  #Lakers_Player_2023_24
    sql= "SELECT * FROM Lakers_Player_2023_24 WHERE Player_id=?;"
    cursor.execute(sql,(player_id,))
    player = cursor.fetchone()
    if player:
        print()
        print(f"Player Information:")
        print(f"Name: {player[1]}")
        print(f"Position: {player[2]}")
        print(f"Jersey Number: {player[3]}")
        print(f"Age: {player[4]}")
        print(f"Salary: {player[5]} million")
        print()
  #Lakers_Player_Attendance_2023_24
    sql = "SELECT * FROM Lakers_Player_Attendance_2023_24 WHERE Player_id = ?;"
    cursor.execute(sql, (player_id,))
    attendance = cursor.fetchone()
    if attendance:
       print(f"Attendance Information:")
       print(f"Present Count: {attendance[2]}")
       print(f"Absent Count: {attendance[3]}")
       print(f"Injured Count: {attendance[4]}")
       print()
  #Lakers_Player_Average_Stats_2023_24
    sql = "SELECT * FROM Lakers_Player_Average_Stats_2023_24 WHERE Player_id = ?;"
    cursor.execute(sql, (player_id,))
    stats = cursor.fetchone()
    if stats:
      print(f"Average Stats Information:")
      print(f"Minutes per Game: {stats[2]}")
      print(f"Points per Game: {stats[3]}")
      print(f"Rebounds per Game: {stats[4]}")
      print(f"Assists per Game: {stats[5]}")
      print(f"Steals per Game: {stats[6]}")
      print(f"Blocks per Game: {stats[7]}")
      print(f"Turnovers per Game: {stats[8]}")
      print()
    else:
        print(f"No Player found with Player_id {player_id}")
    #loop finished here
    db.close()


#main code
while True:
    user_input = input(
    """
    What would you like to do.
    1.  Print all Lakers
    2.  Print Lakers Player
    3.  Print Lakers Attendance
    4.  Print Lakers Average Stats
    5.  Print Lakers Player Salary_million From highest to lowest
    6.  Print Lakers Player Average Stats Points per game From highest to lowest
    7.  Print Lakers Player Average Stats Rebounds per game From highest to lowest
    8.  Print Lakers Player Average Stats Assists per game From highest to lowest
    9.  Search and Print Player by Player ID
    10.  Exit
    """)
    print()
    if user_input == "1":
      print_all_Lakers()
    elif user_input =="2":
      print_Lakers_Player()
    elif user_input == "3":
      print_Laker_Attendance()
    elif user_input == "4":
      print_Lakers_Average_Stats()
    elif user_input =="5":
      print_Lakers_Player_Salary_million()
    elif user_input =="6":
      print_Lakers_Average_Stats_Points_per_game()
    elif user_input =="7":
      print_Lakers_Average_Stats_Rebounds_per_game()
    elif user_input =="8":
      print_Lakers_Average_Stats_Assists_per_game()
    elif user_input =="9":
      search_and_print_player()
    elif user_input =="10":
        break
    else:
         print('That was not an option\n')
     