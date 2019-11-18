import pandas as pd

sam_defaults = dict()


#sam_defaults['crane_specs']

crane_specs_columns = ['Equipment name'          ,    'Crane name'          ,    'Boom system',  'Crane capacity tonne' , 'Speed of travel km per hr' , 'Hoist speed m per min' ,'Crew type ID', 'Equipment ID' , 'Setup time hr' , 'Max wind speed m per s' , 'Hub height m' , 'Max capacity tonne' , 'Radius m' , 'Hook Height m' , 'Mobilization cost USD']


crane_specs_data = \
    [  #'Equipment name'       ,    'Crane name'      ,     'Boom system'               ,       'Crane capacity tonne'  ,   'Speed of travel km per hr' ,   'Hoist speed m per min' ,   'Crew type ID'  ,   'Equipment ID'  ,   'Setup time hr' ,   'Max wind speed m per s'    ,   'Hub height m'  ,   'Max capacity tonne'    ,   'Radius m'  ,   'Hook Height m' ,   'Mobilization cost USD'
        ['Offload crane'       ,    'LB 75'           ,     'Hydraulic'                 ,       '75'                    ,   '40'                        ,   '60'                    ,   'C0'            ,   'OL1'           ,   '0'             ,   '10'                        ,   '12.5'          ,   '38'                    ,   '5.4'       ,   '12.5'          ,   '99'],
        ['Offload crane'       ,    'LB 258'          ,     'Hydraulic'                 ,       '200'                   ,   '40'                        ,   '60'                    ,   'C0'            ,   'OL2'           ,   '0'             ,   '10'                        ,   '48.0'          ,   '63'                    ,   '11.0'      ,   '48.0'          ,   '99'],
        ['Crawler crane'       ,    'M999'            ,     '22EL'                      ,       '275'                   ,   '2'                         ,   '20'                    ,   'C1'            ,   'B1'            ,   '0'             ,   '9'                         ,   '57.0'          ,   '67'                    ,   '14.0'      ,   '57.0'          ,   '99'],
        ['Crawler crane'       ,    'LR1500'          ,     'SL3F'                      ,       '500'                   ,   '2'                         ,   '20'                    ,   'C1'            ,   'E1'            ,   '0'             ,   '9'                         ,   '80.0'          ,   '102'                   ,   '16.0'      ,   '94.0'          ,   '99'],
        ['Crawler crane'       ,    'LR1500'          ,     'SL3F'                      ,       '500'                   ,   '2'                         ,   '20'                    ,   'C1'            ,   'E1'            ,   '0'             ,   '9'                         ,   '85.0'          ,   '95'                    ,   '16.0'      ,   '100.0'         ,   '99'],
        ['Crawler crane'       ,    'LR1500'          ,     'SL3F'                      ,       '500'                   ,   '2'                         ,   '20'                    ,   'C1'            ,   'E1'            ,   '0'             ,   '9'                         ,   '90.0'          ,   '87'                    ,   '16.0'      ,   '106.0'         ,   '99'],
        ['Crawler crane'       ,    'LR1500'          ,     'SL3F'                      ,       '500'                   ,   '2'                         ,   '20'                    ,   'C1'            ,   'E1'            ,   '0'             ,   '9'                         ,   '100.0'         ,   '77'                    ,   '18.0'      ,   '112.0'         ,   '99'],
        ['Crawler crane'       ,    'LR1500'          ,     'SL4DFB + Derrick'          ,       '500'                   ,   '2'                         ,   '20'                    ,   'C1'            ,   'E1'            ,   '2'             ,   '9'                         ,   '80.0'          ,   '112'                   ,   '16.0'      ,   '94.0'          ,   '99'],
        ['Crawler crane'       ,    'LR1500'          ,     'SL4DFB + Derrick'          ,       '500'                   ,   '2'                         ,   '20'                    ,   'C1'            ,   'E1'            ,   '2'             ,   '9'                         ,   '90.0'          ,   '105'                   ,   '16.0'      ,   '100.0'         ,   '99'],
        ['Crawler crane'       ,    'LR1500'          ,     'SL4DFB + Derrick'          ,       '500'                   ,   '2'                         ,   '20'                    ,   'C1'            ,   'E1'            ,   '2'             ,   '9'                         ,   '100.0'         ,   '90'                    ,   '16.0'      ,   '112.0'         ,   '99'],
        ['Crawler crane'       ,    'LR1500'          ,     'SL4DFB + Derrick'          ,       '500'                   ,   '2'                         ,   '20'                    ,   'C1'            ,   'E1'            ,   '2'             ,   '9'                         ,   '120.0'         ,   '74'                    ,   '18.0'      ,   '130.0'         ,   '99'],
        ['Crawler crane'       ,    'LR1500'          ,     'SL4DFB + Derrick'          ,       '500'                   ,   '2'                         ,   '20'                    ,   'C1'            ,   'E1'            ,   '2'             ,   '9'                         ,   '130.0'         ,   '60'                    ,   '20.0'      ,   '142.0'         ,   '99'],
        ['Crawler crane'       ,    'LR1600/2'        ,     'SL8F3'                     ,       '600'                   ,   '2'                         ,   '20'                    ,   'C2'            ,   'E2'            ,   '0'             ,   '9'                         ,   '80.0'          ,   '137'                   ,   '18.0'      ,   '93.0'          ,   '99'],
        ['Crawler crane'       ,    'LR1600/2'        ,     'SL8F3'                     ,       '600'                   ,   '2'                         ,   '20'                    ,   'C2'            ,   'E2'            ,   '0'             ,   '9'                         ,   '100.0'         ,   '118'                   ,   '18.0'      ,   '114.0'         ,   '99'],
        ['Crawler crane'       ,    'LR1600/2'        ,     'SL3F'                      ,       '600'                   ,   '2'                         ,   '20'                    ,   'C2'            ,   'E2'            ,   '0'             ,   '9'                         ,   '105.0'         ,   '93'                    ,   '18.0'      ,   '117.0'         ,   '99'],
        ['Crawler crane'       ,    'LR1600/2'        ,     'HSL4DF + Derrick boom'     ,       '600'                   ,   '2'                         ,   '20'                    ,   'C2'            ,   'E2'            ,   '2'             ,   '9'                         ,   '120.0'         ,   '87'                    ,   '20.0'      ,   '135.0'         ,   '99'],
        ['Crawler crane'       ,    'LR1600/2'        ,     'SL13DFB + Derrick'         ,       '600'                   ,   '2'                         ,   '20'                    ,   'C2'            ,   'E2'            ,   '2'             ,   '9'                         ,   '135.0'         ,   '96'                    ,   '20.0'      ,   '147.0'         ,   '99'],
        ['Crawler crane'       ,    'LR1600/2'        ,     'SL13DFB + Derrick'         ,       '600'                   ,   '2'                         ,   '20'                    ,   'C2'            ,   'E2'            ,   '2'             ,   '9'                         ,   '140.0'         ,   '87'                    ,   '24.0'      ,   '152.0'         ,   '99'],
        ['Crawler crane'       ,    'LR1600/2'        ,     'SL13DFB2 + Derrick'        ,       '600'                   ,   '2'                         ,   '20'                    ,   'C2'            ,   'E2'            ,   '2'             ,   '9'                         ,   '150.0'         ,   '71'                    ,   '24.0'      ,   '164.0'         ,   '99'],
        ['Crawler crane'       ,    'LR1750/2'        ,     'HSL8HS'                    ,       '750'                   ,   '2'                         ,   '20'                    ,   'C3'            ,   'E3'            ,   '0'             ,   '9'                         ,   '80.0'          ,   '111'                   ,   '18.0'      ,   '101.0'         ,   '99'],
        ['Crawler crane'       ,    'LR1500/2'        ,     'HSL8HS'                    ,       '750'                   ,   '2'                         ,   '20'                    ,   'C3'            ,   'E3'            ,   '0'             ,   '9'                         ,   '95.0'          ,   '110'                   ,   '18.0'      ,   '109.0'         ,   '99'],
        ['Crawler crane'       ,    'LR1750/2'        ,     'HSL7DHS'                   ,       '750'                   ,   '2'                         ,   '20'                    ,   'C3'            ,   'E3'            ,   '2'             ,   '9'                         ,   '120.0'         ,   '108'                   ,   '18.0'      ,   '136.0'         ,   '99'],
        ['Crawler crane'       ,    'LR1750/2'        ,     'HSL7DHS'                   ,       '750'                   ,   '2'                         ,   '20'                    ,   'C3'            ,   'E3'            ,   '2'             ,   '9'                         ,   '130.0'         ,   '98'                    ,   '18.0'      ,   '147.0'         ,   '99'],
        ['Crawler crane'       ,    'LR1500/2'        ,     'HSL7DHS'                   ,       '750'                   ,   '2'                         ,   '20'                    ,   'C3'            ,   'E3'            ,   '2'             ,   '9'                         ,   '140.0'         ,   '89'                    ,   '22.0'      ,   '152.0'         ,   '99'],
        ['Crawler crane'       ,    'LR1750/2'        ,     'SX3D4F2B Derrick (walk)'   ,       '750'                   ,   '2'                         ,   '20'                    ,   'C3'            ,   'E3'            ,   '0'             ,   '9'                         ,   '140.0'         ,   '141'                   ,   '28.0'      ,   '154.0'         ,   '99'],
        ['Crawler crane'       ,    'LR1750/2'        ,     'SX3D4F2B Derrick (walk)'   ,       '750'                   ,   '2'                         ,   '20'                    ,   'C3'            ,   'E3'            ,   '0'             ,   '9'                         ,   '150.0'         ,   '118'                   ,   '28.0'      ,   '165.0'         ,   '99'],
        ['Crawler crane'       ,    'LR11000'         ,     'SL3F'                      ,       '1000'                  ,   '1'                         ,   '25'                    ,   'C4'            ,   'E4'            ,   '3'             ,   '9'                         ,   '100.0'         ,   '179'                   ,   '18.0'      ,   '114.0'         ,   '99'],
        ['Crawler crane'       ,    'LR11000'         ,     'SL3F'                      ,       '1000'                  ,   '1'                         ,   '25'                    ,   'C4'            ,   'E4'            ,   '3'             ,   '9'                         ,   '110.0'         ,   '152'                   ,   '18.0'      ,   '120.0'         ,   '99'],
        ['Crawler crane'       ,    'LR11000'         ,     'SL2DFB'                    ,       '1000'                  ,   '1'                         ,   '25'                    ,   'C4'            ,   'E4'            ,   '3'             ,   '9'                         ,   '120.0'         ,   '179'                   ,   '20.0'      ,   '132.0'         ,   '99'],
        ['Crawler crane'       ,    'LR11000'         ,     'SL2DFB'                    ,       '1000'                  ,   '1'                         ,   '25'                    ,   'C4'            ,   'E4'            ,   '3'             ,   '9'                         ,   '140.0'         ,   '133'                   ,   '18.0'      ,   '136.0'         ,   '99'],
        ['Crawler crane'       ,    'LR11000'         ,     'SL2DFB'                    ,       '1000'                  ,   '1'                         ,   '25'                    ,   'C4'            ,   'E4'            ,   '3'             ,   '9'                         ,   '150.0'         ,   '154'                   ,   '18.0'      ,   '147.0'         ,   '99'],
        ['Crawler crane'       ,    'LR11000'         ,     'SL2DFB'                    ,       '1000'                  ,   '1'                         ,   '25'                    ,   'C4'            ,   'E4'            ,   '3'             ,   '9'                         ,   '155.0'         ,   '140'                   ,   '22.0'      ,   '152.0'         ,   '99'],
        ['Crawler crane'       ,    'LR11000'         ,     'SL2DFB'                    ,       '1000'                  ,   '1'                         ,   '25'                    ,   'C4'            ,   'E4'            ,   '3'             ,   '9'                         ,   '160.0'         ,   '120'                   ,   '26.0'      ,   '174.0'         ,   '99'],
        ['Crawler crane'       ,    'LR11000'         ,     'SL2DFB'                    ,       '1000'                  ,   '1'                         ,   '25'                    ,   'C4'            ,   'E4'            ,   '3'             ,   '9'                         ,   '180.0'         ,   '73'                    ,   '22.0'      ,   '192.0'         ,   '99'],
        ['Crawler crane'       ,    'LR11000'         ,     'SL2DFB'                    ,       '1000'                  ,   '1'                         ,   '25'                    ,   'C4'            ,   'E4'            ,   '3'             ,   '9'                         ,   '185.0'         ,   '54'                    ,   '34.0'      ,   '198.0'         ,   '99'],
        ['Crawler crane'       ,    'LR11000'         ,     'PDW3B Derrick'             ,       '1000'                  ,   '1'                         ,   '25'                    ,   'C4'            ,   'E4'            ,   '6'             ,   '9'                         ,   '130.0'         ,   '227'                   ,   '28.0'      ,   '147.0'         ,   '99'],
        ['Crawler crane'       ,    'LR11000'         ,     'PDW3B2 Derrick'            ,       '1000'                  ,   '1'                         ,   '25'                    ,   'C4'            ,   'E4'            ,   '6'             ,   '9'                         ,   '165.0'         ,   '142'                   ,   '26.0'      ,   '174.0'         ,   '99']
    ]

