import random
from telegram.ext import Dispatcher,CommandHandler
import balence


def pog(update, context):
    msg44 = """What do you want to do with your life? 
    
/DAdventure 冒险 
/DWork 工作
/DStudy 学习
/DSearch 探索
    """
    msg44 += "\n\nAuthorised By Noah <3\n作者：Noah"
    update.message.reply_text(msg44)

def add_handler(dp:Dispatcher):
    list_handler = CommandHandler('DList', pog)
    dp.add_handler(list_handler)




