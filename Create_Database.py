# This script is run outside of the Planner to create a sqlite database that the Planner needs to run.
# The database can be called from the Planner and contains all the relevant information about the following:
#  Races
#  Professions
#  Skills
#  Maneuvers

#!/usr/bin/python

import sys
import sqlite3

con = sqlite3.connect("GS4_Planner.db")
cur = con.cursor()

# Check to see if the database already exists. If it does, exit the program.
cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Races';")
data = cur.fetchone()

if data != None:
	print("Database already exists. Exiting...")  
	sys.exit(1)
	
	
# Creates the Races table. This will contain all the known information about every race in GS4
cur.execute("CREATE TABLE Races (name, manauever_bonus, max_health, health_regen, spirit_regen, decay_timer, encumberance_factor, weight_factor, elemental_td, spiritual_td, sorc_td, poison_td, disease_td, strength_bonus, constitution_bonus, dexterity_bonus, agility_bonus, discipline_bonus, aura_bonus, logic_bonus, intuition_bonus, wisdom_bonus, influence_bonus, strength_adj, constitution_adj, dexterity_adj, agility_adj, discipline_adj, aura_adj, logic_adj, intuition_adj, wisdom_adj, influence_adj)")
   
cur.execute("INSERT INTO Races VALUES('Aelotoi', 'good', 120, 1, 1, 10, 0.75, 0.65, 0, 0, 0, 0, 0,  -5, 0, 5, 10, 5, 0, 5, 5, 0, 0,  0, -2, 3, 3, 2, 0, 0, 2, 0, 3) ")
cur.execute("INSERT INTO Races VALUES('Burghal Gnome', 'best', 90, 1, 1, 14, 0.78, 0.7, 0, 0, 0, 0, 0,  -15, 10, 10, 10, -5, 5, 10, 5, 0, -5,  -5, 0, 3, 3, -3, -2, 5, 5, 0, 0) ")
cur.execute("INSERT INTO Races VALUES('Dark Elf', 'good', 120, 1, 1, 10, 0.84, 0.75, -5, -5, -5, 10, 100,  0, -5, 10, 5, -10, 10, 0, 5, 5, -5,  0, -2, 5, 5, 5, -2, 0, 0, 0, 0) ")
cur.execute("INSERT INTO Races VALUES('Dwarf', 'average', 140, 3, 2, 16, 0.8, 0.75, 30, 0, 15, 20, 15,  10, 15, 0, -5, 10, -10, 0, 0, 0, -10,  5, 5, -3, -5, 3, 0, 0, 0, 3, -2) ")
cur.execute("INSERT INTO Races VALUES('Elf', 'excellent', 130, 1, 1, 10, 0.78, 0.7, -5, -5, -5, 10, 100,  0, 0, 5, 15, -15, 5, 0, 0, 0, 10,  0, -5, 5, 3, -5, 5, 0, 0, 0, 3) ")
cur.execute("INSERT INTO Races VALUES('Erithian', 'good', 120, 1, 1, 13, 0.85, 0.75, 0, 0, 0, 0, 0,  -5, 10, 0, 0, 5, 0, 5, 0, 0, 10,  -2, 0, 0, 0, 3, 0, 2, 0, 0, 3) ")
cur.execute("INSERT INTO Races VALUES('Forest Gnome', 'excellent', 100, 1, 2, 16, 0.6, 0.45, 0, 0, 0, 0, 0,  -10, 10, 5, 10, 5, 0, 5, 0, 5, -5,  -3, 2, 2, 3, 2, 0, 0, 0, 0, 0) ")
cur.execute("INSERT INTO Races VALUES('Giantman', 'average', 200, 3, 1, 13, 1.33, 1.2, -5, -5, 0, 0, 0,  15, 10, -5, -5, 0, -5, 0, 0, 0, 5,  5, 3, -2, -2, 0, 0, 0, 2, 0, 0) ")
cur.execute("INSERT INTO Races VALUES('Half Elf', 'good', 135, 2, 1, 10, 0.92, 0.8, -5, -5, -5, 0, 50,  0, 0, 5, 10, -5, 0, 0, 0, 0, 5,  2, 0, 2, 2, -2, 0, 0, 0, 0, 0) ")
cur.execute("INSERT INTO Races VALUES('Half Krolvin', 'excellent', 165, 1, 1, 13, 1.1, 1, 0, 0, 0, 0, 0,  10, 10, 0, 5, 0, 0, -10, 0, -5, -5,  0, -2, 3, 3, 2, 0, 0, 2, 0, 3) ")
cur.execute("INSERT INTO Races VALUES('Halfling', 'excellent', 100, 3, 2, 16, 0.5, 0.45, 40, 0, 20, 30, 30,  -15, 10, 15, 10, -5, -5, 5, 10, 0, -5,  -5, 5, 5, 5, -2, 0, -2, 0, 0, 0) ")
cur.execute("INSERT INTO Races VALUES('Human', 'average', 150, 2, 1, 14, 1, 0.9, 0, 0, 0, 0, 0,  5, 0, 0, 0, 0, 0, 5, 5, 0, 0,  2, 2, 0, 0, 0, 0, 0, 2, 0, 0) ")
cur.execute("INSERT INTO Races VALUES('Sylvankind', 'good', 130, 1, 1, 10, 0.81, 0.7, -5, -5, -5, 10, 100,  0, 0, 10, 5, -5, 5, 0, 0, 0, 0,  -3, -2, 5, 5, -5, 3, 0, 0, 0, 3) ")
	
	
# Creates the Professions table. This contains the general information about all the professions in GS4. Skill costs are handled by the Skills table.	
cur.execute("CREATE TABLE Professions (name, type, prime_statistics1, prime_statistics2, mana_statistic1, mana_statistic2, spell_circle1, spell_circle2, spell_circle3, strength_growth, constitution_growth, dexterity_growth, agility_growth, discipline_growth, aura_growth, logic_growth, intuition_growth, wisdom_growth, influence_growth)")	
	
