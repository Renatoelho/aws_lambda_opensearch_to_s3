
index_query = {
    "size": 0,
    "aggs": {
        "max_data_processamento": {
            "max": {
                "field": "data_processamento"
            }
        },
        "doc_count": {
            "value_count": {
                "field": "_index"
            }
        }
    }
}