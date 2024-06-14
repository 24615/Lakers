#docstring- Jayden Zheng -Lakers_2023_24 database application
#imports
import sqlite3
from colorama import Fore, Style, init

#Define user name and password saparate by user and admin
users = {
"Jayden":{'password':'081207', 'role' :'admin' },
"24615":{'password':'Hihi2007','role':'admin'},
"Eric":{'password':'Kahu8189','role':'user'},
"Hyacinth":{'password':'20240606','role':'user'},
"Mr.Thew":{'password':'123456','role':'admin'},
}

#Initialize colorma
init(autoreset=True)

#contants and varibles
DATABASE="/Users/jaydenzheng/Desktop/Database/Lakers/Database.db"



#Login
def login():
   while True:
      username=input("Please enter your username: ")
      password=str(input("Please enter your password: "))
      if username=='exit':
         break
      if username and username in users and password == users[username]['password']:
         print('Login successful! Welcome to the world of the Lakers. Lakers are the champions!')
         return username, users[username]['role']
      else :
         print(Fore.RED +"Incorrect username or password. Please try again. To exit, enter 'exit' as the username.")


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
    print(Fore.CYAN + f"Name                 Position     Jersey_number    Age     Salary_million")
    for Player in results:
        print(f"{Fore.GREEN}{Player[1]:<20} {Player[2]:<12} {Player[3]:<16} {Player[4]:<7} {Player[5]:<4}")
    print()
    input("Press Enter to continue...")
     
    #Lakers_Player_attendance
    sql= "SELECT * FROM Lakers_Player_Attendance_2023_24;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results first
    print(Fore.CYAN + f"Player_id       Present_count   Absent_count    Injured_count")
    for Attendance in results:
        print(f"{Fore.YELLOW}{Attendance[1]:<15} {Attendance[2]:<15} {Attendance[3]:<15} {Attendance[4]:<4}")
    print()
    input("Press Enter to continue...")
    
    #Lakers_Player_average_stats
    sql= "SELECT * FROM Lakers_Player_Average_Stats_2023_24;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results first
    print(Fore.CYAN + f"Player_id    Minutes_per_game  Points_per_game  Rebounds_per_game  Assists_per_game  Steals_per_game  Blocks_per_game     Turnovers_per_game")
    for Average in results:
        print(f"{Fore.MAGENTA}{Average[1]:<12} {Average[2]:<17} {Average[3]:<16} {Average[4]:<18} {Average[5]:<17} {Average[6]:<16} {Average[7]:<19} {Average[8]:<4}")
    print()
    #loop finished here
    db.close()
    input("Press Enter to continue...")

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
   print(Fore.CYAN + f"Name                 Position     Jersey_number    Age     Salary_million")
   for Player in results:
        print(f"{Fore.GREEN}{Player[1]:<20} {Player[2]:<12} {Player[3]:<16} {Player[4]:<7} {Player[5]:<4}")
   print()
   #loop finished here
   db.close()
   input("Press Enter to continue...")
  

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
    print(Fore.CYAN + f"Player_id       Present_count   Absent_count    Injured_count")
    for Attendance in results:
        print(f"{Fore.YELLOW}{Attendance[1]:<15} {Attendance[2]:<15} {Attendance[3]:<15} {Attendance[4]:<4}")
    print()
    #loop finished here
    db.close()
    input("Press Enter to continue...")


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
    print(Fore.CYAN + f"Player_id    Minutes_per_game  Points_per_game  Rebounds_per_game  Assists_per_game  Steals_per_game  Blocks_per_game     Turnovers_per_game")
    for Average in results:
        print(f"{Fore.MAGENTA}{Average[1]:<12} {Average[2]:<17} {Average[3]:<16} {Average[4]:<18} {Average[5]:<17} {Average[6]:<16} {Average[7]:<19} {Average[8]:<4}")
    print()
    #loop finished here
    db.close()
    input("Press Enter to continue...")


#5.Lakers Player sorted by Salary_million
def print_Lakers_Player_Salary_million():
    '''print Lakers_Player_Salary_million from highest to lowest '''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #Lakers_Player
    sql= "SELECT * FROM Lakers_Player_2023_24 ORDER BY Salary_million DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results first
    print(f"Name                 Position     Jersey_number    Age     "+ Fore.CYAN + "Salary_million")
    for Player in results:
        print(f"{Player[1]:<20} {Player[2]:<12} {Player[3]:<16} {Player[4]:<7} {Fore.GREEN}{Player[5]:<4}")
    print()
    #loop finished here
    db.close()    
    input("Press Enter to continue...")


