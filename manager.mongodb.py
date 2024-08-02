from pymongo import MongoClient
from bson import ObjectId
# yha dikkat kya rhi h id ke sath ki jab ham terminal se id copy paste krke de rhe to wo as a string de rha usse jisse wo match nhi ho paa rhi
    # ishliye hamne bson import karayaa jisse wo id ko bson me convert krke de rha



username = "username"
password = "pass"
cluster = "cluster0.n1opmb4.mongodb.net"

# Construct the MongoDB URI
uri = f"mongodb+srv://{username}:{password}@{cluster}/?retryWrites=true&w=majority"

# Connect to MongoDB
try:
    client = MongoClient(uri, tlsAllowInvalidCertificates=True)
    db = client["ytmanager"]
    video_collection = db["videos"]
    print("Connected to the MongoDB server successfully.")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    exit(1)


print(video_collection);

def list_all_videos():
    try:
        for video in video_collection.find():
            print(f"ID: {video['_id']} Name: {video['name']} Time: {video['time']}")
    except Exception as e:
        print(f"Error listing videos: {e}")

def add_video(name, duration):
    try:
        video_collection.insert_one({"name": name, "time": duration})
        print("Video added successfully.")
    except Exception as e:
        print(f"Error adding video: {e}")

def update_video(video_id, new_name, new_time):
    try:
        video_collection.update_one({'_id': ObjectId(video_id)}, {"$set": {'name': new_name, 'time': new_time}})
        print("Video updated successfully.")
    except Exception as e:
        print(f"Error updating video: {e}")

def delete_video(video_id):
    try:
        video_collection.delete_one({'_id': ObjectId(video_id)})
        print("Video deleted successfully.")
    except Exception as e:
        print(f"Error deleting video: {e}")

def main():
    while True:
        print("\nYouTube Manager | Choose an Option")
        print("1- List all YouTube videos")
        print("2- Add a YouTube video")
        print("3- Update a YouTube video")
        print("4- Delete a YouTube video")
        print("5- Exit the app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_all_videos()
        elif choice == '2':
            name = input("Enter the name of the video: ")
            time = input("Enter the duration: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter the video ID: ")
            name = input("Enter the new name of the video: ")
            time = input("Enter the new duration: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter the video ID: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice entered.")

if __name__ == "__main__":
    main()
