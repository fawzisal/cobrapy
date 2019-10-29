# Removes all fields not given as fieldnames from the models
#
# USAGE:
#
#    restrictedModels = restrictModelsToFields(models, fieldNames)
#
# INPUT:
#    models:           A Cell array of model structs (or single model
#                      struct that has all fieldNames provided.
#    fieldNames:       Names of the fields the models will be restricted
#                      to.
#
# OUTPUT:
#    restrictedModels:    The models with the non names fields removed, or a single struct if its just one model.
#
# .. Author: - Thomas Pfau May 2017

def restrictModelsToFields(models, fieldNames):
    restrictedModels = models.copy();
    for cmodel in restrictedModels:
        modelfields = cmodel.__keys__.keys();
        for f in modelfields:
            if not f in fieldnames:
                cmodel.__delattrr__(f)

    return restrictedModels;
