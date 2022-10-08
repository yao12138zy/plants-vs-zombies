# welcome page :
advanture_button_info = ((330,140),(470,100))  # [ [size][left-top-position] ]

# select page:
all_plant_list = (100,90)  # (pos)
selected_plant = (100,0)
start_button = ((154,37),(255,550))  # (size),(pos)

card_size = (50,70)
peashooter = (123,134)  # r1c1  column diff = 52, row diff = 72;  # (pos)
cherrybomb = (175,134)  # r1c2
sunflower = (227,134)  # r1c3
wallnut = (279,134)  # r1c4
squash = (331,134)  # r1c5
snowpea = (125,206)     # r2c1
chomper =  (177,206)     # r2c2
hypnoshroom = (229,206) # r2c3
iceshroom = (281,206)  # r2c4
repeaterpea = (333,206) #r2c5

plants = {"peashooter":peashooter, "cherrybomb":cherrybomb, "sunflower":sunflower, "wallnut":wallnut,\
        "squash":squash, "snowpea":snowpea, "chomper":chomper, "hypnoshroom":hypnoshroom, "iceshroom":iceshroom, \
        "repeaterpea":repeaterpea }

slots_for_chosen = [(178, 9), (232, 9), (286, 9), (340, 9), (394, 9), (448, 9), (502, 9), (556, 9)] # diff = 54

#  ----------------------------------------------  game start page:
plant_image_size = (60,60)
font_size = 20  # for sunshine number
font_pos = (125,65)  # for sunshine number
panel = (100,0)

# sunshine
sunshine_size = (40,40)
sunshine_x_range = [165,838]
sunshine_fall_speed = 0.5
sunshine_generate_inverval = 4  # seconds
each_sunshine_worth = 25
sunshine_vanish_time = 3 # seconds

grass_positions = [[(180, 110), (257, 110), (334, 110), (411, 110), (488, 110), (565, 110), (642, 110),\
                    (719, 110), (796, 110)], [(180, 205), (257, 205), (334, 205), (411, 205), (488, 205), \
                    (565, 205), (642, 205), (719, 205), (796, 205)], [(180, 300), (257, 300), (334, 300), \
                    (411, 300), (488, 300), (565, 300), (642, 300), (719, 300), (796, 300)], [(180, 395), \
                    (257, 395), (334, 395), (411, 395), (488, 395), (565, 395), (642, 395), (719, 395), \
                    (796, 395)], [(180, 490), (257, 490), (334, 490), (411, 490), (488, 490), (565, 490), \
                    (642, 490), (719, 490), (796, 490)]]


plant_price = [50, 100, 150, 50, 50, 175, 150, 75, 75, 200]  # price based on plant_index

plant_index = {"sunflower": 0, "peashooter": 1, "cherrybomb": 2 , "wallnut": 3, \
        "squash": 4, "snowpea": 5, "chomper": 6, "hypnoshroom": 7, "iceshroom": 8, \
        "repeaterpea": 9 }

# sunflower
sunflower_generate_interval = [10,25]

# wallnut
wallnut_health = 800

# cherrybomb
cherrybomb_attack_damage = 1000000

# peashooter
bullet_size = (30,30)



# ------------------------------------- Zombie Constants
zombie_image_size = (55, 90)
house_x_pos = 160
zombie_x_start = 850
zombie_y_pos = [90, 185, 280, 375, 470]
zombie_index = {"basic": 0,"conehead": 1, "buckethead": 2, "football": 3}

# conehead zombie
conehead_zombie_health = 100

# buckethead zombie
buckethead_zombie_health = 200

# football zombie
football_zombie_health = 200
football_zombie_move_speed = 0.3

total_zombies = 10