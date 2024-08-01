import sqlite3

con = sqlite3.connect('Youtube_videos.db')

cursor= con.cursor()

# to make the basic table we have to execute the cursor

# in the cursor we use the triple quote to make the fomatting as it is
cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                time TEXT NOT NULL
                )

''')

def list_all_videos():
    # yha cursor execute krata h or sari values select krta h
    # ye hame ek tuple return krke deta h
    cursor.execute("SELECT * FROM VIDEOS")
    videoss=cursor.fetchall()
    # yha ye cursor hold krke rakhra h sari values
    if not videoss:
        print("No videos listed yet..")
    else:
        for row in videoss: #yha ham sari values ko ek sath print kra skte or ek ek krke bhi print kra skte
    
         print(row)
    print("\n")
    print('*'* 70)


def add_video(name,time):
    cursor.execute("INSERT INTO videos(name,time) VALUES(?,?)",(name,time))
    # ab hame query commit bhi krni padegi
    # cursor.commit() cursor to query excute krta h commit to connection krta h
    print("Video is Added")
    print("\n")
    print('*'* 70)
    con.commit()
     

def update_video(video_id,new_name,new_time):
    cursor.execute("UPDATE videos SET name=?, time=? WHERE id=?",(new_name,new_time,video_id))
    print("Video is Updated")
    print("\n")
    print('*'* 70)
    con.commit()

def delete_video(video_id):
    # ye ek tuple tha ishliye sirf tuple me jab bhi ek paramter pass krenge to last me , bhi lagayenge tabhi wo tuple mana jayega
    cursor.execute("DELETE FROM videos WHERE id=?",(video_id,))
    print("Video is Deleted")
    print("\n")
    print('*'* 70)
    con.commit()


# making a main method for the entry point
def main():
    while True:
        print("\n Youtube Manager | Choose an Option")
        print("1- List all youtube videos")
        print("2- Add a youtube video")
        print("3- Update a youtube video")
        print("4- Delete a youtube video")
        print("5- Exit the app")
        choice= input("Enter you Choice: ")

        if choice=='1':
            list_all_videos()

        elif choice=='2':
            name =input("Enter the name of the video: ")
            time=input("Enter the duration: ")
            add_video(name,time)

        elif choice=='3':
            # kyuki yha ham sari video nhi bhej rhe to hame video id ki jarurt h 
            # or hamne enumerate krne ki bhi jarurut nhi kyuki db apne app indexing deta h
            video_id=input("Enter the video id: ")
            name =input("Enter the name of the video you want to update: ")
            time=input("Enter the duration: ")
            update_video(video_id,name,time)

        elif choice=='4':
            video_id=input("Enter the video id: ")
        
            delete_video(video_id)

        elif choice=='5':
            break

        else:
            print("Invalid choice Entered")

    con.close()

    





if __name__ =="__main__":
    main()
