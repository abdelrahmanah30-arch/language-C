# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_security.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kali <marvin@42.fr>                        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/24 13:45:09 by kali              #+#    #+#              #
#    Updated: 2026/03/24 14:30:59 by kali             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class	Plant:
	def __init__ (self, name, height, age):
		self._name = name
		self._height = height
		self._age = age

		self.set_height(height)
		self.set_age(age)

	def set_height(self, height):
		if height < 0:
			print(f"Invalid operation attempted: height", {height}, "cm [REJECTED]")
			print("Security: Negative height rejected")

		else:
			self._height = height
			print("Height updated: {height}cm [OK]")

	def set_age(self, age):
		if age < 0:
			print(f"Invalid operation attempted: age", {age}, " [REJECTED]")
			print("Security: Negative age rejected")

		else:
			self._age = age
			print(f"Height updated: {age}days [OK]")

	def get_height(self):
                return self._height

	def get_age(self):
                return self._age
if __name__ == "__main__":
	plant = Plant("Rose", 25, 30)
	print("=== Garden Security System ===")
	
	plant.set_height(9)
	print(f"Current plant: {plant._name} ({plant.get_height()}cm, {plant.get_age()} days)")
