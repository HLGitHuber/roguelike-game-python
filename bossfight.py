"""Epic boss fight."""

from time import sleep

enter_text = """
You fall into a huge pit. It looks like some kind of arena.
You look around and see huge pilars flowing with lava.
At the opposite end you see a huge monster facing backwards.
The monster heard your fall, you have to act quick!
"""

first_choice = """
                                   :J7.                               
                     .::..::::.   .P57.                               
                   .!7~^:::!JJ?!::?^                                  
                  .J?7!~~~JP5YY??^:                                   
            :.    ?GGGGBGJ7J55Y~:....                                 
           .GP7!~!G#GPG5P!::^~!7!~~~^.                                      _,.
            .:...7GG5YY5P5JYJJ!^~7?7~^.                                   ,` -.)
                  YY?JPBBGY77~::~5!^^^^..:.                              ( _/-\\-._
                  !GPGGGP5J7???GG7:^^^^^:^!YJ7~?5?                      /,|`--._,-^|             ,
                  .PPPGBBGB###BP!~!~^^^~:..!BBBGPG:                     \_| |`-._/||           ,'|
              ?P5YGBGPPGGP5YJ?????7~^^~~:.:5##BGGP^                       |  `-, / |          /  /
             J#B#&#BBGGPPGPPPP5YJ7~^^!!~^!PBB#GGBB7...                    |     || |         /  /
          .:~B##&&#BBBBGGGPPP5Y????777!~5B##GGBB##Y^^^:.....               `r-._||/   __    /  /
         :~!Y&&&&&&&#BBBGGBBBGGGG5J777?G####BB####5?777!~:....         __,-<_     )`-/  `. /  /
        ^??YG&&&&&&&&&BBGPP555YJ??Y5PB####&&######PP5JJJ?!^::...      '  \   `---'   \    /  /
       !Y5PGG#&&&&&&&&##BP77?J5PB##B#####&##BBB#&##GPPYY5Y!~^::...    |   |           |. /  /
     .?YPGGGGB&&##&&&##&&&####J?GB#B#######BB#B###&&PPGPGPYJ?~^::..   |   |           |./  /
    .J55PPGGGB&&&#&#&###B?!7J?~:^5BBB#&###########BBP.^B#BGY!^^::..   |   /           //  /
    J5PPPGGBB#&&&&&&&&##Y^::^^:::75PP55PP5Y55GGGGB#BG: G#G?!~^^::.:.  \_/' \         |/  /
   ~PPPGGGGB#5B&&##BBB5J!~^:::^::::^:.......::::::^~~ :#B5?!~~^:::^.   |    |   _,^-'/  /
   ?PPPPGGGBBG.JGPP5?7!~~^:......................:... ?B5J7!7!~^^^.    |    , ``  (\/  /_
   ~GPPPPGGBB#?!G5J7~~^^^^^:....:.................::::BGY?7!77~^^:      \,.->._    \X-=/^
    ?GPGGGGGGB#GP5J7!~~~^^:::::....................::YBP5J!!~~~~~       (  /   `-._//^`
     7GGGGGGGB#GP55Y?777~^^^:::::::::............:::^G#GGPY?7!~~:        `Y-.____(__}
      ^PBGGGBBBGPPP55YJ?7!!!^^^:::::^::.::::..:::::!G#PYJY5555J~          |     {__)
        ?GBGBB##GPPPPP5J?77!~~~^^^^::::::::::^^~7JPG#B5JJJ?????~                ()
         :YP#####BGPPPPP5Y??77!!~^^^^^^^^^~!7YPGBP?:~G555YYYJJJ?.     
            !G&&BB#&#BGGPP55YJJ???777?JY5PBBBGY!^:::^!J5J!!?7::.      
              ^PBGGB#&&&&&&#############BPY7~::::^::~                 
               YBGGGPPGGBB######BGP5Y?7~^^^:^^:::^^^~                 
              .GGGGGGGPPP5???77!!!!~~~~^^~~^^^:::::^!.                
               ~BPY??JY5P5YJYYYJ??J??7!!!!~^^:::^~~^:                 
               .&##B5JJJJ555YYYYJJJJJ777777JY55PGG!                   
               .##BBB#&#B7^!77777???7!!G####BGGGPY                    
                P&#BGB#&&.             G@&##GGGGG~                    
                7&BBB#B#&5             !&&&&#BGGG?                    
                :&#BBBBB&&             J&&&&&BGGGP.                   
                 P&#BBBG#G             ?@&&&&#BBG5                    (1) Charge on the monster with your mighty sword!
                 :&#BBBGG:              B&&&&#BBG:                    (2) Wait for it's move.
                 .#&BBBB~               .G&&##BBY                     (3) Lay down and pretend to be dead.
                G#&#GGGGG.               ~&&##BGGP?.                  
               ^#@@&&##&&.               Y&&&&&&@@G                   
             ^Y#&&&&&###&!                Y@@&&&&&#.                  
         .?PB##BB##&&&&##P                G&&&&&&&&Y                  
         :PGP555555J!^^:.                5@#B#####&#P^                
                                         ^Y5PP5P555JJ!                
"""
choice1_charge = """
You gather all your strength and courage and charge at the mighty beast!
As you run the giant starts to turn while scratching his head.
When it turns you're almost near it, you lunge your sword forward!
The beast looks at your lousy attempt and starts to roar, the blow is so hard you fall to the ground.
This green abomination catches your foot and lifts you in the air.
You both look into each others eyes. But you're upside down, trapped in a powerfull grip.
"""
choice1_wait = """
You decide to wait for the monster to make its first move.
It turns around and starts staring at you. Every second passes it smiles more and more.
You notice it's dripping saliva out of that giant mouth. This doesn't look good.
It starts running right at you. Its speed is incredible!
Your armor is too heavy, you won't make the dodge in time!
"""
choice1_drop = """
You drop dead hoping the monster wouldn't notice you or just ignore like a dead pest.
You're afraid to open your eyes, mumbling to yourself 'please leave me alone', 'i don't want to die'.
You hear footsteps getting louder and the floor trembling with each step.
Suddenly the sound stops, you can hear the giants breath and its saliva drips on your head.
The foul stench is making you nauseous, you can barely hold youself from screaming.
You can feel a hard grip around your leg and suddenly the monster is holding you in the air.
"""

