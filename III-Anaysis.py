"""                    TD PART III :
#################################################################
    ANALYSIS AND HYPOTHESIS WITH A GENOME SCALE METABOLIC MODEL
From the given functions, the information you got about the cobra language,
and the result of previous TD part, try to answer the following questions.
files: practical_metabolic_model.pdf
model : e_coli_core.xml
        other to download
For a better understanding, you can also open the file functions.py to see how functions are built.
During this tutorial you will use object oriented language.
"""
######A
# 1- Load module:
from functions import *

#2- Download and import e_coli_core model:

#3 - Print information about the model:

#4- Launch the flux balance analysis without changing any parameter:

#5- Print the objective value. Was it what you expected? 

#6- Print fluxes. How many reactions are active in this condition?

#7 From the fluxes, define which metabolites are consumed and produced by the model?
#Verify your results with the summary function:


#8- print the summary of one of these metabolites  to see how it's produced and consumed:

#9- Verify if the model can grow without oxygen:
## Create a new model to keep initial state

## Set upper bound and lower bound:

## Launch fba

## Conclude

#10- Verify if the model can use other carbon sources : lactate or formate.
## Create a copy of the model

## Close the model

## Change bounds to allow entry of the target metabolite and verify that the change is done:

#11- It is possible to produce acetate and to grow? change the objective function (growth min 0.20):

## Change the coefficient for ac from 1 to 0.5 for example. What do you observe?

#######B
#Let's look all of this in an entire model;
"""  In biggest model is more difficult to interpret something. Lets see if we can answer to some
question using different functions.
"""

"""  I - You know that you will receive a Saccharomyces cerevisiae strain that you have to grow.
You have 3 different media. Which one will you use to be sure that the strain will grow?"""
Medium1 = ['ac_e','ade_e','ala__L_e','arg__L_e','asn__L_e','asp__L_e','ca2_e',
           'cit_e','cys_L_e','man_e','gln__L_e','glu__L_e','h2o_e','his__L_e',
           'ile__L_e','mg2_e','nad_e','nh4_e','nac_e','pi_e','pro__L_e','ser__L_e',
           'so4_e','try__L_e','tyr__L_e','trp__L_e','h2_e','o2_e' ]
Medium2 = ['ac_e','ade_e','ala__L_e','arg__L_e','asn__L_e','asp__L_e','ca2_e',
           'cit_e','cu2_e','cys_L_e','fe2_e','fe3_e','fru_e','glc__D_e',
           'gln__L_e','glu__L_e','h2o_e','his__L_e','ile__L_e','mg2_e','nad_e',
           'nh4_e','nac_e','no3_e','pi_e','pro__L_e','ser__L_e','so4_e','try__L_e',
           'tyr__L_e','ura_e','val__L_e','trp__L_e','h2_e','o2_e' ]
Medium3 = ['4abz_e','ac_e','ace_e','ade_e','ala__L_e','arg__L_e','ascb__L_e','asn__L_e',
           'asp__L_e','btn_e','cbl1_e','cit_e','cl_e','cobalt2_e',
           'cu2_e','cys_L_e','fe2_e','fe3_e','fol_e','glc__D_e','glu__L_e','gly_e','gthrd_e',
           'gua_e','h2o_e','hco3_e','his__L_e','i_e','ile__L_e','inost_e','k_e','leu_L_e','met__L_e','co2_e','no2_e',
           'mg2_e','mn2_e','mndn_e','mobd_e','na1_e','nad_e','nh4_e','nac_e','ni2_e',
           'no3_e','pi_e','pnto__R_e','pro__L_e','pydam_e','pydxn_e','rezrn_e','ribflv_e',
           'ser__L_e','so4_e','thci_e','thm_e','try__L_e','tyr__L_e','ura_e','val__L_e',
           'xan_e','zn2_e','h_e','trp__L_e', 'mobd_e','slnt_e', 'tungs_e','lipoate_e',
           'pydx_e','o2_e' ]

# Download one model from bigg database 

# Verify that the model can grow without changing any parameter:

# Verify how the model can grow in each medium and conclude:



""" II- You work for an agribusiness company specialized in yoghurt production.
In, purpose to improve the taste of some product, you want to produce the molecule RR 2 3 Butanediol which gave the 
butter/creamy taste. Your company wants a biological way to produce this molecule instead of chemical.
you have 3 species in your bacteria collection:
    - Saccharomyces cerevisiae
    - Lactococcus lactis
    - Klebsiella pneumoniae
Can you tell which species is the most likely to produce this molecule? """

# Find molecule id on Bigg database / its exchange reaction associated

# Load the 3 models


# Run following function for 'lactococcus lactis':
#%%% = updateLactococcus(%%%)

# Verify that models can grow:

#for each model find biomass function position or name

#=> Choice 1 :
#- Update the biomass bound (>0)
#- Change the objective function
#- Run FBA

#=> Choice 2 :
#- Change the objective function with both reactions
#- Run FBA


# What can you conclude?

# Did you check if models could spontaneously produce the molecule?


"""" A research lab is working on gut microbial communities and crossfeeding interaction, and found out that,
Fecalibacterium prausnitzii needs acetate to grow.  From these different gut species,which one is the most likely
to cooperate with Faecalibaterium?
 - Blautia hydrogenotrophica 
 - Roseburia intestinalis
 Visit: https://www.vmh.life/ download XML file
"""




