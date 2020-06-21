from .classifier import pick_best_model
from .data_treatment import read_data


def main(input_path="data", output_path="models"):
    x, y = read_data(f"{input_path}/entries.tsv")
    identifier = "modelo_1"

    _, config, best_model, tokenizer = pick_best_model(identifier, x, y, output_path)


if __name__ == '__main__':
    main()
