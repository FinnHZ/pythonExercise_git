
import pyprofibus
import pyprofibus.phy_serial
from pyprofibus.dp_master import DpSlaveState, DpMaster
# from pyprofibus.phy_serial import CpPhySerial
import time


# profibusDPMaster = DpSlaveState("COM9", 1)


# abc = profibusDPMaster.getState()

# print(abc)

# config = pyprofibus.PbConf.fromFile("./modbusCommunicate/static/document/example_dummy_inputonly.conf")  #../modbusCommunicate/static/example_dummy_inputonly.conf



phyClass = pyprofibus.phy_serial.CpPhySerial
# dpmObj = DpMaster(dpmClass, pyObj, masterAddr)


# for slaveConf in config.slaveConfs:


# slaveConf = config.slaveConfs[0]    
# slaveDesc = slaveConf.makeDpSlaveDesc()

# master = config.makeDPM()


phy = phyClass(#debug=(self.debug >= 2),
            port="COM9",
            #spiBus=self.phySpiBus,
            #spiCS=self.phySpiCS,
            #spiSpeedHz=self.phySpiSpeedHz,
            #**extraKwArgs
            )



# while True:
    # profibusDPMaster = DpSlaveState(master, slaveDesc)
    # a = profibusDPMaster.getState()
    # b = profibusDPMaster.getRxQueue()
    # c = profibusDPMaster.flushRxQueue()
    # d = profibusDPMaster.getNextState()
    # e = profibusDPMaster.stateJustEntered()
    # f = profibusDPMaster.stateIsChanging()
    # g = profibusDPMaster.restartStateTimeout()
    # h = profibusDPMaster.stateHasTimeout()
    
    # print(a)
    # print(b)
    # print(c)
    # print(d)
    # print(e)
    # print(f)
    # print(g)
    # print(h)
    # print("***************************************************")

    # time.sleep(0.5)
profibusDPMaster = DpMaster(1, phy, 1)
print(profibusDPMaster.getSlaveList())
