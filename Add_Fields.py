# File: Add_Bridge_Fields.py
# Date: 12/26/2018
# Author: 
# Use:  Add fields necessary bridge-flood analysis
# Needs: CSV file with list of fields to be added.
# Arguments:
#    Arg[0] is the location of the workspace
#    Arg[1] is the location of the feature class

# Import modules
import os
import csv
import arcpy
import time

arcpy.env.workspace = arcpy.GetParameterAsText(0)
Path = arcpy.env.workspace


