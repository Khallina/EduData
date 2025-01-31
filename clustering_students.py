import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def main():

    df = pd.read_csv("MainTable.csv")

    attempt_counts = (
        df.groupby(['SubjectID', 'ProblemID'])['EventID']
        .nunique()  # counts unique EventIDs
        .reset_index(name='num_attempts')
    )

    avg_attempts_per_student = (
        attempt_counts
        .groupby('SubjectID')['num_attempts']
        .mean()
        .reset_index(name='avg_attempts')
    )

    # COMPUTE AVERAGE SCORE PER STUDENT


    avg_score_per_student = (
        df.groupby('SubjectID')['Score']
        .max()
        .reset_index(name='avg_score')
    )

    # MERGE AVERAGE ATTEMPTS AND AVERAGE SCORES
    student_stats = pd.merge(
        avg_attempts_per_student,
        avg_score_per_student,
        on='SubjectID',
        how='inner'
    ).dropna()

    # PERFORM K-MEANS CLUSTERING ON [avg_attempts, avg_score]
    X = student_stats[['avg_attempts', 'avg_score']]

    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(X)

    # Assign cluster labels
    student_stats['cluster'] = kmeans.labels_

    # INSPECT CORRELATION & PLOT THE CLUSTERS

    correlation = student_stats['avg_attempts'].corr(student_stats['avg_score'])
    print("Correlation between avg_attempts and avg_score:", correlation)

    # Scatter plot
    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(
        student_stats['avg_attempts'],
        student_stats['avg_score'],
        c=student_stats['cluster'],
        cmap='viridis',
        alpha=0.7
    )
    plt.xlabel('Average Attempts')
    plt.ylabel('Average Score')
    plt.title('Student Clusters by Attempts vs. Score')
    plt.colorbar(scatter, label='Cluster')
    plt.show()


if __name__ == "__main__":
    main()
