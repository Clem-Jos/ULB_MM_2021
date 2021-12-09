from cobra import *
import pandas as pd
import numpy as np
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def modelMetabolites(model):
    L=[]
    for x in model.metabolites:
        L.append(x.id)
    return L
def modelReactions(model):
    L=[]
    for x in model.reactions:
        L.append(x.id)
    return L

def modelGenes(model):
    L=[]
    for x in model.genes:
        L.append(x.id)
    return L
def stoicMatrix(model):
    matrix = util.array.create_stoichiometric_matrix(model)
    column = modelReactions(model)
    line = modelMetabolites(model)
    stoiMatrix = pd.DataFrame(matrix, columns=column, index=line)
    return stoiMatrix

def summary(model):
    print("Reactions")
    print("---------")
    for x in model.reactions:
        print("%s : %s" % (x.id, x.reaction))

    print("")
    print("Metabolites")
    print("-----------")
    for x in model.metabolites:
        print('%9s : %s' % (x.id, x.formula))

    print("")
    print("Genes")
    print("-----")
    for x in model.genes:
        associated_ids = (i.id for i in x.reactions)
        print("%s is associated with reactions: %s" %
              (x.id, "{" + ", ".join(associated_ids) + "}"))

def objectiveFunction(model):
    L = []
    return L

def isExchangeRxn(model):
    L=[]
    for x in model.reactions:
        L.append(medium.boundary_types.is_boundary_type(x,'exchange','e'))
    return L

def isSinkRxn(model):
    L=[]
    for x in model.reactions:
        L.append(medium.boundary_types.is_boundary_type(x,'sink','e'))
    return L

def isDemandRxn(model):
    L=[]
    for x in model.reactions:
        L.append(medium.boundary_types.is_boundary_type(x,'demand','e'))
    return L

def isMetabolicRxns(model):
    L=[]
    for x in model.reactions:
        a=medium.boundary_types.is_boundary_type(x,'demand','e')
        b=medium.boundary_types.is_boundary_type(x,'exchange','e')
        c=medium.boundary_types.is_boundary_type(x,'sink','e')
        if a == 1 or b ==1 or c ==1:
            L.append(False)
        else:
            L.append(True)
    return L

def reactionType(reaction):
    dico = reaction.metabolites
    cpt=[]
    ids = []
    stoic = []
    for key in dico:
        cpt.append(key.compartment)
        ids.append(key.id)
        stoic.append(dico[key])
    if 'biom' in reaction.name or 'Biom' in reaction.name or 'BIOM' in reaction.name:
        res='biomass'
    elif len(unique(cpt))>1:
        res='trans'
    elif oneSign(stoic):
        if unique(cpt)[0]=='e':
            res='exch'
        elif reaction.reversibility:
            res='sink'
        else :
            res='demand'
    else:
        res='metabolic'
    return(res)

def reactionsType(model):
    res=[]
    for rxn in model.reactions:
        res.append(reactionType(rxn))
    return res

def findExcRxn(model):
    res = reactionsType(model)
    rxns=[]
    pos=[]
    for i in range(len(res)):
        if res[i]=='exch':
            pos.append(1)
            rxns.append(model.reactions[i].id)
        else:
            pos.append(0)
    return(pos,rxns)


def unique(L):
    unique = []
    for val in L:
        if val not in unique:
            unique.append(val)
    return unique

def oneSign(L):
    res=True
    i=1

    while res == True and i < len(L):
        if abs(L[i]+L[i-1]) < abs(L[i]):
            res = False
        i=i+1
    return res

def getRxnsFromMet(aModel,aMet):
    rxns = stoicMatrix(aModel)
    if isinstance(aMet, str):
        rxns=rxns.loc[aMet]
    else:
        rxns=rxns.loc[aMet.id]
    rxns = rxns.replace(0, np.nan)
    rxns = rxns.dropna(how='all', axis=0)
    rxns=rxns.index.values
    return rxns

    #matrix = stoicMatrix(model)

def info(model):
    print('Metabolites : ',len(model.metabolites))
    print('Reactions : ',len(model.reactions))
    print('Genes : ',len(model.genes))
    print('Compartments : ',model.compartments)
    print('Objective function : \n', model.objective,'\n')

def deleteNull(df):
    df = df.replace(0, np.nan)
    df = df.dropna(how='all', axis = 0)
    return(df)

def closeModel(model,condition = 'aero'):
    keep=['EX_h2o_e','EX_pi_e','EX_co2_e','EX_nh4_e','EX_h_e']
    if condition == 'aero':
        keep.append('EX_o2_e')
    excRxns = model.exchanges
    for rxn in excRxns:
        if rxn.id not in keep:
            model.reactions.get_by_id(rxn.id).lower_bound = 0
    return model

def medium(model,mets,ex = 'EX'):
    for i in range(len(mets)):
        mets[i]= ex+'_'+mets[i]
    excRxns = model.exchanges
    for rxn in excRxns:
        if rxn.id not in mets:
            model.reactions.get_by_id(rxn.id).lower_bound = 0
        else:
            model.reactions.get_by_id(rxn.id).lower_bound = -10

    return model

def updateLactococcus(model):
    rxns= ['EX_leu__L_e','EX_akg_e','EX_nmn_e','EX_cys__L_e','EX_ura_e']
    for rxn in rxns :
        model.reactions.get_by_id(rxn).lower_bound=-3
    
    model.reactions.get_by_id('EX_glc__D_e').lower_bound=-150
    return model
