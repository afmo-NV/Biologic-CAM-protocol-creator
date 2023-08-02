BT-LAB SETTING FILE

Number of linked techniques : 3

BT-LAB for windows v1.74 (software)
Internet server v1.74 (firmware)
Command interpretor v1.74 (firmware)

Filename : C:\Users\QC-Cycler\Documents\QC\Cycle_Life_Standard_Protocol-Template-C-N.mps

Device : BCS-810
Ecell ctrl range : min = 0,00 V, max = 10,00 V
Safety Limits :
	Ecell min = 2,50 V
	Ecell max = 4,50 V
	for t > 100 ms
Electrode material : 
Initial state : 
Electrolyte : 
Comments : 
Mass of active material : 0,001 mg
 at x = 0,000
Molecular weight of active material (at x = 0) : 0,001 g/mol
Atomic weight of intercalated ion : 0,001 g/mol
Acquisition started at : xo = 0,000
Number of e- transfered per intercalated ion : 1
for DX = 1, DQ = 26,802 mA.h
Battery capacity : 0,000 A.h
Electrode surface area : 0,000 cm²
Characteristic mass : 0,001 g
Volume (V) : 0,001 cm³
Cycle Definition : Charge/Discharge alternance
Turn to OCV between techniques

Technique : 1
Open Circuit Voltage
tR (h:m:s)          3:00:0,0000         
dER/dt (mV/h)       0,0                 
record              Ewe                 
dER (mV)            5,00                
dtR (s)             10,000              
E range min (V)     0,000               
E range max (V)     10,000              

Technique : 2
Galvanostatic Cycling with Potential Limitation
Ns                  0                   1                   2                   
Set I/C             I                   C / N               C / N               
Is                  0,000               1,500               -3,000              
unit Is             mA                  mA                  mA                  
vs.                 <None>              <None>              <None>              
N                   1,00                2,00                1,00                
I sign              > 0                 > 0                 < 0                 
t1 (h:m:s)          0:00:0,0000         5:00:0,0000         3:00:0,0000         
I Range             10 mA               10 mA               10 mA                
Bandwidth           1                   1                   1                   
dE1 (mV)            0,00                5,00                5,00                
dt1 (s)             0,000               10,000              10,000              
EM (V)              0,000               4,300               3,000               
tM (h:m:s)          0:00:0,0000         2:00:0,0000         0:00:0,0000         
Im                  0,000               150,000             0,000             
unit Im             mA                  µA                  µA                  
dI/dt               0,000               0,000               0,000               
dunit dI/dt         mA/s                mA/s                mA/s                
E range min (V)     0,000               0,000               0,000               
E range max (V)     10,000              10,000              10,000              
dq                  0,000               0,000               0,000               
unit dq             A.h                 A.h                 A.h                 
dtq (s)             0,000               10,000              10,000              
dQM                 0,000               0,000               0,000               
unit dQM            mA.h                mA.h                mA.h                
dxM                 0,000               0,000               0,000               
delta SoC (%)       pass                pass                pass                
tR (h:m:s)          0:00:0,0000         0:05:0,0000         0:05:0,0000         
dER/dt (mV/h)       0,0                 0,0                 0,0                 
dER (mV)            0,00                0,00                0,00                
dtR (s)             60,000              10,000              10,000              
EL (V)              pass                pass                pass                
goto Ns'            0                   0                   0                   
nc cycles           0                   0                   0                   

Technique : 3
Loop
goto Ne             2                   
nt times            49                  
