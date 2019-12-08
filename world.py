import random
from star import Star
from star_names_stack import StarNamesStack

class World:

	def __init__(self, config):
		self._star_names = StarNamesStack()
		self.stars = []
		for n in range(len(self._star_names.names)):
			star = Star(
				self._star_names.pop(),
				random.randrange(config.world_width),
				random.randrange(config.world_height)
			)
			self.stars.append(star)

			nb_planets = random.randrange(
				config.min_planets_per_star,
				config.max_planets_per_star + 1)
			for n in range(nb_planets):
				star.add_planet(
					random.randrange(config.system_width),
					random.randrange(config.system_height)
				)

			self._scatter_planets(config, star)
			self._scatter_planets(config, star)

		self._scatter_stars(config)
		self._scatter_stars(config)

	def _scatter_planets(self, config, star):
		screen_center_x = config.system_width / 2
		screen_center_y = config.system_height / 2

		# for p in star.planets:

			# # Move planets out of (scaled up) star's way
			# if screen_center_x - 64 < p.rect.x < screen_center_x + 64:
			# 	if screen_center_y - 64 < p.rect.y < screen_center_y + 64:
			# 		p.rect.x = random.randrange(config.window_width - 32) + 16
			# 		p.rect.y = random.randrange(config.window_height - 32) + 16
			# 		p.name_rect.midtop = p.rect.midbottom

			# # Move planets out of each other's way
			# for o in star.planets:
			# 	if (o == p): continue

			# 	if (abs(p.rect.x - o.rect.x) + abs(p.rect.y - o.rect.y) < 32):

			# 		if (p.rect.x < o.rect.x):
			# 			if (p.rect.x > 32):
			# 				p.rect.move_ip(-32, 0)
			# 				p.name_rect.move_ip(-32, 0)
			# 			else:
			# 				p.rect.move_ip(64, 0)
			# 				p.name_rect.move_ip(64, 0)
			# 		else:
			# 			if (p.rect.x < config.window_width - 16):
			# 				p.rect.move_ip(32, 0)
			# 				p.name_rect.move_ip(32, 0)
			# 			else:
			# 				p.rect.move_ip(-64, 0)
			# 				p.name_rect.move_ip(-64, 0)

	def _scatter_stars(self, config):
		pass
		# for s in self.stars:
		# 	for o in self.stars:
		# 		if (o == s): continue

		# 		if (abs(s.rect.x - o.rect.x) + abs(s.rect.y - o.rect.y) < 32):

		# 			if (s.rect.x < o.rect.x):
		# 				if (s.rect.x > 32):
		# 					s.rect.move_ip(-32, 0)
		# 					s.name_rect.move_ip(-32, 0)
		# 				else:
		# 					s.rect.move_ip(64, 0)
		# 					s.name_rect.move_ip(64, 0)
		# 			else:
		# 				if (s.rect.x < config.window_width - 16):
		# 					s.rect.move_ip(32, 0)
		# 					s.name_rect.move_ip(32, 0)
		# 				else:
		# 					s.rect.move_ip(-64, 0)
		# 					s.name_rect.move_ip(-64, 0)

