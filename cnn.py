google.colab import drive
import pandas as pd
drive.mount('/content/drive')
file_path = "/contentfro/drive/Shared drives/Your Drive Name/dataset.csv"
df = pd.read_csv(file_path)
