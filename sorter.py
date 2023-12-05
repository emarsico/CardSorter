import os
import shutil

# Define the paths where the card folders are located
card_folders = ['cards1', 'cards2', 'cards3']

# Define the base path where the suit folders will be created
base_path = 'suits'

# Dictionary to hold the mapping of suits to their files across folders
suits = {
    'hearts': [],
    'diamonds': [],
    'clubs': [],
    'spades': [],
}

# Function to handle name conflicts
def handle_name_conflict(target_folder, file_name):
    base_name, extension = os.path.splitext(file_name)
    counter = 1
    new_name = file_name
    # Check if file exists and create a new name if it does
    while os.path.exists(os.path.join(target_folder, new_name)):
        new_name = f"{base_name}_{counter}{extension}"
        counter += 1
    return new_name

# Go through each card folder
for card_folder in card_folders:
    # Populate the dictionary with file paths
    for folder_name in os.listdir(card_folder):
        for suit in suits:
            if suit in folder_name:
                folder_path = os.path.join(card_folder, folder_name)
                # Add all files from the current folder to the corresponding suit list
                suits[suit].extend([
                    os.path.join(folder_path, file_name)
                    for file_name in os.listdir(folder_path)
                ])

# Create folders by suit and move files into them
for suit, file_paths in suits.items():
    # Create target folder if it doesn't exist
    target_folder = os.path.join(base_path, suit)
    os.makedirs(target_folder, exist_ok=True)
    
    for file_path in file_paths:
        file_name = os.path.basename(file_path)
        # Handle name conflicts
        unique_file_name = handle_name_conflict(target_folder, file_name)
        # Move file to the target folder
        shutil.move(file_path, os.path.join(target_folder, unique_file_name))

print('Files have been organized by suit.')
