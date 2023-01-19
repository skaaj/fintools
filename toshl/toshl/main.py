if __name__ == "__main__":
    import api
    import json
    print(json.dumps(api.list_entries("2023-01-01", "2024-01-01")))
