# common
command_prefix = '!'
error = 'I\'m sorry %s. I\'m afraid I can\'t do that.'

## COMMANDS
# 8ball
magicball_responses = [
    # affirmative
    'It is certain.',
    'It is decidedly so.',
    'Without a doubt.',
    'Yes – definitely.',
    'You may rely on it.',
    'As I see it, yes.',
    'Most likely.',
    'Outlook good.',
    'Yes.',
    'Signs point to yes.',

    # non-committal
    'Reply hazy, try again.',
    'Ask again later.',
    'Better not tell you now.',
    'Cannot predict now.',
    'Concentrate and ask again.',

    # negative
    'Don\'t count on it.',
    'My reply is no.',
    'My sources say no.',
    'Outlook not so good.',
    'Very doubtful.',
]
magicball_error = 'Please include a question in your message.'

# choose
choose_result = 'I have chosen: %s'
choose_nooptions = choose_result % 'give me some options'

# help
help_all = f"""
```
{command_prefix}8ball  | Consult the Magic 8-Ball.
{command_prefix}choose | Make a choice. Separate options with " or ".
{command_prefix}quote  | Quote of the day.
{command_prefix}roll   | Roll some dice. Try "!roll 2d6" or "!roll d4".
```
"""

# quote
quote_response = '```"An SSL error has occured and a secure connection to the server cannot be made." - William Shakespeare```'

# roll
roll_result = 'You rolled %s.'
roll_error = 'Bad argument. Try `!roll 2d6` or `!roll d4`.'

## OTHER
## ree
reegex = '(\\s|^)re{2,}(\\s|$)';
ree = 'reeeeeeeeeeeeeeeee'

## same
same = 'same'