cur.execute("INSERT INTO Professions VALUES ('Bard', 'semi',  'Influence', 'Aura',  'Influence', 'Aura',  'Minor Elemental', 'Bard', 'NONE',  25, 20, 25, 20, 15, 25, 10, 15, 20, 30) ")
cur.execute("INSERT INTO Professions VALUES ('Cleric', 'pure',  'Wisdom', 'Intuition',  'Wisdom', 'Wisdom',  'Minor Spiritual', 'Major Spiritual', 'Cleric',  20, 20, 10, 15, 25, 15, 25, 25, 30, 20) ")
cur.execute("INSERT INTO Professions VALUES ('Empath', 'pure',  'Wisdom', 'Influence',  'Wisdom', 'Influence',  'Minor Spiritual', 'Major Spiritual', 'Empath',  10, 20, 15, 15, 25, 20, 25, 20, 30, 25) ")
cur.execute("INSERT INTO Professions VALUES ('Monk', 'square',  'Agility', 'Strength',  'Wisdom', 'Logic',  'Minor Spiritual', 'Minor Mental', 'NONE',  25, 25, 20, 30, 25, 15, 20, 20, 15, 10) ")
cur.execute("INSERT INTO Professions VALUES ('Paladin', 'semi',  'Wisdom', 'Strength',  'Wisdom', 'Wisdom',  'Minor Spiritual', 'Paladin', 'NONE',  30, 25, 20, 20, 25, 15, 10, 15, 25, 20) ")
cur.execute("INSERT INTO Professions VALUES ('Ranger', 'semi',  'Dexterity', 'Intuition',  'Wisdom', 'Wisdom',  'Minor Spiritual', 'Ranger', 'NONE',  25, 20, 30, 20, 20, 15, 15, 15, 25, 10) ")
cur.execute("INSERT INTO Professions VALUES ('Rogue', 'square',  'Dexterity', 'Agility',  'Aura', 'Wisdom',  'Minor Elemental', 'Minor Spiritual', 'NONE',  25, 20, 25, 30, 20, 15, 20, 25, 10, 15) ")
cur.execute("INSERT INTO Professions VALUES ('Savant', 'pure',  'Influence', 'Logic',  'Influence', 'Influence',  'Minor Mental', 'Major Mental', 'Savant',  0, 0, 0, 0, 0, 0, 0, 0, 0, 0) ")
cur.execute("INSERT INTO Professions VALUES ('Sorcerer', 'pure',  'Aura', 'Wisdom',  'Aura', 'Wisdom',  'Minor Elemental', 'Minor Spiritual', 'Sorcerer',  10, 15, 20, 15, 25, 30, 25, 20, 25, 20) ")
cur.execute("INSERT INTO Professions VALUES ('Warrior', 'square',  'Constitution', 'Strength',  'Aura', 'Wisdom',  'Minor Elemental', 'Minor Spiritual', 'NONE',  30, 25, 25, 25, 20, 15, 10, 20, 15, 20) ")
cur.execute("INSERT INTO Professions VALUES ('Wizard', 'pure',  'Aura', 'Logic',  'Aura', 'Aura',  'Minor Elemental', 'Major Elemental', 'Wizard',  10, 15, 25, 15, 20, 30, 25, 25, 20, 20) ")
	

# Creates the Skills table. This includes the name, type, subskill, redux value, and PTP/MTP costs and max ranks per level for every profession.
cur.execute("CREATE TABLE Skills (name, type, subskill_group, redux_value, bard_ptp, bard_mtp, bard_max_ranks, cleric_ptp, cleric_mtp, cleric_max_ranks, empath_ptp, empath_mtp, empath_max_ranks, monk_ptp, monk_mtp, monk_max_ranks, paladin_ptp, paladin_mtp, paladin_max_ranks, ranger_ptp, ranger_mtp, ranger_max_ranks, rogue_ptp, rogue_mtp, rogue_max_ranks, savant_ptp, savant_mtp, savant_max_ranks, sorcerer_ptp, sorcerer_mtp, sorcerer_max_ranks, warrior_ptp, warrior_mtp, warrior_max_ranks, wizard_ptp, wizard_mtp, wizard_max_ranks) ")
	
