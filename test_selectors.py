import requests
import pandas as pd
import time
from collections import defaultdict

# Load data to get sample URLs for each source
cached_data = pd.read_json("news_data/cryptopanic_all_cache.json").T
cached_data = cached_data.reset_index(drop=True)
unique_source_cached_data = cached_data.loc[cached_data['Source'].drop_duplicates().index]
unique_source_cached_data['news_redirect'] = 'https://cryptopanic.com/news/click/' + unique_source_cached_data['URL'].str.split('/').str[2] + '/'

# Import all headers from data_load.py
batch_1 = {
    "99bitcoins.com": {
        "Accept": "application/json",
        "Authorization": "Bearer jina_4d7479b1a43542138c177e3e3a76f7c7RgVhcuusmPIdTaGzSVumpW_Zf3Gi",
        "X-Retain-Images": "none",
        "X-Target-Selector": ".nnbtc-article__content-main",
        "X-Remove-Selector": "section ~ *"
    },
    "@btc_archive": {
        "Accept": "application/json",
        "Authorization": "Bearer jina_4d7479b1a43542138c177e3e3a76f7c7RgVhcuusmPIdTaGzSVumpW_Zf3Gi",
        "X-Retain-Images": "none",
        "X-Target-Selector": "article"
    },
    "@cryptoquant_com": {
        "Accept": "application/json",
        "Authorization": "Bearer jina_4d7479b1a43542138c177e3e3a76f7c7RgVhcuusmPIdTaGzSVumpW_Zf3Gi",
        "X-Retain-Images": "none",
        "X-Target-Selector": "article"
    },
    "@daancrypto": {
        "Accept": "application/json",
        "Authorization": "Bearer jina_4d7479b1a43542138c177e3e3a76f7c7RgVhcuusmPIdTaGzSVumpW_Zf3Gi",
        "X-Retain-Images": "none",
        "X-Target-Selector": "article"
    },
    "@lookonchain": {
        "Accept": "application/json",
        "Authorization": "Bearer jina_4d7479b1a43542138c177e3e3a76f7c7RgVhcuusmPIdTaGzSVumpW_Zf3Gi",
        "X-Retain-Images": "none",
        "X-Target-Selector": "article"
    }
}
