from .udf import Udf


if __name__ == "__main__":
    udf = Udf()
    udf.load_jsonconfig()
    udf.to_udf()