crane_specs = pd.DataFrame(crane_specs_data, columns=crane_specs_columns)
sam_defaults['crane_specs'] = crane_specs



equip_columns =  ['Equipment ID'    ,   'Operation'  ,     'Equipment name'   ,   'Crane capacity tonne'  ,      'Number of equipment']
equip_data = [ # Equipment ID    ,   Operation       Equipment name      Crane capacity tonne        Number of equipment
            ['E1'           ,   'Base'      ,   'Crawler crane'     ,'500'                  ,   '1'],
            ['E1'           ,   'Base'      ,   'Truck crane'       ,'50'                   ,   '1'],
            ['E1'           ,   'Top'       ,   'Crawler crane'     ,'500'                  ,   '1'],
            ['E1'           ,   'Top'       ,   'Truck crane'       ,'50'                   ,   '2'],
            ['E2'           ,   'Top'       ,   'Crawler crane'     ,'600'                  ,   '1'],
            ['E2'           ,   'Top'       ,   'Truck crane'       ,'50'                   ,   '2'],
            ['E2'           ,   'Top'       ,   'RT'                ,'100'                  ,   '2'],
            ['E3'           ,   'Top'       ,   'Crawler crane'     ,'750'                  ,   '1'],
            ['E3'           ,   'Top'       ,   'RT'                ,'100'                  ,   '2'],
            ['E4'           ,   'Top'       ,   'Crawler crane'     ,'1000'                 ,   '1'],
            ['E4'           ,   'Top'       ,   'RT'                ,'100'                  ,   '2'],
            ['ST1'          ,   'Top'       ,   'Mobile crane'      ,'200'                  ,   '1'],
            ['ST1'          ,   'Top'       ,   'RT'                ,'100'                  ,   '2'],
            ['OL1'          ,   'Offload'   ,   'Offload crane'     ,'75'                   ,   '2'],
            ['OL2'          ,   'Offload'   ,   'Offload crane'     ,'200'                  ,   '2'],
            ['B1'           ,   'Base'      ,   'Crawler crane'     ,'275'                  ,   '1'],
            ['B1'           ,   'Base'      ,   'Truck crane'       ,'50'                   ,   '1'],
            ['E2'           ,   'Base'      ,   'Crawler crane'     ,'600'                  ,   '1'],
            ['E2'           ,   'Base'      ,   'Truck crane'       ,'50'                   ,   '2'],
            ['E2'           ,   'Base'      ,   'RT'                ,'100'                  ,   '2'],
            ['E3'           ,   'Base'      ,   'Crawler crane'     ,'750'                  ,   '1'],
            ['E3'           ,   'Base'      ,   'RT'                ,'100'                  ,   '2'],
            ['E4'           ,   'Base'      ,   'Crawler crane'     ,'1000'                 ,   '1'],
            ['E4'           ,   'Base'      ,   'RT'                ,'100'                  ,   '2'],
            ['ST1'          ,   'Base'      ,   'Mobile crane'      ,'200'                  ,   '1'],
            ['ST1'          ,   'Base'      ,   'RT'                ,'100'                  ,   '2'],
            ['OL2'          ,   'Base'      ,   'Offload crane'     ,'200'                  ,   '2']
          ]
