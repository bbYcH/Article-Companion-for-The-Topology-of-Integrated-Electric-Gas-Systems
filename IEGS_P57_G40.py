"""Hardcoded P57_G40 integrated energy system benchmark.

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

CASE_NAME = "P57_G40"
POWER_CASE_NAME = "case57"
GAS_CASE_ID = 40


def GAS_40N():

    # Well:     well data
    # Storage:  Storage sources data
    # Comp:     Cmperossor data
    # Pipeline: Pipeline data
    # Node:     Nodes data

    Gas = {}

    ## Well source data
    Gas["Well"] = array([
        #  0   ,    1    ,    2    ,          3         ,    4   ,     5     ,    6   
        # Node ,  Max    ,  Min    ,  Cost              ,  index ,  Ref_flag ,  output
        # -    ,  MSm3/h ,  MSm3/h ,  cost coefficient  ,  -     ,  -        ,  MSm3/h
        [  1.0 ,     2.5 ,    -1.0 ,  2692.336249754718 ,    1.0 ,       1.0 ,     0.0 ],
        [  2.0 ,     1.5 ,     0.0 ,  2243.613541462265 ,    2.0 ,       0.0 ,     0.0 ],
        [  3.0 ,     1.5 ,     0.0 ,  2243.613541462265 ,    3.0 ,       0.0 ,     0.0 ],
    ], dtype=np.float64)


    # GenGas coupled generator data
    # Gentype: 1=gas turbine/gas generator; 0=non-gas generator.
    Gas["GenGas"] = array([
        #    0    ,      1      ,     2    ,     3    
        # Gentype ,  efficiency ,  GasNode ,  PowerBus
        # -       ,  p.u.       ,  -       ,  -       
        [     0.0 ,         0.0 ,      1.0 ,       2.0 ],
        [     0.0 ,         0.0 ,      1.0 ,       3.0 ],
        [     0.0 ,         0.0 ,      1.0 ,       6.0 ],
        [     1.0 ,        0.55 ,     36.0 ,       8.0 ],
        [     0.0 ,         0.0 ,      1.0 ,       9.0 ],
        [     1.0 ,        0.45 ,     40.0 ,      12.0 ],
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
        [  1.0 ,     81.01325 ,  68.0 ,          0.0 ,   1.0 ,      74.0 ],
        [  2.0 ,     81.01325 ,  30.0 ,          0.0 ,   3.0 ,       0.0 ],
        [  3.0 ,     81.01325 ,  30.0 ,          0.0 ,   3.0 ,       0.0 ],
        [  4.0 ,     81.01325 ,  30.0 ,        0.075 ,   2.0 ,       0.0 ],
        [  5.0 ,     81.01325 ,  30.0 ,        0.075 ,   2.0 ,       0.0 ],
        [  6.0 ,     81.01325 ,  30.0 ,        0.075 ,   2.0 ,       0.0 ],
        [  7.0 ,     81.01325 ,  30.0 ,        0.075 ,   2.0 ,       0.0 ],
        [  8.0 ,     81.01325 ,  30.0 ,        0.075 ,   2.0 ,       0.0 ],
        [  9.0 ,     81.01325 ,  30.0 ,        0.075 ,   2.0 ,       0.0 ],
        [ 10.0 ,     81.01325 ,  30.0 ,        0.075 ,   2.0 ,       0.0 ],
        [ 11.0 ,     81.01325 ,  30.0 ,        0.075 ,   2.0 ,       0.0 ],
        [ 12.0 ,     81.01325 ,  30.0 ,        0.075 ,   2.0 ,       0.0 ],
        [ 13.0 ,     81.01325 ,  30.0 ,        0.075 ,   2.0 ,       0.0 ],
        [ 14.0 ,     81.01325 ,  30.0 ,        0.075 ,   2.0 ,       0.0 ],
        [ 15.0 ,     81.01325 ,  30.0 ,        0.075 ,   2.0 ,       0.0 ],
        [ 16.0 ,     81.01325 ,  30.0 ,        0.075 ,   2.0 ,       0.0 ],
        [ 17.0 ,     81.01325 ,  30.0 ,        0.075 ,   2.0 ,       0.0 ],
        [ 18.0 ,     81.01325 ,  30.0 ,        0.075 ,   2.0 ,       0.0 ],
        [ 19.0 ,     81.01325 ,  30.0 ,        0.075 ,   2.0 ,       0.0 ],
        [ 20.0 ,     81.01325 ,  30.0 ,        0.075 ,   2.0 ,       0.0 ],
        [ 21.0 ,     81.01325 ,  30.0 ,        0.075 ,   2.0 ,       0.0 ],
        [ 22.0 ,     81.01325 ,  30.0 ,        0.075 ,   2.0 ,       0.0 ],
        [ 23.0 ,     81.01325 ,  30.0 ,        0.075 ,   2.0 ,       0.0 ],
        [ 24.0 ,     81.01325 ,  30.0 ,        0.075 ,   2.0 ,       0.0 ],
        [ 25.0 ,     81.01325 ,  30.0 ,        0.075 ,   2.0 ,       0.0 ],
        [ 26.0 ,     81.01325 ,  30.0 ,        0.075 ,   2.0 ,       0.0 ],
        [ 27.0 ,     81.01325 ,  30.0 ,        0.075 ,   2.0 ,       0.0 ],
        [ 28.0 ,     81.01325 ,  30.0 ,        0.075 ,   2.0 ,       0.0 ],
        [ 29.0 ,     81.01325 ,  30.0 ,        0.075 ,   2.0 ,       0.0 ],
        [ 30.0 ,     81.01325 ,  30.0 ,        0.075 ,   2.0 ,       0.0 ],
        [ 31.0 ,     81.01325 ,  30.0 ,        0.075 ,   2.0 ,       0.0 ],
        [ 32.0 ,     81.01325 ,  30.0 ,        0.075 ,   2.0 ,       0.0 ],
        [ 33.0 ,     81.01325 ,  30.0 ,          0.0 ,   0.0 ,       0.0 ],
        [ 34.0 ,     81.01325 ,  30.0 ,          0.0 ,   0.0 ,       0.0 ],
        [ 35.0 ,     81.01325 ,  30.0 ,          0.0 ,   0.0 ,       0.0 ],
        [ 36.0 ,     81.01325 ,  30.0 ,          0.0 ,   0.0 ,       0.0 ],
        [ 37.0 ,     81.01325 ,  30.0 ,          0.0 ,   0.0 ,       0.0 ],
        [ 38.0 ,     81.01325 ,  30.0 ,          0.0 ,   0.0 ,       0.0 ],
        [ 39.0 ,     81.01325 ,  30.0 ,          0.0 ,   0.0 ,       0.0 ],
        [ 40.0 ,     81.01325 ,  30.0 ,          0.0 ,   0.0 ,       0.0 ],
    ], dtype=np.float64)


    ## Pipeline without compressor data
    Gas["Pipeline"] = array([
        #     0     ,     1     ,          2          ,     3     ,       4      ,            5           
        # BeginNode ,  TermNode ,  Length             ,  Diameter ,  Km          ,  Kq                    
        # -         ,  -        ,  m                  ,  m        ,  (MSm3/h)/Pa ,  (MSm3/h)^2/bar^2      
        [       1.0 ,       6.0 ,             13071.0 ,       1.0 ,       0.0152 ,  0.00020984493122057585 ],
        [      33.0 ,      19.0 ,             38447.0 ,       0.8 ,       0.0188 ,  4.7436733945623526e-05 ],
        [      38.0 ,      16.0 ,             21558.0 ,       1.0 ,       0.0129 ,   6.899888573908876e-05 ],
        [      16.0 ,      17.0 ,              6998.0 ,       1.0 ,       0.0118 ,   7.589877431299764e-05 ],
        [      17.0 ,      13.0 ,             58219.0 ,       0.8 ,       0.0271 ,  0.00011803777381157391 ],
        [      28.0 ,      29.0 ,             43345.0 ,       0.8 ,       0.0129 ,   6.899888573908876e-05 ],
        [      29.0 ,      12.0 ,             16579.0 ,       0.6 ,       0.0188 ,  4.7436733945623526e-05 ],
        [      12.0 ,      21.0 ,             10023.0 ,       0.6 ,       0.0188 ,  4.7436733945623526e-05 ],
        [      29.0 ,       7.0 ,             35219.0 ,       0.6 ,       0.0271 ,  0.00011803777381157391 ],
        [       7.0 ,      23.0 ,             20322.0 ,       0.6 ,       0.0188 ,  4.7436733945623526e-05 ],
        [      21.0 ,       9.0 ,             32868.0 ,       0.8 ,       0.0188 ,  4.7436733945623526e-05 ],
        [      28.0 ,      40.0 ,             47488.0 ,       0.8 ,       0.0188 ,  4.7436733945623526e-05 ],
        [       9.0 ,      10.0 ,              3803.0 ,       0.6 ,       0.0188 ,  4.7436733945623526e-05 ],
        [       9.0 ,      25.0 ,             39036.0 ,       1.8 ,       0.0188 ,  4.7436733945623526e-05 ],
        [      10.0 ,      27.0 ,             38660.0 ,       1.8 ,       0.0188 ,  4.7436733945623526e-05 ],
        [      25.0 ,       4.0 ,             18018.0 ,       1.8 ,       0.0188 ,  4.7436733945623526e-05 ],
        [      27.0 ,      24.0 ,              3068.0 ,       1.8 ,       0.0188 ,  4.7436733945623526e-05 ],
        [      24.0 ,      15.0 ,             12016.0 ,       1.8 ,       0.0188 ,  4.7436733945623526e-05 ],
        [      10.0 ,       8.0 ,             14043.0 ,       0.4 ,       0.0188 ,  4.7436733945623526e-05 ],
        [       8.0 ,      20.0 ,             20635.0 ,       0.6 ,       0.0152 ,  0.00020984493122057585 ],
        [      20.0 ,       7.0 ,             10586.0 ,       0.6 ,       0.0188 ,  4.7436733945623526e-05 ],
        [      20.0 ,      11.0 ,             10452.0 ,       0.6 ,       0.0129 ,   6.899888573908876e-05 ],
        [       6.0 ,      26.0 ,             12397.0 ,       0.8 ,       0.0118 ,   7.589877431299764e-05 ],
        [      11.0 ,      23.0 ,             19303.0 ,       0.6 ,       0.0271 ,  0.00011803777381157391 ],
        [      28.0 ,      23.0 ,             66037.0 ,       0.6 ,       0.0129 ,   6.899888573908876e-05 ],
        [      28.0 ,      18.0 ,             18969.0 ,       1.0 ,       0.0188 ,  4.7436733945623526e-05 ],
        [      18.0 ,      32.0 ,             36061.0 ,       0.8 ,       0.0188 ,  4.7436733945623526e-05 ],
        [      32.0 ,      31.0 ,             22224.0 ,       0.8 ,       0.0271 ,  0.00011803777381157391 ],
        [      32.0 ,       5.0 ,             31180.0 ,       0.8 ,       0.0188 ,  4.7436733945623526e-05 ],
        [       5.0 ,      18.0 ,             12767.0 ,       1.0 ,       0.0188 ,  4.7436733945623526e-05 ],
        [      32.0 ,      39.0 ,             32921.0 ,       0.8 ,       0.0188 ,  4.7436733945623526e-05 ],
        [      36.0 ,      22.0 ,             49866.0 ,       0.8 ,       0.0188 ,  4.7436733945623526e-05 ],
        [      22.0 ,      35.0 ,              3479.0 ,       0.8 ,       0.0188 ,  4.7436733945623526e-05 ],
        [      36.0 ,      37.0 ,              3418.0 ,       1.0 ,       0.0188 ,  4.7436733945623526e-05 ],
        [      30.0 ,      37.0 ,  32448.999999999996 ,       1.0 ,       0.0188 ,  4.7436733945623526e-05 ],
        [      30.0 ,      22.0 ,             26427.0 ,       0.8 ,       0.0188 ,  4.7436733945623526e-05 ],
        [      13.0 ,      14.0 ,             18137.0 ,       1.0 ,       0.0188 ,  4.7436733945623526e-05 ],
        [      13.0 ,      34.0 ,             32528.5 ,       0.8 ,       0.0188 ,  4.7436733945623526e-05 ],
        [      13.0 ,      35.0 ,             32766.0 ,       0.8 ,       0.0188 ,  4.7436733945623526e-05 ],
    ], dtype=np.float64)

    ## Pipeline with compressor data
    # Type: 1=electric compressor, 2=gas compressor.
    Gas["Comp"] = array([
        #     0     ,      1      ,   2   ,     3     ,    4   ,   5  ,   6  ,   7   ,   8   ,   9   ,    10  ,   11  ,   12  ,      13     ,    14 
        # InputNode ,  OutputNode ,  Type ,  CompFact ,  alpha ,  k1  ,  k2  ,  Rmin ,  Rmax ,  Hmin ,  Hmax  ,  Bus  ,  loss ,  efficiency ,  ratio
        # -         ,  -          ,  -    ,  -        ,  -     ,  -   ,  -   ,  -    ,  -    ,  MW   ,  MW    ,  -    ,  p.u. ,  p.u.       ,  -    
        [      38.0 ,        28.0 ,   1.0 ,       1.1 ,   0.24 ,  1.2 ,  1.0 ,   1.0 ,   1.2 ,   0.0 ,  800.0 ,   8.0 ,  0.04 ,        0.55 ,    0.0 ],
        [      14.0 ,        33.0 ,   2.0 ,       1.1 ,   0.24 ,  1.2 ,  1.0 ,   1.0 ,   1.2 ,   0.0 ,   50.0 ,   8.0 ,  0.04 ,        0.55 ,    0.0 ],
        [      22.0 ,        34.0 ,   2.0 ,       1.1 ,   0.24 ,  1.2 ,  1.0 ,   1.0 ,   1.2 ,   0.0 ,   50.0 ,  12.0 ,  0.04 ,        0.55 ,    0.0 ],
        [       3.0 ,        36.0 ,   1.0 ,       1.1 ,   0.24 ,  1.2 ,  1.0 ,   1.0 ,   1.2 ,   0.0 ,  800.0 ,   8.0 ,  0.04 ,        0.55 ,    0.0 ],
        [       2.0 ,        39.0 ,   2.0 ,       1.1 ,   0.24 ,  1.2 ,  1.0 ,   1.0 ,   1.2 ,   0.0 ,   50.0 ,   8.0 ,  0.04 ,        0.55 ,    0.0 ],
        [       6.0 ,        40.0 ,   2.0 ,       1.1 ,   0.24 ,  1.2 ,  1.0 ,   1.0 ,   1.2 ,   0.0 ,   50.0 ,  12.0 ,  0.04 ,        0.55 ,    0.0 ],
    ], dtype=np.float64)

    ## P2G data
    # Compact schema: PowerBus, GasNode, efficiency, P, mBase, Pmax, Pmin.
    Gas["P2G"] = array([
        #    0     ,     1    ,      2      ,   3  ,    4   ,    5   ,   6  
        # PowerBus ,  GasNode ,  efficiency ,  P   ,  mBase ,  Pmax  ,  Pmin
        # -        ,  -       ,  p.u.       ,  MW  ,  MVA   ,  MW    ,  MW  
        [     12.0 ,     24.0 ,        0.45 ,  0.0 ,  100.0 ,  150.0 ,  70.0 ],
    ], dtype=np.float64)

    return Gas


# -----------------------------------------------------------------------------
# Integrated energy system construction
# -----------------------------------------------------------------------------
from pathlib import Path
import sys
import warnings

import pandapower as pp
from pandapower.converter.pypower import from_ppc
from pandapower.toolbox import create_continuous_bus_index

THIS_DIR = Path(__file__).resolve().parent
WORKSPACE_ROOT = THIS_DIR.parent
RL_OPF_ROOT = WORKSPACE_ROOT / "RL_OPF"

if str(RL_OPF_ROOT) not in sys.path:
    sys.path.insert(0, str(RL_OPF_ROOT))

from utilities.getMyDataG import getMyDataG  # noqa: E402


def IEGS_P57_G40():
    Gas = GAS_40N()

    from pypower.api import case57 as pypower_case57
    from pypower.idx_bus import BASE_KV

    ppc = pypower_case57()
    ppc["bus"][:, BASE_KV] = 115.0
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        power_net = from_ppc(ppc, f_hz=60)
    create_continuous_bus_index(power_net, start=0)

    power_net.load.reset_index(drop=True, inplace=True)
    power_net.gen.reset_index(drop=True, inplace=True)
    power_net.ext_grid.reset_index(drop=True, inplace=True)

    bus_ids = set(np.asarray(power_net.bus.index, dtype=int))
    load_bus_ids = set(np.asarray(power_net.load.bus, dtype=int))
    for bus in sorted(bus_ids - load_bus_ids):
        pp.create_load(power_net, bus=int(bus), p_mw=0.0, q_mvar=0.0, name="coupling_anchor")
    power_net.load.sort_values("bus", inplace=True)
    power_net.load.reset_index(drop=True, inplace=True)

    power_net.ext_grid["name"] = "GP"
    power_net.gen["name"] = "GP"
    power_net.gen.loc[[3, 5], "name"] = "GT"

    Data = getMyDataG(Gas, power_net, DynamicUsed=1)
    Data.setdefault("verbose", 0)
    Data.setdefault("nr_tol", 1e-4)
    Data.setdefault("nr_xtol", 1e-10)
    Data["iegs_case_name"] = CASE_NAME
    Data["power_case_name"] = POWER_CASE_NAME
    Data["gas_case_id"] = GAS_CASE_ID
    return Gas, power_net, Data


if __name__ == "__main__":
    gas, net, data = IEGS_P57_G40()
    print(CASE_NAME, gas["GenGas"].shape, gas["P2G"].shape, len(net.bus), len(net.gen), data["GN"])
