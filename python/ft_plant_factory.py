# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_factory.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kali <marvin@42.fr>                        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/24 11:11:55 by kali              #+#    #+#              #
#    Updated: 2026/03/24 12:08:04 by kali             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class	Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age
	
	def get_info(self):
		return f"Created: {self.name} ({self.height}cm, {self.age}days)"

if __name__ == "__main__":
	plants = [
	Plant("Rose", 25, 30),
	Plant("Oak", 200, 365),
	Plant("Cactus", 5, 90),
	Plant("Sunflower", 80, 45),
	Plant("Fern", 15, 120)
	]

	print("=== Plant Factory Output ===")
	for plant in plants:
		print(plant.get_info())
	print("Total plants created:", len(plants))
