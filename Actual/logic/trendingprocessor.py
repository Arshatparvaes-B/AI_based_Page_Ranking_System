import numpy as np
import pandas as pd

def search_goal_creator():
        # File paths
    file_paths = ['logic\searches_1_global.txt', 'logic\searches_2_india.txt','logic\preferences.txt']

    # Set to store unique topics
    unique_topics_set = set()

    # Traverse over each file
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            # Read each line in the file
            for line in file:
                # Remove leading and trailing whitespaces
                topic = line.strip()
                
                # Check if the topic is not already in the set
                if topic not in unique_topics_set:
                    # Add the topic to the set
                    unique_topics_set.add(topic)

def search_domain_creator():
# Load the CSV file into a Pandas DataFrame
    file_path = 'your_file.csv'
    df = pd.read_csv(file_path)
    # Extract the first 10 million URLs into a NumPy array
    urls_array = np.array(df['domain'][:10000000])
    # Print the first few URLs for verification
    print(urls_array[:10])



def heuristic_creator():
    # Load your DataFrame from the CSV file
    df = pd.read_csv('logic/top10milliondomains.csv', encoding='utf-8')
    # Extract domain names and Open PageRank values
    domains = df['Domain'][:10000000]
    openpagerank = df['Open Page Rank'][:10000000]
    # Create a structured NumPy array with two fields: 'domain' and 'openpagerank'
    dt = np.dtype([('Domain', 'U50'), ('Openpagerank', float)])
    urls_array = np.empty(len(domains), dtype=dt)
    urls_array['Domain'] = domains
    urls_array['Openpagerank'] = openpagerank
    return urls_array
#don't run this file as it the unique_topics numpy array is already created.
#main program
if __name__=="__main__":

    #dont run this file as the processed data is already stored in top_1mil_urls.npy
#heuristic creation.
    # unique_topics_set=heuristic_creator()
    # unique_topics_array = np.array(list(unique_topics_set))
    # np.save('logic\unique_topics_array.npy',unique_topics_array,allow_pickle=True)
    # # Load the array from the file
    # loaded_array = np.load('logic\unique_topics_array.npy')
    # print(loaded_array)
#search space creation.
    # urls_array=heuristic_creator()
    # print(urls_array[:10])
    # np.save('logic/top_10mil_urls.npy', urls_array,allow_pickle=True)

    # Load and print the first 10 rows of the saved NumPy array
    loaded_array_1 = np.load('logic/top_10mil_urls.npy')
    loaded_array_2= np.load('logic/top_1mil_urls.npy',allow_pickle=True)
    loaded_array_3=np.load('logic/unique_topics.npy')
    print("The Heuristic function is:.....",loaded_array_1[:10])
    print("The search space space/nodes to be explored is..",loaded_array_2[:10])
    print("The goal states are.........",loaded_array_3[:10])




