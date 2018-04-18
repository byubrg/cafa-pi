#!/usr/bin/env python
import sys
import os

GO_biofilm = "GO:0042710"
GO_mobile = "GO:0001539"


biofilm_list = set(["GO:0032022","GO:0043707","GO:0043708","GO:0043709","GO:0043710","GO:0044010","GO:0044011","GO:0044399","GO:0044400","GO:0044401","GO:0044407","GO:0090604","GO:0090605","GO:0090606","GO:0090607","GO:0090608","GO:0090609","GO:0098775","GO:0098785","GO:1900187","GO:1900188","GO:1900189","GO:1900190","GO:1900191" ,"GO:1900192" ,"GO:1900228","GO:1900229","GO:1900230","GO:1900231","GO:1900232","GO:1900233"])
mobile_list=set([ "GO:0060285","GO:0071973","GO:0060294","GO:0060295","GO:0060296","GO:0071945","GO:0071977","GO:0071978","GO:0097588","GO:0097590","GO:1902019","GO:1902020","GO:1902021","GO:1902201","GO:1905419","GO:2000155"])


#Input is the GO term
#Return is the GO term for biofilm or mobile 
#Input can be the GO term for biofilm or mobile
#return "na" if not biofilm or mobile child


def get_parent (GO_term):
    if (GO_term in mobile_list or GO_term == GO_mobile):
        return GO_mobile
    if (GO_term in biofilm_list or GO_term == GO_mobile):
        return GO_biofilm
    return "na"

