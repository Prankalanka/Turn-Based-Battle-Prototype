
# 1. create the team and enemy side that changes the amount depending on how many members there are (a square per person)
# 1a. each box is a side with a maximum of 8 members,
# they should be able to change proportions based on how many members there are. (probably set them up as fractions of the screen to be compatible with all resolutions)

# WHAT ENTITIES AND TEMPLATES ARE: Entities are independent copies (instance) of a template (object), the template holds basestats and an ability/ies (idk) based on turns, (like regains health every 2 turns or, freezes are 2 targeted enemies), that are able to be used inside a battle or held within an inventory.
# They can not be assigned to a side but at all times must be held within an inventory to exist.

# the system that creates characters and draws them inside the boxes when active
# (not connected with any inventory yet)e
# the architecture plan:
# the class entity_template will hold base stats and abilities for a member instance to copy
# the abilities will probably be a function that has functions that augment an entity's / side's attributes
# the entire battle will probably run on a list with functions on it


# elemental reaction system for up to 2 or probs 3 elements





# each member should have their own rect within the rect
# the rect should appear to be divided up to achieve this

# so like make two rects, within the rect and draw them

# ARCHITECTURE

# SIDES - Sides should hold up to eight entities and change how many squares there are based on that. They will have conditions able to be influenced by abilities. Entities should be able to swap between them.
# THE GAP - The Gap should be divided into three, and in some way dangerous to cross. This will be rewarded though, with powerups / currency (rewards), and the ability to swap sides.
# ENTITIES - Entities actually do things, they can obviously attack opposing entities, they can influence conditions on the sides, they can move to the gap, and if they reach the middle of the gap, they can even swap sides (nothing actually decided yet).
# TURNS -
# swapping sides watchinhg utube video on what turn based system i want
# DEALING WITH RNG - We could have predictions or smthn for different areas or fights (like, one of your characters will die maybe, that might not be good though)
# "the random parts just need to be something that has a lower chance of screwing you over if you're able to prepare for it"

# The Stat System
# Characters probably have a main combat move (like their elemental skill), an ult (elemental burst), and a passive probz
