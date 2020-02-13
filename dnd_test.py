import discord
import sqlite3
from sqlite3 import Error

from discord.ext import commands
bot = commands.Bot(command_prefix='$')

def create_connection(db_file):
	""" create a database connection to a SQLite database """
	conn = None
	try:
		conn = sqlite3.connect(db_file)
		print(sqlite3.version)
		return conn
	except Error as e:
		print(e)

	return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS character (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL
                                    ); """

conn = create_connection('./dnd.sqlite3')
if conn is not None:
	create_table(conn, sql_create_projects_table)
else:
	print("Error! cannot create the database connection.")


@bot.command()
async def addChar(ctx, *args):
	print('Got something')
	try:
		cursor = conn.cursor()
		sql = ''' INSERT INTO character (name) VALUES (?) '''
		cursor.execute(sql, ('SOME NAME',))
		conn.commit()
	finally:
		pass

	await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))


bot.run('Njc3Mjc2MTQ5MTQ3MTA3MzI5.XkSTtA.oaVarFpnqtAf1foL45eATeA24PI')
