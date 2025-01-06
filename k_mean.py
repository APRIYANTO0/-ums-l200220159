from metaflow import FlowSpec, step, catch
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

class ManyKmeansFlow(FlowSpec):
    @catch(var='error')
    @step
    def start(self):
        try:
            df = pd.read_csv('data_cleaned.csv', encoding='utf-8')
            texts = df['message'].fillna('').tolist()
            vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
            self.data = vectorizer.fit_transform(texts).toarray()
            self.vocabulary = vectorizer.get_feature_names_out()
        except Exception as e:
            print(f"Error loading data: {e}")
            self.data = np.array([])

        self.next(self.cluster_3)

    @step
    def cluster_3(self):
        if self.data.size > 0:
            kmeans_3 = KMeans(n_clusters=3, random_state=42)
            self.top_3 = self.process_clustering(kmeans_3)
        else:
            self.top_3 = []

        self.next(self.cluster_4)

    @step
    def cluster_4(self):
        if self.data.size > 0:
            kmeans_4 = KMeans(n_clusters=4, random_state=42)
            self.top_4 = self.process_clustering(kmeans_4)
        else:
            self.top_4 = []

        self.next(self.cluster_5)

    @step
    def cluster_5(self):
        if self.data.size > 0:
            kmeans_5 = KMeans(n_clusters=5, random_state=42)
            self.top_5 = self.process_clustering(kmeans_5)
        else:
            self.top_5 = []

        self.next(self.join)

    @step
    def join(self):
        self.top = {
            3: self.top_3,
            4: self.top_4,
            5: self.top_5
        }

        self.next(self.end)

    @step
    def end(self):
        self.analyze_clusters()
        print("Clustering selesai.")

    def process_clustering(self, clusterer):
        if self.data.size == 0:
            return []

        labels = clusterer.fit_predict(self.data)
        clusters = {}
        for idx, label in enumerate(labels):
            if label not in clusters:
                clusters[label] = []
            clusters[label].append(idx)

        top_words = []
        for cluster_indices in clusters.values():
            cluster_data = self.data[cluster_indices]
            cluster_centroid = cluster_data.mean(axis=0)
            top_word_indices = cluster_centroid.argsort()[-3:][::-1]
            top_cluster_words = [self.vocabulary[idx] for idx in top_word_indices]

            top_words.append(top_cluster_words)

        return top_words

    def analyze_clusters(self):
        print("Analisis Cluster:")
        for k, clusters in self.top.items():
            print(f"\nHasil Clustering {k} Kluster:")
            for i, cluster in enumerate(clusters):
                print(f"Kluster {i+1}: {cluster}")


if __name__ == '__main__':
    ManyKmeansFlow()
