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


@cli.command()
@click.argument('path')
@click.password_option()
@click.option('--name', required=True)
@click.option('--username', required=False)
@click.option('--password', 'pwd', required=False)
def update(path, password, name, username, pwd):
    ok = store.update_entry(path, password, name, username=username, pwd=pwd)
    click.echo("Updated" if ok else "Not found")


@cli.command()
@click.argument('path')
@click.password_option()
@click.option('--name', required=True)
def delete(path, password, name):
    ok = store.delete_entry(path, password, name)
    click.echo("Deleted" if ok else "Not found")


@cli.command()
@click.argument('path')
@click.password_option()
@click.option('--query', required=True)
def search(path, password, query):
    results = store.search_entries(path, password, query)
    for e in results:
        click.echo(f"{e['name']} {e['username']}")

if __name__ == '__main__':
    cli()
