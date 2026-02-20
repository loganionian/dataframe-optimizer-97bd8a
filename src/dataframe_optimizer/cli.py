import click
import pandas as pd
from .core import optimize

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
def cli(input_file, output_file):
    """Optimize a DataFrame from an input CSV file and save it to an output CSV file."""
    df = pd.read_csv(input_file)
    optimized_df = optimize(df)
    optimized_df.to_csv(output_file, index=False)

if __name__ == '__main__':
    cli()