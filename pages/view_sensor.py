PAGE_NAME = "view_sensor"
OBJECTTYPE = "sensor"
DEBUG = False

INDEX_SIZE = {
	8:0,
	"8":0,
	6:1,
	"6":1,
}

INDEX_SHAPE = {
	'full':0,
	'half':1,
	'five':2,
	'three':3,
	'semi':4,
	'semi(-)':5,
	'choptwo':6,
}

INDEX_INSPECTION = {
	'pass':0,
	True:0,
	'fail':1,
	False:1,
}


class func(object):
	def __init__(self,fm,page,setUIPage,setSwitchingEnabled):
		self.page      = page
		self.setUIPage = setUIPage
		self.setMainSwitchingEnabled = setSwitchingEnabled

		self.sensor = fm.sensor()
		self.sensor_exists = None

		self.mode = 'setup'


	def enforce_mode(mode):
		if not (type(mode) in [str,list]):
			raise ValueError
		def wrapper(function):
			def wrapped_function(self,*args,**kwargs):
				if type(mode) is str:
					valid_mode = self.mode == mode
				elif type(mode) is list:
					valid_mode = self.mode in mode
				else:
					valid_mode = False
				if valid_mode:
					if DEBUG:
						print("page {} with mode {} req {} calling function {} with args {} kwargs {}".format(
							PAGE_NAME,
							self.mode,
							mode,
							function.__name__,
							args,
							kwargs,
							))
					function(self,*args,**kwargs)
				else:
					print("page {} mode is {}, needed {} for function {} with args {} kwargs {}".format(
						PAGE_NAME,
						self.mode,
						mode,
						function.__name__,
						args,
						kwargs,
						))
			return wrapped_function
		return wrapper


	@enforce_mode('setup')
	def setup(self):
		self.rig()
		self.mode = 'view'
		print("{} setup completed".format(PAGE_NAME))
		self.update_info()

	@enforce_mode('setup')
	def rig(self):
		self.page.sbID.valueChanged.connect(self.update_info)

		self.page.pbNew.clicked.connect(self.startCreating)
		self.page.pbEdit.clicked.connect(self.startEditing)
		self.page.pbSave.clicked.connect(self.saveEditing)
		self.page.pbCancel.clicked.connect(self.cancelEditing)

		self.page.pbGoShipment.clicked.connect(self.goShipment)

		self.page.pbDeleteComment.clicked.connect(self.deleteComment)
		self.page.pbAddComment.clicked.connect(self.addComment)

		self.page.pbGoStepSensor.clicked.connect(self.goStepSensor)
		self.page.pbGoProtomodule.clicked.connect(self.goProtomodule)
		self.page.pbGoModule.clicked.connect(self.goModule)



	@enforce_mode('view')
	def update_info(self,ID=None,*args,**kwargs):
		if ID is None:
			ID = self.page.sbID.value()
		else:
			self.page.sbID.setValue(ID)

		self.sensor_exists = self.sensor.load(ID)

		self.page.listShipments.clear()
		for shipment in self.sensor.shipments:
			self.page.listShipments.addItem(str(shipment))

		self.page.leLocation.setText(    "" if self.sensor.location     is None else self.sensor.location    )
		self.page.leIdentifier.setText(  "" if self.sensor.identifier   is None else self.sensor.identifier  )
		self.page.leManufacturer.setText("" if self.sensor.manufacturer is None else self.sensor.manufacturer)
		self.page.leType.setText(        "" if self.sensor.type         is None else self.sensor.type        )
		self.page.cbSize.setCurrentIndex(INDEX_SIZE.get(  self.sensor.size , -1))
		self.page.cbShape.setCurrentIndex(INDEX_SHAPE.get(self.sensor.shape, -1))
		self.page.sbRotation.setValue(-1 if self.sensor.rotation is None else self.sensor.rotation)
		self.page.sbChannels.setValue(-1 if self.sensor.channels is None else self.sensor.channels)
		if self.page.sbRotation.value() == -1:self.page.sbRotation.clear()
		if self.page.sbChannels.value() == -1:self.page.sbChannels.clear()

		self.page.listComments.clear()
		for comment in self.sensor.comments:
			self.page.listComments.addItem(comment)
		self.page.pteWriteComment.clear()

		self.page.cbInspection.setCurrentIndex(INDEX_INSPECTION.get(self.sensor.inspection,-1))

		self.page.sbStepSensor.setValue( -1 if self.sensor.step_sensor is None else self.sensor.step_sensor)
		self.page.sbProtomodule.setValue(-1 if self.sensor.protomodule is None else self.sensor.protomodule)
		self.page.sbModule.setValue(     -1 if self.sensor.module      is None else self.sensor.module     )
		if self.page.sbStepSensor.value()  == -1: self.page.sbStepSensor.clear()
		if self.page.sbProtomodule.value() == -1: self.page.sbProtomodule.clear()
		if self.page.sbModule.value()      == -1: self.page.sbModule.clear()

		self.updateElements()


	@enforce_mode(['view','editing','creating'])
	def updateElements(self):
		mode_view     = self.mode == 'view'
		mode_editing  = self.mode == 'editing'
		mode_creating = self.mode == 'creating'
		
		sensor_exists      = self.sensor_exists
		shipments_exist    = self.page.listShipments.count() > 0
		step_sensor_exists = self.page.sbStepSensor.value() >= 0
		protomodule_exists = self.page.sbProtomodule.value() >= 0
		module_exists      = self.page.sbModule.value() >= 0

		self.setMainSwitchingEnabled(mode_view)
		self.page.sbID.setEnabled(mode_view)

		self.page.pbNew.setEnabled(     mode_view and not sensor_exists )
		self.page.pbEdit.setEnabled(    mode_view and     sensor_exists )
		self.page.pbSave.setEnabled(    mode_editing or mode_creating )
		self.page.pbCancel.setEnabled(  mode_editing or mode_creating )

		self.page.pbGoShipment.setEnabled(mode_view and shipments_exist)

		self.page.leIdentifier.setReadOnly(   not (mode_creating or mode_editing) )
		self.page.leManufacturer.setReadOnly( not (mode_creating or mode_editing) )
		self.page.leType.setReadOnly(         not (mode_creating or mode_editing) )
		self.page.cbSize.setEnabled(               mode_creating or mode_editing  )
		self.page.cbShape.setEnabled(              mode_creating or mode_editing  )
		self.page.sbRotation.setReadOnly(     not (mode_creating or mode_editing) )
		self.page.sbChannels.setReadOnly(     not (mode_creating or mode_editing) )

		self.page.pbDeleteComment.setEnabled(mode_creating or mode_editing)
		self.page.pbAddComment.setEnabled(   mode_creating or mode_editing)
		self.page.pteWriteComment.setEnabled(mode_creating or mode_editing)

		self.page.cbInspection.setEnabled(   mode_creating or mode_editing   )
		self.page.pbGoStepSensor.setEnabled( mode_view and step_sensor_exists)
		self.page.pbGoProtomodule.setEnabled(mode_view and protomodule_exists)
		self.page.pbGoModule.setEnabled(     mode_view and module_exists     )


	@enforce_mode('view')
	def startCreating(self,*args,**kwargs):
		if not self.sensor_exists:
			ID = self.page.sbID.value()
			self.mode = 'creating'
			self.sensor.new(ID)
			self.updateElements()
		else:
			pass

	@enforce_mode('view')
	def startEditing(self,*args,**kwargs):
		if not self.sensor_exists:
			pass
		else:
			self.mode = 'editing'
			self.updateElements()

	@enforce_mode(['editing','creating'])
	def cancelEditing(self,*args,**kwargs):
		self.mode = 'view'
		self.update_info()

	@enforce_mode(['editing','creating'])
	def saveEditing(self,*args,**kwargs):

		self.sensor.identifier   = str(self.page.leIdentifier.text()  ) if str(self.page.leIdentifier.text()  ) else None
		self.sensor.manufacturer = str(self.page.leManufacturer.text()) if str(self.page.leManufacturer.text()) else None
		self.sensor.type         = str(self.page.leType.text()        ) if str(self.page.leType.text()        ) else None
		self.sensor.size         = str(self.page.cbSize.currentText() ) if str(self.page.cbSize.currentText() ) else None
		self.sensor.shape        = str(self.page.cbShape.currentText()) if str(self.page.cbShape.currentText()) else None
		self.sensor.rotation     =     self.page.sbRotation.value()     if    self.page.sbRotation.value() >=0  else None
		self.sensor.channels     =     self.page.sbChannels.value()     if    self.page.sbChannels.value() >=0  else None

		num_comments = self.page.listComments.count()
		self.sensor.comments = []
		for i in range(num_comments):
			self.sensor.comments.append(str(self.page.listComments.item(i).text()))

		self.sensor.inspection = str(self.page.cbInspection.currentText()) if str(self.page.cbInspection.currentText()) else None

		self.sensor.save()
		self.mode = 'view'
		self.update_info()


	
	@enforce_mode(['editing','creating'])
	def deleteComment(self,*args,**kwargs):
		row = self.page.listComments.currentRow()
		if row >= 0:
			self.page.listComments.takeItem(row)

	@enforce_mode(['editing','creating'])
	def addComment(self,*args,**kwargs):
		text = str(self.page.pteWriteComment.toPlainText())
		if text:
			self.page.listComments.addItem(text)
			self.page.pteWriteComment.clear()

	@enforce_mode('view')
	def goShipment(self,*args,**kwargs):
		item = self.page.listShipments.currentItem()
		if not (item is None):
			self.setUIPage('shipments',ID=str(item.text()))
	
	@enforce_mode('view')
	def goStepSensor(self,*args,**kwargs):
		ID = self.page.sbStepSensor.value()
		if ID >= 0:
			self.setUIPage('sensor placement steps',ID=ID)
	
	@enforce_mode('view')
	def goProtomodule(self,*args,**kwargs):
		ID = self.page.sbProtomodule.value()
		if ID >= 0:
			self.setUIPage('protomodules',ID=ID)

	@enforce_mode('view')
	def goModule(self,*args,**kwargs):
		ID = self.page.sbModule.value()
		if ID >= 0:
			self.setUIPage('modules',ID=ID)
		else:
			return



	@enforce_mode('view')
	def load_kwargs(self,kwargs):
		if 'ID' in kwargs.keys():
			ID = kwargs['ID']
			if not (type(ID) is int):
				raise TypeError("Expected type <int> for ID; got <{}>".format(type(ID)))
			if ID < 0:
				raise ValueError("ID cannot be negative")
			self.page.sbID.setValue(ID)

	@enforce_mode('view')
	def changed_to(self):
		print("changed to {}".format(PAGE_NAME))
		self.update_info()