cur.execute("INSERT INTO Skills VALUES ('Armor Use', 'armor', 'NONE', 0.4,  5,0,2,  8,0,1,  15,0,1,  10,0,2,  3,0,3,  5,0,2,  5,0,2,  15,0,1,  15,0,1,  2,0,3,  14,0,1) ")
cur.execute("INSERT INTO Skills VALUES ('Shield Use', 'armor', 'NONE', 0.4,  5,0,2,  13,0,1,  13,0,1,  8,0,2,  3,0,2,  5,0,2,  4,0,1,  13,0,1,  13,0,1,  2,0,3,  13,0,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Edged Weapons', 'weapon', 'NONE', 0.3,  3,1,2,  4,2,1,  6,2,1,  2,1,2,  3,1,2,  3,1,2,  2,1,2,  6,2,1,  6,2,1,  2,1,2,  6,2,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Blunt Weapons', 'weapon', 'NONE', 0.3,  4,1,2,  4,2,1,  6,2,1,  3,1,2,  3,1,2,  4,1,2,  3,1,2,  6,2,1,  6,2,1,  2,1,2,  6,2,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Two-Handed Weapons', 'weapon', 'NONE', 0.3,  7,2,2,  10,3,1,  13,3,1,  5,2,2,  4,2,2,  6,2,2,  6,2,2,  14,3,1,  14,3,1,  3,1,2,  14,3,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Ranged Weapons', 'weapon', 'NONE', 0.3,  4,2,2,  9,3,1,  14,3,1,  4,1,2,  6,2,2,  3,1,2,  3,1,2,  14,3,1,  14,3,1,  2,1,2,  14,3,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Thrown Weapons', 'weapon', 'NONE', 0.3,  3,1,2,  9,3,1,  9,3,1,  2,1,2,  5,2,2,  2,1,2,  2,1,2,  9,3,1,  9,3,1,  2,1,2,  8,2,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Polearm Weapons', 'weapon', 'NONE', 0.3,  6,1,2,  11,3,1,  14,3,1,  6,2,2,  5,2,2,  7,2,2,  7,2,2,  14,3,1,  14,3,1,  3,1,2,  14,3,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Brawling Weapons', 'weapon', 'NONE', 0.3,  3,1,2,  6,1,1,  10,2,1,  2,1,2,  4,1,2,  4,2,2,  3,1,2,  10,2,1,  10,2,1,  2,1,2,  10,2,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Ambush', 'combat', 'NONE', 0.4,  4,4,1,  12,12,1,  15,15,1,  3,2,2,  4,5,1,  3,3,2,  2,1,2,  15,15,1,  15,14,1,  3,4,2,  15,10,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Two Weapon Combat', 'combat', 'NONE', 0.4,  3,2,2,  9,9,1,  12,12,1,  2,2,2,  3,3,2,  3,2,2,  2,2,2,  12,12,1,  12,12,1,  3,4,2,  12,12,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Combat Maneuvers', 'combat', 'NONE', 0.4,  8,4,2,  10,6,1,  12,8,1,  5,3,2,  5,4,2,  5,4,2,  4,4,2,  12,8,1,  12,8,1,  4,3,2,  12,8,1) ")
cur.execute("INSERT INTO Skills VALUES ('Multi Opponent Combat', 'combat', 'NONE', 0.4,  7,3,1,  15,8,1,  12,10,1,  5,2,2,  5,2,1,  10,4,1,  10,3,1,  15,10,1,  15,10,1,  4,3,2,  15,10,1) ")
cur.execute("INSERT INTO Skills VALUES ('Physical Fitness', 'combat', 'NONE', 1,  4,0,2,  7,0,1,  2,0,3,  2,0,3,  3,0,2,  4,0,2,  3,0,2,  8,0,1,  8,0,1,  2,0,3,  8,0,1) ")
cur.execute("INSERT INTO Skills VALUES ('Dodging', 'combat', 'NONE', 0.4,  6,6,2,  20,20,1,  20,20,1,  1,1,3,  5,3,2,  7,5,2,  2,1,3,  20,20,1,  20,20,1,  4,2,3,  20,20,1) ")
cur.execute("INSERT INTO Skills VALUES ('Arcane Symbols', 'magic', 'NONE', 0,  0,4,2,  0,2,2,  0,2,2,  0,6,1,  0,5,1,  0,5,1,  0,7,1,  0,2,2,  0,2,2,  0,7,1,  0,1,2) ")
cur.execute("INSERT INTO Skills VALUES ('Magic Item Use', 'magic', 'NONE', 0,  0,4,2,  0,2,2,  0,2,2,  0,7,1,  0,6,1,  0,5,1,  0,8,1,  0,2,2,  0,2,2,  0,8,1,  0,1,2) ")
cur.execute("INSERT INTO Skills VALUES ('Spell Aiming', 'magic', 'NONE', 0,  3,10,1,  3,2,2,  3,1,2,  5,20,1,  5,20,1,  5,15,1,  4,22,1,  3,1,2,  3,1,2,  5,25,1,  2,1,2) ")
cur.execute("INSERT INTO Skills VALUES ('Harness Power', 'magic', 'NONE', 0,  0,5,2,  0,4,3,  0,4,3,  0,6,1,  0,5,2,  0,5,2,  0,9,1,  0,4,3,  0,4,3,  0,10,1,  0,4,3) ")
cur.execute("INSERT INTO Skills VALUES ('Elemental Mana Control', 'magic', 'NONE', 0,  0,6,1,  0,12,1,  0,12,1,  0,15,1,  0,15,1,  0,10,1,  0,12,1,  0,3,2,  0,10,1,  0,10,1,  0,4,2) ")
cur.execute("INSERT INTO Skills VALUES ('Mental Mana Control', 'magic', 'NONE', 0,  0,6,1,  0,12,1,  0,3,2,  0,8,1,  0,15,1,  0,15,1,  0,15,1,  0,3,2,  0,12,1,  0,15,1,  0,12,1) ")
cur.execute("INSERT INTO Skills VALUES ('Spiritual Mana Control', 'magic', 'NONE', 0,  0,12,1,  0,3,3,  0,3,2,  0,8,1,  0,6,1,  0,5,1,  0,10,1,  0,12,1,  0,3,2,  0,10,1,  0,15,1) ")
cur.execute("INSERT INTO Skills VALUES ('Spell Research, Minor Spiritual', 'magic', 'Spell Research', 0,  0,0,0,  0,8,3,  0,8,3,  0,38,1,  0,27,2,  0,17,2,  0,67,1,  0,0,0,  0,8,3,  0,120,1,  0,0,0) ")
cur.execute("INSERT INTO Skills VALUES ('Spell Research, Major Spiritual', 'magic', 'Spell Research', 0,  0,0,0,  0,8,3,  0,8,3,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0) ")
cur.execute("INSERT INTO Skills VALUES ('Spell Research, Cleric', 'magic', 'Spell Research', 0,  0,0,0,  0,8,3,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0) ")
cur.execute("INSERT INTO Skills VALUES ('Spell Research, Minor Elemental', 'magic', 'Spell Research', 0,  0,17,2,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,67,1,  0,0,0,  0,8,3,  0,120,1,  0,8,3) ")
cur.execute("INSERT INTO Skills VALUES ('Spell Research, Major Elemental', 'magic', 'Spell Research', 0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,8,3) ")
cur.execute("INSERT INTO Skills VALUES ('Spell Research, Ranger', 'magic', 'Spell Research', 0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,17,2,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0) ")
cur.execute("INSERT INTO Skills VALUES ('Spell Research, Sorcerer', 'magic', 'Spell Research', 0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,8,3,  0,0,0,  0,0,0) ")
cur.execute("INSERT INTO Skills VALUES ('Spell Research, Wizard', 'magic', 'Spell Research', 0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,8,3) ")
cur.execute("INSERT INTO Skills VALUES ('Spell Research, Bard', 'magic', 'Spell Research', 0,  0,17,2,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0) ")
cur.execute("INSERT INTO Skills VALUES ('Spell Research, Empath', 'magic', 'Spell Research', 0,  0,0,0,  0,0,0,  0,8,3,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0) ")
cur.execute("INSERT INTO Skills VALUES ('Spell Research, Savant', 'magic', 'Spell Research', 0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,8,3,  0,0,0,  0,0,0,  0,0,0) ")
cur.execute("INSERT INTO Skills VALUES ('Spell Research, Minor Mental', 'magic', 'Spell Research', 0,  0,0,0,  0,0,0,  0,0,0,  0,38,1,  0,0,0,  0,0,0,  0,0,0,  0,8,3,  0,0,0,  0,0,0,  0,0,0) ")
cur.execute("INSERT INTO Skills VALUES ('Spell Research, Major Mental', 'magic', 'Spell Research', 0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,8,3,  0,0,0,  0,0,0,  0,0,0) ")
cur.execute("INSERT INTO Skills VALUES ('Spell Research, Paladin', 'magic', 'Spell Research', 0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,17,2,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0) ")
cur.execute("INSERT INTO Skills VALUES ('Elemental Lore, Air', 'magic', 'Elemental Lore', 0,  0,8,1,  0,20,1,  0,20,1,  0,40,1,  0,20,1,  0,20,1,  0,15,1,  0,20,1,  0,7,2,  0,15,1,  0,6,2) ")
cur.execute("INSERT INTO Skills VALUES ('Elemental Lore, Earth', 'magic', 'Elemental Lore', 0,  0,8,1,  0,20,1,  0,20,1,  0,40,1,  0,20,1,  0,20,1,  0,15,1,  0,20,1,  0,7,2,  0,15,1,  0,6,2) ")
cur.execute("INSERT INTO Skills VALUES ('Elemental Lore, Fire', 'magic', 'Elemental Lore', 0,  0,8,1,  0,20,1,  0,20,1,  0,40,1,  0,20,1,  0,20,1,  0,15,1,  0,20,1,  0,7,2,  0,15,1,  0,6,2) ")
cur.execute("INSERT INTO Skills VALUES ('Elemental Lore, Water', 'magic', 'Elemental Lore', 0,  0,8,1,  0,20,1,  0,20,1,  0,40,1,  0,20,1,  0,20,1,  0,15,1,  0,20,1,  0,7,2,  0,15,1,  0,6,2) ")	
cur.execute("INSERT INTO Skills VALUES ('Spiritual Lore, Blessings', 'magic', 'Spiritual Lore', 0,  0,20,1,  0,6,2,  0,6,2,  0,12,1,  0,7,2,  0,10,1,  0,15,1,  0,20,1,  0,7,2,  0,15,1,  0,20,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Spiritual Lore, Religion', 'magic', 'Spiritual Lore', 0,  0,20,1,  0,6,2,  0,6,2,  0,12,1,  0,7,2,  0,10,1,  0,15,1,  0,20,1,  0,7,2,  0,15,1,  0,20,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Spiritual Lore, Summoning', 'magic', 'Spiritual Lore', 0,  0,20,1,  0,6,2,  0,6,2,  0,12,1,  0,7,2,  0,10,1,  0,15,1,  0,20,1,  0,7,2,  0,15,1,  0,20,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Sorcerous Lore, Demonology', 'magic', 'Sorcerous Lore', 0,  0,18,1,  0,10,1,  0,12,1,  0,35,1,  0,18,1,  0,18,1,  0,30,1,  0,12,1,  0,6,2,  0,30,1,  0,10,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Sorcerous Lore, Necromancy', 'magic', 'Sorcerous Lore', 0,  0,18,1,  0,10,1,  0,12,1,  0,35,1,  0,18,1,  0,18,1,  0,30,1,  0,12,1,  0,6,2,  0,30,1,  0,10,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Mental Lore, Divination', 'magic', 'Mental Lore', 0,  0,8,1,  0,20,1,  0,6,2,  0,12,1,  0,20,1,  0,20,1,  0,40,1,  0,6,2,  0,20,1,  0,40,1,  0,20,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Mental Lore, Manipulation', 'magic', 'Mental Lore', 0,  0,8,1,  0,20,1,  0,6,2,  0,12,1,  0,20,1,  0,20,1,  0,40,1,  0,6,2,  0,20,1,  0,40,1,  0,20,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Mental Lore, Telepathy', 'magic', 'Mental Lore', 0,  0,8,1,  0,20,1,  0,6,2,  0,12,1,  0,20,1,  0,20,1,  0,40,1,  0,6,2,  0,20,1,  0,40,1,  0,20,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Mental Lore, Transference', 'magic', 'Mental Lore', 0,  0,8,1,  0,20,1,  0,6,2,  0,12,1,  0,20,1,  0,20,1,  0,40,1,  0,6,2,  0,20,1,  0,40,1,  0,20,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Mental Lore, Transformation', 'magic', 'Mental Lore', 0,  0,8,1,  0,20,1,  0,6,2,  0,12,1,  0,20,1,  0,20,1,  0,40,1,  0,6,2,  0,20,1,  0,40,1,  0,20,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Survival', 'general', 'NONE', 0,  2,2,2,  3,2,2,  3,2,2,  2,2,2,  2,2,2,  1,1,2,  2,2,2,  3,2,2,  3,2,1,  1,3,2,  3,2,2) ")	
cur.execute("INSERT INTO Skills VALUES ('Disarm Traps', 'general', 'NONE', 0,  2,3,2,  2,6,2,  2,6,2,  3,4,2,  2,5,1,  2,4,2,  1,1,3,  2,6,1,  2,6,1,  2,4,2,  2,6,2) ")
cur.execute("INSERT INTO Skills VALUES ('Picking Locks', 'general', 'NONE', 0,  2,1,2,  2,4,2,  2,4,2,  3,3,2,  2,4,2,  2,3,2,  1,1,3,  2,4,1,  2,4,1,  2,3,2,  2,4,2) ")
cur.execute("INSERT INTO Skills VALUES ('Stalking and Hiding', 'general', 'NONE', 0,  3,2,2,  5,4,5,  5,4,1,  3,2,2,  4,4,1,  2,1,2,  1,1,3,  5,4,1,  5,4,1,  2,3,2,  5,4,1) ")
cur.execute("INSERT INTO Skills VALUES ('Perception', 'general', 'NONE', 0,  0,3,2,  0,3,2,  0,3,2,  0,2,2,  0,3,2,  0,3,2,  0,1,3,  0,3,2,  0,3,2,  0,3,2,  0,3,2) ")
cur.execute("INSERT INTO Skills VALUES ('Climbing', 'general', 'NONE', 0,  3,0,2,  4,0,1,  4,0,1,  1,0,2,  3,0,2,  2,0,2,  1,0,2,  4,0,1,  4,0,1,  3,0,2,  4,0,1) ")
cur.execute("INSERT INTO Skills VALUES ('Swimming', 'general', 'NONE', 0,  3,0,2,  3,0,1,  3,0,1,  2,0,2,  2,0,2,  2,0,2,  2,0,2,  3,0,1,  3,0,1,  2,0,2,  3,0,1) ")
cur.execute("INSERT INTO Skills VALUES ('First Aid', 'general', 'NONE', 0,  2,1,2,  1,1,2,  1,0,3,  1,2,2,  1,1,2,  2,1,2,  1,2,2,  2,1,2,  2,1,2,  1,2,2,  2,1,2) ")
cur.execute("INSERT INTO Skills VALUES ('Trading', 'general', 'NONE', 0,  0,2,2,  0,3,2,  0,0,3,  0,3,2,  0,3,2,  0,3,2,  0,3,2,  0,3,2,  0,3,2,  0,4,2,  0,3,2) ")
cur.execute("INSERT INTO Skills VALUES ('Pickpocketing', 'general', 'NONE', 0,  2,1,2,  3,3,1,  3,3,1,  2,2,2,  4,4,1,  2,3,1,  1,0,2,  3,3,1,  3,3,1,  2,3,1,  3,3,1) ")
	
	
# Creates the Maneuvers table. This table contains every Combat Maneuver, Shield Maneuver, and Armor Specializion. The base costs, profession availability, and prerequisites are also in this table.
cur.execute("CREATE TABLE Maneuvers (name, mnemonic, type, ranks, cost_rank1, cost_rank2, cost_rank3, cost_rank4, cost_rank5, available_bard, available_cleric, available_empath, available_monk, available_paladin, available_ranger, available_rogue, available_savant, available_sorcerer, available_warrior, available_wizard, prerequisites)")
	
