
import pandas as pd

from utils.queries import index_query
from connections.connections import OpenSearchClient


data = []
opensearch = OpenSearchClient()


def formats_data(index_list: list) -> object:
    for index_name in index_list:
        try:
            response = opensearch.search(
                index_name,
                index_query
            )
        except Exception as error:
            print(error)
            response = {}
        
        max_agg = response.get("aggregations", {}).get("max_data_processamento", {})
        max_value = max_agg.get("value_as_string", "NULL")

        doc_count_agg = response.get("aggregations", {}).get("doc_count", {})
        doc_count = doc_count_agg.get("value", 0)

        data.append({
            "index_name": index_name,
            "max_data_processamento": max_value,
            "doc_count": doc_count
        })

    df_indexes = pd.DataFrame(data)
    print(df_indexes)
    return df_indexes.to_csv(sep=";", index=False)
