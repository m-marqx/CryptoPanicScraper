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


batch_2 = {
    "@rewkang": {
        "Accept": "application/json",
        "Authorization": "Bearer jina_4d7479b1a43542138c177e3e3a76f7c7RgVhcuusmPIdTaGzSVumpW_Zf3Gi",
        "X-Retain-Images": "none",
        "X-Target-Selector": "article"
    },
    "@solidintel_x": {
        "Accept": "application/json",
        "Authorization": "Bearer jina_4d7479b1a43542138c177e3e3a76f7c7RgVhcuusmPIdTaGzSVumpW_Zf3Gi",
        "X-Retain-Images": "none",
        "X-Target-Selector": "article"
    },
    "ambcrypto.com": {
        "Accept": "application/json",
        "Authorization": "Bearer jina_4d7479b1a43542138c177e3e3a76f7c7RgVhcuusmPIdTaGzSVumpW_Zf3Gi",
        "X-Retain-Images": "none",
        "X-Target-Selector": ".post-inner-content",
        "X-Remove-Selector": "div[id^='amb_article_'], .amb-trending-posts, header, .breadcrumbs, .post-category, .post-meta, .social-share, .author-box, .related-posts, footer"
    },
    "atlas21.com": {
        "Accept": "application/json",
        "Authorization": "Bearer jina_4d7479b1a43542138c177e3e3a76f7c7RgVhcuusmPIdTaGzSVumpW_Zf3Gi",
        "X-Retain-Images": "none",
        "X-Target-Selector": ".entry-content"
    },
    "bankless.com": {
        "Accept": "application/json",
        "Authorization": "Bearer jina_4d7479b1a43542138c177e3e3a76f7c7RgVhcuusmPIdTaGzSVumpW_Zf3Gi",
        "X-Retain-Images": "none",
        "X-Target-Selector": ".post-content",
        "X-Remove-Selector": ".postSponsor, #cookies-eu-banner"
    }
}

batch_3 = {
    "beincrypto.com": {
        "Accept": "application/json",
        "Authorization": "Bearer jina_4d7479b1a43542138c177e3e3a76f7c7RgVhcuusmPIdTaGzSVumpW_Zf3Gi",
        "X-Retain-Images": "none",
        "X-Target-Selector": "div.Content-sc-e9e4289e-11",
        "X-Remove-Selector": ".MoreByAuthor-sc-4b5de9b4-0, .ShareArticle-sc-4d23ff5e-0, .TopPlatforms-sc-8ba59215-6, .MostRead-sc-15cb59b9-11, .Newsletter-sc-f28af7a7-0, header, footer"
    },
    "blocknews.com": {
        "Accept": "application/json",
        "Authorization": "Bearer jina_4d7479b1a43542138c177e3e3a76f7c7RgVhcuusmPIdTaGzSVumpW_Zf3Gi",
        "X-Retain-Images": "none",
        "X-Target-Selector": ".content-inner",
        "X-Remove-Selector": ".jeg_share_top, .jeg_share_bottom, .jnews_prev_next_container, .jnews_author_box_container, .jnews_related_post_container, .jnews_comment_container"
    },
    "blockworks.co": {
        "Accept": "application/json",
        "Authorization": "Bearer jina_4d7479b1a43542138c177e3e3a76f7c7RgVhcuusmPIdTaGzSVumpW_Zf3Gi",
        "X-Retain-Images": "none",
        "X-Target-Selector": "article"
    },
    "br.beincrypto.com": {
        "Accept": "application/json",
        "Authorization": "Bearer jina_4d7479b1a43542138c177e3e3a76f7c7RgVhcuusmPIdTaGzSVumpW_Zf3Gi",
        "X-Retain-Images": "none",
        "X-Target-Selector": "div.Content-sc-e9e4289e-11"
    },
    "catenaa.com": {
        "Accept": "application/json",
        "Authorization": "Bearer jina_4d7479b1a43542138c177e3e3a76f7c7RgVhcuusmPIdTaGzSVumpW_Zf3Gi",
        "X-Retain-Images": "none",
        "X-Target-Selector": "article"
    }
}