cur.execute("INSERT INTO Maneuvers VALUES ('Armor Spike Focus', 'SPIKEFOCUS', 'combat', 2,  5, 10, 'NONE', 'NONE', 'NONE',  0,0,0,0,1,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Bearhug', 'BEARHUG', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,1,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Berserk', 'BERSERK', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Block Mastery', 'BMASTERY', 'combat', 3,  4, 8, 12, 'NONE', 'NONE',  0,0,0,0,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Bull Rush', 'BULLRUSH', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,1,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Burst of Swiftness', 'BURST', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,1,0,0,0,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Charge', 'CHARGE', 'combat', 5,  2, 4, 6, 8, 10,  1,0,0,1,1,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Cheapshots', 'CHEAPSHOTS', 'combat', 5,  2, 3, 4, 5, 6,  1,0,0,1,0,0,1,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Combat Focus', 'FOCUS', 'combat', 5,  2, 4, 6, 8, 10,  1,0,0,1,1,1,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Combat Mastery', 'CMASTERY', 'combat', 2,  2, 4, 'NONE', 'NONE', 'NONE',  1,1,1,1,1,1,1,1,1,1,1, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Combat Mobility', 'MOBILITY', 'combat', 2,  5, 10, 'NONE', 'NONE', 'NONE',  0,0,0,1,0,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Combat Movement', 'CMOVEMENT', 'combat', 5,  2, 3, 4, 5, 6,  1,1,1,1,1,1,1,1,1,1,1, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Combat Toughness', 'TOUGHNESS', 'combat', 3,  6, 8, 10, 'NONE', 'NONE',  0,0,0,1,1,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Coup de Grace', 'COUPDEGRACE', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,0,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Crowd Press', 'CPRESS', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,1,1,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Cunning Defense', 'CDEFENSE', 'combat', 5,  2, 3, 4, 5, 6,  1,1,1,1,1,1,1,1,1,1,1, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Cutthroat', 'CUTTROAT', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,0,0,1,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Dirtkick', 'DIRTKICK', 'combat', 5,  2, 3, 4, 5, 6,  1,1,1,1,1,1,1,1,1,1,1, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Disarm Weapon', 'DISARM', 'combat', 5,  2, 4, 6, 8, 10,  1,1,1,1,1,1,1,1,1,1,1, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Divert', 'DIVERT', 'combat', 5,  2, 3, 4, 5, 6,  0,0,0,0,0,0,1,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Duck and Weave', 'WEAVE', 'combat', 3,  4, 8, 12, 'NONE', 'NONE',  0,0,0,1,0,0,1,0,0,0,0, 'CM:Combat Movement:2') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Dust Shroud', 'SSHROUD', 'combat', 5,  2, 3, 4, 5, 6,  0,0,0,0,0,0,1,0,0,0,0, 'CM:Dirtkick:5') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Evade Mastery', 'EMSATERY', 'combat', 3,  4, 8, 12, 'NONE', 'NONE',  0,0,0,1,0,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES (\"Executioner's Stance\", 'EXECUTIONER', 'combat', 3,  4, 8, 12, 'NONE', 'NONE',  0,0,0,0,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Feint', 'FEINT', 'combat', 5,  2, 3, 5, 7, 10,  1,1,1,1,1,1,1,1,1,1,1, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Flurry of Blows', 'FLURRY', 'combat', 3,  3, 6, 9, 'NONE', 'NONE',  0,0,0,1,0,0,0,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Garrote', 'GARROTE', 'combat', 5,  2, 4, 6, 8, 10,  1,0,0,1,0,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Grapple Mastery', 'GMSATERY', 'combat', 3,  4, 8, 12, 'NONE', 'NONE',  0,0,0,1,0,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES (\"Griffin's Voice\", 'GRIFFIN', 'combat', 3,  3, 6, 9, 'NONE', 'NONE',  0,0,0,0,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Groin Kick', 'GKICK', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,0,0,1,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Hamstring', 'HAMSTRING', 'combat', 5,  2, 4, 6, 8, 10,  1,0,0,0,0,1,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Haymaker', 'HAYMAKER', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Headbutt', 'HAYMAKER', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,1,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Inner Harmony', 'IHARMONY', 'combat', 3,  4, 8, 12, 'NONE', 'NONE',  0,0,0,1,0,0,0,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Internal Power', 'IPOWER', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,1,0,0,0,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Ki Focus', 'IPOWER', 'combat', 3,  3, 6, 9, 'NONE', 'NONE',  0,0,0,1,0,0,0,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Kick Mastery', 'KMSATERY', 'combat', 3,  4, 8, 12, 'NONE', 'NONE',  0,0,0,1,0,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Mighty Blow', 'MBLOW', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Multi-Fire', 'DISARM', 'combat', 5,  2, 4, 6, 8, 10,  1,1,1,1,1,1,1,1,1,1,1, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Mystic Strike', 'MYSTICSTRIKE', 'combat', 5,  2, 3, 4, 5, 6,  0,0,0,1,0,0,0,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Perfect Self', 'PERFECTSELF', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,1,0,0,0,0,0,0,0, 'CM:Burst of Speed:3&CM:Surge of Strength:3') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Precision', 'PRECISION', 'combat', 2,  4, 6, 'NONE', 'NONE', 'NONE',  1,1,1,1,1,1,1,1,1,1,1, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Punch Mastery', 'PUNCHMASTERY', 'combat', 3,  4, 8, 12, 'NONE', 'NONE',  0,0,0,1,0,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES (\"Predator's Eye\", 'PREDATOR', 'combat', 3,  4, 6, 7, 'NONE', 'NONE',  0,0,0,0,0,0,1,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Quickstrike', 'QSTRIKE', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,1,0,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Rolling Krynch Stance', 'KRYNCH', 'combat', 3,  4, 8, 12, 'NONE', 'NONE',  0,0,0,1,0,0,0,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shadow Mastery', 'SMASTERY', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,1,0,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shield Bash', 'SBASH', 'combat', 5,  2, 4, 6, 8, 10,  1,0,0,0,1,1,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shield Charge', 'SCHARGE', 'combat', 5,  2, 4, 6, 8, 10,  1,0,0,0,1,1,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Side By Side', 'SIDEBYSIDE', 'combat', 5,  2, 4, 6, 8, 10,  1,1,1,1,1,1,1,1,1,1,1, 'CM:Combat Movement:2') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Silent Strike', 'SILENTSTRIKE', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,0,0,1,0,0,0,0, 'CM:Shadow Mastery:2') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Slippery Mind', 'SLIPPERYMIND', 'combat', 3,  4, 8, 12, 'NONE', 'NONE',  0,0,0,1,0,0,1,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Specialization I', 'WSPEC1', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,1,0,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Specialization II', 'WSPEC2', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,1,0,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Specialization III', 'WSPEC3', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,1,0,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Spell Cleaving', 'SCLEAVE', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,1,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Spell Parry', 'SPARRY', 'combat', 3,  4, 8, 12, 'NONE', 'NONE',  0,0,0,1,0,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Spell Thieve', 'THIEVE', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,0,0,1,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Spin Attack', 'SATTACK', 'combat', 5,  2, 4, 6, 8, 10,  1,0,0,1,0,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Staggering Blow', 'SBLOW', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Stance of the Mongoose', 'MONGOOSE', 'combat', 3,  4, 8, 12, 'NONE', 'NONE',  0,0,0,1,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Stun Maneuvers', 'STUNMAN', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,1,0,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Subdue', 'SUBDUE', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,0,0,1,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Sucker Punch', 'SPUNCH', 'combat', 5,  2, 3, 4, 5, 6,  0,0,0,0,0,0,1,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Sunder Shield', 'SUNDER', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Surge of Strength', 'SUNDER', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,1,1,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Sweep', 'SWEEP', 'combat', 5,  2, 4, 6, 8, 10,  1,0,0,1,0,1,1,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Tackle', 'TACKLE', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Tainted Bond', 'TAINTED', 'combat', 1,  12, 'NONE', 'NONE', 'NONE', 'NONE',  0,0,0,0,1,0,0,0,0,1,0, 'CM:Weapon Bonding:5|Skill:Spell Research, Paladin:25') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Trip', 'TRIP', 'combat', 5,  2, 4, 6, 8, 10,  1,1,1,1,1,1,1,1,1,1,1, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Truehand', 'TRUEHAND', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,1,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Twin Hammerfists', 'TWINHAMM', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Unarmed Specialist', 'UNARMEDSPEC', 'combat', 1,  6, 'NONE', 'NONE', 'NONE', 'NONE',  1,1,1,1,1,1,1,1,1,1,1, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Vanish', 'VANISH', 'combat', 3,  4, 8, 12, 'NONE', 'NONE',  0,0,0,0,0,0,1,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Weapon Bonding', 'BOND', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,0,0,0,0,0,1,0, 'CM:Specialization I:3|CM:Specialization II:3|CM:Specialization III:3') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Whirling Dervish', 'DERVISH', 'combat', 3,  4, 8, 12, 'NONE', 'NONE',  0,0,0,0,0,0,1,0,0,1,0, 'NONE') ")
    