equip = pd.DataFrame(equip_data, columns=equip_columns)
sam_defaults['equip'] = equip

equip_price_columns = ['Equipment name',  'Crane capacity tonne',  'Equipment price USD per hour',  'Cost USD per breakdown',  'Fuel consumption gal per day']
equip_price_data = [# Equipment name        Crane capacity tonne        Equipment price USD per hour        Cost USD per breakdown      Fuel consumption gal per day
                        ['Mobile crane'     ,   '75'                    ,   '99'                         ,   'NaN'                   ,   '99.0'],
                        ['Mobile crane'     ,   '200'                   ,   '99'                         ,   'NaN'                   ,   '99.0'],
                        ['Crawler crane'    ,   '275'                   ,   '99'                         ,   '99.0'                  ,   '99.0'],
                        ['Crawler crane'    ,   '250'                   ,   '99'                         ,   '99.0'                  ,   '99.0'],
                        ['Crawler crane'    ,   '400'                   ,   '99'                         ,   '99.0'                  ,   '99.0'],
                        ['Crawler crane'    ,   '500'                   ,   '99'                         ,   '99.0'                  ,   '99.0'],
                        ['Crawler crane'    ,   '600'                   ,   '99'                         ,   '99.0'                  ,   '99.0'],
                        ['Crawler crane'    ,   '750'                   ,   '99'                         ,   '99.0'                  ,   '99.0'],
                        ['Crawler crane'    ,   '1000'                  ,   '99'                         ,   '99.0'                  ,   '99.0'],
                        ['Crawler crane'    ,   '1350'                  ,   '99'                         ,   '99.0'                  ,   '99.0'],
                        ['Truck crane'      ,   '50'                    ,   '99'                         ,   'NaN'                   ,   'NaN'],
                        ['RT'               ,   '100'                   ,   '99'                         ,   'NaN'                   ,   'NaN'],
                        ['Offload crane'    ,   '75'                    ,   '99'                         ,   'NaN'                   ,   '99.0'],
                        ['Offload crane'    ,   '200'                   ,   '99'                         ,   'NaN'                   ,   '99.0']
                    ]