second_choice = """
                                                             ..:^~~~!!!!!~~^.                                                               
                                                          .:^~~~~~!!!!!777??JJ?!:                                                           
                                 ::.                 .~7??!!~~~~~~~!!7!!!777??JJYJ7:                                                        
                               ^5BG5Y:             !5PPPGGGPPP5PP5Y???7!~7?YY5Y55PGBG5J^                .                                   
                              :GB##B5G~           !?7777??JJY5PGPYYJYY?77YPBB#######&&&&G:            ^5BG?                                 
                              7GBBBBYGGY:        :~~~~!!!777?????JJJ5J??J5PGPPGGGGGGGGGGBB:         .!5#&##Y                                
                              ^JY5GGBBBBB5~.    .~~~!7JY5PGGGGGPP5YYYJ?J5GBBBBGGBBBGGGGGPGJ        ^!?B&##B#~                               
                                ...:^~7JG##B57^:^~!?Y5P55PG####GPYJJJYYPBB###########BBGGPP:   .~5GP5GB##BBB!                               
                                         :JBG7^^~!?Y57^:~7775B#PY?77?JYGBB###&&BP55PG###BGGY~?5B&&#BP5YJ?7~:                                
                                           :7::^!!?P^..P#&&B!7##Y~~~!7?YGBB#&#J7JPG577P&#BGPPB#BY^                                          
                                            .:^^~~!?7!~B&&&&5PGY^^^~!!!7J5GB&BJ5@&@@B7?G#GGP5P?.                                            
                                           .::^^^^~~!?JJ55Y?7!~^~~!!!!!7777J5GBB#&&#GGBBGPP5YY                                              
                                          .:::^^^^^^^^^^^^^^^^~!7777777??JJY555PPPPPGGGPP555YY7                                             
                                          ::::^^^^^^^^^~7~^^~!!!77777??JJY5PGPP55PGP55YY5555YYY^                                            
                                          ::::^^^^^^~~?5Y7Y5YJJ??JJJJY55PPGGGGGGGPGBGPP5555YYYY7                                            
                                         .::::^^^^~!7JGGJ5B&&&&&#BBBBBBBBB##&&&&&#B#GPPP5555YYJJ                                            
                                         ::::^^^^~!?5G57~~!77?Y5PGB#######&&&&&###B#BGGPP555YYYY.                                           
                                         :::^^^~~7JPP?^^^^^~~~~~!?JJY5PGBBBBGGGGGGGGBBGGPP55YYYY.                                           
                                         :^^^^~~7JP57^^^^^^^^^^~7??777777?J5PPPPPPPPGBBBGGP5YYYY                                            
                                        .:^^^~~!?55!^^^::::^^^^~!!!!!!!!~~~?Y5555555PGBBBGPP555Y.                                           
                                     ~5#5:^^^~!7Y5?^::^~!77??77777!!!!!~!!?YPP5555555PBBBGGP55Y5&G?~:        .~G&&J                         
                   :~7^.          ^J#&BJ^:^^~~!?5J^^?PB#&&&&######BBBBBBB##&######BGP5GBBGGP55Y5&&&&&#GJ^  .Y&&@@&@!                        
                 .5#&&&#BY:   ..~P&&P!::::^^~~7?Y!^P&&@@@&&&&&@&&###&&#BBB&&&&&&&&&&&BPBBGGP55Y5G&&&&&&@@&B&&&&&&&&#                        
                :G#####BGGPY7?YYB&B?::::::^^~!7JJ^P&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&BGBGGPP5Y5PG&&&&&&&@@&&@&&&&&&7                       
                J#&&#&#G5YJJJ55P##7:::::::^^~!7J77#&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&#GBGPPP55PPP#@@&&&&&&&&@&&&&&&#Y7~^:.                 
               .B&&&&&GPPY?YP5P#B!^^::::::^^!7?Y!Y#&&&@@@@@@@&&&&&&&&&&&&&&@@@@@@&&&@&#GBGPP555PPPB&&&&&&&@&&&@&&&&&#5???77!^.              
               7&&&&&#PGPYJ5GG#&?^^^^:::::^~!7JY!Y#&###@@@&&&&&&&&&&&&&&&&&&&@@@&#&&@&BGBPPP55PGPPB&&&&#&@&&&&&&&&&&&5J?????77!^.           
           ....J#&&&&#PPPY5G#GB&!^~^^^:^::^~!7JYJYB&@B~!B@&&&&&&&&&&&&&&&&&&&@@&BG#@@#GGGPPPPPGPPPB&&&&&&&@&&&&&&&&&&GJ????????77~:         
        .. ....J#&&&&#GG5PGGGP#&J:^^^^^^^^^^~!?Y5J5G&#!^:Y#&&&#####&&&&&&&&&&BGPP5B@#BBBGGGGGGGPPPB&@&&&&&&&&&&&&&&&&PJ????????7777!:       
       ........?&&&&&GGGPGPPPG#&P:^~^^^^^^^^^~7?YY7JYPB7^7JGBBGPPPPPGGGB#BP5~:!5#&&BGGBGGGGGGGGPPGG#&@&&@@@@&@&&&&&@&PJ??????????7777~.     
     .:........7&&&&#BPGGPGGGG#&B^:^!~^^^^^^^^~!7??!7?JJJ?^:~!!7J777~~~7~..^?GB##BGGGBBGBGGPGPGPGGB&&&&@@&&&&&@&&&&@#5JJJJ????????7777!:    
    :~:....::::~#&&#BGG#GPGBBGB&#7.:~!~^^^^^^^^~!!7~!777???7J57!!~!?!7?5GJYPB#BGPPGGBBBGGPPPPGGGGGB@@@&&@@&&&#&@&&&&BYJJJ??????????7?77!.   
   .7~^::::::::^5&##GG##GPP###BB#5^.:!?!^^^^^^^~!!7!~!77777??Y55PGB###BB#BBBGGGGGGBBBBGPPPPPGGGPPP#@&@@@@&&&&&&&&&&&GJJJJ?????????????77!.  
   ^?7!~~~~~~~~~?##BGB&BG#BGG#BB&B?:.:~!7!~~^^~~~!777!!7JYYYJJJJJJYYY5PGGGPGBBBBBBBBBGPPPPPPGPPP5G&@@@@@@&&&&&&&&&&&PJJJJJJ????????????7!~  
   !????7777777!J##BBB#GBBGGB##BB#B?:.:^777~~~~~~!!7??7!!7YPBBBBBBBBBBBBBBBBBBBBBBBBGGPPGGPGP55Y5&&&&@&&@&&@&@@&@&&&PJJJJJJJ???????J???7!!: 
   !??????JJJJJ?5&&#####&B#BB&#GB###J^..:!?J?!~~~~!!7??JJJJYPBBBBBBBBBBBBBBBBBBBBBGGGGGGGGPP5YYYB&&@&@@&&&&&&&@&@@&&BYJJJJJJJJJJJJ?????7!!!.
   7???JJJJJJJYYG&&&&&#&&#&##G#&B####P7:.:~?77!!~~!!77??JY5PPGBB#######BB#BBBBBBBGGGGGGPPGP55YYB&&&@@&&&@&&&&&&&&@&&#5JJJJYJJJJJJJJ?J??77!!!
  .???JJJJJJJJYYB&&&&&&&#&@&B#&&@#PBB&G?^.::^!!?J?!!!77??JJY55Y5PGBB###BBBBBBBBBBBGGGGGP555YYYG&&&&@@@@&@@&&&&&&&@&&&5JJYYYYYJJJJJJJJJ?777!!
  .???JJJJJJJYY5&&&&@&&&&&&&&&#&@&&&BB#BY^...:^!?JJ?7!77??JY55555YY5PGBBBBBBBBBGGGPGGP55YJJYYG&&&@@@@&@@@&@@&&&&&@@@&PYJYYYYYYYYYYJJJJ???77!
  
                                        
										(1) Cut off your leg!
										(2)	Swing your sword hoping to cut the monsters face!
										(3)	Just give up and wait for the inevitable.
"""

