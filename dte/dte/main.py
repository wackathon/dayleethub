import os

import click


TEMPLATE_PATH = os.environ['DTE_TEMPLATE_PATH']


@click.command()
@click.option('--streakCount', 'streak_count', type=int)
@click.option('--currentDayCompleted', 'current_day_completed', type=str)
@click.argument('path', type=str)  # TODO(Anton Orlov): use path type
def app(streak_count: int, current_day_completed: str, path: str):
    assert current_day_completed in {'true', 'false'}, f"currentDayCompleted is one of 'true' or 'false'"
    with open(TEMPLATE_PATH) as template_file:
        template_source = template_file.read()
    output = template_source.replace('STREAK_SIZE', str(streak_count))
    with open(path, mode='w') as output_file:
        output_file.write(output)