equip_price = pd.DataFrame(equip_data, columns=equip_columns)
sam_defaults['equip'] = equip_price

crew_price_columns = ['Labor type ID' , 'Hourly rate USD per hour' , 'Per diem USD per day']
crew_price_data = [ # Labor type ID'        ,   Hourly rate USD per hour    ,   Per diem USD per day
                    ['Crane operator'       ,   '99.0'                      ,   '99'],
                    ['Oiler'                ,   '99.0'                      ,   '99'],
                    ['Rigger'               ,   '99.0'                      ,   '99'],
                    ['Truck driver'         ,   '99.0'                      ,   '99'],
                    ['Iron worker'          ,   '99.0'                      ,   '99'],
                    ['Project manager'      ,   '99.0'                      ,   '99'],
                    ['Site manager'         ,   '99.0'                      ,   '99'],
                    ['Construction manager' ,   '99.0'                      ,   '99'],
                    ['Project engineer'     ,   '99.0'                      ,   '99'],
                    ['Safety or qc manager' ,   '99.0'                      ,   '99'],
                    ['Logistics manager'    ,   '99.0'                      ,   '99'],
                    ['Rigger foreman'       ,   '99.0'                      ,   '99'],
                    ['Rigger'               ,   '99.0'                      ,   '99'],
                    ['Operator'             ,   '99.0'                      ,   '99'],
                    ['Oiler'                ,   '99.0'                      ,   '99'],
                    ['Electrician'          ,   '99.0'                      ,   '99'],
                    ['Tool room'            ,   '99.0'                      ,   '99'],
                    ['QC/QA tech'           ,   '99.0'                      ,   '99'],
                    ['Office admin'         ,   '99.0'                      ,   '99'],
                    ['RSMeans'              ,   'NaN'                       ,   '99']]

