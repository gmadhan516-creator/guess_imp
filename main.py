import os
import discord
from discord.ext import commands
from discord import app_commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Game Storage
active_players = []
host_id = None


class LobbyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Join Game", emoji="✅", style=discord.ButtonStyle.success)
    async def join_game(self, interaction: discord.Interaction, button: discord.ui.Button):

        global active_players

        if interaction.user.id not in active_players:
            active_players.append(interaction.user.id)

        embed = discord.Embed(
            title="🎭 Guess The Imposter",
            description=f"Players Joined: **{len(active_players)}**",
            color=discord.Color.blue()
        )

        player_list = ""

        for player_id in active_players:
            member = interaction.guild.get_member(player_id)
            if member:
                player_list += f"👤 {member.display_name}\n"

        if player_list == "":
            player_list = "No players yet."

        embed.add_field(
            name="Current Players",
            value=player_list,
            inline=False
        )

        await interaction.response.edit_message(
            embed=embed,
            view=self
        )

    @discord.ui.button(label="Leave Game", emoji="❌", style=discord.ButtonStyle.danger)
    async def leave_game(self, interaction: discord.Interaction, button: discord.ui.Button):

        global active_players

        if interaction.user.id in active_players:
            active_players.remove(interaction.user.id)

        embed = discord.Embed(
            title="🎭 Guess The Imposter",
            description=f"Players Joined: **{len(active_players)}**",
            color=discord.Color.blue()
        )

        player_list = ""

        for player_id in active_players:
            member = interaction.guild.get_member(player_id)
            if member:
                player_list += f"👤 {member.display_name}\n"

        if player_list == "":
            player_list = "No players yet."

        embed.add_field(
            name="Current Players",
            value=player_list,
            inline=False
        )

        await interaction.response.edit_message(
            embed=embed,
            view=self
        )

    @discord.ui.button(label="Start Game", emoji="🚀", style=discord.ButtonStyle.primary)
    async def start_game(self, interaction: discord.Interaction, button: discord.ui.Button):

        global host_id

        if interaction.user.id != host_id:
            await interaction.response.send_message(
                "❌ Only the host can start the game.",
                ephemeral=True
            )
            return

        if len(active_players) < 3:
            await interaction.response.send_message(
                "❌ Need at least 3 players.",
                ephemeral=True
            )
            return

        await interaction.response.send_message(
            f"🎉 Game starting with {len(active_players)} players!\n\nNext stage: Imposter Selection",
            ephemeral=False
        )


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash commands")
    except Exception as e:
        print(e)


@bot.tree.command(
    name="ping",
    description="Check if the bot is online"
)
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(
        "🏓 Pong! Guess The Imposter Bot is online."
    )


@bot.tree.command(
    name="imposter",
    description="Create a new Guess The Imposter lobby"
)
async def imposter(interaction: discord.Interaction):

    global active_players
    global host_id

    active_players = []
    host_id = interaction.user.id

    embed = discord.Embed(
        title="🎭 Guess The Imposter",
        description="Press Join Game to enter the lobby.",
        color=discord.Color.purple()
    )

    embed.add_field(
        name="Players",
        value="No players yet.",
        inline=False
    )

    embed.set_footer(
        text=f"Host: {interaction.user.display_name}"
    )

    await interaction.response.send_message(
        embed=embed,
        view=LobbyView()
    )


bot.run(TOKEN)import os
import discord
from discord.ext import commands
from discord import app_commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Game Storage
active_players = []
host_id = None


class LobbyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Join Game", emoji="✅", style=discord.ButtonStyle.success)
    async def join_game(self, interaction: discord.Interaction, button: discord.ui.Button):

        global active_players

        if interaction.user.id not in active_players:
            active_players.append(interaction.user.id)

        embed = discord.Embed(
            title="🎭 Guess The Imposter",
            description=f"Players Joined: **{len(active_players)}**",
            color=discord.Color.blue()
        )

        player_list = ""

        for player_id in active_players:
            member = interaction.guild.get_member(player_id)
            if member:
                player_list += f"👤 {member.display_name}\n"

        if player_list == "":
            player_list = "No players yet."

        embed.add_field(
            name="Current Players",
            value=player_list,
            inline=False
        )

        await interaction.response.edit_message(
            embed=embed,
            view=self
        )

    @discord.ui.button(label="Leave Game", emoji="❌", style=discord.ButtonStyle.danger)
    async def leave_game(self, interaction: discord.Interaction, button: discord.ui.Button):

        global active_players

        if interaction.user.id in active_players:
            active_players.remove(interaction.user.id)

        embed = discord.Embed(
            title="🎭 Guess The Imposter",
            description=f"Players Joined: **{len(active_players)}**",
            color=discord.Color.blue()
        )

        player_list = ""

        for player_id in active_players:
            member = interaction.guild.get_member(player_id)
            if member:
                player_list += f"👤 {member.display_name}\n"

        if player_list == "":
            player_list = "No players yet."

        embed.add_field(
            name="Current Players",
            value=player_list,
            inline=False
        )

        await interaction.response.edit_message(
            embed=embed,
            view=self
        )

    @discord.ui.button(label="Start Game", emoji="🚀", style=discord.ButtonStyle.primary)
    async def start_game(self, interaction: discord.Interaction, button: discord.ui.Button):

        global host_id

        if interaction.user.id != host_id:
            await interaction.response.send_message(
                "❌ Only the host can start the game.",
                ephemeral=True
            )
            return

        if len(active_players) < 3:
            await interaction.response.send_message(
                "❌ Need at least 3 players.",
                ephemeral=True
            )
            return

        await interaction.response.send_message(
            f"🎉 Game starting with {len(active_players)} players!\n\nNext stage: Imposter Selection",
            ephemeral=False
        )


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash commands")
    except Exception as e:
        print(e)


@bot.tree.command(
    name="ping",
    description="Check if the bot is online"
)
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(
        "🏓 Pong! Guess The Imposter Bot is online."
    )


@bot.tree.command(
    name="imposter",
    description="Create a new Guess The Imposter lobby"
)
async def imposter(interaction: discord.Interaction):

    global active_players
    global host_id

    active_players = []
    host_id = interaction.user.id

    embed = discord.Embed(
        title="🎭 Guess The Imposter",
        description="Press Join Game to enter the lobby.",
        color=discord.Color.purple()
    )

    embed.add_field(
        name="Players",
        value="No players yet.",
        inline=False
    )

    embed.set_footer(
        text=f"Host: {interaction.user.display_name}"
    )

    await interaction.response.send_message(
        embed=embed,
        view=LobbyView()
    )


bot.run(TOKEN)
