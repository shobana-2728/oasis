import tkinter as tk
from tkinter import messagebox

def calculate_bmi_gui():
    """Calculates BMI and displays the result in the GUI."""
    try:
        
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        
        
        if weight <= 0 or height <= 0:
            messagebox.showerror("Invalid Input", "Weight and height must be positive numbers.")
            return

        
        bmi = weight / (height ** 2)
        
        
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"
            
        
        result_label.config(text=f"Your BMI is: {bmi:.2f}\nCategory: {category}")
        
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for weight and height.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")


root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x300")
root.configure(bg="#f0f0f0")


tk.Label(root, text="BMI Calculator", font=("Arial", 20, "bold"), bg="#f0f0f0").pack(pady=10)


input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Weight (kg):", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5)
weight_entry = tk.Entry(input_frame, font=("Arial", 12), width=15)
weight_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Height (m):", font=("Arial", 12), bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=5)
height_entry = tk.Entry(input_frame, font=("Arial", 12), width=15)
height_entry.grid(row=1, column=1, padx=5, pady=5)


calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi_gui, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", bd=0, relief="flat", padx=10, pady=5)
calculate_button.pack(pady=10)


result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0", fg="#333333")
result_label.pack(pady=20)


root.mainloop()