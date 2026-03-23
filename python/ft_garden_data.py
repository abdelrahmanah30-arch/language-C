# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_data.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kali <marvin@42.fr>                        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/23 09:00:47 by kali              #+#    #+#              #
#    Updated: 2026/03/23 20:13:38 by kali             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age

if __name__ == "__main__":
	plant1 = plant("Rose", 25, 30)
	plant2 = plant("sunflower", 80, 45)
	plant3 = plant("cactus", 15, 120)

	print("=== Garden Plant Registry ===")
	print(f"{plant1.name}, {plant1.height}cm, {plant1.age}days")
	print(f"{plant2.name}, {plant2.height}cm, {plant2.age}days")
	print(f"{plant3.name}, {plant3.height}cm, {plant3.age}days")
