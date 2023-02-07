from PyQt5 import QtWidgets, QtGui
import sys
from frontend import Ui_PredatorNonSense
from ecwrite import ec_write, ec_read
import enum
# ?Constants
GPU_FAN_MODE_CONTROL = '0x21'
GPU_AUTO_MODE = '0x50'
GPU_TURBO_MODE = '0x60'
GPU_MANUAL_MODE = '0x70'
GPU_MANUAL_SPEED_CONTROL = '0x3A'
COOL_BOOST_CONTROL = '0x10'
COOL_BOOST_ON = '0x01'
COOL_BOOST_OFF = '0x00'
TURBO_LED_CONTROL = '0x5B'
TURBO_LED_ON = '0x01'
TURBO_LED_OFF = '0x00'
CPU_FAN_MODE_CONTROL = '0x22'
CPU_AUTO_MODE = '0x54'
CPU_TURBO_MODE = '0x58'
CPU_MANUAL_MODE = '0x5C'
CPU_MANUAL_SPEED_CONTROL = '0x37'
KB_BRIGHTNESS = '0x19'
BRIGHTNESS_STANDARDS = ['0x00', '0x19', '0x32', '0x4B', '0x64']
AUTO_TURN_OFF = '0x06'
AUTO_TURN_OFF_ON = '0x1E'
AUTO_TURN_OFF_OFF = '0x00'
KB_STATIC = '0x00'
KB_BREATHING = '0x01'
KB_NEON = '0x02'
KB_WAVE = '0x03'
KB_SHIFTING = '0x04'
KB_MODE_SET = '0x17'
KB_SPEED_SET = '0x18'
KB_COLOR_SET = ['0x1C', '0x1D', '0x1E']
KB_DIRECTION_LTR = '0x01'
KB_DIRECTION_RTL = '0x02'
KB_RS = ['0x3C', '0x3F', '0x42', '0x45']
KB_GS = ['0x3D', '0x40', '0x43', '0x46']
KB_BS = ['0x3E', '0x41', '0x44', '0x47']
ZONES_ON = [1, 1, 1, 1]
KB_30_SEC_AUTO = '0x06'
KB_30_AUTO_OFF = '0x00'
KB_30_AUTO_ON = '0x1E'
FAN_PROFILE_CONTROL = '0x29'
FAN_PROFILE_NORMAL = '0x00'
FAN_PROFILE_PERF = '0x01'
FAN_PROFILE_AGGR = '0x02'
BAT_LIMIT_CONTROL = "0x03"
BAT_LIMIT_100 = "0x31"
BAT_LIMIT_80 = "0x71"


class PFS(enum.Enum):  # ProcessorFanState
    Manual = 0
    Auto = 1
    Turbo = 2


class PU(enum.Enum):  # ProcessingUnit
    CPU = 0
    GPU = 1


class MainWindow(QtWidgets.QDialog, Ui_PredatorNonSense):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.cb = True if ec_read(int(COOL_BOOST_CONTROL, 0)) == 1 else False
        if self.cb:
            self.checkBox.setChecked(True)
        tempvar = int(ec_read(int(CPU_FAN_MODE_CONTROL, 0)))
#        print(tempvar)
        if tempvar == 84 or tempvar == 00:
            self.cpuFanMode = PFS.Auto
            self.radioButton.setChecked(True)
        elif tempvar == 88:
            self.cpuFanMode = PFS.Turbo
            self.radioButton_3.setChecked(True)
        elif tempvar == 92 or tempvar == 93:
            self.cpuFanMode = PFS.Manual
            self.radioButton_2.setChecked(True)
        else:
            print('FOUND', tempvar)
            print('UNKNOWN VALUE FOUND EXITT at cpu box')
            self.cpuauto()
#           exit(1)
        tempvar = int(ec_read(int(GPU_FAN_MODE_CONTROL, 0)))
        if tempvar == 80 or tempvar == 00:
            self.gpuFanMode = PFS.Auto
            self.radioButton_4.setChecked(True)
        elif tempvar == 96:
            self.gpuFanMode = PFS.Turbo
            self.radioButton_5.setChecked(True)
        elif tempvar == 112:
            self.gpuFanMode = PFS.Manual
            self.radioButton_6.setChecked(True)
        else:
            print('FOUND', tempvar)
            print('UNKNOWN VALUE FOUND EXITT at gpu box')
            self.gpuauto()
