from plugin import Plugin
import random

class Git(Plugin):

    fancy_name='Git Repo'

    async def get_commands(self, server):
        commands = [
            {
                'name': '!git',
                'description': 'Zeigt dir dir mee6 Github Seite'
            },
        ]
        return commands

    async def on_message(self, message):

        flavortext = [
            "Schön dass du frast!",
            "Du willst also den Code sehen?",
            "Hier ist der Code aber bitte skidde nicht!",
            "Bitteschön."
            ]

        if message.content == '!git':
            await self.mee6.send_message(
                message.channel,
                '{}\nhttps://github.com/Schlaubi/mee6'.format(
                random.choice(flavortext)
                )
             )
