#!/bin/python
import logging;
import sys;

project_name = "roomai";

logger = logging.getLogger(project_name);
logger.setLevel(logging.INFO);

handler = logging.StreamHandler(sys.stderr);
handler.setLevel(logging.INFO);

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s");
handler.setFormatter(formatter);

logger.addHandler(handler);

def initlog(opts):
    global logger;
    global handler;
    global project_name;

    print opts;
    if "project_name" in opts:
        project_name = opts["project_name"];
        print "in Logger", project_name;

    logger.removeHandler(handler);
    logger = logging.getLogger(project_name);

    #set longer
    if "logfile" in opts:
        handler = logging.FileHandler(opts["logfile"]);
    else:
        handler = logging.StreamHandler(sys.stderr);
    
    #set formatter
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s");
    handler.setFormatter(formatter);

    ##set level
    logger.setLevel(logging.INFO);
    if "level" in opts:
        if "notset" == opts["level"].lowcase():
            logger.setLevel(logging.NOTSET)
        elif "debug" == opts["level"].lowcase():
            logger.setLevel(logging.DEBUG)
        elif "info"  == opts["level"].lowcase():
            logger.setLevel(logging.INFO)
        elif "warning" == opts["level"].lowcase():
            logger.setLevel(logging.WARNING)
        elif "error" == opts["level"].lowcase():
            logger.setLevel(logging.ERROR)
        elif "critical" == opts["level"].lowcase():
            logger.setLevel(logging.critical)   

    logger.addHandler(handler);
   