import pandas as pd
import csv
import matplotlib.pyplot as plt

df = pd.read_csv('results.txt', sep=',')
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')
df.to_csv('output_file.csv', index=False)

print(df.columns)
print(df.info())  # Display information about the DataFrame, including column names and data types"
#print(df.shape) # it gives the number of rows and columns in the form of a tuple"

with open('output_file.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
    print(data)

prof = set()
for lines in data:
   prof.add(lines[1])
print(prof)

prof_dev = 0
hobby_dev = 0
learning_dev = 0
earlier_dev = 0
temp_dev = 0

for line in data:
    if line[1] == 'I am a developer by profession':
        prof_dev += 1
    elif line[1] == 'I code primarily as a hobby':
        hobby_dev += 1
    elif line[1] == 'I am learning to code':
        learning_dev += 1
    elif line[1] == 'I used to be a developer by profession, but no longer am':
        earlier_dev += 1
    else:
        temp_dev += 1
print(prof_dev, hobby_dev, learning_dev, earlier_dev, temp_dev)

total_respondents = len(data) - 1
print(f"percentage of developers by profession: {prof_dev / total_respondents * 100:.2f}%")
print(f"percentage of developers by hobby: {hobby_dev / total_respondents * 100:.2f}%")
print(f"percentage of developers learning to code: {learning_dev / total_respondents * 100:.2f}%")
print(f"percentage of developers who used to be professionals: {earlier_dev / total_respondents * 100:.2f}%")
print(f"percentage of people who write code sometimes: {temp_dev / total_respondents * 100:.2f}%")

#Number of people who writes code in each country:
country_count = {}
country_index = data[0].index('Country')
for line in data[1:]:
   country = line[country_index]
   if country in country_count:
      country_count[country] += 1
   else:
      country_count[country] = 1
      
for country, count in country_count.items():
   print(f"{country}: {count}")

prof_dev_usa = 0
for line in data[1:]:
    country = line[country_index]
    if line[1] == 'I am a developer by profession' and country == 'United States of America':
        prof_dev_usa += 1
print(f"percentage of developers by profession in USA: {prof_dev_usa}/{country_count['United States of America']} = {prof_dev_usa / country_count['United States of America'] * 100:.2f}%")
print(f"percentage of developers by profession from USA in total developers by profession: {prof_dev_usa}/{prof_dev} = {prof_dev_usa / prof_dev * 100:.2f}%")
print(f"percentage of developers by profession from USA in total population: {prof_dev_usa}/{total_respondents} = {prof_dev_usa / total_respondents * 100:.2f}%")

prof_dev_india = 0
for line in data[1:]:
    country = line[country_index]
    if line[1] == 'I am a developer by profession' and country == 'India':
        prof_dev_india += 1
print(f"percentage of developers by profession in India: {prof_dev_india}/{country_count['India']} = {prof_dev_india / country_count['India'] * 100:.2f}%")
print(f"percentage of developers by profession from India in total developers by profession: {prof_dev_india}/{prof_dev} = {prof_dev_india / prof_dev * 100:.2f}%")
print(f"percentage of developers by profession from India in total population: {prof_dev_india}/{total_respondents} = {prof_dev_india / total_respondents * 100:.2f}%")

#Number of developers by profession in each country:

lst1 = list(df[df['MainBranch'] == 'I am a developer by profession']['Country'].value_counts())
print(lst1)
prof_dev = df[df["mainbranch"] == "I am a developer by profession"]["country"].value_counts()
for country, developers in prof_dev.items():
    print(f"{country}: {developers}")

#df["Age"].describe()
#df["age"].value_counts()
print("Percentage of each age group:")
print(f" {df['age'].value_counts(normalize=True)*100}%")
    
age_value = df["age"].value_counts()
percentage = age_value / len(df) * 100
print(f"Percentage of each age group:")
print(f"{percentage}")

languages = df["languagehaveworkedwith"].dropna().str.split(";").explode()
language_counts = languages.value_counts()
print(language_counts)

for language, count in language_counts.items():
   dict[language] = count / len(df) * 100
print(dict)
    
language_percentage = language_counts / len(df) * 100
print(language_percentage) 
df.groupby(["mainbranch", "age"]).size()

df[df["mainbranch"] == "I am a developer by profession"]["age"].value_counts()
dev_by_profession = df[df["mainbranch"] == "I am a developer by profession"]
dev_by_profession_age_count = dev_by_profession["age"].value_counts()
percentage = dev_by_profession_age_count / len(dev_by_profession) * 100
print(f" percentage of each age group among those a developer by profession is: {percentage.round(2)})")

  
learning_to_code = df[df["mainbranch"] == "I am learning to code"]
learning_to_code_age_count = learning_to_code["age"].value_counts()
percentage = learning_to_code_age_count / len(learning_to_code) * 100
print(f" percentage of each age group among those learning to code is: {percentage.round(2)}")

learning_age = learning_to_code["age"].value_counts()
professional_age = dev_by_profession["age"].value_counts()
print("Learning to code:")
print(learning_age)
print("Professional developers:")
print(professional_age)
   
groups = ["Professional Developers", "Learning to Code"]
percentages = [18, 55.46]

plt.bar(groups, percentages)
plt.title("Percentage of Respondents Aged 18–24")
plt.xlabel("Respondent Group")
plt.ylabel("Percentage (%)")
plt.ylim(0, 100)
# Display percentage values above the bars
for i, value in enumerate(percentages):
    plt.text(i, value + 1, f"{value:.2f}%", ha="center")
plt.show()
