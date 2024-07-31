import json

# ***********LOADING THE DATA IN JSON***************
def load_data():
    try:
        with open ('youtube.txt','r') as file:
            res=json.load(file)
            print(type(res))  # list ayegi
            return  res
# ab yha ye json kya krega ki jo bhi file me data hoga ushe load krega or json me convert krr dega
    except FileNotFoundError:
# agr file avialabe hi na ho
        return []  # return empty list
    
# **************HELPER FUNCTION WHICH SAVE THE DATA************

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)
# dump me ham likhte ki kya save krna h or kha save krna h


# ****************SHOW THE LIST OF ALL VIDEOS***************

def list_all_videos(videos):
    print("\n")
    print("*"*70)
    for i,video in enumerate(videos,start=1):
        print(f"{i}. Name={video['name']} Duration={video['Duration']}")
    print("\n")
    print("*"*70)


# ****************ADD THE VIDEO IN VIDEOS LIST AS OBJECT***************  

def add_video(videos):
    name=input("Enter the name of the video: ")
    time = input("Enther the time duration of the video: ")
    videos.append({'name': name, 'Duration': time})  # yeh line user inputs ko list mein add kar rahi hai
    save_data_helper(videos)  # yeh line updated list ko file mein save kar rahi hai


# ****************UPDATE THE VIDEO IN THE VIDEOS***************     

def update_videos(videos):
    list_all_videos(videos)
    index=int(input("Enter the video number you want to update "))
    if 0<index<=len(videos):
        name=input("Enter the name you want to update ")
        time= input("Enter the duration of the video ")
        videos[index-1]= {'name':name, 'Duration':time}
        save_data_helper(videos)
    else:
        print("Invalid number choise")


# ****************DELETE THE VIDEO***************

def delete_videos(videos):
    list_all_videos(videos)

    index=int(input("Enter the video number you want to Delete: "))
    print(index)
    if 0<index<=len(videos):
        print(f"Video number {index} is Deleted  |  Name={videos[index-1]['name']}")
        videos.pop(index-1)
        save_data_helper(videos)
    else:
        print("Invalid number choise")


# *********************************MAIN FUNCTION***********************************

# Ek entry pooint to banana tha dusre programming langauge ki trah se
# jisse pta chal jaye ki ha ye supporitng functions h or niche se main function start hua h
def main():
    videos = load_data()  # yeh line ya to file se data load karegi ya empty list return karegi
    # print(videos)
       
    while True:
         print("\n Youtube Manager | choose an Option");
         print("1- List all youtube videos")
         print("2- Add a Youtube video")
         print("3- Update a Youtube video details")
         print("4- Delete a youtube video")
         print("5- Exit the app")
         choice=input("Enter your choice: ")

         match choice:
             case '1':
                 list_all_videos(videos)
             case '2':
                 add_video(videos)
             case '3':
                 update_videos(videos)
             case '4':
                 delete_videos(videos)
             case '5':
                   break
             case _:
                  print("Invalid Choice")
                 
if __name__ =="__main__":
    main()

