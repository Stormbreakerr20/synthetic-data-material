import random
import json
import re
from faker import Faker

# Initialize Faker with Indian locale
fake = Faker('en_IN')

# List of common Indian names (a more comprehensive list would be better)
indian_names = [
    "Aarav", "Aditi", "Aditya", "Akshay", "Aman", "Amit", "Ananya", "Anil", "Anita", "Anjali", 
    "Arjun", "Aryan", "Ashish", "Bhavesh", "Chetan", "Deepak", "Deepika", "Devika", "Diya", "Gaurav", 
    "Harsh", "Ishan", "Ishaan", "Jaya", "Karan", "Kavita", "Krishna", "Kunal", "Lakshmi", "Manish", 
    "Meera", "Mohan", "Mohit", "Neha", "Nikhil", "Nisha", "Pankaj", "Pooja", "Pradeep", "Pranav", 
    "Priya", "Rahul", "Raj", "Rajesh", "Rishi", "Rohan", "Sachin", "Sanjay", "Sarika", "Shikha", 
    "Shivani", "Shreya", "Shruti", "Siddharth", "Simran", "Sonam", "Sonia", "Sunil", "Suresh", "Tanvi", 
    "Tarun", "Usha", "Varun", "Vijay", "Vipul", "Vishal", "Yash", "Preeti", "Suhail", "Suhaib",
    "Jashwanth", "Diya", "Revanth", "Ayan", "Parthiv", "Bali", "David", "Masud", "Anthea"
]

def is_likely_indian_name(username):
    """Check if username likely contains an Indian name"""
    # Convert to lowercase for easier matching
    username_lower = username.lower()
    
    # Extract parts that might be names
    # This regex extracts alphabetic sequences that might be names
    potential_names = re.findall(r'[a-zA-Z]+', username_lower)
    
    for part in potential_names:
        for name in indian_names:
            if part == name.lower() or (len(part) > 3 and name.lower() in part):
                return name
    
    return None

def generate_roll_number():
    """Generate a roll number in the format B2XXXX"""
    batch_year = random.choice(["1", "2", "3", "4"])
    roll_num = random.randint(1, 300)
    return f"B2{batch_year}{roll_num:03d}"

def process_github_usernames(usernames):
    """Process GitHub usernames and generate Indian names and roll numbers"""
    results = []
    
    for username in usernames:
        # Check if username contains an Indian name
        indian_name = is_likely_indian_name(username)
        
        # If no match, assign a random Indian name
        if not indian_name:
            indian_name = random.choice(indian_names)
            
        # Generate a roll number
        roll_number = generate_roll_number()
        
        # Add to results
        results.append({
            "github_username": username,
            "generated_name": indian_name,
            "roll_number": roll_number
        })
    
    return results

def main():
    # Read usernames from file
    try:
        with open("stargazers.txt", "r") as file:
            github_usernames = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("Error: stargazers.txt not found!")
        # Use the example usernames if file not found
        github_usernames = [
            "davidyassa", "BaliTarunTeja", "parthiv147", "harsh241082",
            "pranathiarigela", "SuhaibK10", "adijoshi07", "Itsbhavesh1101",
            "crt4l", "Masuddar", "Jashwanth020", "diyadas1411",
            "rahulntsh", "Rizzwick", "Arni005", "Anthea-c",
            "revanth1718", "ayan-aslam", "PREETCHAUHAN2005", "Nikhil-1122"
        ]
        print("Using example usernames instead.")
    
    # Process the usernames
    results = process_github_usernames(github_usernames)
    
    # Save to JSON file
    with open("github_indian_names.json", "w") as json_file:
        json.dump(results, json_file, indent=2)
    
    # Also save as CSV for easy viewing
    with open("github_indian_names.csv", "w") as csv_file:
        csv_file.write("Github Username,Generated Name,Roll Number\n")
        for item in results:
            csv_file.write(f"{item['github_username']},{item['generated_name']},{item['roll_number']}@students.iitmandi.ac.in\n")
    
    # Print results
    print(f"Processed {len(results)} GitHub usernames:")
    for item in results:
        print(f"Username: {item['github_username']} → Name: {item['generated_name']}, Roll: {item['roll_number']}@students.iitmandi.ac.in")
    
    print("\nResults saved to github_indian_names.json and github_indian_names.csv")

if __name__ == "__main__":
    main()