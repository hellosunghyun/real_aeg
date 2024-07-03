from nextcord import Interaction, Embed, ui, ButtonStyle, InteractionType
from nextcord.ext import commands
import os

DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")

bot = commands.Bot()

SERVER_ID = int(os.environ.get("SERVER_ID"))
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))
ROLE_ID = int(os.environ.get("ROLE_ID"))

class party_view(ui.View):
    def __init__(self):
        super().__init__()
        self.embeds = []
        self.embeds.append(Embed(title="진짜 반쪽이가 되시겠습니까?",
                                 description=f"아래 인증하기 버튼을 눌러 진짜 반쪽이가 되세요!", color=0x00ff00))
        self.embeds[0].set_footer(text="인증 완료시 채널 조회가 가능합니다.")
        self.add_item(ui.Button(label="인증하기", style=ButtonStyle.green, custom_id="verify"))

@bot.event
async def on_ready():
    print("Bot is ready.")

@bot.slash_command(name="인증시작", description="인증을 시작해요.", guild_ids=[SERVER_ID])
async def 파티(interaction: Interaction):
    if interaction.channel_id == CHANNEL_ID:
        view = party_view()
        await interaction.response.send_message(embeds=view.embeds, view=view)
    else:
        await interaction.response.send_message("이 채널에서는 사용할 수 없습니다.", ephemeral=True)

@bot.listen()
async def on_interaction(interaction: Interaction):
    if interaction.type == InteractionType.component:
        if interaction.data["custom_id"] == "verify":
            guild = interaction.guild
            role = guild.get_role(ROLE_ID)
            await interaction.user.add_roles(role)
            await interaction.response.send_message("인증이 완료 되었어요!", ephemeral=True)

bot.run(DISCORD_BOT_TOKEN)