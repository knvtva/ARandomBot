from discord.ext import commands
from discord.ext.commands import Context

class HelloWorld(commands.Cog, name="Hello World"):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="helloworld",
        description="Responds to the requested user Hello World",
    )

    async def hello_world(self, ctx: Context) -> None:
        await ctx.send(f"Hello, {ctx.author.name}!")

async def setup(bot) -> None:
    await bot.add_cog(HelloWorld(bot))