#6.Lakers Player Average Stats sorted by Points per game 
def print_Lakers_Average_Stats_Points_per_game():
    '''print Lakers Player Average Stats Points per game from highest to lowest'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
  #Lakers_Player_average_stats
    sql= "SELECT * FROM Lakers_Player_Average_Stats_2023_24 order by Points_per_game DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results first
    print(f"Player_id    Minutes_per_game  "+ Fore.CYAN + "Points_per_game" +Style.RESET_ALL+ "  Rebounds_per_game  Assists_per_game  Steals_per_game  Blocks_per_game     Turnovers_per_game")
    for Average in results:
        print(f"{Average[1]:<12} {Average[2]:<17} {Fore.MAGENTA}{Average[3]:<16}{Style.RESET_ALL} {Average[4]:<18} {Average[5]:<17} {Average[6]:<16} {Average[7]:<19} {Average[8]:<4}")
    print()
    #loop finished here
    db.close()
    input("Press Enter to continue...")


#7.Lakers Player Average Stats sorted by Rebounds per game
def print_Lakers_Average_Stats_Rebounds_per_game():
    '''print Lakers Player Average Stats Rebounds per game from highest to lowest'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
  #Lakers_Player_average_stats
    sql= "SELECT * FROM Lakers_Player_Average_Stats_2023_24 order by Rebounds_per_game DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results first
    print(f"Player_id    Minutes_per_game  Points_per_game  "+ Fore.CYAN + "Rebounds_per_game"+Style.RESET_ALL+"  Assists_per_game  Steals_per_game  Blocks_per_game     Turnovers_per_game")
    for Average in results:
        print(f"{Average[1]:<12} {Average[2]:<17} {Average[3]:<16} {Fore.MAGENTA}{Average[4]:<18}{Style.RESET_ALL} {Average[5]:<17} {Average[6]:<16} {Average[7]:<19} {Average[8]:<4}")
    print()
    #loop finished here
    db.close()
    input("Press Enter to continue...")