crew_price = pd.DataFrame(crew_price_data, columns=crew_price_columns)
sam_defaults['crew_price'] = crew_price

material_price_columns = ['Material type ID',  'Material price USD per unit' , 'Unit'  ,'Notes']
material_price_data =[# 'Material type ID',                         'Material price USD per unit'           'Unit'                          ,   'Notes'
                        ['unique identifier for the material'   ,   'price of material per unit'        ,   'unit of measure used for cost' ,   'NaN'],
                        ['Concrete 3000 psi'                    ,   '99'                                ,   'cubic yard'                    ,   ''],
                        ['Concrete 5000 psi'                    ,   '99'                                ,   'cubic yard'                    ,   ''],
                        ['Concrete 8000 psi'                    ,   '99'                                ,   'cubic yard'                    ,   ''],
                        ['Steel - rebar'                        ,   '99'                                ,   'ton (short)'                   ,   ''],
                        ['Road base - 3/4 inch crushed stone'   ,   '99'                                ,   'Loose cubic yard'              ,   ''],
                        ['Excavated dirt'                       ,   '0'                                 ,   'cubic yard'                    ,   'NaN'],
                        ['Backfill'                             ,   '0'                                 ,   'cubic yard'                    ,   'NaN']]

material_price = pd.DataFrame(material_price_data, columns=material_price_columns)
sam_defaults['material_price'] = material_price


