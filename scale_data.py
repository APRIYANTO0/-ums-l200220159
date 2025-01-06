import tarfile
from itertools import islice
from metaflow import S3
import pandas as pd

def load_data_group(num_docs):
    """Memuat data dari file data_group.csv"""
    # Pastikan path 'data_group.csv' sesuai
    data_path = '/ums-l200220159.github.io/data_group.csv'
    
    # Membaca file CSV
    data = pd.read_csv(data_path)
    
    # Mengambil sejumlah dokumen tertentu (num_docs)
    return data['text'][:num_docs].tolist()

def make_matrix(docs, binary=False):
    """Membuat matriks fitur berdasarkan dokumen."""
    from sklearn.feature_extraction.text import CountVectorizer
    
    # Membuat CountVectorizer
    vec = CountVectorizer(min_df=10, max_df=0.1, binary=binary)
    
    # Transformasi dokumen menjadi matriks
    mtx = vec.fit_transform(docs)
    
    # Membuat daftar kolom (fitur)
    cols = [None] * len(vec.vocabulary_)
    for word, idx in vec.vocabulary_.items():
        cols[idx] = word
    
    return mtx, cols

# Contoh penggunaan
if __name__ == "__main__":
    num_docs = 100  # Tentukan jumlah dokumen yang ingin dimuat
    docs = load_data_group(num_docs)  # Memuat data dari file data_group.csv
    mtx, cols = make_matrix(docs, binary=False)  # Membuat matriks fitur
    
    # Menampilkan hasil matriks fitur
    print(f"Matriks fitur: {mtx.shape}")
    print(f"Fitur pertama: {cols[:10]}")