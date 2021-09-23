import click
import yfinance as yf
@click.command()
@click.option('--symbol', help='Symbol of the stock. Eg: Apple- AAPL')
@click.option('--fr0m', help='Start date of required data')
@click.option('--t0', help='End date of requried data')
def main(symbol, fr0m, t0):
    data_df = yf.download(symbol, start=fr0m, end=t0)
    data_df.to_csv(symbol+".csv", sep=',', index=False)
    #click.echo(symbol)
    #click.echo(fr0m)
    #click.echo(t0)

if __name__=='__main__':
    main()