components_columns = ['Component', 'Mass tonne', 'Lift height m', 'Surface area sq m', 'Coeff drag', 'Coeff drag (installed)', 'Section height m', 'Lever arm m', 'Cycle time installation hrs', 'Offload hook height m', 'Offload cycle time hrs', 'Multplier drag rotor', 'Multiplier tower drag', 'Operation']
components_data = [#  Component                ,   Mass tonne  ,    Lift height m   ,   Surface area sq m  ,   Coeff drag  ,   Coeff drag (installed)  ,   Section height m    ,   Lever arm m     ,   Cycle time installation hrs ,   Offload hook height m   ,   Offload cycle time hrs  ,   Multplier drag rotor    ,   Multiplier tower drag Operation
                    ['IEA 3.6-130 Bedplate'    ,   '80'        ,    '82'            ,   '32.00'            ,   '0.7'       ,   '0.7'                   ,   '0'                 ,   '85.0'          ,   '2'                         ,   '6'                     ,   '0.5'                   ,   '1.000000'              ,   '0'                     ,    'Top'],
                    ['IEA 3.6-130 Drivetrain'  ,   '80'        ,    '86'            ,   '20.00'            ,   '0.9'       ,   '0.9'                   ,   '0'                 ,   '85.0'          ,   '2'                         ,   '6'                     ,   '0.5'                   ,   '0.000000'              ,   '0'                     ,    'Top'],
                    ['Hub'                     ,   '35'        ,    '85'            ,   '12.16'            ,   '1.1'       ,   '1.1'                   ,   '0'                 ,   '85.0'          ,   '1'                         ,   '6'                     ,   '0.5'                   ,   '0.000000'              ,   '0'                     ,    'Top'],
                    ['Blade 1'                 ,   '17'        ,    '85'            ,   '68.80'            ,   '0.1'       ,   '1.4'                   ,   '0'                 ,   '85.0'          ,   '1'                         ,   '6'                     ,   '0.5'                   ,   '0.666667'              ,   '0'                     ,    'Top'],
                    ['Blade 2'                 ,   '17'        ,    '85'            ,   '68.80'            ,   '0.1'       ,   '1.4'                   ,   '0'                 ,   '85.0'          ,   '1'                         ,   '6'                     ,   '0.5'                   ,   '0.666667'              ,   '0'                     ,    'Top'],
                    ['Blade 3'                 ,   '17'        ,    '85'            ,   '68.80'            ,   '0.1'       ,   '1.4'                   ,   '0'                 ,   '85.0'          ,   '1'                         ,   '6'                     ,   '0.5'                   ,   '0.666667'              ,   '0'                     ,    'Top'],
                    ['Tower section 1'         ,   '65'        ,    '20'            ,   '85.00'            ,   '0.6'       ,   '1.1'                   ,   '20'                ,   '10.0'          ,   '1'                         ,   '6'                     ,   '0.5'                   ,   '0.000000'              ,   '1'                     ,   'Base'],
                    ['Tower section 2'         ,   '55'        ,    '40'            ,   '85.00'            ,   '0.6'       ,   '1.1'                   ,   '20'                ,   '30.0'          ,   '1'                         ,   '6'                     ,   '0.5'                   ,   '0.000000'              ,   '1'                     ,   'Base'],
                    ['Tower section 3'         ,   '45'        ,    '60'            ,   '85.00'            ,   '0.6'       ,   '1.1'                   ,   '20'                ,   '50.0'          ,   '1'                         ,   '6'                     ,   '0.5'                   ,   '0.000000'              ,   '1'                     ,   'Base'],
                    ['Tower section 4'         ,   '40'        ,    '85'            ,   '90.00'            ,   '0.6'       ,   '1.1'                   ,   '25'                ,   '72.5'          ,   '1'                         ,   '6'                     ,   '0.5'                   ,   '0.000000'              ,   '1'                     ,    'Top']]

components = pd.DataFrame(components_data, columns=components_columns)
sam_defaults['components'] = components