#8.Lakers Player Average Stats sorted by Assists per game
def print_Lakers_Average_Stats_Assists_per_game():
    '''print Lakers Player Average Stats Assists per game from highest to lowest'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
  #Lakers_Player_average_stats
    sql= "SELECT * FROM Lakers_Player_Average_Stats_2023_24 order by Assists_per_game DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results first
    print(f"Player_id    Minutes_per_game  Points_per_game  Rebounds_per_game  "+ Fore.CYAN + "Assists_per_game"+Style.RESET_ALL+"  Steals_per_game  Blocks_per_game     Turnovers_per_game")
    for Average in results:
        print(f"{Average[1]:<12} {Average[2]:<17} {Average[3]:<16} {Average[4]:<18} {Fore.MAGENTA}{Average[5]:<17}{Style.RESET_ALL} {Average[6]:<16} {Average[7]:<19} {Average[8]:<4}")
    print()
    #loop finished here
    db.close()
    input("Press Enter to continue...")


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
    print(Fore.CYAN +f"Player_id     Name")
    for Name in results:
        print(f"{Fore.GREEN} {Name[0]:<12} {Name[1]:<12}")
    print()
  #Input Player_id
    while True : 
      try:
         player_id = int(input("Enter Player_id to view Player_information:"))
         if player_id==0:
           print(f"No Player found with Player_id 0")
         if player_id>0:
           break
      except ValueError:
         print(Fore.RED+f"Invaild input. Please try again")
  #Lakers_Player_2023_24
    sql= "SELECT * FROM Lakers_Player_2023_24 WHERE Player_id=?;"
    cursor.execute(sql,(player_id,))
    player = cursor.fetchone()
    if player:
        print()
        print(Fore.CYAN +f"Player Information:")
        print(Fore.GREEN+f"Name: {player[1]}")
        print(Fore.GREEN+f"Position: {player[2]}")
        print(Fore.GREEN+f"Jersey Number: {player[3]}")
        print(Fore.GREEN+f"Age: {player[4]}")
        print(Fore.GREEN+f"Salary: {player[5]} million")
        print()
        input("Press Enter to continue...")
  #Lakers_Player_Attendance_2023_24
    sql = "SELECT * FROM Lakers_Player_Attendance_2023_24 WHERE Player_id = ?;"
    cursor.execute(sql, (player_id,))
    attendance = cursor.fetchone()
    if attendance:
       print(Fore.CYAN +f"Attendance Information:")
       print(Fore.YELLOW+f"Present Count: {attendance[2]}")
       print(Fore.YELLOW+f"Absent Count: {attendance[3]}")
       print(Fore.YELLOW+f"Injured Count: {attendance[4]}")
       print()
       input("Press Enter to continue...")
  #Lakers_Player_Average_Stats_2023_24
    sql = "SELECT * FROM Lakers_Player_Average_Stats_2023_24 WHERE Player_id = ?;"
    cursor.execute(sql, (player_id,))
    stats = cursor.fetchone()
    if stats:
      print(Fore.CYAN +f"Average Stats Information:")
      print(Fore.MAGENTA+f"Minutes per Game: {stats[2]}")
      print(Fore.MAGENTA+f"Points per Game: {stats[3]}")
      print(Fore.MAGENTA+f"Rebounds per Game: {stats[4]}")
      print(Fore.MAGENTA+f"Assists per Game: {stats[5]}")
      print(Fore.MAGENTA+f"Steals per Game: {stats[6]}")
      print(Fore.MAGENTA+f"Blocks per Game: {stats[7]}")
      print(Fore.MAGENTA+f"Turnovers per Game: {stats[8]}")
      print()
    else:
        print(f"No Player found with Player_id {player_id}")
    #loop finished here
    db.close()
    input("Press Enter to continue...")


#10.Add new Player into Lakers_Player_2023_24
def add_player():
   '''Adding new Player'''
   db = sqlite3.connect(DATABASE)
   cursor = db.cursor()
   #Input Player data
   while True:
      try:
          player_id = int(input('Enter Player ID must be an integer and greater than 19: '))       
          name = input('Enter Player name: ')
          position = input('Enter Player position: ')
          jersey_number = int(input('Enter Player jersey number: '))
          age = int(input('Enter Player age: '))
          salary = float(input('Enter player salary (in million): '))
          #Insert into Lakera_Player_2023_24
          sql="INSERT INTO Lakers_Player_2023_24 (Player_id, Name, Position, Jersey_number, Age, Salary_million) VALUES (?, ?, ?, ?, ?, ?);"
          cursor.execute(sql,(player_id, name, position, jersey_number, age, salary,))
          db.commit()
          print(Fore.GREEN+ "Player added successfully")
          break 
      except ValueError:
         print(Fore.RED + f"Invalid input.")
         quit=input("Type"+ Fore.RED +' exit' + Fore.WHITE+ " to quit or Press " +Fore.RED +'enter' + Fore.WHITE+" to try again: ")
         if quit=='exit':
            break
      except sqlite3.Error:
          print(Fore.RED + f"Database error")
          break 
   #loop finished here
   db.close()
   input("Press Enter to continue...")
  

#11.Delete Player in Lakers_Player_2023_24
def delete_player():
   '''Delete Player'''
   db = sqlite3.connect(DATABASE)
   cursor = db.cursor()
   #Print Player_ID and Name
   sql="SELECT Player_id, Name FROM Lakers_Player_2023_24;"
   cursor.execute(sql)
   results = cursor.fetchall()
   #loop through all the results first
   print(Fore.CYAN +f"Player_id     Name")
   for Name in results:
        print(f"{Fore.GREEN} {Name[0]:<12} {Name[1]:<12}")
   print()
   while True:
     try:
      #Input Player data
      player_id = int(input('Enter Player ID to delete: '))
      #Delect Player in Lakera_Player_2023_24
      sql="DELETE FROM Lakers_Player_2023_24 WHERE Player_id = ?;"
      cursor.execute(sql,(player_id,))
      db.commit()
      print(Fore.GREEN+ "Player deleted successfully")
      break
     except ValueError:
         print(Fore.RED + f"Invalid input. Please try again.")  
         quit=input("Type"+ Fore.RED +' exit' + Fore.WHITE+ " to quit or Press " +Fore.RED +'enter' + Fore.WHITE+" to try again: ")
         if quit=='exit':
            break  
   db.close
   input("Press Enter to continue...")


#main code
if __name__ == '__main__':
   username, role=login()
   if username is None:
      exit()

   while True:
      if role == "admin":
         user_input = input(
"""
What would you like to do.
1.  Print all Lakers
2.  Print Lakers Player
3.  Print Lakers Attendance
4.  Print Lakers Average Stats
5.  Print Lakers Player sorted by Salary_million
6.  Print Lakers Player Average Stats sorted by Points per game 
7.  Print Lakers Player Average Stats sorted by Rebounds per game
8.  Print Lakers Player Average Stats sorted by Assists per game
9.  Search and Print Player by Player ID
10. Add new Player into Lakers_Player_2023_24
11. Delete Player in Lakers_Player_2023_24
12. Exit
""")
      else:
            user_input = input(Fore.CYAN + """
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
      elif user_input =="10" and role=="admin":
        add_player()
      elif user_input=='11' and role=="admin":
        delete_player()
      elif user_input=='12' or (user_input == "10" and role == 'user'):
         break
      else:
         print(Fore.RED +'That was not an option\n')
         input("Press Enter to continue...")
       
     
