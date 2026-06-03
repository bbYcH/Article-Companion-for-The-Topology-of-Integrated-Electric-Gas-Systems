"""Hardcoded P14_G11 integrated energy system benchmark.

Power-system topology data source:
Zimmerman R D, Murillo-Sánchez C E, Thomas R J. MATPOWER: Steady-state
operations, planning, and analysis tools for power systems research and
education[J]. IEEE Transactions on power systems, 2010, 26(1): 12-19.

Gas-network topology data source:
Schmidt M, Aßmann D, Burlacu R, et al. GasLib—A library of gas network
instances[J]. Data, 2017, 2(4): 40.
"""

from numpy import array
import numpy as np

CASE_NAME = "P14_G11"
POWER_CASE_NAME = "case14"
GAS_CASE_ID = 11


def GAS_11N():

    # Well:     well data
    # Storage:  Storage sources data
    # Comp:     Cmperossor data
    # Pipeline: Pipeline data
    # Node:     Nodes data

    Gas = {}

    ## Well source data
    Gas["Well"] = array([
        #  0   ,    1    ,    2    ,          3          ,    4   ,     5     ,    6   
        # Node ,  Max    ,  Min    ,  Cost               ,  index ,  Ref_flag ,  output
        # -    ,  MSm3/h ,  MSm3/h ,  cost coefficient   ,  -     ,  -        ,  MSm3/h
        [  1.0 ,    0.16 ,     0.0 ,  228.56626147549375 ,    1.0 ,       1.0 ,     0.0 ],
        [  2.0 ,   0.115 ,     0.0 ,  190.47188456291147 ,    2.0 ,       0.0 ,     0.0 ],
        [  3.0 ,     1.0 ,     0.0 ,   355.5475178507681 ,    3.0 ,       0.0 ,     0.0 ],
    ], dtype=np.float64)


    # GenGas coupled generator data
    # Gentype: 1=gas turbine/gas generator; 0=non-gas generator.
    Gas["GenGas"] = array([
        #    0    ,      1      ,     2    ,     3    
        # Gentype ,  efficiency ,  GasNode ,  PowerBus
        # -       ,  p.u.       ,  -       ,  -       
        [     1.0 ,        0.55 ,      3.0 ,       5.0 ],
        [     0.0 ,         0.0 ,      1.0 ,       4.0 ],
        [     1.0 ,        0.45 ,      5.0 ,       7.0 ],
    ], dtype=np.float64)

    ## Load
    TN = 24
    # Gas demand profile
    # Columns: 0..23 timestep index
    # Units:   p.u. gas-load multiplier
    Gas["Demand"] = np.ones(TN, dtype=np.float64)
    ## Gas Load Data
    #
    Gas["Load"] = array([
        #  0   ,       1      ,   2   ,       3      ,   4   ,     5    
        # Node ,  Pressuremax ,  pmin ,  load_demand ,  flag ,  pressure
        # -    ,  bar         ,  bar  ,  MSm3/h      ,  -    ,  bar     
        # flag: 1=reference, 2=gas load, 3=gas source, 0=junction
        [  1.0 ,         70.0 ,  40.0 ,          0.0 ,   1.0 ,      50.0 ],
        [  2.0 ,         70.0 ,  40.0 ,          0.0 ,   3.0 ,       0.0 ],
        [  3.0 ,         70.0 ,  40.0 ,          0.0 ,   3.0 ,       0.0 ],
        [  4.0 ,         70.0 ,  40.0 ,          0.1 ,   2.0 ,       0.0 ],
        [  5.0 ,         60.0 ,  40.0 ,         0.12 ,   2.0 ,       0.0 ],
        [  6.0 ,         60.0 ,  40.0 ,         0.08 ,   2.0 ,       0.0 ],
        [  7.0 ,         70.0 ,  40.0 ,          0.0 ,   0.0 ,       0.0 ],
        [  8.0 ,         70.0 ,  40.0 ,          0.0 ,   0.0 ,       0.0 ],
        [  9.0 ,         70.0 ,  40.0 ,          0.0 ,   0.0 ,       0.0 ],
        [ 10.0 ,         70.0 ,  40.0 ,          0.0 ,   0.0 ,       0.0 ],
        [ 11.0 ,         70.0 ,  40.0 ,          0.0 ,   0.0 ,       0.0 ],
    ], dtype=np.float64)


    ## Pipeline without compressor data
    Gas["Pipeline"] = array([
        #     0     ,     1     ,     2    ,     3     ,       4      ,            5           
        # BeginNode ,  TermNode ,  Length  ,  Diameter ,  Km          ,  Kq                    
        # -         ,  -        ,  m       ,  m        ,  (MSm3/h)/Pa ,  (MSm3/h)^2/bar^2      
        [       1.0 ,       2.0 ,  55000.0 ,       0.5 ,       0.0152 ,  0.00020984493122057585 ],
        [       7.0 ,       8.0 ,  55000.0 ,       0.5 ,       0.0188 ,  4.7436733945623526e-05 ],
        [       3.0 ,       9.0 ,  55000.0 ,       0.5 ,       0.0129 ,   6.899888573908876e-05 ],
        [       8.0 ,       4.0 ,  55000.0 ,       0.5 ,       0.0118 ,   7.589877431299764e-05 ],
        [       8.0 ,      10.0 ,  55000.0 ,       0.5 ,       0.0271 ,  0.00011803777381157391 ],
        [       9.0 ,      10.0 ,  55000.0 ,       0.5 ,       0.0129 ,   6.899888573908876e-05 ],
        [      11.0 ,       5.0 ,  55000.0 ,       0.5 ,       0.0188 ,  4.7436733945623526e-05 ],
        [      11.0 ,       6.0 ,  55000.0 ,       0.5 ,       0.0188 ,  4.7436733945623526e-05 ],
    ], dtype=np.float64)

    ## Pipeline with compressor data
    # Type: 1=electric compressor, 2=gas compressor.
    Gas["Comp"] = array([
        #     0     ,      1      ,   2   ,     3     ,    4   ,   5  ,   6  ,   7   ,   8   ,   9   ,   10  ,   11 ,   12  ,      13     ,    14 
        # InputNode ,  OutputNode ,  Type ,  CompFact ,  alpha ,  k1  ,  k2  ,  Rmin ,  Rmax ,  Hmin ,  Hmax ,  Bus ,  loss ,  efficiency ,  ratio
        # -         ,  -          ,  -    ,  -        ,  -     ,  -   ,  -   ,  -    ,  -    ,  MW   ,  MW   ,  -   ,  p.u. ,  p.u.       ,  -    
        [       2.0 ,         7.0 ,   2.0 ,       1.1 ,   0.24 ,  1.2 ,  1.0 ,   1.0 ,   1.2 ,   0.0 ,  50.0 ,  5.0 ,  0.04 ,        0.55 ,    0.0 ],
        [      10.0 ,        11.0 ,   2.0 ,       1.1 ,   0.24 ,  1.2 ,  1.0 ,   1.0 ,   1.2 ,   0.0 ,  50.0 ,  5.0 ,  0.04 ,        0.55 ,    0.0 ],
    ], dtype=np.float64)

    ## P2G data
    # Compact schema: PowerBus, GasNode, efficiency, P, mBase, Pmax, Pmin.
    Gas["P2G"] = array([
        #    0     ,     1    ,      2      ,   3  ,    4   ,   5   ,   6  
        # PowerBus ,  GasNode ,  efficiency ,  P   ,  mBase ,  Pmax ,  Pmin
        # -        ,  -       ,  p.u.       ,  MW  ,  MVA   ,  MW   ,  MW  
        [      3.0 ,      6.0 ,        0.45 ,  0.0 ,  100.0 ,   5.0 ,   0.0 ],
    ], dtype=np.float64)

    return Gas

