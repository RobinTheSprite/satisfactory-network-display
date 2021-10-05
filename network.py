import networkx as nx
import matplotlib
matplotlib.use('WebAgg')
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from items import *

adjlist = {
    copper_ore: [copper_ingot],
    copper_ingot: [copper_powder, copper_sheet, copper_wire, alclad_aluminum_sheet],
    copper_wire: [beacon, cable, stator],
    copper_sheet: [ai_limiter, circuit_board, heat_sink],
    copper_powder: [nuclear_pasta],
    limestone: [concrete],
    iron_ore: [iron_ingot, steel_ingot],
    iron_ingot: [iron_plate, iron_rod],
    iron_plate: [beacon, nitric_acid, reinforced_iron_plate],
    iron_rod: [beacon, modular_frame, rotor, screw],
    screw: [computer, heavy_modular_frame, reinforced_iron_plate, rotor],
    reinforced_iron_plate: [crystal_oscillator, modular_frame, smart_plating],
    coal: [aluminum_scrap, steel_ingot, compacted_coal],
    caterium_ore: [caterium_ingot, quickwire],
    quickwire: [ai_limiter, high_speed_connector],
    sulfur: [sulfuric_acid, compacted_coal],
    sulfuric_acid: [battery, encased_uranium_cell, non_fissile_uranium],
    compacted_coal: [turbofuel],
    bauxite: [alumina_solution, silica],
    silica: [aluminum_ingot, non_fissile_uranium],
    crude_oil: [fuel, plastic, rubber, polymer_resin, heavy_oil_residue],
    fuel: [turbofuel],
    polymer_resin: [plastic, rubber],
    heavy_oil_residue: [fuel, petroleum_coke, turbofuel],
    nitrogen_gas: [cooling_system, fused_modular_frame, nitric_acid],
    raw_quartz: [quartz_crystal, silica],
    quartz_crystal: [crystal_oscillator],
    crystal_oscillator: [radio_control_unit],
    water: [alumina_solution, cooling_system, liquid_biofuel, nitric_acid, plastic, plutonium_waste, rubber, sulfuric_acid, uranium_waste],
    leaves: [biomass],
    wood: [biomass],
    biomass: [fabric, solid_biofuel],
    solid_biofuel: [liquid_biofuel],
    alumina_solution: [aluminum_scrap, battery],
    aluminum_scrap: [aluminum_ingot],
    aluminum_ingot: [alclad_aluminum_sheet, aluminum_casing, empty_fluid_tank],
    aluminum_casing: [battery, fused_modular_frame, radio_control_unit],
    alclad_aluminum_sheet: [heat_sink],
    nitric_acid: [non_fissile_uranium],
    uranium: [encased_uranium_cell, sulfuric_acid],
    uranium_fuel_rod: [uranium_waste],
    uranium_waste: [non_fissile_uranium, plutonium_pellet],
    non_fissile_uranium: [plutonium_pellet],
    plutonium_fuel_rod: [plutonium_waste],
    plutonium_pellet: [encased_plutonium_cell],
    cable: [automated_wiring, beacon, computer, crystal_oscillator, high_speed_connector],
    concrete: [encased_industrial_beam, encased_plutonium_cell, encased_uranium_cell],
    modular_frame: [heavy_modular_frame, versatile_framework],
    rotor: [motor, smart_plating],
    smart_plating: [modular_engine],
    steel_ingot: [steel_beam, steel_pipe],
    steel_beam: [encased_industrial_beam, plutonium_fuel_rod, versatile_framework],
    steel_pipe: [heavy_modular_frame, stator],
    versatile_framework: [magnetic_field_generator],
    automated_wiring: [adaptive_control_unit],
    encased_industrial_beam: [heavy_modular_frame, uranium_fuel_rod],
    heavy_modular_frame: [adaptive_control_unit, fused_modular_frame],
    motor: [modular_engine, turbo_motor],
    stator: [automated_wiring, electromagnetic_control_rod, motor],
    adaptive_control_unit: [assembly_director_system],
    circuit_board: [adaptive_control_unit, computer, high_speed_connector],
    computer: [adaptive_control_unit, radio_control_unit, supercomputer],
    modular_engine: [thermal_propulsion_rocket],
    plastic: [circuit_board, computer, empty_canister, supercomputer],
    rubber: [cooling_system, modular_engine, turbo_motor],
    battery: [magnetic_field_generator],
    radio_control_unit: [pressure_conversion_cube, turbo_motor],
    cooling_system: [thermal_propulsion_rocket, turbo_motor],
    electromagnetic_control_rod: [magnetic_field_generator, plutonium_fuel_rod, uranium_fuel_rod],
    encased_plutonium_cell: [plutonium_fuel_rod],
    encased_uranium_cell: [uranium_fuel_rod],
    fused_modular_frame: [pressure_conversion_cube, thermal_propulsion_rocket],
    heat_sink: [cooling_system, plutonium_fuel_rod],
    pressure_conversion_cube: [nuclear_pasta],
    turbo_motor: [thermal_propulsion_rocket],
    ai_limiter: [electromagnetic_control_rod, supercomputer],
    high_speed_connector: [supercomputer],
    supercomputer: [assembly_director_system],
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

pos = nx.drawing.nx_pydot.graphviz_layout(G, prog='dot')

figure_scale = 50

fig, subaxis = plt.subplots(figsize=(figure_scale, figure_scale))
nx.draw(G, pos=pos, with_labels=True, font_weight='bold', ax=subaxis)
plt.show()
