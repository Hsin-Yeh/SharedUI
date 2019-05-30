from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg    as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

PAGE_NAME = "view_module"
DEBUG = False

USE_MICROAMP = True
MICRO = 1e6

LBL_TIME = 'time (seconds)'
LBL_VOLTAGE = 'voltage (volts)'
LBL_CURRENT = 'current ({})'.format('microamps' if USE_MICROAMP else 'amps')
LBL_VSOURCE = 'sourced voltage (volts)'
LABELS = [LBL_TIME,LBL_VOLTAGE,LBL_CURRENT,LBL_VSOURCE]


class func(object):
	def __init__(self,fm,page,setUIPage,setSwitchingEnabled):
		self.page      = page
		self.setUIPage = setUIPage
		self.setMainSwitchingEnabled = setSwitchingEnabled

		self.ivModuleID = None
		self.ivDataName = None
		self.ivData     = None

		self.module = fm.module()
		self.module_exists = None
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
		self.setupFigures()
		self.rig()
		self.mode = 'view'
		print("{} setup completed".format(PAGE_NAME))
		self.update_info()

	@enforce_mode('setup')
	def setupFigures(self):
		self.fig = Figure()
		self.ax  = self.fig.add_subplot(111)
		self.fc  = FigureCanvas(self.fig)
		self.tb  = NavigationToolbar(self.fc,self.page)
		self.page.vlPlotIV.addWidget(self.tb)
		self.page.vlPlotIV.addWidget(self.fc)
		self.fig.subplots_adjust(left=0.06,right=0.995,top=0.995,bottom=0.102)

	@enforce_mode('setup')
	def rig(self):
		self.page.sbModuleID    .valueChanged.connect(self.update_info )
		self.page.pbGoBaseplate .clicked     .connect(self.goBaseplate )
		self.page.pbGoSensor    .clicked     .connect(self.goSensor    )
		self.page.pbGoPCB       .clicked     .connect(self.goPCB       )
		self.page.pbGoKaptonStep.clicked     .connect(self.goKaptonStep)
		self.page.pbGoSensorStep.clicked     .connect(self.goSensorStep)
		self.page.pbGoPCBStep   .clicked     .connect(self.goPCBStep   )

		self.page.cbIVCurves .currentIndexChanged.connect(self.updateIVData)
		self.page.ckPlotAsc  .stateChanged       .connect(self.updateIVPlot)
		self.page.ckPlotDesc .stateChanged       .connect(self.updateIVPlot)
		self.page.cbBinsXAxis.currentIndexChanged.connect(self.updateIVPlot)
		self.page.cbBinsYAxis.currentIndexChanged.connect(self.updateIVPlot)
		self.page.cbRawXAxis .currentIndexChanged.connect(self.updateIVPlot)
		self.page.cbRawYAxis .currentIndexChanged.connect(self.updateIVPlot)
		self.page.tabBinsRaw .currentChanged     .connect(self.updateIVPlot)

		self.page.pbModuleNew   .clicked.connect(self.startCreating)
		self.page.pbModuleEdit  .clicked.connect(self.startEditing )
		self.page.pbModuleSave  .clicked.connect(self.saveEditing  )
		self.page.pbModuleCancel.clicked.connect(self.cancelEditing)


	@enforce_mode('view')
	def update_info(self,ID=None,*args,**kwargs):
		if ID is None:
			ID = self.page.sbModuleID.value()
		else:
			self.page.sbModuleID.setValue(ID)

		self.module_exists = self.module.load(ID)
		self.page.cbIVCurves.clear()
		# do above for daq data

		if self.module_exists:
			self.page.sbBaseplateID.setValue(self.module.baseplate   if not (self.module.baseplate   is None) else -1  ) # Load values into UI elements
			self.page.sbSensorID   .setValue(self.module.sensor      if not (self.module.sensor      is None) else -1  ) # 
			self.page.sbPCBID      .setValue(self.module.pcb         if not (self.module.pcb         is None) else -1  ) # 
			self.page.dsbThickness .setValue(self.module.thickness   if      self.module.thickness            else  0.0) # 
			self.page.sbKaptonStep .setValue(self.module.step_kapton if not (self.module.step_kapton is None) else -1  ) # 
			self.page.sbSensorStep .setValue(self.module.step_sensor if not (self.module.step_sensor is None) else -1  ) # 
			self.page.sbPCBStep    .setValue(self.module.step_pcb    if not (self.module.step_pcb    is None) else -1  ) # 

			if not (self.module.iv_data is None):
				self.page.cbIVCurves.addItems(self.module.iv_data)
			# do above for daq data

		else:
			self.page.sbBaseplateID.setValue(-1  )
			self.page.sbSensorID   .setValue(-1  )
			self.page.sbPCBID      .setValue(-1  )
			self.page.dsbThickness .setValue( 0.0)
			self.page.sbKaptonStep .setValue(-1  )
			self.page.sbSensorStep .setValue(-1  )
			self.page.sbPCBStep    .setValue(-1  )

		if self.page.sbBaseplateID.value() == -1  : self.page.sbBaseplateID.clear()
		if self.page.sbSensorID   .value() == -1  : self.page.sbSensorID   .clear()
		if self.page.sbPCBID      .value() == -1  : self.page.sbPCBID      .clear()
		if self.page.dsbThickness .value() ==  0.0: self.page.dsbThickness .clear()
		if self.page.sbKaptonStep .value() == -1  : self.page.sbKaptonStep .clear()
		if self.page.sbSensorStep .value() == -1  : self.page.sbSensorStep .clear()
		if self.page.sbPCBStep    .value() == -1  : self.page.sbPCBStep    .clear()

		self.updateElements()

	@enforce_mode(['view','editing','creating'])
	def updateElements(self):

		mode_view     = self.mode == 'view'
		mode_editing  = self.mode == 'editing'
		mode_creating = self.mode == 'creating'

		module_exists      = self.module_exists
		baseplate_exists   = self.page.sbBaseplateID.value() >= 0
		sensor_exists      = self.page.sbSensorID.value()    >= 0
		pcb_exists         = self.page.sbPCBID.value()       >= 0		
		kapton_step_exists = self.page.sbKaptonStep.value()  >= 0
		sensor_step_exists = self.page.sbSensorStep.value()  >= 0
		pcb_step_exists    = self.page.sbPCBStep.value()     >= 0

		self.setMainSwitchingEnabled(mode_view) 

		self.page.pbModuleNew   .setEnabled( mode_view and not module_exists )
		self.page.pbModuleEdit  .setEnabled( mode_view and     module_exists )
		self.page.pbModuleSave  .setEnabled( mode_creating or mode_editing   )
		self.page.pbModuleCancel.setEnabled( mode_creating or mode_editing   )

		self.page.pbGoBaseplate .setEnabled( mode_view and baseplate_exists   )
		self.page.pbGoSensor    .setEnabled( mode_view and sensor_exists      )
		self.page.pbGoPCB       .setEnabled( mode_view and pcb_exists         )
		self.page.pbGoKaptonStep.setEnabled( mode_view and kapton_step_exists )
		self.page.pbGoSensorStep.setEnabled( mode_view and sensor_step_exists )
		self.page.pbGoPCBStep   .setEnabled( mode_view and pcb_step_exists    )
		self.page.sbModuleID    .setEnabled( mode_view )

		self.page.tabBinsRaw.setEnabled( mode_view and module_exists )
		self.page.cbIVCurves.setEnabled( mode_view and module_exists )
		self.tb             .setEnabled( mode_view and module_exists )
		self.fc             .setEnabled( mode_view and module_exists )

		self.page.dsbThickness .setReadOnly( not (mode_editing or mode_creating) )
		self.page.sbBaseplateID.setReadOnly( not (mode_editing or mode_creating) )
		self.page.sbSensorID   .setReadOnly( not (mode_editing or mode_creating) )
		self.page.sbPCBID      .setReadOnly( not (mode_editing or mode_creating) )
		self.page.sbKaptonStep .setReadOnly( not (mode_editing or mode_creating) )
		self.page.sbSensorStep .setReadOnly( not (mode_editing or mode_creating) )
		self.page.sbPCBStep    .setReadOnly( not (mode_editing or mode_creating) )

	@enforce_mode('view')
	def startCreating(self,*args,**kwargs):
		if not self.module_exists:
			ID = self.page.sbModuleID.value()
			self.mode = 'creating'
			self.module.new(ID)
			self.updateElements()
		else:
			pass

	@enforce_mode('view')
	def startEditing(self,*args,**kwargs):
		if not self.module_exists:
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
		self.module.baseplate  = self.page.sbBaseplateID.value() if self.page.sbBaseplateID.value() >= 0 else None
		self.module.sensor     = self.page.sbSensorID.value()    if self.page.sbSensorID.value()    >= 0 else None
		self.module.pcb        = self.page.sbPCBID.value()       if self.page.sbPCBID.value()       >= 0 else None
		self.module.thickness  = self.page.dsbThickness.value()  if self.page.dsbThickness.value()  >  0 else None
		self.module.kaptonstep = self.page.sbKaptonStep.value()  if self.page.sbKaptonStep.value()  >= 0 else None
		self.module.sensorstep = self.page.sbSensorStep.value()  if self.page.sbSensorStep.value()  >= 0 else None
		self.module.PCBstep    = self.page.sbPCBStep.value()     if self.page.sbPCBStep.value()     >= 0 else None
		
		self.module.save()
		self.mode = 'view'
		self.update_info()


	@enforce_mode('view')
	def updateIVData(self,index,*args,**kwargs):
		#print("")
		#print("Beginning updateIVData")
		if self.page.cbIVCurves.currentIndex() == -1:
			#print("index -1 : data set to None")
			self.ivData = None
			self.ivDataName = None
			self.ivModuleID = self.page.sbModuleID.value()
			#print("")
			self.updateIVPlot()
			return

		if self.page.sbModuleID.value() == self.ivModuleID and self.page.cbIVCurves.currentText() == self.ivDataName:
			#print("Neither module ID nor text selection have changed : not changing data")
			#print("")
			return
		
		#print("New module ID ({} -> {}) or text ({} -> {}) - load new dataset!".format(self.ivModuleID,self.page.sbModuleID.value(),self.ivDataName,self.page.cbIVCurves.currentText()))
		self.ivModuleID = self.page.sbModuleID.value()
		self.ivDataName = self.page.cbIVCurves.currentText()
		self.ivData     = [self.module.load_iv(self.ivDataName), *self.module.load_iv_bins(self.ivDataName)] #self.fm.loadModuleIV(self.ivModuleID,self.ivDataName)
		#print("")
		self.updateIVPlot()

	@enforce_mode('view')
	def updateIVPlot(self,*args,**kwargs):
		print("Update plot!")
		tab       = self.page.tabBinsRaw .currentIndex()
		bins_asc  = self.page.ckPlotAsc  .isChecked()
		bins_desc = self.page.ckPlotDesc .isChecked()
		bins_x    = self.page.cbBinsXAxis.currentIndex()
		bins_y    = self.page.cbBinsYAxis.currentIndex()
		raw_x     = self.page.cbRawXAxis .currentIndex()
		raw_y     = self.page.cbRawYAxis .currentIndex()

		if self.ivData is None:
			self.ax.clear()
			self.fc.draw()
			print("No data - clearing")

		elif tab == 0: # bins
			self.ax.clear()

			self.ax.set_xlabel(LABELS[bins_x])
			self.ax.set_ylabel(LABELS[bins_y])

			axdata = self.ivData[1][...,bins_x]
			aydata = self.ivData[1][...,bins_y]
			dxdata = self.ivData[2][...,bins_x]
			dydata = self.ivData[2][...,bins_y]

			if bins_asc:
				self.ax.plot(axdata*(MICRO if bins_x==2 and USE_MICROAMP else 1),aydata*(MICRO if bins_y==2 and USE_MICROAMP else 1),'r.',label='ascending')
			if bins_desc:
				self.ax.plot(dxdata*(MICRO if bins_x==2 and USE_MICROAMP else 1),dydata*(MICRO if bins_y==2 and USE_MICROAMP else 1),'b.',label='descending')
			if bins_asc and bins_desc:
				self.ax.legend()

			self.fc.draw()
			print("Plotting bins!")

		elif tab == 1: # raw
			self.ax.clear()
			self.ax.set_xlabel(LABELS[raw_x])
			self.ax.set_ylabel(LABELS[raw_y])
			xdata = self.ivData[0][...,raw_x]
			ydata = self.ivData[0][...,raw_y]
			self.ax.plot(xdata*(MICRO if raw_x==2 and USE_MICROAMP else 1),ydata*(MICRO if raw_y==2 and USE_MICROAMP else 1),'r.')
			self.fc.draw()
			print("Plotting raw!")

		else:
			self.ax.clear()
			self.fc.draw()
			print("Invalid tab - clearing")


	@enforce_mode('view')
	def goBaseplate(self,*args,**kwargs):
		ID = self.page.sbBaseplateID.value()
		if ID>=0:
			self.setUIPage('baseplates',ID=ID)
		else:
			return

	@enforce_mode('view')
	def goSensor(self,*args,**kwargs):
		ID = self.page.sbSensorID.value()
		if ID>=0:
			self.setUIPage('sensors',ID=ID)
		else:
			return

	@enforce_mode('view')
	def goPCB(self,*args,**kwargs):
		ID = self.page.sbPCBID.value()
		if ID>=0:
			self.setUIPage('PCBs',ID=ID)
		else:
			return

	@enforce_mode('view')
	def goKaptonStep(self,*args,**kwargs):
		ID = self.page.sbKaptonStep.value()
		if ID>=0:
			self.setUIPage('kapton placement steps',ID=ID)
		else:
			return

	@enforce_mode('view')
	def goSensorStep(self,*args,**kwargs):
		ID = self.page.sbSensorStep.value()
		if ID>=0:
			self.setUIPage('sensor placement steps',ID=ID)
		else:
			return

	@enforce_mode('view')
	def goPCBStep(self,*args,**kwargs):
		ID = self.page.sbPCBStep.value()
		if ID>=0:
			self.setUIPage('PCB placement steps',ID=ID)
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
			self.page.sbModuleID.setValue(ID)

	@enforce_mode('view')
	def changed_to(self):
		print("changed to {}".format(PAGE_NAME))
