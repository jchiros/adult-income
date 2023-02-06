import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
import sql

def plot_agerace(data):
    data['Age Range'] = pd.cut(data['age'], [0, 18, 25, 35, 60, 100], labels=['0-18', '18-25', '25-35', '35-60', '60+'])

    age_range_counts = data.groupby(['Age Range']).size().reset_index(name='Counts')

    fig, axs = plt.subplots(1, 2, figsize=(8, 4))
    axs[0].bar(age_range_counts['Age Range'], age_range_counts['Counts'])
    axs[0].set_xlabel('Age Range')
    axs[0].set_ylabel('Counts')
    axs[0].set_title('Age Range Distribution')

    race_counts = data.groupby(['race']).size().reset_index(name='Counts')

    axs[1].pie(race_counts['Counts'], labels=race_counts['race'], autopct='%1.1f%%')
    axs[1].set_title('Race Distribution')
    plt.show()


if __name__ == "__main__":
    db = sql.Database("adult_income.db")
    df = pd.DataFrame(db.fetch(), columns=["primary_key", "age", "workclass", "education", "occupation", "race", "gender", "hours_per_week", "native_country", "income"])
    print(df.columns)
    plot_agerace(df)
