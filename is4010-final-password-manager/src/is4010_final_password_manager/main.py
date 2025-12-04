import click
from . import store

@click.group()
def cli():
    pass

@cli.command()
@click.argument('path')
@click.password_option()
def init(path, password):
    store.init_store(path, password)
    click.echo(f"Created store at {path}")

@cli.command()
@click.argument('path')
@click.password_option()
@click.option('--name', required=True)
@click.option('--username', required=True)
@click.option('--password', 'pwd', required=True)
def add(path, password, name, username, pwd):
    store.add_entry(path, password, name, username, pwd)
    click.echo(f"Added entry {name}")

@cli.command()
@click.argument('path')
@click.password_option()
@click.option('--name', required=True)
def get(path, password, name):
    entry = store.get_entry(path, password, name)
    if entry:
        click.echo(f"{entry['name']} {entry['username']} {entry['password']}")
    else:
        click.echo("Not found")

@cli.command()
@click.argument('path')
@click.password_option()
def list_cmd(path, password):
    names = store.list_entries(path, password)
    for n in names:
        click.echo(n)


@cli.command()
@click.option('--length', default=16, type=int)
@click.option('--no-symbols', is_flag=True)
def generate(length, no_symbols):
    pwd = store.generate_password(length=length, use_symbols=not no_symbols)
    click.echo(pwd)

if __name__ == '__main__':
    cli()
