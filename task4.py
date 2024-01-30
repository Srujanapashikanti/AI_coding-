import tkinter as tk
from tkinter import messagebox

# Function to recommend movies for a given user
def recommend_movies_for_user(user_id):
    try:
        # Call your recommendation function here
        recommended_movies = ["Movie 1", "Movie 2", "Movie 3"]  # Example recommended movies
        messagebox.showinfo("Recommendations", f"Recommended movies for user {user_id}:\n" + "\n".join(recommended_movies))
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to handle button click event
def on_recommend_button_click():
    user_id = int(user_id_entry.get())
    recommend_movies_for_user(user_id)

# Create the main application window
root = tk.Tk()
root.title("Movie Recommendation System")

# Create and place widgets
user_id_label = tk.Label(root, text="Enter User ID:")
user_id_label.grid(row=0, column=0, padx=5, pady=5)

user_id_entry = tk.Entry(root)
user_id_entry.grid(row=0, column=1, padx=5, pady=5)

recommend_button = tk.Button(root, text="Recommend Movies", command=on_recommend_button_click)
recommend_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Run the application
root.mainloop()