cur.execute("INSERT INTO Maneuvers VALUES ('Small Shield Focus', 'SFOCUS', 'shield', 5,  4, 6, 8, 10, 12,  0,0,0,0,0,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Medium Shield Focus', 'MFOCUS', 'shield', 5,  4, 6, 8, 10, 12,  0,0,0,0,1,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Large Shield Focus', 'LFOCUS', 'shield', 5,  4, 6, 8, 10, 12,  0,0,0,0,1,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Tower Shield Focus', 'TFOCUS', 'shield', 5,  4, 6, 8, 10, 12,  0,0,0,0,1,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shield Bash', 'SBASH', 'shield', 5,  2, 4, 6, 8, 10,  0,0,0,0,1,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shield Charge', 'SCHARGE', 'shield', 5,  2, 4, 6, 8, 10,  0,0,0,0,1,0,0,0,0,1,0, 'SM:Shield Bash:2|CM:Shield Bash:2') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shield Push', 'PUSH', 'shield', 5,  2, 4, 6, 8, 10,  0,0,0,0,1,0,0,0,0,1,0, 'SM:Shield Bash:2|CM:Shield Bash:2') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shield Pin', 'PIN', 'shield', 5,  2, 4, 6, 8, 10,  0,0,0,0,1,0,0,0,0,1,0, 'SM:Shield Bash:2|CM:Shield Bash:2') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shield Swiftness', 'SWIFTNESS', 'shield', 3,  6, 12, 18, 'NONE', 'NONE',  0,0,0,0,0,0,1,0,0,1,0, 'SM:Small Shield Focus:3|SM:Medium Shield Focus:3|SM:Large Shield Focus:3|SM:Tower Shield Focus:3') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Prop Up', 'PROP', 'shield', 3,  6, 12, 18, 'NONE', 'NONE',  0,0,0,0,1,0,0,0,0,1,0, 'SM:Large Shield Focus:3|SM:Tower Shield Focus:3') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Adamantine Bulwark', 'BULWARK', 'shield', 3,  6, 12, 18, 'NONE', 'NONE',  0,0,0,0,0,0,0,0,0,1,0, 'SM:Prop Up:2') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shield Riposte', 'RIPOSTE', 'shield', 3,  4, 8, 12, 'NONE', 'NONE',  0,0,0,0,0,0,1,0,0,1,0, 'SM:Shield Bash:2|CM:Shield Bash:2') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shield Forward', 'FORWARD', 'shield', 3,  4, 8, 12, 'NONE', 'NONE',  0,0,0,0,1,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shield Spike Focus', 'SPIKEFOCUS', 'shield', 2,  8, 12, 'NONE', 'NONE', 'NONE',  0,0,0,0,1,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shield Spike Mastery', 'SPIKEMASTERY', 'shield', 2,  8, 12, 'NONE', 'NONE', 'NONE',  0,0,0,0,1,0,1,0,0,1,0, 'SM:Shield Spike Focus:2') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Deflection Training', 'DTRAINING', 'shield', 3,  6, 12, 18, 'NONE', 'NONE',  0,0,0,0,0,0,1,0,0,1,0, 'SM:Small Shield Focus:3|SM:Medium Shield Focus:3|SM:Large Shield Focus:3~SM|Tower Shield Focus:3') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Deflection Mastery', 'DMASTERY', 'shield', 5,  8, 10, 12, 14, 16,  0,0,0,0,0,0,1,0,0,1,0, 'SM:Deflection Training:3') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Block the Elements', 'EBLOCK', 'shield', 3,  6, 12, 18, 'NONE', 'NONE',  0,0,0,0,1,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Deflect the Elements', 'DEFLECT', 'shield', 3,  6, 12, 18, 'NONE', 'NONE',  0,0,0,0,0,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Steady Shield', 'STEADY', 'shield', 2,  4, 6, 'NONE', 'NONE', 'NONE',  0,0,0,0,0,0,1,0,0,1,0, 'CM:Stun Maneuvers:2') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Disarming Presence', 'DPRESENCE', 'shield', 3,  6, 12, 18, 'NONE', 'NONE',  0,0,0,0,1,0,0,0,0,1,0, 'CM:Disarm Weapon:2') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Guard Mastery', 'GUARDMASTERY', 'shield', 3,  6, 12, 18, 'NONE', 'NONE',  0,0,0,0,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Tortoise Stance', 'TORTOISE', 'shield', 3,  6, 12, 18, 'NONE', 'NONE',  0,0,0,0,0,0,0,0,0,1,0, 'SM:Block Mastery:2') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Spell Block', 'SPELLBLOCK', 'shield', 3,  6, 12, 18, 'NONE', 'NONE',  0,0,0,0,1,0,1,0,0,1,0, 'SM:Small Shield Focus:3|SM:Medium Shield Focus:3|SM:Large Shield Focus:3|SM:Tower Shield Focus:3') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shield Mind', 'MIND', 'shield', 3,  6, 12, 18, 'NONE', 'NONE',  0,0,0,0,1,0,1,0,0,1,0, 'SM:Spell Block:2') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Protective Wall', 'PWALL', 'shield', 2,  4, 5, 'NONE', 'NONE', 'NONE',  0,0,0,0,1,0,1,0,0,1,0, 'SM:Tower Shield Focus:2') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shield Strike', 'STRIKE', 'shield', 5,  2, 4, 6, 8, 10,  0,0,0,0,1,0,1,0,0,1,0, 'SM:Shield Bash:2|CM:Shield Bash:2') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shield Strike Mastery', 'STRIKEMASTERY', 'shield', 1,  30, 'NONE', 'NONE', 'NONE', 'NONE',  0,0,0,0,1,0,1,0,0,1,0, 'SM:Shield Strike:2&Skill:Multi Opponent Combat:30') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shield Trample', 'TRAMPLE', 'shield', 5,  2, 4, 6, 8, 10,  0,0,0,0,0,0,0,0,0,1,0, 'SM:Shield Charge:2') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shield Trample Mastery', 'TMASTERY', 'shield', 3,  8, 10, 12, 'NONE', 'NONE',  0,0,0,0,0,0,0,0,0,1,0, 'SM:Shield Trample:3&Skill:Multi Opponent Combat:30') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Steely Resolve', 'RESOLVE', 'shield', 3,  6, 12, 18, 'NONE', 'NONE',  0,0,0,0,1,0,0,0,0,1,0, 'SM:Tower Shield Focus:3') ")    
cur.execute("INSERT INTO Maneuvers VALUES ('Phalanx', 'PHALANX', 'shield', 5,  2, 4, 6, 8, 10,  0,0,0,0,1,0,1,0,0,1,0, 'NONE') ")
	
