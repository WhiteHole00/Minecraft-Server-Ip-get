import discord,os
client = discord.Client(Intents = discord.Intents.all())
import os,subprocess, base64

#서버 아이피 확인
#마인리스트 추천조작 잔액 미연동
#SuperMinelist

@client.event
async def on_message(message):
    if(message.content.lower().startswith("!ip ")):
        if( not message.channel.id == 123123132):
            return
        replied_msg = await message.reply("진행중..")
        dmin = message.content.split(" ")[1]
        print(dmin)
        try:
            proc = subprocess.Popen(["powershell", "-EncodedCommand", base64.b64encode(f"ping {dmin} -n 1 -w 1".encode('utf-16-le')).decode()], stdout=subprocess.PIPE)
            out, err = proc.communicate()
            print(out)
            normal_ping = str(out).split("[")[1].split("]")[0]
        except:
            normal_ping = "보안도메인이여서 일반 아이피 없습니다"
        try:
            p = subprocess.Popen(
                ['cmd'],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
            p.stdin.write(b"NSLOOKUP\n")
            p.stdin.flush()
            p.stdin.write(b'set type=srv\n')
            p.stdin.flush()
            p.stdin.write(f'_minecraft._tcp.{dmin}\n'.encode())

            stdout, stderr = p.communicate()
            listed_str =  list(str(stdout).split("svr hostname   = ")[1].split(" ")[0])
            listed_str.reverse()
            listed_str = listed_str[5:]
            listed_str.reverse()
            domain_or_ip = "".join(listed_str  )
            



            proc = subprocess.Popen(["powershell", "-EncodedCommand", base64.b64encode(f"ping {domain_or_ip} -n 1 -w 1".encode('utf-16-le')).decode()], stdout=subprocess.PIPE)
            out, err = proc.communicate()
            p = subprocess.Popen(
                ['cmd'],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
            
            srv_pinged = str(out).split("[")[1].split("]")[0]
        except:
            srv_pinged = "일반도메인이라 보안아이피 없"

        embed=discord.Embed()
        embed.add_field(name=f"**{dmin}**", value=f"일반조회: {normal_ping}\n보안 조회: {srv_pinged}", inline=False)
        # await ctx.send(embed=embed)
        await replied_msg.edit( f"", embed=embed )
client.run("")
