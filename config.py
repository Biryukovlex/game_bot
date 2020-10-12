# -*- coding: utf-8 -*-
import sqlite3

# Добавляет новую строчку в базу
def push_player_pics(player_name, file_id, file_path):
	conn = sqlite3.connect('./vassals.db')
	c = conn.cursor()
	c.execute('INSERT INTO Players VALUES (?, ?, ?)', (player_name, file_id, file_path))
	conn.commit()
	conn.close()
	print (f"Successfully added a set for {player_name}")

# Возвращает массив строк БД для player_name
def extract_player_pics(player_name):
	conn = sqlite3.connect('./vassals.db')
	c = conn.cursor()
	c.execute('SELECT * FROM Players WHERE player_name = (?)', (player_name,))
	pics = c.fetchall()
	conn.commit()
	conn.close()
	return pics

# Возвращает список уникальных player_name
def extract_player_names():
	conn = sqlite3.connect('./vassals.db')
	c = conn.cursor()
	players_new_list = []
	c.execute('SELECT DISTINCT player_name FROM Players')
	players = c.fetchall()
	for player in players:
		for i in player:
			players_new_list.append(i)
	conn.commit()
	conn.close()
	return(players_new_list)

# Удаляет все строки из БД для player_name
def delete_player(player_name):
	conn = sqlite3.connect('./vassals.db')
	c = conn.cursor()
	c.execute('DELETE FROM Players WHERE player_name = (?)', (player_name,))
	conn.commit()
	conn.close()
	print(f'Successfully deleted all for {player_name}')

# Удаляет все строки из таблицы Players
def delete_all():
	players_in_table = extract_player_names()
	for player in players_in_table:
		delete_player(f'{player}')
	print('Deleted all players and pics from vassals.db, "Players" table')

#push_player_pics("Valera12", "12314n3pc1e5dfg3", "file_path123")
#print(extract_player_names())
#delete_player_pics('Anna1234')
#delete_all()