cur.execute("INSERT INTO Maneuvers VALUES ('Crush Protection', 'CRUSH', 'armor', 5,  20, 30, 40, 50, 60,  0,0,0,0,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Puncture Protection', 'PUNCTURE', 'armor', 5,  20, 30, 40, 50, 60,  0,0,0,0,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Slash Protection', 'SLASH', 'armor', 5,  20, 30, 40, 50, 60,  0,0,0,0,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Armored Casting', 'CASTING', 'armor', 5,  20, 30, 40, 50, 60,  0,0,0,0,1,0,0,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Armored Evasion', 'EVASION', 'armor', 5,  20, 30, 40, 50, 60,  0,0,0,0,0,0,1,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Armored Fluidity', 'FLUIDITY', 'armor', 5,  20, 30, 40, 50, 60,  0,0,0,0,1,0,0,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Armor Reinforcement', 'REINFORCE', 'armor', 5,  20, 30, 40, 50, 60,  0,0,0,0,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Armored Stealth', 'STEALTH', 'armor', 5,  20, 30, 40, 50, 60,  0,0,0,0,0,0,1,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Armor Support', 'SUPPORT', 'armor', 5,  20, 30, 40, 50, 60,  0,0,0,0,0,0,0,0,0,1,0, 'NONE') ")
	
con.commit()
con.close()   
