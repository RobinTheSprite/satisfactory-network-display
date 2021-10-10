import networkx as nx
import matplotlib
matplotlib.use('WebAgg')
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from items import *

adjlist = {
    bauxite: [alumina_solution, silica],
    caterium_ore: [caterium_ingot],
    coal: [aluminum_scrap, steel_ingot, compacted_coal],
    copper_ore: [copper_ingot],
    crude_oil: [fuel, plastic, rubber, polymer_resin, heavy_oil_residue],
    iron_ore: [iron_ingot, steel_ingot],
    leaves: [biomass],
    limestone: [concrete],
    nitrogen_gas: [cooling_system, fused_modular_frame, nitric_acid],
    raw_quartz: [quartz_crystal, silica],
    sulfur: [sulfuric_acid, compacted_coal],
    uranium: [encased_uranium_cell, sulfuric_acid],
    water: [alumina_solution, cooling_system, liquid_biofuel, nitric_acid, plastic, plutonium_waste, rubber, sulfuric_acid, uranium_waste],
    wood: [biomass],

    biomass: [fabric, solid_biofuel],
    cable: [automated_wiring, beacon, computer, crystal_oscillator, high_speed_connector],
    concrete: [encased_industrial_beam, encased_plutonium_cell, encased_uranium_cell],
    copper_ingot: [copper_powder, copper_sheet, copper_wire, alclad_aluminum_sheet],
    copper_wire: [beacon, cable, stator],
    iron_ingot: [iron_plate, iron_rod],
    iron_plate: [beacon, nitric_acid, reinforced_iron_plate],
    iron_rod: [beacon, modular_frame, rotor, screw],
    reinforced_iron_plate: [crystal_oscillator, modular_frame, smart_plating],
    screw: [computer, heavy_modular_frame, reinforced_iron_plate, rotor],

    copper_sheet: [ai_limiter, circuit_board, heat_sink],
    modular_frame: [heavy_modular_frame, versatile_framework],
    rotor: [motor, smart_plating],
    smart_plating: [modular_engine],
    solid_biofuel: [liquid_biofuel],

    steel_beam: [encased_industrial_beam, plutonium_fuel_rod, versatile_framework],
    steel_ingot: [steel_beam, steel_pipe],
    steel_pipe: [heavy_modular_frame, stator],
    versatile_framework: [magnetic_field_generator],

    automated_wiring: [adaptive_control_unit],
    encased_industrial_beam: [heavy_modular_frame, uranium_fuel_rod],
    heavy_modular_frame: [adaptive_control_unit, fused_modular_frame],
    motor: [modular_engine, turbo_motor],
    stator: [automated_wiring, electromagnetic_control_rod, motor],

    adaptive_control_unit: [assembly_director_system],
    circuit_board: [adaptive_control_unit, computer, high_speed_connector],
    compacted_coal: [turbofuel],
    computer: [adaptive_control_unit, radio_control_unit, supercomputer],
    fuel: [turbofuel],
    heavy_oil_residue: [fuel, petroleum_coke, turbofuel],
    modular_engine: [thermal_propulsion_rocket],
    plastic: [circuit_board, computer, empty_canister, supercomputer],
    polymer_resin: [plastic, rubber],
    rubber: [cooling_system, modular_engine, turbo_motor],

    alumina_solution: [aluminum_scrap, battery],
    aluminum_casing: [battery, fused_modular_frame, radio_control_unit],
    alclad_aluminum_sheet: [heat_sink],
    aluminum_scrap: [aluminum_ingot],
    aluminum_ingot: [alclad_aluminum_sheet, aluminum_casing, empty_fluid_tank],
    battery: [magnetic_field_generator],
    crystal_oscillator: [radio_control_unit],
    quartz_crystal: [crystal_oscillator],
    radio_control_unit: [pressure_conversion_cube, turbo_motor],
    silica: [aluminum_ingot, non_fissile_uranium],
    sulfuric_acid: [battery, encased_uranium_cell, non_fissile_uranium],

    ai_limiter: [electromagnetic_control_rod, supercomputer],
    caterium_ingot: [quickwire],
    cooling_system: [thermal_propulsion_rocket, turbo_motor],
    copper_powder: [nuclear_pasta],
    electromagnetic_control_rod: [magnetic_field_generator, plutonium_fuel_rod, uranium_fuel_rod],
    encased_plutonium_cell: [plutonium_fuel_rod],
    encased_uranium_cell: [uranium_fuel_rod],
    fused_modular_frame: [pressure_conversion_cube, thermal_propulsion_rocket],
    heat_sink: [cooling_system, plutonium_fuel_rod],
    high_speed_connector: [supercomputer],
    nitric_acid: [non_fissile_uranium],
    non_fissile_uranium: [plutonium_pellet],
    plutonium_fuel_rod: [plutonium_waste],
    plutonium_pellet: [encased_plutonium_cell],
    pressure_conversion_cube: [nuclear_pasta],
    quickwire: [ai_limiter, high_speed_connector],
    supercomputer: [assembly_director_system],
    turbo_motor: [thermal_propulsion_rocket],
    uranium_fuel_rod: [uranium_waste],
    uranium_waste: [non_fissile_uranium, plutonium_pellet],
}

