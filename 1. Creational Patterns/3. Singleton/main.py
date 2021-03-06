class SingleObject:
	name = None

	@staticmethod 
	def get_instance():
		if not hasattr(SingleObject, 'instance'):
			SingleObject.instance = SingleObject()
		return SingleObject.instance

	def set_name(self, name):
		self.name = name

	def get_name(self):
		return self.name


singleton_object = SingleObject.get_instance()
singleton_object.set_name('Ajesh')
print('Singleton object name:', singleton_object.get_name())

new_singleton_object = SingleObject.get_instance()
print('New Singleton object name:', new_singleton_object.get_name())