#            exit(1)
        tempvar = ec_read(int(KB_30_SEC_AUTO, 0))
        # print('kb30',tempvar)
        if tempvar == int(KB_30_AUTO_OFF, 0):
            self.checkBox_2.setChecked(False)
        else:
            self.checkBox_2.setChecked(True)
        tempvar = ec_read(int(FAN_PROFILE_CONTROL, 0))
        if tempvar == int(FAN_PROFILE_NORMAL, 0):
            self.radioButton_14.setChecked(True)
        elif tempvar == int(FAN_PROFILE_PERF, 0):
            self.radioButton_15.setChecked(True)
        elif tempvar == int(FAN_PROFILE_AGGR, 0):
            self.radioButton_16.setChecked(True)
        tempvar = ec_read(int(BAT_LIMIT_CONTROL, 0))
        if tempvar == int(BAT_LIMIT_100, 0):
            self.radioButton_17.setChecked(True)
        elif tempvar == int(BAT_LIMIT_80, 0):
            self.radioButton_18.setChecked(True)
        self.radioButton.toggled['bool'].connect(self.cpuauto)
        self.radioButton_3.toggled.connect(self.cpureeeer)
        self.radioButton_4.toggled.connect(self.gpuauto)
        self.radioButton_5.toggled.connect(self.gpureeeer)
        self.checkBox.clicked['bool'].connect(self.toggleCB)
        self.verticalSlider.valueChanged.connect(self.cpumanual)
        self.verticalSlider_2.valueChanged.connect(self.gpumanual)
        self.radioButton_2.toggled.connect(self.cpusetmanual)
        self.radioButton_6.toggled.connect(self.gpusetmanual)
        self.pushButton.clicked.connect(exit)
        self.radioButton_8.clicked.connect(self.setstatic)
        self.pushButton_4.clicked.connect(self.setcolor)
        self.radioButton_10.clicked.connect(self.setbreathing)
        self.verticalSlider_4.sliderMoved.connect(self.setbrightness)
        self.radioButton_11.clicked.connect(self.setneon)
        self.radioButton_12.clicked.connect(self.setwave)
        self.radioButton_13.clicked.connect(self.setshifting)
        self.pushButton_2.clicked.connect(self.changedirtortl)
        self.pushButton_3.clicked.connect(self.changedirtoltr)
        self.pushButton_5.clicked.connect(self.z0)
        self.pushButton_6.clicked.connect(self.z1)
        self.pushButton_7.clicked.connect(self.z2)
        self.pushButton_8.clicked.connect(self.z3)
        self.checkBox_2.clicked['bool'].connect(self.togglekbauto)
        self.radioButton_14.toggled.connect(self.fanprofnormal)
        self.radioButton_15.toggled.connect(self.fanprofperf)
        self.radioButton_16.toggled.connect(self.fanprofaggr)
        self.radioButton_17.toggled.connect(self.batLimitOff)
        self.radioButton_18.toggled.connect(self.batLimitOn)

    def cpureeeer(self):
        ec_write(int(CPU_FAN_MODE_CONTROL, 0), int(CPU_TURBO_MODE, 0))
        self.cpuFanMode = PFS.Turbo
        self.ledset()

    def gpureeeer(self):
        ec_write(int(GPU_FAN_MODE_CONTROL, 0), int(GPU_TURBO_MODE, 0))
        self.gpuFanMode = PFS.Turbo
        self.ledset()

    def cpuauto(self):
        ec_write(int(CPU_FAN_MODE_CONTROL, 0), int(CPU_AUTO_MODE, 0))
        self.cpuFanMode = PFS.Auto
        self.ledset()

    def gpuauto(self):
        ec_write(int(GPU_FAN_MODE_CONTROL, 0), int(GPU_AUTO_MODE, 0))
        self.gpuFanMode = PFS.Auto
        self.ledset()

    def ledset(self):
        if self.cpuFanMode == PFS.Turbo or self.gpuFanMode == PFS.Turbo:
            ec_write(int(TURBO_LED_CONTROL, 0), int(TURBO_LED_ON, 0))
        else:
            ec_write(int(TURBO_LED_CONTROL, 0), int(TURBO_LED_OFF, 0))

    def toggleCB(self, tog):
        print('tog')
        if tog:
            ec_write(int(COOL_BOOST_CONTROL, 0), int(COOL_BOOST_ON, 0))
        elif not tog:
            ec_write(int(COOL_BOOST_CONTROL, 0), int(COOL_BOOST_OFF, 0))

    def cpumanual(self, level):
        print(str(level*10), end=', ')
        print(hex(level*10))
        ec_write(int(CPU_MANUAL_SPEED_CONTROL, 0), level*10)

    def gpumanual(self, level):
        print(level*10, end=', ')
        print(hex(level*10))
        ec_write(int(GPU_MANUAL_SPEED_CONTROL, 0), level*10)

    def cpusetmanual(self):
        ec_write(int(CPU_FAN_MODE_CONTROL, 0), int(CPU_MANUAL_MODE, 0))
        self.cpuFanMode = PFS.Manual

    def gpusetmanual(self):
        ec_write(int(GPU_FAN_MODE_CONTROL, 0), int(GPU_MANUAL_MODE, 0))
        self.gpuFanMode = PFS.Manual

    def setstatic(self):
        ec_write(int(KB_MODE_SET, 0), int(KB_STATIC, 0))
        self.setcolor()

    def setbreathing(self):
        ec_write(int(KB_MODE_SET, 0), int(KB_BREATHING, 0))
        ec_write(int(KB_SPEED_SET, 0), int(self.verticalSlider_3.value()))
        self.setcolor()

    def setneon(self):
        ec_write(int(KB_MODE_SET, 0), int(KB_NEON, 0))
        ec_write(int(KB_SPEED_SET, 0), int(self.verticalSlider_3.value()))

    def setwave(self):
        ec_write(int(KB_MODE_SET, 0), int(KB_WAVE, 0))
        ec_write(int(KB_SPEED_SET, 0), int(self.verticalSlider_3.value()))

    def setshifting(self):
        ec_write(int(KB_MODE_SET, 0), int(KB_SHIFTING, 0))
        ec_write(int(KB_SPEED_SET, 0), int(self.verticalSlider_3.value()))

    def setbrightness(self, bt):
        ec_write(int(KB_BRIGHTNESS, 0), int(BRIGHTNESS_STANDARDS[bt], 0))

    def changedirtoltr(self):
        ec_write(int('0x1B', 0), int(KB_DIRECTION_LTR, 0))

    def changedirtortl(self):
        ec_write(int('0x1B', 0), int(KB_DIRECTION_RTL, 0))

    def z0(self):
        if ZONES_ON[0] == 1:
            ZONES_ON[0] = 0
        else:
            ZONES_ON[0] = 1
        self.togglezones()

    def z1(self):
        if ZONES_ON[1] == 1:
            ZONES_ON[1] = 0
        else:
            ZONES_ON[1] = 1
        self.togglezones()

    def z2(self):
        if ZONES_ON[2] == 1:
            ZONES_ON[2] = 0
        else:
            ZONES_ON[2] = 1
        self.togglezones()

    def z3(self):
        if ZONES_ON[3] == 1:
            ZONES_ON[3] = 0
        else:
            ZONES_ON[3] = 1
        self.togglezones()

    def togglezones(self):
        s = 0
        for i in range(4):
            s += ZONES_ON[i]*(2**i)
        print(s)
        ec_write(int('0x1F', 0), s)

    def setcolor(self):
        colors = [self.spinBox.value(), self.spinBox_2.value(),
                  self.spinBox_3.value()]
        print(colors)
        for i in range(3):
            ec_write(int(KB_COLOR_SET[i], 0), colors[i])
        for i in KB_RS:
            ec_write(int(i, 0), colors[0])
        for i in KB_GS:
            ec_write(int(i, 0), colors[1])
        for i in KB_BS:
            ec_write(int(i, 0), colors[2])

    def togglekbauto(self, tog):
        # print('received', tog)
        if not tog:
            # self.checkBox_2.setChecked(False)
            ec_write(int(KB_30_SEC_AUTO, 0), int(KB_30_AUTO_OFF, 0))
        else:
            # self.checkBox_2.setChecked(True)
            ec_write(int(KB_30_SEC_AUTO, 0), int(KB_30_AUTO_ON, 0))

    def fanprofnormal(self):
        ec_write(int(FAN_PROFILE_CONTROL, 0), int(FAN_PROFILE_NORMAL, 0))

    def fanprofperf(self):
        ec_write(int(FAN_PROFILE_CONTROL, 0), int(FAN_PROFILE_PERF, 0))

    def fanprofaggr(self):
        ec_write(int(FAN_PROFILE_CONTROL, 0), int(FAN_PROFILE_AGGR, 0))

    def batLimitOff(self):
        ec_write(int(BAT_LIMIT_CONTROL, 0), int(BAT_LIMIT_100, 0))

    def batLimitOn(self):
        ec_write(int(BAT_LIMIT_CONTROL, 0), int(BAT_LIMIT_80, 0))


app = QtWidgets.QApplication([])
application = MainWindow()
# application.cpuauto()
# application.gpuauto()
app.setStyle('Breeze')
# application.radioButton.toggled.
application.setWindowIcon(QtGui.QIcon('acer.png'))
application.show()
sys.exit(app.exec())
