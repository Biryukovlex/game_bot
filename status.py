import sqlite3

def newtable():
	conn = sqlite3.connect('./vassals.db')
	c = conn.cursor()
	c.execute("""CREATE TABLE temp (
		chat_id TEXT,
		status TEXT,
		player_name TEXT
	)
	""")

# Добавляет новый статус для чата
def add_status(chat_id, status, player_name):
	conn = sqlite3.connect('./vassals.db')
	c = conn.cursor()
	c.execute('INSERT INTO temp VALUES (?, ?, ?)', (chat_id, status, player_name))
	conn.commit()
	conn.close()
	print (f"Successfully added status {status} for {chat_id}")

# Обновляет статус для чата
def update_status(chat_id, status):
	conn = sqlite3.connect('./vassals.db')
	c = conn.cursor()
	c.execute('UPDATE temp SET status=(?) WHERE chat_id=(?)', (status, chat_id))
	conn.commit()
	conn.close()
	print (f"Successfully changed status to {status} for {chat_id}")

# Обновляет сохраненное временно имя для чата
def update_name(chat_id, player_name):
	conn = sqlite3.connect('./vassals.db')
	c = conn.cursor()
	c.execute('UPDATE temp SET player_name=(?) WHERE chat_id=(?)', (player_name, chat_id))
	conn.commit()
	conn.close()
	print (f"Successfully changed saved name to {player_name} for {chat_id}")

# Возвращает статус для чата
def get_status(chat_id):
	current_status=[]
	conn = sqlite3.connect('./vassals.db')
	c = conn.cursor()
	c.execute('SELECT status FROM temp WHERE chat_id=(?)', (chat_id,))
	status_now = c.fetchall()
	for status in status_now:
		for i in status:
			current_status = i
	conn.commit()
	conn.close()
	if status_now:
		return(current_status)
	else:
		return(False)

# Возвращает временно занесенное имя игрока для сохранения картинки
def get_name(chat_id):
	saved_name=[]
	conn = sqlite3.connect('./vassals.db')
	c = conn.cursor()
	c.execute('SELECT player_name FROM temp WHERE chat_id=(?)', (chat_id,))
	player_now = c.fetchall()
	for player in player_now:
		for i in player:
			saved_name = i
	conn.commit()
	conn.close()
	if player_now != '0':
		return(saved_name)
	else:
		return(False)

# Удаляет статус для чата
def delete_status(chat_id):
	conn = sqlite3.connect('./vassals.db')
	c = conn.cursor()
	c.execute('DELETE FROM temp WHERE chat_id=(?)', (chat_id,))
	conn.commit()
	conn.close()
	print(f'Successfully deleted all for {chat_id}')

# newtable()
# add_status('123e13dcqef2', '0')
# delete_status('135131191')
# print(get_status('123e13dcqef2'))
