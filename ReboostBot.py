from telegram import Update
from telegram.ext import Updater, MessageHandler, CallbackContext, Filters, CommandHandler, InlineQueryHandler
from datetime import datetime
import time
import random,copy

def setSchedule(update: Update, context: CallbackContext) -> None:
    if len(context.args) < 4:
        update.message.reply_text("Please send your command again with the time allocations "
                                  "you want to add, in the following format:"
                                  " /setSchedule work_start_time, work_end_time, break_start_time, and break_end_time")
    else:
        context.bot_data["schedule"] = {}
        context.bot_data["schedule"]["work_start_time"] = context.args[0]
        context.bot_data["schedule"]["work_end_time"] = context.args[1]
        context.bot_data["schedule"]["break_start_time"] = context.args[2]
        context.bot_data["schedule"]["break_end_time"] = context.args[3]
        update.message.reply_text("Schedule set successfully! :)")


def time(bot, update,job_queue):
    job = job_queue.run_repeating(timeChecker, 5, context=update)

def viewSchedule(update: Update, context: CallbackContext) -> None:
    if "work_start_time" in context.bot_data["schedule"]:
        view_text = "Your work today begins at: {} \nYour work ends at: {}\nYour break begins at: {}\nYour break ends at: {}\n"\
            .format(context.bot_data["schedule"]["work_start_time"], context.bot_data["schedule"]["work_end_time"],
                    context.bot_data["schedule"]["break_start_time"],context.bot_data["schedule"]["break_end_time"])
        update.message.reply_text(view_text)
    else:
        update.message.reply_text("You don't have a schedule yet!")

def clearSchedule(update: Update, context: CallbackContext) -> None:
    context.bot_data["schedule"] = {}
    update.message.reply_text("Schedule cleared! :) ")


def otherThan(update: Update, context: CallbackContext):
    update.message.reply_text("Please try again, I do not really understand what you're typing.")


def timeChecker(update: Update, context: CallbackContext, job) -> None:
    #will be doing a if-else chain to chain all events, and run it through a while True loop as a checker
    if "work_start_time" in context.bot_data["schedule"]:
        currentTime = datetime.now().strftime("%H%M")
        if ((context.bot_data["schedule"]["work_start_time"]) == currentTime):
            job.context.message.reply_text("Work has started!")
        elif ((context.bot_data["schedule"]["break_start_time"]) == currentTime):
            job.context.message.reply_text("break has started!")
        elif ((context.bot_data["schedule"]["break_end_time"]) == currentTime):
            job.context.message.reply_text("break has ended!")
        elif ((context.bot_data["schedule"]["work_end_time"]) == currentTime):
            job.context.message.reply_text("work has ended!")
        else:
            pass
    else:
        pass


updater = Updater('1638946406:AAEXLY6xzPpqwV1pgkIaMz9jcVx3fxllyrk')


updater.dispatcher.add_handler(CommandHandler("setSchedule", setSchedule))
updater.dispatcher.add_handler(CommandHandler("viewSchedule", viewSchedule))
updater.dispatcher.add_handler(CommandHandler("clearSchedule", clearSchedule))
updater.dispatcher.add_handler(CommandHandler("timeChecker", timeChecker))
updater.dispatcher.add_handler(MessageHandler(Filters.text, time, pass_job_queue=True))
updater.dispatcher.add_handler(MessageHandler(Filters.all, otherThan))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    updater.start_polling()
    updater.idle()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/














##default function

##def greet(update: Update, context: CallbackContext) -> None:
    ##user_id = update.message.from_user.id
    ##if "users_talked_to" not in context.bot_data:
    ##    context.bot_data["users_talked_to"] = set()
    ##context.bot_data["users_talked_to"].add(user_id)
    ##num_people = len(context.bot_data["users_talked_to"])
    ##update.message.reply_text(f"Hello! A total of {num_people} people have spoken to this bot.")

##updater.dispatcher.add_handler(MessageHandler(Filters.text & (~ Filters.forwarded), greet))

# def addSecretGift(update: Update, context: CallbackContext) -> None:
#     user_id = update.message.from_user.id
#     if "gift_list" not in context.bot_data:
#         context.bot_data["gift_list"] = []
#     if len(context.args) < 1:
#         update.message.reply_text("Please send your command again with the gift you want to add in the following format: /put 'giftname'")
#     else:
#         context.bot_data["gift_list"].append({user_id: " ".join(context.args)})
#         update.message.reply_text("The gift was added successfully :)")
#         update.message.reply_text(context.bot_data["gift_list"])

# def takeSecretGift(update: Update, context: CallbackContext) -> None:
#
#     if "gift_list" not in context.bot_data:
#         update.message.reply_text("There are no gifts currently available!")
#         return
#
#     user_id = update.message.from_user.id
#     ls = copy.deepcopy(context.bot_data)
#     ##list(filter(lambda x: ))
#
#     update.message.reply_text("Your gift was chosen! You got: \n" + " " + "\n:)")