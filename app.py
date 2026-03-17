import pandas as pd


def test():
    return "i'm anas and this is mlops a4"


def pretty_table_example() -> str:
    df = pd.DataFrame(
        [
            {"model": "baseline", "accuracy": 0.87, "f1": 0.84},
            {"model": "improved", "accuracy": 0.91, "f1": 0.89},
            {"model": "final", "accuracy": 0.93, "f1": 0.91},
        ]
    )
    return df.to_string(index=False)


if __name__ == "__main__":
    print(test())
    print("\nPretty metrics table:\n")
    print(pretty_table_example())
