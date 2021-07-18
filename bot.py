import discord 
from discord.ext import commands
from discord_components import DiscordComponents, Button, Select, SelectOption

client = commands.Bot(command_prefix = ";") 
ddb = DiscordComponents(client)

@client.event
async def on_ready():
    print(f"{client.user} is ready!")
    DiscordComponents(client)

@client.command()
async def something(ctx):
    guild = client.get_guild(830233837119471637)
    memberList = guild.members
    print(memberList)


@client.command()
async def button(ctx):
    await ctx.send("Hello World", components=[Button(label="Wow buttons")])
    interaction = await client.wait_for("button_click", check=lambda i: i.component.label.startswith("WOW"))
    await interaction.respond(content="Button Clicked")


@client.command()
async def select(ctx):

    await ctx.send(

        "Hello, World!",

        components=[

            Select(placeholder="select something!", options=[SelectOption(
                label="a", value="A"), SelectOption(label="b", value="B")])

        ]

    )

    interaction = await client.wait_for("select_option", check=lambda i: i.component[0].value == "A")

    await interaction.respond(content=f"{interaction.component[0].label} selected!")


client.run("ODAxMDEyODc4OTM2NzY4NTIy.YAafYA.E89qrJFYeNIG35D1gto5OyLly38")