shells_by_tier = [
    [
        bauxite,
        caterium_ore,
        coal,
        copper_ore,
        crude_oil,
        iron_ore,
        leaves,
        limestone,
        mycelia,
        nitrogen_gas,
        raw_quartz,
        sam_ore,
        sulfur,
        uranium,
        water,
        wood,
    ],

    [
        biomass,
        cable,
        concrete,
        copper_ingot,
        copper_wire,
        fabric,
        iron_ingot,
        iron_plate,
        iron_rod,
        reinforced_iron_plate,
        screw,
        beacon,
    ],

    [
        copper_sheet,
        modular_frame,
        rotor,
        smart_plating,
        solid_biofuel,
    ],

    [
        steel_beam,
        steel_ingot,
        steel_pipe,
        versatile_framework,
    ],

    [
        automated_wiring,
        encased_industrial_beam,
        heavy_modular_frame,
        motor,
        stator,
    ],


    [
        adaptive_control_unit,
        circuit_board,
        compacted_coal,
        computer,
        empty_canister,
        fuel,
        heavy_oil_residue,
        liquid_biofuel,
        modular_engine,
        petroleum_coke,
        plastic,
        polymer_resin,
        rubber,
        turbofuel,
    ],


    [
        alumina_solution,
        aluminum_casing,
        alclad_aluminum_sheet,
        aluminum_scrap,
        aluminum_ingot,
        assembly_director_system,
        battery,
        crystal_oscillator,
        quartz_crystal,
        radio_control_unit,
        silica,
        sulfuric_acid,
    ],

    [
        ai_limiter,
        caterium_ingot,
        cooling_system,
        copper_powder,
        electromagnetic_control_rod,
        empty_fluid_tank,
        encased_plutonium_cell,
        encased_uranium_cell,
        fused_modular_frame,
        heat_sink,
        high_speed_connector,
        magnetic_field_generator,
        nitric_acid,
        non_fissile_uranium,
        nuclear_pasta,
        plutonium_fuel_rod,
        plutonium_pellet,
        plutonium_waste,
        pressure_conversion_cube,
        quickwire,
        supercomputer,
        thermal_propulsion_rocket,
        turbo_motor,
        uranium_fuel_rod,
        uranium_waste,
    ]
]
shells_by_tier.reverse()

edgelist = []
for ingredient, products in adjlist.items():
    for product in products:
        edgelist.append((ingredient, product))

G = nx.DiGraph(edgelist)

V = len(G.nodes)
E = len(G.edges)
print(f"Network has {V} vertices and {E} edges")

# pos = nx.drawing.nx_pydot.graphviz_layout(G, prog='dot')
pos = nx.shell_layout(G, nlist=shells_by_tier)

figure_scale = 50

fig, subaxis = plt.subplots(figsize=(figure_scale, figure_scale))
nx.draw(G, pos=pos, with_labels=True, font_weight='bold', ax=subaxis)
plt.show()