rsmeans_columns = ['Operation ID', 'Type of cost', 'Material type ID', 'Rate USD per unit', 'Units', 'Daily output', 'Per Diem Hours (per unit)', 'Module', 'Number of workers', 'Notes']
rsmeans_data = [
                        #Operation ID                                       ,   Type of cost        ,       Material type ID                            , Rate USD per unit ,   Units                           ,   Daily output                ,   Per Diem Hours (per unit)   ,   Module          ,   Number of workers   ,   Notes
                        ['Concrete placement'                               ,   'Equipment rental'  ,       'Concrete 5000 psi'                         ,   '99.0'          ,   '$/cubic yard'                  ,   'NaN'                       ,   'NaN'                       ,   'Foundations'   ,   'NaN'               ,   ''
                        ['Rebar installation'                               ,   'Equipment rental'  ,       'Steel - rebar'                             ,   '99.0'          ,   '$/ton (short)'                 ,   'NaN'                       ,   'NaN'                       ,   'Foundations'   ,   'NaN'               ,   ''
                        ['Survey'                                           ,   'Equipment rental'  ,       'NaN'                                       ,   'NaN'           ,   'NaN'                           ,   'NaN'                       ,   'NaN'                       ,   'Roads'         ,   'NaN'               ,   ''
                        ['Clear and grub'                                   ,   'Equipment rental'  ,       'NaN'                                       ,   'NaN'           ,   'NaN'                           ,   'NaN'                       ,   'NaN'                       ,   'Roads'         ,   'NaN'               ,   ''
                        ['Topsoil stripping and stockpiling'                ,   'Equipment rental'  ,       'NaN'                                       ,   '99.0'          ,   'cubic yard'                    ,   'NaN'                       ,   '99.0'                      ,   'Roads'         ,   '99.0'              ,   ''
                        ['Stormwater pollution prevention'                  ,   'Equipment rental'  ,       'NaN'                                       ,   'NaN'           ,   'NaN'                           ,   'NaN'                       ,   'NaN'                       ,   'Roads'         ,   'NaN'               ,   ''
                        ['Culverts'                                         ,   'Equipment rental'  ,       'NaN'                                       ,   'NaN'           ,   'NaN'                           ,   'NaN'                       ,   'NaN'                       ,   'Roads'         ,   'NaN'               ,   ''
                        ['Compaction of soil (subgrade and crane path)'     ,   'Equipment rental'  ,       'NaN'                                       ,   '99.0'          ,   'embankment cubic yards crane'  ,   'NaN'                       ,   '99.0'                      ,   'Roads'         ,   '99.0'              ,   ''
                        ['Mass material movement (cut and fill)'            ,   'Equipment rental'  ,       'NaN'                                       ,   'NaN'           ,   'NaN'                           ,   'NaN'                       ,   'NaN'                       ,   'Roads'         ,   'NaN'               ,   ''
                        ['Placing road base (hauling)'                      ,   'Equipment rental'  ,       'Road base - 3/4 inch crushed stone'        ,   '99.0'          ,   'loose cubic yard'              ,   'NaN'                       ,   '99.0'                      ,   'Roads'         ,   '99.0'              ,   ''
                        ['Rough grading road base'                          ,   'Equipment rental'  ,       'NaN'                                       ,   '99.0'          ,   'Each (100000 square feet)'     ,   'NaN'                       ,   '99.0'                      ,   'Roads'         ,   '99.0'              ,   ''
                        ['Compacting road base'                             ,   'Equipment rental'  ,       'NaN'                                       ,   '99.0'          ,   'embankment cubic yards road'   ,   'NaN'                       ,   '99.0'                      ,   'Roads'         ,   '99.0'              ,   ''
                        ['Final grading'                                    ,   'Equipment rental'  ,       'NaN'                                       ,   'NaN'           ,   'NaN'                           ,   'NaN'                       ,   'NaN'                       ,   'Roads'         ,   'NaN'               ,   ''
                        ['Road maintanance'                                 ,   'Equipment rental'  ,       'NaN'                                       ,   'NaN'           ,   'NaN'                           ,   'NaN'                       ,   'NaN'                       ,   'Roads'         ,   'NaN'               ,   ''
                        ['Decompaction of crane paths'                      ,   'Equipment rental'  ,       'NaN'                                       ,   'NaN'           ,   'NaN'                           ,   'NaN'                       ,   'NaN'                       ,   'Roads'         ,   'NaN'               ,   ''
                        ['Reseeding, planting, etc'                         ,   'Equipment rental'  ,       'NaN'                                       ,   'NaN'           ,   'NaN'                           ,   'NaN'                       ,   'NaN'                       ,   'Roads'         ,   'NaN'               ,   ''
                        ['Concrete placement'                               ,   'Labor'             ,       'Concrete 5000 psi'                         ,   '99.0'          ,   '$/cubic yard'                  ,   '99.0'                      ,   'NaN'                       ,   'Foundations'   ,   '99.0'              ,   ''
                        ['Rebar installation'                               ,   'Labor'             ,       'Steel - rebar'                             ,   '99.0'          ,   '$/ton (short)'                 ,   '99.0'                      ,   'NaN'                       ,   'Foundations'   ,   '99.0'              ,   ''
                        ['Survey'                                           ,   'Labor'             ,       'NaN'                                       ,   'NaN'           ,   'NaN'                           ,   'NaN'                       ,   'NaN'                       ,   'Roads'         ,   'NaN'               ,   ''
                        ['Clear and grub'                                   ,   'Labor'             ,       'NaN'                                       ,   'NaN'           ,   'NaN'                           ,   'NaN'                       ,   'NaN'                       ,   'Roads'         ,   'NaN'               ,   ''
                        ['Topsoil stripping and stockpiling'                ,   'Labor'             ,       'NaN'                                       ,   '99.0'          ,   'cubic yard'                    ,   '99.0'                      ,   '99.0'                      ,   'Roads'         ,   '99.0'              ,   ''
                        ['Stormwater pollution prevention'                  ,   'Labor'             ,       'NaN'                                       ,   'NaN'           ,   'NaN'                           ,   'NaN'                       ,   'NaN'                       ,   'Roads'         ,   'NaN'               ,   ''
                        ['Culverts'                                         ,   'Labor'             ,       'NaN'                                       ,   'NaN'           ,   'NaN'                           ,   'NaN'                       ,   'NaN'                       ,   'Roads'         ,   'NaN'               ,   ''
                        ['Compaction of soil (subgrade and crane path)'     ,   'Labor'             ,       'NaN'                                       ,   '99.0'          ,   'embankment cubic yards crane'  ,   '99.0'                      ,   '99.0'                      ,   'Roads'         ,   '99.0'              ,   ''
                        ['Mass material movement (cut and fill)'            ,   'Labor'             ,       'NaN'                                       ,   'NaN'           ,   'NaN'                           ,   'NaN'                       ,   'NaN'                       ,   'Roads'         ,   'NaN'               ,   ''
                        ['Placing road base (hauling)'                      ,   'Labor'             ,       'Road base - 3/4 inch crushed stone'        ,   '99.0'          ,   'loose cubic yard'              ,   '99.0'                      ,   '99.0'                      ,   'Roads'         ,   '99.0'              ,   ''
                        ['Rough grading road base'                          ,   'Labor'             ,       'NaN'                                       ,   '99.0'          ,   'Each (100000 square feet)'     ,   '99.0'                      ,   '99.0'                      ,   'Roads'         ,   '99.0'              ,   ''
                        ['Compacting road base'                             ,   'Labor'             ,       'NaN'                                       ,   '99.0'          ,   'embankment cubic yards road'   ,   '99.0'                      ,   '99.0'                      ,   'Roads'         ,   '99.0'              ,   ''
                        ['Final grading'                                    ,   'Labor'             ,       'NaN'                                       ,   'NaN'           ,   'NaN'                           ,   'NaN'                       ,   'NaN'                       ,   'Roads'         ,   'NaN'               ,   ''
                        ['Road maintanance'                                 ,   'Labor'             ,       'NaN'                                       ,   'NaN'           ,   'NaN'                           ,   'NaN'                       ,   'NaN'                       ,   'Roads'         ,   'NaN'               ,   ''
                        ['Decompaction of crane paths'                      ,   'Labor'             ,       'NaN'                                       ,   'NaN'           ,   'NaN'                           ,   'NaN'                       ,   'NaN'                       ,   'Roads'         ,   'NaN'               ,   ''
                        ['Reseeding, planting, etc'                         ,   'Labor'             ,       'NaN'                                       ,   'NaN'           ,   'NaN'                           ,   'NaN'                       ,   'NaN'                       ,   'Roads'         ,   'NaN'               ,   ''
                        ['Excavation'                                       ,   'Equipment rental'  ,       'Excavated dirt'                            ,   '99.0'          ,   '$/cubic yard'                  ,   'NaN'                       ,   'NaN'                       ,   'Foundations'   ,   'NaN'               ,   ''
                        ['Excavation'                                       ,   'Labor'             ,       'Excavated dirt'                            ,   '99.0'          ,   '$/cubic yard'                  ,   '99.0'                      ,   '99.0'                      ,   'Foundations'   ,   '99.0'              ,   ''
                        ['Backfill'                                         ,   'Equipment rental'  ,       'Backfill'                                  ,   '99.0'          ,   '$/cubic yard'                  ,   'NaN'                       ,   'NaN'                       ,   'Foundations'   ,   'NaN'               ,   ''
                        ['Backfill'                                         ,   'Labor'             ,       'Backfill'                                  ,   '99.0'          ,   '$/cubic yard'                  ,   '99.0'                      ,   '99.0'                      ,   'Foundations'   ,   '99.0'              ,   ''
                        ['Collection'                                       ,   'Labor'             ,       'NaN'                                       ,   '99.0'          ,   '$/hr'                          ,   '99.0'                      ,   '99.0'                      ,   'Collection'    ,   '99.0'              ,   ''
                        ['Collection'                                       ,   'Equipment'         ,       'NaN'                                       ,   '99.0'          ,   '$/hr'                          ,   '99.0'                      ,   '99.0'                      ,   'Collection'    ,   'NaN'               ,   ''
                        ['Collection'                                       ,   'Labor'             ,       'dozer operator and .5 laborer cable reels' ,   '99.0'          ,   '$/hr'                          ,   'NaN'                      ,    '99.0'                      ,   'Collection'    ,   '99.0'              ,   ''
                        ['Collection'                                       ,   'Equipment'         ,       '200 hp dozer cable reels'                  ,   '99.0'          ,   '$/hr'                          ,   'NaN'                      ,    '99.0'                      ,   'Collection'    ,   'NaN'               ,   ''
                        ['Collection'                                       ,   'Labor'             ,       'Forklift Operator'                         ,   '99.0'          ,   '$/hr'                          ,   'NaN'                      ,    '99.0'                      ,   'Collection'    ,   '99.0'              ,   ''
                        ['Collection'                                       ,   'Equipment'         ,       'all terrain fork lift for reel changes'    ,   '99.0'          ,   '$/hr'                          ,   'NaN'                      ,    '99.0'                      ,   'Collection'    ,   'NaN'               ,   '']]

rsmeans = pd.DataFrame(rsmeans_data, columns=rsmeans_columns)
sam_defaults['rsmeans'] = rsmeans
