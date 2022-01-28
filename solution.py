# PennyMac Developer Challenge
# Utilizes Pandas library to extract data from provided data files. Outputs outline of process and solution to text
# file
# Emiliano Villalobos, January 2022

# Import libraries
import pandas as pd

# Open Output File and begin output
outputFile = open("output.txt", "w")
outputFile.write("* Weather Solution *\n")

# Constants for File paths
weatherDataPath = "w_data.dat"
soccerDataPath = "soccer.dat"

# Load Data into Dataframe for weather
outputFile.write("Importing data as a pandas Dataframe\n")
weatherData = pd.read_csv(weatherDataPath, header=2, delim_whitespace=True, usecols=[0, 1, 2],
                          names=["day", "maxTemp", "minTemp"], skipfooter=2, engine='python')

# Clean Columns from non-numeric characters
outputFile.write("Cleaning entries from non-numeric characters\n")
weatherData['maxTempClean'] = weatherData["maxTemp"].str.extract('(-?[0-9]+)')
weatherData['minTempClean'] = weatherData["minTemp"].str.extract('(-?[0-9]+)')

# Convert Clean columns to integers
outputFile.write("Converting cleaned strings to integers\n")
weatherData['maxTempClean'] = pd.to_numeric(weatherData['maxTempClean'])
weatherData['minTempClean'] = pd.to_numeric(weatherData['minTempClean'])

# Calculate Spread
outputFile.write("Calculating spread\n")
weatherData['spread'] = (weatherData['maxTempClean'] - weatherData['minTempClean']).abs()

# Record final dataframe used in output file
outputFile.write("Final Dataframe Used:\n")
outputFile.write(weatherData.to_string() + "\n")

# Locate Minimum Spread
weatherSpreadMin = weatherData[weatherData['spread'] == weatherData['spread'].min()]

# Loop through Rows with minimum spread in the case that there are multiple and output results to file
for row in range(weatherSpreadMin.shape[0]):
    outputFile.write("*Final Answer*\nDay with smallest spread: Day " + str(weatherSpreadMin.iloc[row]["day"]) + "\n\n")

# Begin output for soccer data solution
outputFile.write("* Soccer Solution *\n")

# Load Data into Dataframe for Soccer Data, dropping unhelpful rows
outputFile.write("Importing data as a pandas Dataframe\n")
soccerData = pd.read_csv(soccerDataPath, skiprows=3, delim_whitespace=True, usecols=[1, 6, 8],
                         names=['Team', 'For', 'Against'])
soccerData = soccerData.dropna('index')

# Calculate Spread, using absolute value
outputFile.write("Calculating spread\n")
soccerData['spread'] = (soccerData['For'] - soccerData['Against']).abs()

# Output final dataframe
outputFile.write("Final Dataframe Used:\n" + soccerData.to_string() + "\n")

# Locate Minimum Spread
soccerSpreadMin = soccerData[soccerData['spread'] == soccerData['spread'].min()]

# Loop through rows with minimum spread and output result to file
for row in range(soccerSpreadMin.shape[0]):
    outputFile.write("*Final Answer*\nTeam with smallest spread: " + str(soccerSpreadMin.iloc[row]["Team"]) + "\n")
