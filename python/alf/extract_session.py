# -*- coding:utf-8 -*-
# @Author: Niccolò Bonacchi
# @Date: Thursday, October 11th 2018, 12:11:13 pm
# @Last Modified by: Niccolò Bonacchi
# @Last Modified time: 11-10-2018 12:11:26.2626
"""
Find task name
Check if extractors for specific task exist
Extract data OR return error to user saying that the task has no extractors
"""
import logging
from pathlib import Path
import traceback

from alf.extractors import training_trials, training_wheel
from ibllib.io import raw_data_loaders as raw
import ibllib.io.flags as flags


logger_ = logging.getLogger('ibllib.alf')


# this is a decorator to add a logfile to each extraction and registration on top of the logging
def log2sessionfile(func):
    def func_wrapper(sessionpath, *args, **kwargs):
        fh = logging.FileHandler(Path(sessionpath).joinpath('extract_register.log'))
        str_format = '%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s'
        fh.setFormatter(logging.Formatter(str_format))
        logger_.addHandler(fh)
        f = func(sessionpath, *args, **kwargs)
        logger_.removeHandler(fh)
        return f
    return func_wrapper


def extractors_exist(session_path):
    settings = raw.load_settings(session_path)
    task_name = settings['PYBPOD_PROTOCOL']
    task_name = task_name.split('_')[-1]
    extractor_type = task_name[:task_name.find('ChoiceWorld')]
    if any([extractor_type in x for x in globals()]):
        return extractor_type
    else:
        logger_.warning(str(session_path) +
                        f" No extractors were found for {extractor_type} ChoiceWorld")
        return False


def is_extracted(session_path):
    sp = Path(session_path)
    if (sp / 'alf').exists():
        return True
    else:
        return False


@log2sessionfile
def from_path(session_path, force=False, save=True):
    """
    Extract a session from full ALF path (ex: '/scratch/witten/ibl_witten_01/2018-12-18/001')
    force: (False) overwrite existing files
    save: (True) boolean or list of ALF file names to extract
    """
    logger_.info('Extracting ' + str(session_path))
    extractor_type = extractors_exist(session_path)
    if is_extracted(session_path) and not force:
        print(f"Session {session_path} already extracted.")
        return
    if extractor_type == 'training':
        training_trials.extract_all(session_path, save=save)
        training_wheel.extract_all(session_path, save=save)
    logger_.info('session extracted \n')  # timing info in log


def bulk(subjects_folder, dry=False):
    ses_path = Path(subjects_folder).glob('**/extract_me.flag')
    for p in ses_path:
        # the flag file may contains specific file names for a targeted extraction
        save = flags.read_flag_file(p)
        if dry:
            print(p)
            continue
        try:
            from_path(p.parent, force=True, save=save)
        except Exception as e:
            error_message = str(p.parent) + ' failed extraction' + '\n    ' + str(e)
            error_message += traceback.format_exc()
            logger_.error(error_message)
            err_file = p.parent.joinpath('extract_me.error')
            p.rename(err_file)
            with open(err_file, 'w+') as f:
                f.write(error_message)
            continue
        p.rename(p.parent.joinpath('register_me.flag'))
