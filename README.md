# Fuel_Consumption_Analysis
 A comprehensive analysis of the fuel consumption of a sweeper vehicle, looking at the different factors which play into the fuel usage.

# Log Files

Key columns:
. time
. Longitude and Latitude for Velocity
. Nozzle1downTMSCS
. Nozzle2downTMSCS
. SideBrush1downTMS
. SideBrush2downTMS
. BrushCurrent
. SideBrush1ExtendTMSCS
. SideBrush2ExtendTMSCS
. SideBrush1RetractTMSCS
. SideBrush2RetractTMSCS
. Nozzle1WaterSprayOnOffTMS
. Nozzle2WaterSprayOnOffTMS
. SideBrush1WaterSprayTMS
. SideBrush2WaterSprayTMS
. WSBMotoronoffTMS
. FanOnTMS
. WorkLight1OnOffTMS
. WorkLight2OnOffTMS
. NozGapOpen
. NozGapClose
. Pause_active
. AutoSweepActive
. EngineType
. EngineSpeed
. RoadSpeedTMSCS
. EngineFuelRateTMSCS
. FanSpeed
. TotalFuelConsumption
. GutterSprayOnOff
. AddWaterSprayOnOff
. WaterRe_circOnOff

Fuel information:
. EngineFuelRateTMSCS
. TotalFuelConsumption

Smart sweeping enables an automated response to the nozzle being blocked. This allows for an optimised response, using minimal fuel to control the nozzle and fan speed to clear the blockage.
In this regard the columns of interest are:
. time
. NozGapOpen
. NozGapClose
. FanSpeed
. EngineFuelRateTMSCS
. TotalFuelConsumption

First step is therefore to extract these columns from the log file, putting them into a csv for easier interpretation and manipulation.

extract_columns.py

Inside this python file, a procedure called 'extract_columns(data_filename, requested_columns)', accepts the data file name as an argument which could either be a log file or a vbox file. The procedure also accepts an array of requested columns from that particular data file as another argument. Using this information, the procedure creates a new csv file which is then filled with the specified column data extracted from the given data file. 

