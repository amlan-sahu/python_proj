import sqlite3


conn = sqlite3.connect('manager.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS managers (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )
''')

def list_videos():
    cursor.execute("SELECT * FROM managers")
    print("\n")
    print("*" * 70)
    for row in cursor.fetchall():
        print(f"{row[0]}. {row[1]}, Duration: {row[2]}")
    print("\n")
    print("*" * 70)

def add_video(name, time):
    cursor.execute("INSERT INTO managers (name, time) VALUES (?, ?)", (name, time))
    conn.commit()
    print(f"Video '{name}' added successfully.")

def update_video(video_id, name, time):
    try:
        video_id = int(video_id)
        cursor.execute("UPDATE managers SET name = ?, time = ? WHERE id = ?", (name, time, video_id))
        if cursor.rowcount == 0:
            print(f"No video found with ID {video_id}")
        else:
            conn.commit()
            print(f"Video ID {video_id} updated successfully.")
    except ValueError:
        print("Invalid ID. Please enter a number.")

def delete_video(video_id):
    try:
        video_id = int(video_id)
        cursor.execute("DELETE FROM managers WHERE id = ?", (video_id,))
        if cursor.rowcount == 0:
            print(f"No video found with ID {video_id}")
        else:
            conn.commit()
            print(f"Video ID {video_id} deleted successfully.")
    except ValueError:
        print("Invalid ID. Please enter a number.")

def main():
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
                list_videos()
            case "2":
                name = input("Enter video title: ")
                time = input("Enter video time: ")
                add_video(name, time)
            case "3":
                video_id = input("Enter video ID to update: ")
                name = input("Enter video title to update: ")
                time = input("Enter new video time: ")
                update_video(video_id, name, time)
            case "4":
                video_id = input("Enter video ID to delete: ")
                delete_video(video_id)
            case "5":
                print("Exiting the app. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

    conn.close()       

if __name__ == "__main__":
    main()