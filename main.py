import discord
from discord.ext import commands
import asyncio
from selenium import webdriver
import pyautogui

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle , activity=discord.Game(name=" !help"))
    print("I am ready!")
    print(f"Bot is ready! Latency: {round(bot.latency*1000)}ms")


@bot.command()
async def ping(ctx):
    
    await ctx.reply(f" Latency: {round(bot.latency*1000) }ms")

@bot.command()
async def clear (ctx , amount=10):
    await ctx.channel.purge(limit=amount+1)


@bot.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not role:
        role = await ctx.guild.create_role(name="Muted", reason="Mute Role")
        permissions = discord.Permissions(send_messages=False)
        await role.edit(permissions=permissions)
        for channel in ctx.guild.channels:
            await channel.set_permissions(role, send_messages=False)

    await member.add_roles(role)
    await ctx.reply(f"تم إسكات العضو {member.mention}")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def unmute(ctx , member: discord.Member ) :
 role = discord.utils.get(ctx.guild.roles, name="Muted")
    
 if role in member.roles:
        await member.remove_roles(role)
        await ctx.reply(f"تم إلغاء الاسكات عن العضو {member.mention}")
 else:
        await ctx.reply(f"العضو {member.mention} ليس مكتومًا بالفعل")

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: commands.MemberConverter, *, reason=None):
    await member.ban(reason=reason)
    await ctx.reply(f"تم حظر العضو {member.mention} بنجاح")



@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx , member: discord.Member , reason=None):
    await member.kick(reason=reason)
    await ctx.reply("تم طرد هذا العضو")

@bot.command()
async def avatar(ctx, member: discord.Member = None):
    
    if member is None:
        member = ctx.author

    
    avatar_url = member.avatar.url

 
    embed = discord.Embed(title=f"صورة الملف الشخصي لـ {member.display_name}")
    embed.set_image(url=avatar_url)

    await ctx.reply(embed=embed)


@bot.command()
async def info(ctx):
    server = ctx.guild
    name = server.name
    description = server.description
    owner = server.owner
    region = "EGYPT"
    member_count = server.member_count
    online_members = [member.display_name for member in ctx.guild.members if member.status == discord.Status.online or  member.status == discord.Status.idle or  member.status == discord.Status.do_not_disturb]
    online_members_count = len(online_members)
    offline_members=[member.display_name for member in ctx.guild.members if member.status == discord.Status.offline]
    offline_members_count=len(offline_members)
    
    embed = discord.Embed(title=name, description=description, color=discord.Color.red())
    embed.set_thumbnail(url=server.icon.url)
    embed.add_field(name="المالك", value=owner.mention)
    embed.add_field(name="الدولة", value=region)
    embed.add_field(name="عدد الأعضاء", value=member_count)
    embed.add_field(name="الاعضاء المتصلين" , value=online_members_count)
    embed.add_field(name="الاعضاء الغير متصلين " , value=offline_members_count)
    embed.add_field(name="المطور", value="! Youssef Fathey#5990")
    

    await ctx.reply(embed=embed)




@bot.command()
async def botinfo(ctx):
    
    embed = discord.Embed(title="معلومات البوت", color=discord.Color.blue())
    embed.set_thumbnail(url=bot.user.avatar.url)
    embed.add_field(name="الوصف", value="بوت سيستم تحت التطوير", inline=False)
    embed.add_field(name="الإصدار", value="1.0.0", inline=False)
    embed.add_field(name="المطور", value="! Youssef Fathey#5990", inline=False)
    

    

    await ctx.reply(embed=embed)

@bot.command()
@commands.has_any_role("👑owner👑")  
async def say(ctx, channel: discord.TextChannel = None, *, message=None):
    if message and not channel:
        await ctx.reply("يرجى تحديد اسم الروم لإرسال الرسالة إليه")
        return
    if channel and not message:
        await ctx.reply("لا يوجد محتوى للرسالة 🤨")
        return


    embed = discord.Embed(title="رسالة البوت", description=message, color=discord.Color.blurple())
    await channel.send(embed=embed )








bot.run("MTA3ODQ4NTkzODc2NzkyNTM0OA.GLD_Lm.dLEI7palznMYHnHB9WHFcutiH1zGTP2ZisSD4E")