second_choice_wait = """
                                                             ..:^~~~!!!!!~~^.                                                               
                                                          .:^~~~~~!!!!!777??JJ?!:                                                           
                                 ::.                 .~7??!!~~~~~~~!!7!!!777??JJYJ7:                                                        
                               ^5BG5Y:             !5PPPGGGPPP5PP5Y???7!~7?YY5Y55PGBG5J^                .                                   
                              :GB##B5G~           !?7777??JJY5PGPYYJYY?77YPBB#######&&&&G:            ^5BG?                                 
                              7GBBBBYGGY:        :~~~~!!!777?????JJJ5J??J5PGPPGGGGGGGGGGBB:         .!5#&##Y                                
                              ^JY5GGBBBBB5~.    .~~~!7JY5PGGGGGPP5YYYJ?J5GBBBBGGBBBGGGGGPGJ        ^!?B&##B#~                               
                                ...:^~7JG##B57^:^~!?Y5P55PG####GPYJJJYYPBB###########BBGGPP:   .~5GP5GB##BBB!                               
                                         :JBG7^^~!?Y57^:~7775B#PY?77?JYGBB###&&BP55PG###BGGY~?5B&&#BP5YJ?7~:                                
                                           :7::^!!?P^..P#&&B!7##Y~~~!7?YGBB#&#J7JPG577P&#BGPPB#BY^                                          
                                            .:^^~~!?7!~B&&&&5PGY^^^~!!!7J5GB&BJ5@&@@B7?G#GGP5P?.                                            
                                           .::^^^^~~!?JJ55Y?7!~^~~!!!!!7777J5GBB#&&#GGBBGPP5YY                                              
                                          .:::^^^^^^^^^^^^^^^^~!7777777??JJY555PPPPPGGGPP555YY7                                             
                                          ::::^^^^^^^^^~7~^^~!!!77777??JJY5PGPP55PGP55YY5555YYY^                                            
                                          ::::^^^^^^~~?5Y7Y5YJJ??JJJJY55PPGGGGGGGPGBGPP5555YYYY7                                            
                                         .::::^^^^~!7JGGJ5B&&&&&#BBBBBBBBB##&&&&&#B#GPPP5555YYJJ                                            
                                         ::::^^^^~!?5G57~~!77?Y5PGB#######&&&&&###B#BGGPP555YYYY.                                           
                                         :::^^^~~7JPP?^^^^^~~~~~!?JJY5PGBBBBGGGGGGGGBBGGPP55YYYY.                                           
                                         :^^^^~~7JP57^^^^^^^^^^~7??777777?J5PPPPPPPPGBBBGGP5YYYY                                            
                                        .:^^^~~!?55!^^^::::^^^^~!!!!!!!!~~~?Y5555555PGBBBGPP555Y.                                           
                                     ~5#5:^^^~!7Y5?^::^~!77??77777!!!!!~!!?YPP5555555PBBBGGP55Y5&G?~:        .~G&&J                         
                   :~7^.          ^J#&BJ^:^^~~!?5J^^?PB#&&&&######BBBBBBB##&######BGP5GBBGGP55Y5&&&&&#GJ^  .Y&&@@&@!                        
                 .5#&&&#BY:   ..~P&&P!::::^^~~7?Y!^P&&@@@&&&&&@&&###&&#BBB&&&&&&&&&&&BPBBGGP55Y5G&&&&&&@@&B&&&&&&&&#                        
                :G#####BGGPY7?YYB&B?::::::^^~!7JJ^P&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&BGBGGPP5Y5PG&&&&&&&@@&&@&&&&&&7                       
                J#&&#&#G5YJJJ55P##7:::::::^^~!7J77#&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&#GBGPPP55PPP#@@&&&&&&&&@&&&&&&#Y7~^:.                 
               .B&&&&&GPPY?YP5P#B!^^::::::^^!7?Y!Y#&&&@@@@@@@&&&&&&&&&&&&&&@@@@@@&&&@&#GBGPP555PPPB&&&&&&&@&&&@&&&&&#5???77!^.              
               7&&&&&#PGPYJ5GG#&?^^^^:::::^~!7JY!Y#&###@@@&&&&&&&&&&&&&&&&&&&@@@&#&&@&BGBPPP55PGPPB&&&&#&@&&&&&&&&&&&5J?????77!^.           
           ....J#&&&&#PPPY5G#GB&!^~^^^:^::^~!7JYJYB&@B~!B@&&&&&&&&&&&&&&&&&&&@@&BG#@@#GGGPPPPPGPPPB&&&&&&&@&&&&&&&&&&GJ????????77~:         
        .. ....J#&&&&#GG5PGGGP#&J:^^^^^^^^^^~!?Y5J5G&#!^:Y#&&&#####&&&&&&&&&&BGPP5B@#BBBGGGGGGGPPPB&@&&&&&&&&&&&&&&&&PJ????????7777!:       
       ........?&&&&&GGGPGPPPG#&P:^~^^^^^^^^^~7?YY7JYPB7^7JGBBGPPPPPGGGB#BP5~:!5#&&BGGBGGGGGGGGPPGG#&@&&@@@@&@&&&&&@&PJ??????????7777~.     
     .:........7&&&&#BPGGPGGGG#&B^:^!~^^^^^^^^~!7??!7?JJJ?^:~!!7J777~~~7~..^?GB##BGGGBBGBGGPGPGPGGB&&&&@@&&&&&@&&&&@#5JJJJ????????7777!:    
    :~:....::::~#&&#BGG#GPGBBGB&#7.:~!~^^^^^^^^~!!7~!777???7J57!!~!?!7?5GJYPB#BGPPGGBBBGGPPPPGGGGGB@@@&&@@&&&#&@&&&&BYJJJ??????????7?77!.   
   .7~^::::::::^5&##GG##GPP###BB#5^.:!?!^^^^^^^~!!7!~!77777??Y55PGB###BB#BBBGGGGGGBBBBGPPPPPGGGPPP#@&@@@@&&&&&&&&&&&GJJJJ?????????????77!.  
   ^?7!~~~~~~~~~?##BGB&BG#BGG#BB&B?:.:~!7!~~^^~~~!777!!7JYYYJJJJJJYYY5PGGGPGBBBBBBBBBGPPPPPPGPPP5G&@@@@@@&&&&&&&&&&&PJJJJJJ????????????7!~  
   !????7777777!J##BBB#GBBGGB##BB#B?:.:^777~~~~~~!!7??7!!7YPBBBBBBBBBBBBBBBBBBBBBBBBGGPPGGPGP55Y5&&&&@&&@&&@&@@&@&&&PJJJJJJJ???????J???7!!: 
   !??????JJJJJ?5&&#####&B#BB&#GB###J^..:!?J?!~~~~!!7??JJJJYPBBBBBBBBBBBBBBBBBBBBBGGGGGGGGPP5YYYB&&@&@@&&&&&&&@&@@&&BYJJJJJJJJJJJJ?????7!!!.
   7???JJJJJJJYYG&&&&&#&&#&##G#&B####P7:.:~?77!!~~!!77??JY5PPGBB#######BB#BBBBBBBGGGGGGPPGP55YYB&&&@@&&&@&&&&&&&&@&&#5JJJJYJJJJJJJJ?J??77!!!
  .???JJJJJJJJYYB&&&&&&&#&@&B#&&@#PBB&G?^.::^!!?J?!!!77??JJY55Y5PGBB###BBBBBBBBBBBGGGGGP555YYYG&&&&@@@@&@@&&&&&&&@&&&5JJYYYYYJJJJJJJJJ?777!!
  .???JJJJJJJYY5&&&&@&&&&&&&&&#&@&&&BB#BY^...:^!?JJ?7!77??JY55555YY5PGBBBBBBBBBGGGPGGP55YJJYYG&&&@@@@&@@@&@@&&&&&@@@&PYJYYYYYYYYYYJJJJ???77!
  
                                        
										(1) Try to dodge as fast and hard as you can.
										(2)	Drop your sword and rip off your armor to gain speed. Then try to dodge.
										(3)	Point your sword forward to the giant, you won't go down without a fight!
"""
choice2_leg = """
You fall to the floor with your leg detatched. You desperately try to reach the giants legs.
The monster is stunned, it just stares at your actions. You make it to its foot.
You try to pierce it but with no avail. Your sword blunted from hitting your armor.
It stares at you.                      
You stare at it back.                  
                 
The Ogre picks you up and throws into its mouth... The last thing you see is...
"""
choice2_fight = """
You swing your sword blindly hoping for anything. The monster grabs your sword and throws it away.
You know you can do nothing now. You just wait for it to end.
It stares at you.                      
You stare at it back.                  
                 
The Ogre throws you into its mouth... The last thing you see is...
"""
choice2_giveup = """
You already know there's nothing you can do. The sword slips your hand and falls to the ground.
Your helmet visor opens up, you can see the giants face clearly.
It stares at you.                      
You stare at it back.                  
                 
The Ogre throws you into its mouth... The last thing you see is...
"""
choice2_dodge = """
You try to lunge away as fast and hard as you can. Due to the armor weight you drop just a meter away.
The monster is almost near you. You try to pull up the sword but you don't have enough time.
You feel your bones breaking and the armor flattens cutting your skin from the waist down.
The pain is unbearable. It's the end. You beg it to finish it quick.
It stares at you.                      
You stare at it back.                  
                 
The Ogre picks you up and throws into its mouth... The last thing you see is...
"""
choice2_stirp = """
You hastily try to strip down to get a chance at running away.
You drop your sword, helmet and manage to get your overburdening armor off.
You try to run but it's already too late. The monster grabs you in its palm.
It lifts you up squishing your body like a soft sponge. You bones break, you scream in pain.
It stares at you.                      
You stare at it back.                  
                 
The Ogre throws you into its mouth... The last thing you see is...
"""
choice2_standground = """
You decide to stand your ground and point your sword at the incoming enemy.
As the giant aproaches you it swings its leg yeeting you into the arena wall.
You feel every bone in your body break as you hit a hard surface. Blood fills your mouth.
You fall on the ground. The monster approaches you.
It stares at you.                      
You stare at it back.                  
                 
The Ogre picks you up and throws into its mouth... The last thing you see is...
"""
rekt = """
Y O U   A R E   D E A D
G A M E   O V E R"""
troll = """
    ⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀ ⣀⣀⣤⣤⣤⣀⡀
    ⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀
    ⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆
    ⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆
    ⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆
    ⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠸⣼⡿
    ⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉
    ⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
    ⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇
    ⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇
    ⠀⠀ ⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠇
    ⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇
    ⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""


def bossfight():
    for char in enter_text:
        sleep(0.05)
        print(char, end="", flush=True)
        # text_box.append_html_text(char)
    print(first_choice)
    # text_box.append_html_text(first_choice)
    choice = input()
    if choice == '1':
        for char in choice1_charge:
            sleep(0.05)
            print(char, end="", flush=True)
            # text_box.append_html_text(char)
    if choice == '2':
        for char in choice1_wait:
            sleep(0.05)
            print(char, end="", flush=True)
            # text_box.append_html_text(char)
    if choice == '3':
        for char in choice1_drop:
            sleep(0.05)
            print(char, end="", flush=True)
            # text_box.append_html_text(char)
    if choice == '1' or choice == '3':
        print(second_choice)
        # text_box.append_html_text(second_choice)
        choice2 = input()
        if choice2 == '1':
            for char in choice2_leg:
                sleep(0.05)
                print(char, end="", flush=True)
                # text_box.append_html_text(char)
        if choice2 == '2':
            for char in choice2_fight:
                sleep(0.05)
                print(char, end="", flush=True)
                # text_box.append_html_text(char)
        if choice2 == '3':
            for char in choice2_giveup:
                sleep(0.05)
                print(char, end="", flush=True)
                # text_box.append_html_text(char)
    if choice == '2':
        print(second_choice_wait)
        # text_box.append_html_text(second_choice_wait)
        choice2 = input()
        if choice2 == '1':
            for char in choice2_dodge:
                sleep(0.05)
                print(char, end="", flush=True)
                # text_box.append_html_text(char)
        if choice2 == '2':
            for char in choice2_stirp:
                sleep(0.05)
                print(char, end="", flush=True)
                # text_box.append_html_text(char)
        if choice2 == '3':
            for char in choice2_standground:
                sleep(0.05)
                print(char, end="", flush=True)
                # text_box.append_html_text(char)
    print(troll)
    sleep(3)
    for char in rekt:
        sleep(0.15)
        print(char, end="", flush=True)
        # text_box.append_html_text(char)


bossfight()
