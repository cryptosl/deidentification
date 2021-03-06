#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse
import anonymizer as anonymizer
from config import tags_to_keep, forced_values



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(
        description=("Anonymize a dicom according to dicom standard "))
    parser.add_argument("-in", "--dicom_in", 
                        help="input path of the dicom")
    parser.add_argument("-out", "--dicom_out", 
                        help="output path of the dicom")
    parser.add_argument("-ID", "--subjectID", default='Unknown',
                        help="ID of the subject")
   
    # Get arguments
    args = parser.parse_args()
    dicom_in = args.dicom_in
    dicom_out = args.dicom_out
    subjectID = args.subjectID

    if not os.path.exists(dicom_in):
        raise ValueError("Unknown folder/file %s" % dicom_in)

    forced_values[(0x0010, 0x0010)] = subjectID

    anonymizer.anonymize(
        dicom_in=dicom_in,
        dicom_out=dicom_out,
        tags_to_keep=tags_to_keep,
        forced_values=forced_values)
