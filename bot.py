import requests
import telebot,time
from telebot import types
from gatet import Tele
import os
token = '7757624099:AAHfYRz0CX9IrQD8wWZxK5dbC52jSMBOZFU' #حط توكن بوتك
bot=telebot.TeleBot(token,parse_mode="HTML")
subscriber ='7014650919' # ايدي حسابك
@bot.message_handler(commands=["start"])
def start(message):
	if not str(message.chat.id) == subscriber:
		bot.reply_to(message, "Y𝖔𝖚 𝖈𝖆𝖓𝖓𝖔𝖙 𝖚𝖘𝖊 𝖙𝖍𝖊 𝖇𝖔𝖙 𝖙𝖔 𝖈𝖔𝖓𝖙𝖆𝖈𝖙 𝖉𝖊𝖛𝖊𝖑𝖔𝖕𝖊𝖗𝖘 𝖙𝖔 𝖕𝖚𝖗𝖈𝖍𝖆𝖘𝖊 𝖆 𝖇𝖔𝖙 𝖘𝖚𝖇𝖘𝖈𝖗𝖎𝖕𝖙𝖎𝖔𝖓 @B_6_Q")
		return
	bot.reply_to(message,"S𝖊𝖓𝖉 𝖙𝖍𝖊 𝖋𝖎𝖑𝖊 𝖓𝖔𝖜  \n ارسل الملف الان")
@bot.message_handler(content_types=["document"])
def main(message):
	if not str(message.chat.id) == subscriber:
		bot.reply_to(message, "Y𝖔𝖚 𝖈𝖆𝖓𝖓𝖔𝖙 𝖚𝖘𝖊 𝖙𝖍𝖊 𝖇𝖔𝖙 𝖙𝖔 𝖈𝖔𝖓𝖙𝖆𝖈𝖙 𝖉𝖊𝖛𝖊𝖑𝖔𝖕𝖊𝖗𝖘 𝖙𝖔 𝖕𝖚𝖗𝖈𝖍𝖆𝖘𝖊 𝖆 𝖇𝖔𝖙 𝖘𝖚𝖇𝖘𝖈𝖗𝖎𝖕𝖙𝖎𝖔𝖓@B_6_Q")
		return
	dd = 0
	live = 0
	ch = 0
	ko = (bot.reply_to(message, "Checking Your Cards...⌛").message_id)
	ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
	with open("combo.txt", "wb") as w:
		w.write(ee)
	try:
		with open("combo.txt", 'r') as file:
			lino = file.readlines()
			total = len(lino)
			for cc in lino:
				current_dir = os.getcwd()
				for filename in os.listdir(current_dir):
					if filename.endswith(".stop"):
						bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗')
						os.remove('stop.stop')
						return
				try:
					data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
					
				except:
					pass
				try:
					bank=(data['bank']['name'])
				except:
					bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					emj=(data['country']['emoji'])
				except:
					emj=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					cn=(data['country']['name'])
				except:
					cn=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					dicr=(data['scheme'])
				except:
					dicr=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					typ=(data['type'])
				except:
					typ=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					url=(data['bank']['url'])
				except:
					url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				
				
				try:
					last = str(Tele(cc))
				except Exception as e:
					print(e)
					last = "ERROR"
				if 'risk' in last:
					last='declined'
				elif 'Duplicate' in last:
					last='Approved'
				mes = types.InlineKeyboardMarkup(row_width=1)
				cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
				status = types.InlineKeyboardButton(f"• 𝗦𝗧𝗔𝗧𝗨𝗦 ➤ {last} •", callback_data='u8')
				cm3 = types.InlineKeyboardButton(f"• 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 ✅ ➤ [ {live} ] •", callback_data='x')
				cm4 = types.InlineKeyboardButton(f"• 𝗗𝗘𝗖𝗟𝗜𝗡𝗘𝗗 ❌ ➤ [ {dd} ] •", callback_data='x')
				cm5 = types.InlineKeyboardButton(f"• 𝗧𝗢𝗧𝗔𝗟 ☠️ ➤ [ {total} ] •", callback_data='x')
				stop=types.InlineKeyboardButton(f"[ 𝐒𝐓𝐎𝐏 ]", callback_data='stop')
				mes.add(cm1,status, cm3, cm4, cm5, stop)
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''W𝖆𝖎𝖙 𝖋𝖔𝖗 𝖕𝖗𝖔𝖈𝖊𝖘𝖘𝖎𝖓𝖌 
𝖇𝖞 ➤ @B_6_Q''', reply_markup=mes)
				msg = f'''✘ 𝑪𝑨𝑹𝑫  ➤ {cc} 
✘ 𝑺𝑻𝑨𝑻𝑼𝑺 ➤ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱  ✅ 
✘ 𝑹𝑬𝑺𝑼𝑳𝑻 ➤ Insufficient Funds
✘ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➤ Braintree 
━━━━━━━━━━━━━━━━━
✘ 𝑩𝑰𝑵 ➤ {cc[:6]} - {dicr} - {typ} 
✘ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➤ {cn} - {emj} 
✘ 𝑩𝑨𝑵𝑲 ➤ {bank}
✘ 𝑼𝑹𝑳 ➤ {url}
━━━━━━━━━━━━━━━━━
✘ 𝑩𝒀 : @MoDcAa
✘ 𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
				print(last)
				if "live" in last or 'Funds' in last:
					live += 1
					bot.reply_to(message, msg)
				elif 'successfully' in last:
					msg=f'''✘ 𝑪𝑨𝑹𝑫  ➤ {cc} 
✘ 𝑺𝑻𝑨𝑻𝑼𝑺 ➤ 𝑪𝑯𝑨𝑹𝑮𝑬  ✅ 
✘ 𝑹𝑬𝑺𝑼𝑳𝑻 ➤ 𝑺𝑼𝑪𝑪𝑬𝑺𝑺
✘ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➤ Braintree
━━━━━━━━━━━━━━━━━
✘ 𝑩𝑰𝑵 ➤ {cc[:6]} - {dicr} - {typ} 
✘ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➤ {cn} - {emj} 
✘ 𝑩𝑨𝑵𝑲 ➤ {bank}
✘ 𝑼𝑹𝑳 ➤ {url}
━━━━━━━━━━━━━━━━━
✘ 𝑩𝒀 ➤ @B_6_Q
✘ 𝑷𝑹𝑶𝑿𝒀𝑺 : 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
					bot.reply_to(message, msg)
				else:
					dd += 1
				time.sleep(1)
	except Exception as e:
		print(e)
	bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅'
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	with open("stop.stop", "w") as file:
		pass
print("تم تشغيل البوت")
bot.polling()
