import disnake
from disnake.ext import commands


class verify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command()
    async def verify(self, interaction, member: disnake.Member):
        if interaction.channel.id != 1220617267327406170: # пишем id канала, в котором будет доступна данная команда
            return
        member = member or interaction.author
        role = interaction.guild.get_role(1220617192379252767) # пишем id роли, которая будет выдаватся юзеру которого мы указали в команде
        delete_role = interaction.guild.get_role(1220617193327300608) # пишем id роли, которая будет забиратся у юзера которого мы указали в команде (советуется использовать автороль)
        await member.add_roles(role)
        await member.remove_roles(delete_role)
        await member.send("Пользователь успешно верифицирован!") # получaем сообщение от бота
        await interaction.response.send_message("Пользователь успешно верифицирован!", ephemeral=True) # получaем сообщение от бота



def setup(bot):
    bot.add_cog(verify(bot))



