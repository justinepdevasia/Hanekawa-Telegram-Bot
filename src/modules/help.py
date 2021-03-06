from src import dispatcher

from telegram import Update
from telegram.ext import CommandHandler, CallbackContext as Context

COMMAND_LIST = {
    'start': 'Command to check if I\'m alive',
    'help': '/help: Sends you a message on how to use me\n/help <command>: Sends you the usage of a particular command',
    'list': 'Lists all available commands',
    'remindme': 'Sets a remindmer\nUsage: /remindme <time> <unit>\nExample: */remindme 10 min* sets a reminder for 10 minutes after current time',
    'promote': 'Promotes a group member to admin\nUsage: Send this command as a reply to any message by the person to be promoted',
    'demote': 'Demotes a group admin. Can only be used by owner\nUsage: Send this command as a reply to any message by the person to be demoted',
    'mute': 'Mutes a group member\nUsage: Send this command as a reply to any message by the person to be muted',
    'unmute': 'Unmutes a group member\nUsage: Send this command as a reply to any message by the person to be unmuted',
    'kick': 'Kicks a group member\nUsage: Send this command as a reply to any message by the person to be kicked\nCan also be accessed using /ban',
    'unban': 'Unbans a kicked member\nUsage: Send this command as a reply to any message by the person to be unbanned',
    'pin': 'Pins a message\nUsage: Send this command as a reply to the message to be pinned',
    'unpin': 'Unpins the pinned message',
    'xkcd': 'Retrieves and sends a random xkcd comic',
    'whatsnew': 'Lets you know about the latest feature added to me',
    'whatsnext': 'Lets you know what features my creator is working on adding next'
}

HELP_MESSAGE = (
    "Nyeko is here to help nyaa!\n\nTo see all commands I respond to, use /list\nTo get the usage of a "
    "particular command use /help <command>\n\nIf you "
    "have any other queries or want to request new features, head over to the [support group]("
    "https://t.me/NekoHanekawaGroup)\n")


def help(update: Update, context: Context):
    try:
        command = context.args[0]
        if command[0] == '/':
            command = command[1:]

        update.message.reply_markdown(COMMAND_LIST[command])

    except(ValueError, IndexError):
        update.message.reply_markdown(HELP_MESSAGE)


def list_all(update: Update, context: Context):
    commands = '/' + '\n/'.join(COMMAND_LIST.keys())
    update.message.reply_text("List of available commands:\n%s" % (commands))


help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

list_handler = CommandHandler('list', list_all)
dispatcher.add_handler(list_handler)
