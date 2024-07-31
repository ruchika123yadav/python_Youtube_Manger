
def load_data():
    pass

def list_all_videos(videos):
    pass

def add_video(videos):
    pass

def update_videos(videos):
    pass

def delete_videos(videos):
    pass


# Ek entry pooint to banana tha dusre programming langauge ki trah se
# jisse pta chal jaye ki ha ye supporitng functions h or niche se main function start hua h
def main():
    videos=load_data() # ye kisi or file se data load krega agr agr data hoga to load kr dega other wise show empty file

    while True:
         print("\n Youtube Manager | choose an Option");
         print("1- List all youtube videos")
         print("2- Add a Youtube video")
         print("3- Update a Youtube video details")
         print("4-Delete a youtube video")
         print("Exit the app")
         choice=input("Enter your choice:")

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

          
         
    



 

     
    
     