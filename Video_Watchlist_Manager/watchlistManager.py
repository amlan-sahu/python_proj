import json


def load_data():
    try:
        with open('watchlist.txt', 'r') as file:
            test = json.load(file)
            # print(type(test), test)
            return test
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open('watchlist.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*"*70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['title']}, Duration: {video['time']}")
    print("\n")
    print("*"*70)

def add_video(videos):
    name = input("Enter video title: ")
    time = input("Enter video time: ") 
    videos.append({"title": name, "time": time})
    save_data_helper(videos)

def update_video(video):
    list_all_videos(video)
    index = int(input("Enter the index of the video to update: ")) - 1
    if 0 <= index < len(video):
        new_title = input("Enter new title: ")
        new_time = input("Enter new time: ")
        # video[index]['title'] = new_title
        # video[index]['time'] = new_time
        video[index] = {"title": new_title, "time": new_time}
        save_data_helper(video)
        print("Video updated successfully.")
    else:
        print("Invalid index. No changes made.")

def delete_video(video):
    list_all_videos(video)
    index = int(input("Enter the index of the video to delete: ")) - 1
    if 0 <= index < len(video):
        del video[index]
        save_data_helper(video)
        print("Video deleted successfully.")
    else:
        print("Invalid index. No changes made.")

def main():
    videos = load_data()

    while True:
        print("\n watchlist Manager ")
        print("Choose an option:")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update a video details")
        print("4. Delete a video")
        print("5. Exit the app")
        input_choice = input("Enter your choice (1-5): ")

        match input_choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                print("Exiting the app. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
