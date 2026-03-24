# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kali <marvin@42.fr>                        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/24 09:28:04 by kali              #+#    #+#              #
#    Updated: 2026/03/24 10:30:11 by kali             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class	Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age

	def grow(self):
		self.height += 1
	def age_up(self):
		self.age += 1
	def get_info(self):
		return f"{self.name}: {self.height}cm, {self.age}days old"
if __name__ == "__main__":
	plant1 = Plant("Rose", 25, 30)
	i = 0
	print("=== Day 1 ===")
	print(plant1.get_info())
	for i in range(7):
		plant1.grow()
		plant1.age_up()

	print("=== Day 7 ===")
	print(plant1.get_info())
	print("Growth this week: +6cm")