# -----------------------------------------------------------------------------
# Integrated energy system construction
# -----------------------------------------------------------------------------
from pathlib import Path
import sys

import pandapower.networks as pn

THIS_DIR = Path(__file__).resolve().parent
WORKSPACE_ROOT = THIS_DIR.parent
RL_OPF_ROOT = WORKSPACE_ROOT / "RL_OPF"

if str(RL_OPF_ROOT) not in sys.path:
    sys.path.insert(0, str(RL_OPF_ROOT))

from utilities.getMyDataG import getMyDataG  # noqa: E402


def IEGS_P14_G11():
    Gas = GAS_11N()

    power_net = pn.case14()
    power_net.load.reset_index(drop=True, inplace=True)
    power_net.gen.reset_index(drop=True, inplace=True)
    power_net.ext_grid.reset_index(drop=True, inplace=True)

    power_net.ext_grid["name"] = "GP"
    power_net.gen["name"] = "GP"
    power_net.gen.loc[[2, 3], "name"] = "GT"

    gp_mask = power_net.gen.name == "GP"
    power_net.gen.loc[gp_mask, "min_p_mw"] = np.maximum(
        power_net.gen.loc[gp_mask, "min_p_mw"].astype(float),
        14.0,
    )
    power_net.ext_grid["max_q_mvar"] = np.maximum(
        power_net.ext_grid["max_q_mvar"].astype(float),
        12.0,
    )

    Data = getMyDataG(Gas, power_net, DynamicUsed=1)
    Data.setdefault("verbose", 0)
    Data["iegs_case_name"] = CASE_NAME
    Data["power_case_name"] = POWER_CASE_NAME
    Data["gas_case_id"] = GAS_CASE_ID
    return Gas, power_net, Data


if __name__ == "__main__":
    gas, net, data = IEGS_P14_G11()
    print(CASE_NAME, gas["GenGas"].shape, gas["P2G"].shape, len(net.bus), len(net.gen), data["GN"])
