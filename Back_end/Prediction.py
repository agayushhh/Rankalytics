import pandas as pd

def generate_preference_list(rank, seat_type, quota, exam, gender):
    # Load the CSV file
    try:
        file_path = 
        df = pd.read_csv(file_path)
        df['Predicted Opening Rank'] = pd.to_numeric(df['Predicted Opening Rank'], errors='coerce')
        df['Predicted Closing Rank'] = pd.to_numeric(df['Predicted Closing Rank'], errors='coerce')
    except Exception as e:
        print(f"Error loading file: {e}")
        return pd.DataFrame()

    # Ensure column names are correct
    required_columns = ['Seat Type', 'Quota', 'Exam', 'Gender', 'Predicted Opening Rank', 'Predicted Closing Rank', 'Round', 'Institute', 'Academic Program Name']
    for col in required_columns:
        if col not in df.columns:
            print(f"Missing column: {col}")
            return pd.DataFrame()

    # Filter the data based on user criteria
    try:
        filtered_df = df[
            (df['Seat Type'].str.lower() == seat_type.lower()) &
            (df['Quota'].str.lower() == quota.lower()) &
            (df['Exam'].str.lower() == exam.lower()) &
            (df['Gender'].str.lower() == gender.lower()) &
            (((df['Predicted Opening Rank'] >= rank)) |
             ((df['Predicted Opening Rank'] <= rank) &
              (df['Predicted Closing Rank'] >= rank)))
        ]
    except Exception as e:
        print(f"Error filtering data: {e}")
        return pd.DataFrame()

    # Check if any data remains after filtering
    if filtered_df.empty:
        print("No matching data found for the given criteria.")
        return pd.DataFrame()

    # Sort the data by round and predicted opening rank
    sorted_df = filtered_df.sort_values(by=['Round', 'Predicted Opening Rank'])

    return sorted_df

# Get user input
file_path = 'Updated_Predicted_Data2.csv'
exam = input("Enter the exam type (Advanced/Mains): ")
seat_type = input("Enter your seat type (OPEN/SC/ST/OBC-NCL/OPEN (PwD)/EWS): ")
rank = int(input("Enter your rank: "))
gender = input("Enter your gender (Neutral/Female): ")

if exam != 'Advanced':
    quota = input("Enter the quota (AI/HS/OS): ")
else:
    quota = 'AI'

# Generate and print the preference list
sorted_df = generate_preference_list(file_path, rank, seat_type, quota, exam, gender)

if not sorted_df.empty:
    for round_num in sorted_df['Round'].unique():
        print(f'\nRound number: {round_num}\n')
        round_df = sorted_df[sorted_df['Round'] == round_num]
        round_df = round_df.loc[:, ['Institute', 'Academic Program Name', 'Predicted Opening Rank', 'Predicted Closing Rank']]
        print(round_df.to_string(index=False))

else:
    print("No data to display.")
